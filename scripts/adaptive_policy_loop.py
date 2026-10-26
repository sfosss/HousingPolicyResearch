#!/usr/bin/env python3
"""Adaptive NYC housing-policy research and legislative-update pipeline.

The pipeline proposes redlines without editing canonical PETF/TCAP legislation.
It accepts normalized Web, Midpage, and Box
research packets, deduplicates evidence, maps impacts, scores implementation
importance, emits daily artifacts, updates source indexes, and performs QA.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import tempfile
import time
from dataclasses import dataclass, asdict
from datetime import date, datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import parse_qsl, unquote, urlencode, urlsplit, urlunsplit
from xml.etree import ElementTree

import requests

ROOT = Path(__file__).resolve().parents[1]
TRACKER = ROOT / "datasets" / "NYC_Housing_Subsidy_Policy_News_LIVE.csv"
CONNECTORS = ROOT / "intake" / "connectors"
POLICY_MAP = ROOT / "config" / "policy_map.json"
SOURCES = ROOT / "config" / "policy_sources.json"
INDEX_CSV = ROOT / "indexes" / "POLICY_SOURCE_INDEX.csv"
INDEX_MD = ROOT / "indexes" / "POLICY_SOURCE_INDEX.md"
EXPORTS = ROOT / "exports-for-chatgpt"
POLICY_RESEARCH = ROOT / "policy-research"

FIELDS = [
    "event_id",
    "date_published",
    "date_ingested",
    "source_name",
    "source_type",
    "source_url",
    "canonical_url",
    "headline",
    "summary",
    "jurisdiction",
    "agency",
    "document_type",
    "primary_source",
    "policy",
    "section",
    "paragraph",
    "impact_area",
    "importance",
    "importance_score",
    "legal_pathway",
    "fiscal_roi_effect",
    "proposed_redline",
    "review_status",
    "reviewer",
    "disposition_notes",
    "content_hash",
    "supersedes_event_id",
    "source_updated_at",
    "target_document",
    "opinion_analysis",
]

NYC_TERMS = {
    "new york city",
    "nyc",
    "hp d",
    "hpd",
    "hra",
    "nycha",
    "hud",
    "tenant",
    "housing",
    "rent",
    "homeless",
    "voucher",
    "section 8",
    "public housing",
    "co-op",
    "cooperative",
    "eviction",
    "civil rights",
}
NYC_SIGNALS = {
    "new york city",
    "nyc",
    "hpd",
    "hra",
    "nycha",
    "cityfheps",
    "brooklyn",
    "bronx",
    "queens",
    "manhattan",
    "staten island",
    "public equity transfer framework",
    "tenant co-op acquisition program",
}
TRACKING_PARAMS = {
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "fbclid",
    "gclid",
}


@dataclass
class Record:
    event_id: str = ""
    date_published: str = ""
    date_ingested: str = ""
    source_name: str = ""
    source_type: str = ""
    source_url: str = ""
    canonical_url: str = ""
    headline: str = ""
    summary: str = ""
    jurisdiction: str = "NYC"
    agency: str = ""
    document_type: str = ""
    primary_source: str = "false"
    policy: str = "PETF/TCAP"
    section: str = "Needs mapping"
    paragraph: str = "Needs mapping"
    impact_area: str = "Implementation"
    importance: str = "Considerations"
    importance_score: str = "0"
    legal_pathway: str = "Needs counsel review"
    fiscal_roi_effect: str = "Unquantified"
    proposed_redline: str = ""
    review_status: str = "Proposed"
    reviewer: str = ""
    disposition_notes: str = ""
    content_hash: str = ""
    supersedes_event_id: str = ""
    source_updated_at: str = ""
    target_document: str = ""
    opinion_analysis: str = ""


def clean_text(value: Any, limit: int = 5000) -> str:
    text = re.sub(r"<[^>]+>", " ", str(value or ""))
    return re.sub(r"\s+", " ", text).strip()[:limit]


SENSITIVE_QUERY_NAMES = {
    "key",
    "apikey",
    "xapikey",
    "auth",
    "authorization",
    "password",
    "passwd",
    "secret",
    "clientsecret",
    "token",
    "accesstoken",
    "refreshtoken",
    "securitytoken",
    "signature",
    "sig",
    "credential",
    "credentials",
    "jwt",
    "accesskey",
    "subscriptionkey",
    "ocpapimsubscriptionkey",
}
URL_TEXT = re.compile(r"https?(?:://|%[0-9a-f]{2})[^\s<>\"']+", re.I)


def decoded_parameter(value: str) -> str | None:
    for _ in range(8):
        decoded = unquote(value)
        if decoded == value:
            return value
        value = decoded
    # Reject ambiguous names rather than retaining hidden credentials.
    return None if re.search(r"%[0-9a-f]{2}", value, re.I) else value


def nested_value(value: str) -> str | None:
    for _ in range(8):
        if re.search(r"https?://", value, re.I) or re.match(
            r"^[\w.%-]+=", value
        ):
            return value
        decoded = unquote(value)
        if decoded == value:
            return value
        value = decoded
    return None


def sanitized_text(value: str, depth: int = 0) -> str:
    def replace(match: re.Match) -> str:
        nested = nested_value(match.group())
        return sanitize_source_url(nested, depth + 1) if nested else ""

    return URL_TEXT.sub(replace, value)


def sanitized_query(query: str, depth: int = 0) -> str:
    if depth > 4:
        return ""
    pairs = []
    for pair in re.split(r"[&;]", query):
        for key, value in parse_qsl(pair, keep_blank_values=True):
            decoded_key = decoded_parameter(key)
            if decoded_key is None:
                continue
            name = re.sub(r"[^a-z0-9]", "", decoded_key.lower())
            if (
                not name
                or name in SENSITIVE_QUERY_NAMES
                or name.startswith("xamz")
                or name.endswith(
                    (
                        "token",
                        "secret",
                        "password",
                        "signature",
                        "apikey",
                        "accesskey",
                        "subscriptionkey",
                    )
                )
            ):
                continue
            decoded_value = nested_value(value)
            if decoded_value is None:
                continue
            if re.search(r"https?://", decoded_value, re.I):
                value = sanitized_text(decoded_value, depth)
            elif re.match(r"^[\w.%-]+=", decoded_value):
                value = sanitized_query(decoded_value, depth + 1)
            pairs.append((key, value))
    return urlencode(pairs)


def sanitize_source_url(url: str, depth: int = 0) -> str:
    if not isinstance(url, str) or depth > 4:
        return ""
    try:
        parts = urlsplit(url)
        netloc = parts.netloc.rsplit("@", 1)[-1]
        fragment = parts.fragment
        decoded_fragment = decoded_parameter(fragment)
        if decoded_fragment is None:
            fragment = ""
        elif "?" in decoded_fragment:
            route, query = decoded_fragment.split("?", 1)
            query = sanitized_query(query, depth)
            fragment = route + ("?" + query if query else "")
        elif "=" in decoded_fragment:
            fragment = sanitized_query(decoded_fragment, depth)
        safe = urlunsplit(
            (
                parts.scheme,
                netloc,
                parts.path,
                sanitized_query(parts.query, depth),
                fragment,
            )
        )
        return safe if valid_source_url(safe) else ""
    except (ValueError, UnicodeError):
        return ""


def sanitize_row(row: dict[str, str]) -> dict[str, str]:
    original = row.get("canonical_url", "")
    expected = digest(
        row.get("headline", "").lower(),
        row.get("summary", "").lower(),
        original,
    )
    safe = {
        key: sanitized_text(value) if isinstance(value, str) else value
        for key, value in row.items()
    }
    safe["source_url"] = sanitize_source_url(row.get("source_url", ""))
    safe["canonical_url"] = canonicalize_url(original)
    if row.get("content_hash") == expected:
        safe["content_hash"] = digest(
            safe.get("headline", "").lower(),
            safe.get("summary", "").lower(),
            safe["canonical_url"],
        )
    return safe


def canonicalize_url(url: str) -> str:
    if not valid_source_url(url):
        return ""
    parts = urlsplit(sanitize_source_url(url))
    query = urlencode(
        sorted(
            (k, v)
            for k, v in parse_qsl(parts.query, keep_blank_values=True)
            if k.lower() not in TRACKING_PARAMS
        )
    )
    path = parts.path.rstrip("/") or "/"
    return urlunsplit(
        (parts.scheme.lower(), parts.netloc.lower(), path, query, "")
    )


def valid_source_url(url: str) -> bool:
    if not isinstance(url, str) or re.search(r"[\s\\\x00-\x1f\x7f]", url):
        return False
    try:
        parts = urlsplit(url)
        host = parts.hostname
        return bool(
            parts.scheme.lower() in {"http", "https"}
            and host
            and parts.username is None
            and parts.password is None
            and parts.port != 0
            and (
                ":" in host
                or all(
                    re.fullmatch(
                        r"[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?", label
                    )
                    for label in host.encode("idna")
                    .decode("ascii")
                    .rstrip(".")
                    .split(".")
                )
            )
        )
    except (ValueError, UnicodeError):
        return False


def digest(*parts: str) -> str:
    return hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()


def parse_date(value: str) -> str:
    value = clean_text(value, 100)
    if not value:
        return ""
    for fmt in (
        "%Y-%m-%d",
        "%Y-%m-%dT%H:%M:%S%z",
        "%a, %d %b %Y %H:%M:%S %z",
        "%Y-%m-%dT%H:%M:%SZ",
    ):
        try:
            return datetime.strptime(value, fmt).date().isoformat()
        except ValueError:
            pass
    try:
        return parsedate_to_datetime(value).date().isoformat()
    except (TypeError, ValueError, OverflowError):
        pass
    match = re.search(r"\d{4}-\d{2}-\d{2}", value)
    if match:
        try:
            return date.fromisoformat(match.group(0)).isoformat()
        except ValueError:
            pass
    return ""


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def parse_timestamp(value: Any) -> str:
    if not isinstance(value, str) or not value:
        return ""
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            return ""
        return parsed.astimezone(timezone.utc).isoformat()
    except ValueError:
        return ""


def analyzed_opinion(item: dict[str, Any]) -> bool:
    analysis = item.get("opinion_analysis")
    if not isinstance(analysis, dict):
        return False
    return bool(
        analysis.get("tool") == "analyzeOpinion"
        and analysis.get("status") == "completed"
        and clean_text(analysis.get("analysis_id"))
        and clean_text(analysis.get("proposition"))
        and clean_text(analysis.get("scope_limit"))
        and parse_timestamp(analysis.get("analyzed_at"))
        and canonicalize_url(analysis.get("opinion_url", ""))
        == canonicalize_url(item.get("source_url") or item.get("url") or "")
        and valid_source_url(analysis.get("opinion_url", ""))
    )


def valid_mapping_target(document: str, section: str, paragraph: str) -> bool:
    try:
        path = (ROOT / document).resolve()
        if not document or not path.is_relative_to(ROOT) or not path.is_file():
            return False
        text = path.read_text(encoding="utf-8")
        heading = re.search(
            r"^\*\*" + re.escape(section) + r"\*\*", text, re.M
        )
        if heading is None:
            return False
        start = heading.end()
        body = text[start:].split("\n**§", 1)[0]
        return bool(re.search(r"^" + re.escape(paragraph) + r"\s", body, re.M))
    except (OSError, ValueError):
        return False


def validated_rules(
    rules: list[dict[str, Any]], errors: list[str]
) -> list[dict[str, Any]]:
    valid = []
    for position, rule in enumerate(rules, 1):
        if valid_mapping_target(
            rule.get("target_document", ""),
            rule.get("section", ""),
            rule.get("paragraph", ""),
        ):
            valid.append(rule)
        else:
            errors.append(
                f"Policy map rule {position}: canonical target not found"
            )
    return valid


def packet_items(
    payload: Any, source_type: str, errors: list[str], label: str
) -> list[dict[str, Any]]:
    items = (
        payload
        if isinstance(payload, list)
        else payload.get("items") if isinstance(payload, dict) else None
    )
    if not isinstance(items, list):
        errors.append(
            f"{label}: expected an array or an object "
            "containing an items array"
        )
        return []
    result = []
    for position, item in enumerate(items, 1):
        if not isinstance(item, dict):
            errors.append(f"{label} item {position}: expected an object")
            continue
        headline = item.get("headline") or item.get("title")
        url = item.get("source_url") or item.get("url")
        if (
            not isinstance(headline, str)
            or not clean_text(headline)
            or not valid_source_url(url)
        ):
            errors.append(
                f"{label} item {position}: headline and valid HTTP(S) "
                "source URL required"
            )
            continue
        if clean_text(item.get("jurisdiction", "")).lower() not in {
            "nyc",
            "new york city",
            "ny",
            "new york",
            "federal",
        }:
            errors.append(
                f"{label} item {position}: allowed jurisdiction required"
            )
            continue
        primary = item.get("primary_source", False)
        if not isinstance(primary, bool) and primary not in ("true", "false"):
            errors.append(
                f"{label} item {position}: primary_source must be a boolean"
            )
            continue
        updated = item.get("source_updated_at") or item.get("updated_at")
        if updated and not parse_timestamp(updated):
            errors.append(
                f"{label} item {position}: timezone-aware "
                "source_updated_at required"
            )
            continue
        midpage = (
            source_type == "midpage"
            or clean_text(item.get("source_type", "")).lower() == "midpage"
        )
        if midpage and not analyzed_opinion(item):
            errors.append(
                f"{label} item {position}: completed "
                "analyzeOpinion evidence required"
            )
            continue
        normalized = dict(item)
        normalized.setdefault("source_type", source_type)
        if midpage:
            analysis = item["opinion_analysis"]
            normalized["source_type"] = "midpage"
            normalized["summary"] = (
                f"{analysis['proposition']} "
                f"Scope limit: {analysis['scope_limit']}"
            )
        result.append(normalized)
    return result


def read_connector_packets() -> tuple[list[dict[str, Any]], list[str]]:
    items: list[dict[str, Any]] = []
    errors: list[str] = []
    for provider in ("web", "midpage", "box"):
        folder = CONNECTORS / provider
        if folder.exists():
            for path in sorted(folder.glob("*.json")):
                try:
                    items.extend(
                        packet_items(
                            load_json(path, []), provider, errors, str(path)
                        )
                    )
                except (OSError, ValueError) as exc:
                    errors.append(
                        f"{path}: invalid or unreadable JSON packet "
                        f"({type(exc).__name__})"
                    )
        env_payload = os.getenv(
            f"{provider.upper()}_RESEARCH_JSON", ""
        ).strip()
        if env_payload:
            label = f"{provider.upper()}_RESEARCH_JSON"
            try:
                items.extend(
                    packet_items(
                        json.loads(env_payload), provider, errors, label
                    )
                )
            except ValueError:
                errors.append(f"{label}: invalid JSON packet")
    return items, errors


def fetch_feed(source: dict[str, Any]) -> list[dict[str, Any]]:
    response = requests.get(
        source["url"],
        timeout=30,
        headers={"User-Agent": "HousingPolicyResearch/1.0"},
    )
    response.raise_for_status()
    root = ElementTree.fromstring(response.content)
    entries = list(root.findall(".//{*}item")) or list(
        root.findall(".//{*}entry")
    )
    if not entries:
        raise ValueError("Feed contains no supported RSS/Atom entries")
    output = []
    # Process the full available feed so the per-poll cap cannot lose entries.
    for entry in entries:

        def first(names: Iterable[str]) -> str:
            for name in names:
                node = entry.find(name)
                if node is None:
                    node = entry.find(f"{{*}}{name}")
                if node is not None:
                    if name == "link" and node.attrib.get("href"):
                        return node.attrib["href"]
                    if node.text:
                        return node.text
            return ""

        output.append(
            {
                "source_name": source["name"],
                "source_type": "official_feed",
                "source_url": first(["link"]),
                "headline": first(["title"]),
                "summary": first(["description", "summary", "content"]),
                "date_published": first(["pubDate", "published", "updated"]),
                "jurisdiction": source.get("jurisdiction", "NYC"),
                "agency": source.get("agency", ""),
                "document_type": source.get("document_type", "Release"),
                "primary_source": source.get("primary_source", True),
            }
        )
    return output


def fetch_configured_sources() -> tuple[list[dict[str, Any]], list[str]]:
    items, errors = [], []
    for position, source in enumerate(
        load_json(SOURCES, {}).get("sources", []), 1
    ):
        if not source.get("enabled", True) or source.get("type") != "feed":
            continue
        for attempt in range(3):
            try:
                if not valid_source_url(source.get("url", "")):
                    raise ValueError("Invalid feed URL")
                safe_source = dict(
                    source, url=sanitize_source_url(source["url"])
                )
                items.extend(fetch_feed(safe_source))
                break
            except Exception as exc:
                response = getattr(exc, "response", None)
                status = getattr(response, "status_code", None)
                transient = isinstance(
                    exc, (requests.Timeout, requests.ConnectionError)
                ) or status in {429, 500, 502, 503, 504}
                if transient and attempt < 2:
                    time.sleep(2**attempt)
                    continue
                # Exceptions can contain credentials in redirect URLs.
                errors.append(
                    f"Official feed {position}: {type(exc).__name__}"
                )
                break
    return items, errors


def box_pull() -> tuple[list[dict[str, Any]], list[str]]:
    token, folder_id = os.getenv("BOX_ACCESS_TOKEN", ""), os.getenv(
        "BOX_INBOX_FOLDER_ID", ""
    )
    if not token or not folder_id:
        return [], []
    headers = {"Authorization": f"Bearer {token}"}
    errors, items, offset = [], [], 0
    while True:
        try:
            response = requests.get(
                f"https://api.box.com/2.0/folders/{folder_id}/items",
                headers=headers,
                params={
                    "limit": 100,
                    "offset": offset,
                    "fields": "id,name,type",
                },
                timeout=30,
            )
            response.raise_for_status()
            data = response.json()
            entries = data["entries"]
            if not isinstance(entries, list) or not all(
                isinstance(e, dict) for e in entries
            ):
                raise ValueError("expected Box entries array")
            total_count = int(data["total_count"])
        except (
            requests.RequestException,
            ValueError,
            KeyError,
            TypeError,
        ) as exc:
            errors.append(f"Box inbox listing: {type(exc).__name__}")
            break
        for entry in entries:
            if (
                not isinstance(entry.get("name"), str)
                or not str(entry.get("id", "")).isdigit()
            ):
                errors.append(
                    "Box inbox entry: valid name and file ID required"
                )
                continue
            if entry.get("type") != "file" or not entry.get(
                "name", ""
            ).lower().endswith(".json"):
                continue
            try:
                content = requests.get(
                    f"https://api.box.com/2.0/files/{entry['id']}/content",
                    headers=headers,
                    timeout=30,
                )
                content.raise_for_status()
                items.extend(
                    packet_items(
                        content.json(),
                        "box",
                        errors,
                        f"Box file {entry.get('name')}",
                    )
                )
            except Exception as exc:
                errors.append(
                    f"Box file {entry.get('name')}: {type(exc).__name__}"
                )
        offset += len(entries)
        if offset >= total_count or not entries:
            break
    return items, errors


def matches_term(text: str, term: str) -> bool:
    return bool(
        re.search(
            r"(?<!\w)" + re.escape(term.lower()) + r"(?!\w)", text.lower()
        )
    )


def in_scope(item: dict[str, Any]) -> bool:
    jurisdiction = clean_text(item.get("jurisdiction", "")).lower()
    text = " ".join(
        str(item.get(field, "")) for field in ("headline", "summary")
    ).lower()
    allowed = jurisdiction in {
        "nyc",
        "new york city",
        "ny",
        "new york",
        "federal",
    }
    relevant = any(matches_term(text, term) for term in NYC_TERMS)
    local = jurisdiction in {"nyc", "new york city"}
    city_signal = any(matches_term(text, term) for term in NYC_SIGNALS)
    target_agency = clean_text(item.get("agency", "")).lower() in {
        "hpd",
        "hra",
        "nycha",
        "nyc hpd",
        "nyc hra",
        "nyc housing authority",
    }
    explicit = item.get("applies_to_nyc") is True
    return (
        allowed
        and relevant
        and (local or city_signal or target_agency or explicit)
    )


def normalize(item: dict[str, Any], today: str) -> Record | None:
    headline = clean_text(item.get("headline") or item.get("title"), 500)
    url = item.get("source_url") or item.get("url") or ""
    if not headline or not valid_source_url(url):
        return None
    url = sanitize_source_url(url)
    canonical = canonicalize_url(url)
    published = parse_date(
        str(item.get("date_published") or item.get("published_at") or "")
    )
    summary = clean_text(item.get("summary") or item.get("abstract"), 3000)
    content_hash = digest(headline.lower(), summary.lower(), canonical)
    event_id = digest(canonical, headline.lower(), published)[:20]
    return Record(
        event_id=event_id,
        date_published=published,
        date_ingested=today,
        source_name=clean_text(
            item.get("source_name")
            or item.get("publication")
            or urlsplit(canonical).netloc,
            250,
        ),
        source_type=clean_text(item.get("source_type") or "web", 100),
        source_url=url,
        canonical_url=canonical,
        headline=headline,
        summary=summary,
        jurisdiction=clean_text(item.get("jurisdiction") or "NYC", 100),
        agency=clean_text(item.get("agency"), 150),
        document_type=clean_text(
            item.get("document_type") or "News/Research", 100
        ),
        primary_source=str(item.get("primary_source", False)).lower(),
        content_hash=content_hash,
        source_updated_at=parse_timestamp(
            item.get("source_updated_at") or item.get("updated_at")
        ),
        opinion_analysis=(
            json.dumps(item["opinion_analysis"], sort_keys=True)
            if isinstance(item.get("opinion_analysis"), dict)
            else ""
        ),
    )


def score_and_map(record: Record, rules: list[dict[str, Any]]) -> Record:
    text = " ".join(
        (record.headline, record.summary, record.agency, record.document_type)
    ).lower()
    best, best_hits = None, []
    for rule in rules:
        hits = [
            kw for kw in rule.get("keywords", []) if matches_term(text, kw)
        ]
        if len(hits) > len(best_hits):
            best, best_hits = rule, hits
    if best and best_hits:
        record.policy = best["policy"]
        record.target_document = best.get("target_document", "")
        record.section = best["section"]
        record.paragraph = best.get("paragraph", "Section-wide")
        record.impact_area = best.get("impact_area", "Implementation")
        record.legal_pathway = best.get(
            "legal_pathway", "Needs counsel review"
        )
        record.fiscal_roi_effect = best.get(
            "fiscal_roi_effect", "Unquantified"
        )
        base = int(best.get("base_score", 35))
        status_bonus = (
            20
            if any(
                matches_term(text, x)
                for x in (
                    "enacted",
                    "effective",
                    "final rule",
                    "court held",
                    "signed",
                )
            )
            else (
                10
                if any(
                    matches_term(text, x)
                    for x in ("passed", "adopted", "approved")
                )
                else 0
            )
        )
        authority_bonus = 15 if record.primary_source == "true" else 0
        rights_bonus = (
            10
            if any(
                matches_term(text, x)
                for x in (
                    "civil rights",
                    "discrimination",
                    "eviction",
                    "due process",
                    "immigration",
                )
            )
            else 0
        )
        score = min(
            100,
            base
            + min(15, len(best_hits) * 3)
            + status_bonus
            + authority_bonus
            + rights_bonus,
        )
        record.importance_score = str(score)
        record.importance = (
            "Critical"
            if score >= 85
            else (
                "High"
                if score >= 70
                else (
                    "Medium"
                    if score >= 50
                    else "Low" if score >= 30 else "Considerations"
                )
            )
        )
        action = best.get(
            "redline_template",
            "Add a conforming safeguard responsive to this authority.",
        )
        record.proposed_redline = (
            "[PROPOSED—HUMAN REVIEW REQUIRED] "
            f"{record.target_document}: {record.policy}, "
            f"{record.section}, {record.paragraph}: {action} "
            f"Source: {record.canonical_url}"
        )
        if record.importance == "Critical":
            record.review_status = "Needs Counsel Review"
    return record


def read_tracker() -> list[dict[str, str]]:
    if not TRACKER.exists():
        return []
    with TRACKER.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        required = set(FIELDS) - {
            "source_updated_at",
            "target_document",
            "opinion_analysis",
        }
        if not required.issubset(headers):
            raise ValueError("Tracker missing required columns")
        if len(headers) != len(set(headers)):
            raise ValueError("Tracker contains duplicate column headers")
        rows = list(reader)
        if any(
            None in row
            or not row.get("event_id")
            or any(value is None for value in row.values())
            for row in rows
        ):
            raise ValueError(
                "Tracker contains malformed rows or empty event IDs"
            )
        return rows


def write_csv(
    path: Path, rows: list[dict[str, Any]], fields: list[str]
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            newline="",
            encoding="utf-8",
            dir=path.parent,
            delete=False,
        ) as handle:
            temporary = Path(handle.name)
            writer = csv.DictWriter(
                handle, fieldnames=fields, extrasaction="ignore"
            )
            writer.writeheader()
            writer.writerows(rows)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def upsert(
    existing: list[dict[str, str]],
    incoming: list[Record],
    errors: list[str] | None = None,
) -> tuple[list[dict[str, str]], int]:
    by_id = {
        row.get("event_id", ""): sanitize_row(row)
        for row in existing
        if row.get("event_id")
    }
    by_url = {
        url: key
        for key, row in by_id.items()
        if (url := canonicalize_url(row.get("canonical_url", "")))
    }
    by_hash = {
        row["content_hash"]: key
        for key, row in by_id.items()
        if row.get("content_hash")
    }
    added = 0
    for record in incoming:
        row = sanitize_row(
            {key: str(value) for key, value in asdict(record).items()}
        )
        record = Record(**{key: row[key] for key in FIELDS})
        key = (
            record.event_id
            if record.event_id in by_id
            else by_url.get(record.canonical_url)
            or by_hash.get(record.content_hash)
        )
        if key is None:
            key = record.event_id
            by_id[key] = row
            added += 1
        else:
            previous = by_id[key]
            if previous.get("content_hash") != record.content_hash:
                old_version = parse_timestamp(
                    previous.get("source_updated_at")
                )
                new_version = parse_timestamp(record.source_updated_at)
                if (
                    not old_version
                    or not new_version
                    or new_version <= old_version
                ):
                    if errors is not None:
                        errors.append(
                            f"Event {key}: conflicting evidence needs a newer "
                            "source_updated_at; retained stored evidence"
                        )
                    continue
                # Keep the ledger identity; revisions need fresh review.
                row["event_id"] = key
                by_id[key] = row
                old_hash = previous.get("content_hash")
                if by_hash.get(old_hash) == key:
                    by_hash.pop(old_hash)
            else:
                old_version = parse_timestamp(
                    previous.get("source_updated_at")
                )
                new_version = parse_timestamp(record.source_updated_at)
                if record.date_published and (
                    not old_version or new_version >= old_version
                ):
                    previous["date_published"] = record.date_published
                if new_version and (
                    not old_version or new_version > old_version
                ):
                    previous["source_updated_at"] = new_version
                if (
                    record.primary_source == "true"
                    and previous.get("primary_source") != "true"
                ):
                    # Prefer official provenance for unchanged evidence.
                    was_critical = previous.get("importance") == "Critical"
                    for field in (
                        "source_name",
                        "source_type",
                        "source_url",
                        "primary_source",
                        "importance",
                        "importance_score",
                    ):
                        previous[field] = row[field]
                    if record.importance == "Critical" and (
                        not was_critical or not critical_resolved(previous)
                    ):
                        previous["review_status"] = "Needs Counsel Review"
                        previous["reviewer"] = ""
                        previous["disposition_notes"] = ""
        if record.canonical_url:
            by_url[record.canonical_url] = key
        if record.content_hash:
            by_hash[record.content_hash] = key
    return (
        sorted(
            by_id.values(),
            key=lambda r: (r.get("date_published", ""), r.get("event_id", "")),
            reverse=True,
        ),
        added,
    )


def critical_resolved(row: dict[str, str]) -> bool:
    return row.get("review_status") == "Accepted" and bool(
        row.get("reviewer", "").strip()
    )


def write_qa_exports(
    rows: list[dict[str, str]], today: str, qa: dict[str, Any]
) -> None:
    dated = POLICY_RESEARCH / today.replace("-", "")
    (dated / "QA_REPORT.json").write_text(
        json.dumps(qa, indent=2), encoding="utf-8"
    )
    EXPORTS.mkdir(parents=True, exist_ok=True)
    export = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "qa": qa,
        "items": [r for r in rows if r.get("date_ingested") == today],
    }
    for name in ("policy-update-latest.json", f"policy-update-{today}.json"):
        (EXPORTS / name).write_text(
            json.dumps(export, indent=2), encoding="utf-8"
        )


def build_outputs(
    rows: list[dict[str, str]], today: str, errors: list[str], added: int
) -> dict[str, Any]:
    daily = [row for row in rows if row.get("date_ingested") == today]
    dated = POLICY_RESEARCH / today.replace("-", "")
    dated.mkdir(parents=True, exist_ok=True)
    order = {
        "Critical": 0,
        "High": 1,
        "Medium": 2,
        "Low": 3,
        "Considerations": 4,
    }
    daily.sort(
        key=lambda r: (
            order.get(r.get("importance", ""), 9),
            -int(r.get("importance_score") or 0),
        )
    )

    brief = [
        f"# NYC Housing Policy Research Brief — {today}",
        "",
        "Equity-investment lens; proposed legislative changes "
        "require human approval.",
        "",
    ]
    redlines = [
        f"# Proposed PETF/TCAP Redlines — {today}",
        "",
        "Nothing in this file amends canonical legislation. "
        "Counsel and policy-owner approval are required.",
        "",
    ]
    for row in daily:
        brief += [
            f"## {row['importance']}: {row['headline']}",
            "",
            row["summary"] or "No source summary supplied.",
            "",
            f"- Source: {row['canonical_url']}",
            f"- Mapping: {row['policy']} — {row['section']} "
            f"— {row['paragraph']}",
            f"- ROI effect: {row['fiscal_roi_effect']}",
            f"- Review: {row['review_status']}",
            "",
        ]
        if row.get("proposed_redline"):
            redlines += [
                f"## {row['headline']}",
                "",
                row["proposed_redline"],
                "",
                f"Importance: **{row['importance']}** "
                f"({row['importance_score']}/100)",
                "",
            ]
    if not daily:
        brief += [
            "No new in-scope records were ingested. "
            "Check connector health and source availability.",
            "",
        ]
        redlines += ["No redlines proposed.", ""]
    (dated / "DAILY_BRIEF.md").write_text("\n".join(brief), encoding="utf-8")
    (dated / "PROPOSED_REDLINES.md").write_text(
        "\n".join(redlines), encoding="utf-8"
    )
    (dated / "SOURCE_PACKET.json").write_text(
        json.dumps(
            {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "items": daily,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    total = len(daily)
    primary_rate = (
        sum(r.get("primary_source") == "true" for r in daily) / total
        if total
        else 0
    )
    mapped_rate = (
        sum(r.get("section") != "Needs mapping" for r in daily) / total
        if total
        else 0
    )
    redline_rate = (
        sum(bool(r.get("proposed_redline")) for r in daily) / total
        if total
        else 0
    )
    critical = [r for r in rows if r.get("importance") == "Critical"]
    unresolved = [r for r in critical if not critical_resolved(r)]
    qa = {
        "date": today,
        "records_seen_today": total,
        "new_records_added": added,
        "primary_source_rate": round(primary_rate, 3),
        "section_mapping_rate": round(mapped_rate, 3),
        "redline_coverage_rate": round(redline_rate, 3),
        "unresolved_critical": len(unresolved),
        "connector_errors": [sanitized_text(error) for error in errors],
        "checks": {
            "all_urls_present": all(
                valid_source_url(r.get("canonical_url", "")) for r in rows
            ),
            "all_critical_require_counsel": all(
                r.get("review_status") == "Needs Counsel Review"
                or critical_resolved(r)
                for r in critical
            ),
            "no_unresolved_critical": not unresolved,
            "all_daily_records_mapped": all(
                r.get("section") and r.get("section") != "Needs mapping"
                for r in daily
            ),
            "all_mapping_targets_valid": all(
                valid_mapping_target(
                    r.get("target_document", ""),
                    r.get("section", ""),
                    r.get("paragraph", ""),
                )
                for r in rows
                if r.get("section") != "Needs mapping"
            ),
            "all_daily_records_have_redlines": all(
                r.get("proposed_redline") for r in daily
            ),
            "no_canonical_legislation_modified": True,
            "nyc_scope_only": all(
                r.get("jurisdiction", "").lower()
                in {"nyc", "new york city", "ny", "new york", "federal"}
                for r in daily
            ),
        },
    }
    qa["passed"] = all(qa["checks"].values()) and not errors
    write_qa_exports(rows, today, qa)

    alert = [f"# Critical PETF/TCAP policy alerts — {today}", ""]
    for row in unresolved:
        alert += [
            f"- **{row['headline']}** — {row['policy']} / {row['section']} "
            f"— {row['canonical_url']}"
        ]
    (dated / "CRITICAL_ALERT.md").write_text(
        "\n".join(alert) + "\n", encoding="utf-8"
    )
    return qa


def write_indexes(rows: list[dict[str, str]]) -> None:
    index_fields = [
        "event_id",
        "date_published",
        "source_name",
        "document_type",
        "agency",
        "headline",
        "canonical_url",
        "primary_source",
        "content_hash",
    ]
    write_csv(INDEX_CSV, rows, index_fields)
    lines = [
        "# Source Index",
        "",
        "Generated from the canonical policy-update tracker.",
        "",
        "| Date | Source | Headline | Type |",
        "|---|---|---|---|",
    ]
    for row in rows[:500]:
        headline = row.get("headline", "").replace("|", "\\|")
        lines.append(
            f"| {row.get('date_published', '')} | "
            f"[{row.get('source_name', '')}]"
            f"({row.get('canonical_url', '')}) | {headline} | "
            f"{row.get('document_type', '')} |"
        )
    INDEX_MD.parent.mkdir(parents=True, exist_ok=True)
    INDEX_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def box_upload(paths: list[Path]) -> list[str]:
    token, folder_id = os.getenv("BOX_ACCESS_TOKEN", ""), os.getenv(
        "BOX_OUTPUT_FOLDER_ID", ""
    )
    if not token or not folder_id:
        return []
    errors = []
    headers = {"Authorization": f"Bearer {token}"}
    for path in paths:
        try:
            attributes = json.dumps(
                {"name": path.name, "parent": {"id": folder_id}}
            )
            with path.open("rb") as handle:
                response = requests.post(
                    "https://upload.box.com/api/2.0/files/content",
                    headers=headers,
                    data={"attributes": attributes},
                    files={"file": handle},
                    timeout=60,
                )
            if response.status_code == 409:
                conflicts = (
                    response.json()
                    .get("context_info", {})
                    .get("conflicts", [])
                )
                if isinstance(conflicts, dict):
                    conflicts = [conflicts]
                existing = next(
                    (
                        entry
                        for entry in conflicts
                        if entry.get("type") == "file"
                        and entry.get("name") == path.name
                        and str(entry.get("id", "")).isdigit()
                    ),
                    None,
                )
                if existing:
                    with path.open("rb") as handle:
                        response = requests.post(
                            "https://upload.box.com/api/2.0/files/"
                            f"{existing['id']}/content",
                            headers=headers,
                            files={"file": handle},
                            timeout=60,
                        )
            response.raise_for_status()
        except Exception as exc:
            errors.append(f"Box upload {path.name}: {type(exc).__name__}")
    return errors


def mark_run_complete(today: str, recovered: bool = False) -> None:
    dated = POLICY_RESEARCH / today.replace("-", "")
    (dated / "RUN_COMPLETE.json").write_text(
        json.dumps(
            {
                "date": today,
                "recovered_from_ledger": recovered,
                "generated_at": datetime.now(timezone.utc).isoformat(),
            },
            indent=2,
        ),
        encoding="utf-8",
    )


def recover_missing_outputs(rows: list[dict[str, str]], today: str) -> None:
    required = [
        "DAILY_BRIEF.md",
        "PROPOSED_REDLINES.md",
        "SOURCE_PACKET.json",
        "QA_REPORT.json",
        "CRITICAL_ALERT.md",
        "RUN_COMPLETE.json",
    ]
    for day in sorted({r.get("date_ingested", "") for r in rows}):
        try:
            day = date.fromisoformat(day).isoformat()
        except ValueError:
            continue
        if day == today:
            continue
        dated = POLICY_RESEARCH / day.replace("-", "")
        if all((dated / name).is_file() for name in required):
            continue
        historical = [r for r in rows if r.get("date_ingested", "") <= day]
        build_outputs(
            historical,
            day,
            [
                "Recovered from ledger; "
                "original connector diagnostics unavailable"
            ],
            0,
        )
        mark_run_complete(day, recovered=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--box-pull", action="store_true")
    parser.add_argument("--box-push", action="store_true")
    args = parser.parse_args()

    raw, errors = read_connector_packets()
    fetched, source_errors = fetch_configured_sources()
    errors.extend(source_errors)
    raw.extend(fetched)
    if args.box_pull:
        box_items, box_errors = box_pull()
        raw.extend(box_items)
        errors.extend(box_errors)

    rules = validated_rules(load_json(POLICY_MAP, {}).get("rules", []), errors)
    records = []
    for item in raw:
        if not in_scope(item):
            continue
        record = normalize(item, args.date)
        if not record:
            errors.append(
                "Intake item rejected: headline and valid HTTP(S) "
                "source URL required"
            )
            continue
        records.append(score_and_map(record, rules))

    try:
        existing = [sanitize_row(row) for row in read_tracker()]
    except (OSError, ValueError, csv.Error) as exc:
        errors.append(
            f"Tracker unavailable: {type(exc).__name__}; ledger preserved"
        )
        qa = build_outputs([], args.date, errors, 0)
        print(json.dumps(qa, indent=2))
        return 1
    recover_missing_outputs(existing, args.date)
    rows, added = upsert(existing, records, errors)
    write_csv(TRACKER, rows, FIELDS)
    write_indexes(rows)
    qa = build_outputs(rows, args.date, errors, added)
    dated = POLICY_RESEARCH / args.date.replace("-", "")
    if args.box_push:
        upload_errors = box_upload(
            [
                dated / "DAILY_BRIEF.md",
                dated / "PROPOSED_REDLINES.md",
                dated / "SOURCE_PACKET.json",
                TRACKER,
                INDEX_CSV,
            ]
        )
        if upload_errors:
            qa["connector_errors"].extend(upload_errors)
            qa["passed"] = False
        write_qa_exports(rows, args.date, qa)
        # Mirror QA after the other upload outcomes are known.
        report_errors = box_upload([dated / "QA_REPORT.json"])
        if report_errors:
            qa["connector_errors"].extend(report_errors)
            qa["passed"] = False
            write_qa_exports(rows, args.date, qa)
    mark_run_complete(args.date)
    print(json.dumps(qa, indent=2))
    return 1 if args.strict and not qa["passed"] else 0


if __name__ == "__main__":
    sys.exit(main())
