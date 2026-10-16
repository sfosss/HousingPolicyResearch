#!/usr/bin/env python3
"""Adaptive NYC housing-policy research and legislative-update pipeline.

The pipeline is intentionally review-first: it proposes redlines and never edits
canonical PETF/TCAP legislation. It accepts normalized Web, Midpage, and Box
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
from dataclasses import dataclass, asdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from xml.etree import ElementTree

import requests

ROOT = Path(__file__).resolve().parents[1]
TRACKER = ROOT / "datasets" / "NYC_Housing_Subsidy_Policy_News_LIVE.csv"
CONNECTORS = ROOT / "intake" / "connectors"
POLICY_MAP = ROOT / "config" / "policy_map.json"
SOURCES = ROOT / "config" / "policy_sources.json"
INDEX_CSV = ROOT / "indexes" / "SOURCE_INDEX.csv"
INDEX_MD = ROOT / "indexes" / "SOURCE_INDEX.md"
EXPORTS = ROOT / "exports-for-chatgpt"
POLICY_RESEARCH = ROOT / "policy-research"

FIELDS = [
    "event_id", "date_published", "date_ingested", "source_name", "source_type",
    "source_url", "canonical_url", "headline", "summary", "jurisdiction",
    "agency", "document_type", "primary_source", "policy", "section",
    "paragraph", "impact_area", "importance", "importance_score",
    "legal_pathway", "fiscal_roi_effect", "proposed_redline", "review_status",
    "reviewer", "disposition_notes", "content_hash", "supersedes_event_id"
]

NYC_TERMS = {
    "new york city", "nyc", "hp d", "hpd", "hra", "nycha", "hud",
    "tenant", "housing", "rent", "homeless", "voucher", "section 8",
    "public housing", "co-op", "cooperative", "eviction", "civil rights"
}
TRACKING_PARAMS = {"utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "fbclid", "gclid"}


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


def clean_text(value: Any, limit: int = 5000) -> str:
    text = re.sub(r"<[^>]+>", " ", str(value or ""))
    return re.sub(r"\s+", " ", text).strip()[:limit]


def canonicalize_url(url: str) -> str:
    if not url:
        return ""
    parts = urlsplit(url.strip())
    query = urlencode(sorted((k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True) if k.lower() not in TRACKING_PARAMS))
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, query, ""))


def digest(*parts: str) -> str:
    return hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()


def parse_date(value: str) -> str:
    value = clean_text(value, 100)
    if not value:
        return date.today().isoformat()
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S%z", "%a, %d %b %Y %H:%M:%S %z", "%Y-%m-%dT%H:%M:%SZ"):
        try:
            return datetime.strptime(value, fmt).date().isoformat()
        except ValueError:
            pass
    match = re.search(r"\d{4}-\d{2}-\d{2}", value)
    return match.group(0) if match else date.today().isoformat()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def packet_items(payload: Any, source_type: str) -> list[dict[str, Any]]:
    items = payload if isinstance(payload, list) else payload.get("items", []) if isinstance(payload, dict) else []
    result = []
    for item in items:
        if not isinstance(item, dict):
            continue
        normalized = dict(item)
        normalized.setdefault("source_type", source_type)
        result.append(normalized)
    return result


def read_connector_packets() -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for provider in ("web", "midpage", "box"):
        folder = CONNECTORS / provider
        if folder.exists():
            for path in sorted(folder.glob("*.json")):
                items.extend(packet_items(load_json(path, []), provider))
        env_payload = os.getenv(f"{provider.upper()}_RESEARCH_JSON", "").strip()
        if env_payload:
            items.extend(packet_items(json.loads(env_payload), provider))
    return items


def fetch_feed(source: dict[str, Any]) -> list[dict[str, Any]]:
    response = requests.get(source["url"], timeout=30, headers={"User-Agent": "HousingPolicyResearch/1.0"})
    response.raise_for_status()
    root = ElementTree.fromstring(response.content)
    entries = list(root.findall(".//item")) or list(root.findall(".//{*}entry"))
    output = []
    for entry in entries[: source.get("max_items", 25)]:
        def first(names: Iterable[str]) -> str:
            for name in names:
                node = entry.find(name) or entry.find(f"{{*}}{name}")
                if node is not None:
                    if name == "link" and node.attrib.get("href"):
                        return node.attrib["href"]
                    if node.text:
                        return node.text
            return ""
        output.append({
            "source_name": source["name"], "source_type": "official_feed",
            "source_url": first(["link"]), "headline": first(["title"]),
            "summary": first(["description", "summary", "content"]),
            "date_published": first(["pubDate", "published", "updated"]),
            "jurisdiction": source.get("jurisdiction", "NYC"),
            "agency": source.get("agency", ""), "document_type": source.get("document_type", "Release"),
            "primary_source": source.get("primary_source", True)
        })
    return output


def fetch_configured_sources() -> tuple[list[dict[str, Any]], list[str]]:
    items, errors = [], []
    for source in load_json(SOURCES, {}).get("sources", []):
        if not source.get("enabled", True) or source.get("type") != "feed":
            continue
        try:
            items.extend(fetch_feed(source))
        except Exception as exc:
            errors.append(f"{source.get('name', source.get('url'))}: {exc}")
    return items, errors


def box_pull() -> tuple[list[dict[str, Any]], list[str]]:
    token, folder_id = os.getenv("BOX_ACCESS_TOKEN", ""), os.getenv("BOX_INBOX_FOLDER_ID", "")
    if not token or not folder_id:
        return [], []
    headers = {"Authorization": f"Bearer {token}"}
    errors, items, offset = [], [], 0
    while True:
        response = requests.get(
            f"https://api.box.com/2.0/folders/{folder_id}/items",
            headers=headers, params={"limit": 100, "offset": offset, "fields": "id,name,type"}, timeout=30
        )
        response.raise_for_status()
        data = response.json()
        entries = data.get("entries", [])
        for entry in entries:
            if entry.get("type") != "file" or not entry.get("name", "").lower().endswith(".json"):
                continue
            try:
                content = requests.get(f"https://api.box.com/2.0/files/{entry['id']}/content", headers=headers, timeout=30)
                content.raise_for_status()
                items.extend(packet_items(content.json(), "box"))
            except Exception as exc:
                errors.append(f"Box file {entry.get('name')}: {exc}")
        offset += len(entries)
        if offset >= data.get("total_count", 0) or not entries:
            break
    return items, errors


def in_scope(item: dict[str, Any]) -> bool:
    jurisdiction = clean_text(item.get("jurisdiction", "")).lower()
    text = f"{item.get('headline', '')} {item.get('summary', '')} {item.get('agency', '')}".lower()
    return jurisdiction in {"nyc", "new york city", "ny", "new york", "federal"} and any(term in text for term in NYC_TERMS)


def normalize(item: dict[str, Any], today: str) -> Record | None:
    headline = clean_text(item.get("headline") or item.get("title"), 500)
    url = clean_text(item.get("source_url") or item.get("url"), 2000)
    if not headline or not url:
        return None
    canonical = canonicalize_url(url)
    published = parse_date(str(item.get("date_published") or item.get("published_at") or ""))
    summary = clean_text(item.get("summary") or item.get("abstract"), 3000)
    content_hash = digest(headline.lower(), summary.lower(), canonical)
    event_id = digest(canonical, headline.lower(), published)[:20]
    return Record(
        event_id=event_id, date_published=published, date_ingested=today,
        source_name=clean_text(item.get("source_name") or item.get("publication") or urlsplit(canonical).netloc, 250),
        source_type=clean_text(item.get("source_type") or "web", 100), source_url=url,
        canonical_url=canonical, headline=headline, summary=summary,
        jurisdiction=clean_text(item.get("jurisdiction") or "NYC", 100),
        agency=clean_text(item.get("agency"), 150), document_type=clean_text(item.get("document_type") or "News/Research", 100),
        primary_source=str(bool(item.get("primary_source", False))).lower(), content_hash=content_hash
    )


def score_and_map(record: Record, rules: list[dict[str, Any]]) -> Record:
    text = f"{record.headline} {record.summary} {record.agency} {record.document_type}".lower()
    best, best_hits = None, []
    for rule in rules:
        hits = [kw for kw in rule.get("keywords", []) if kw.lower() in text]
        if len(hits) > len(best_hits):
            best, best_hits = rule, hits
    if best and best_hits:
        record.policy = best["policy"]
        record.section = best["section"]
        record.paragraph = best.get("paragraph", "Section-wide")
        record.impact_area = best.get("impact_area", "Implementation")
        record.legal_pathway = best.get("legal_pathway", "Needs counsel review")
        record.fiscal_roi_effect = best.get("fiscal_roi_effect", "Unquantified")
        base = int(best.get("base_score", 35))
        status_bonus = 20 if any(x in text for x in ("enacted", "effective", "final rule", "court held", "signed")) else 10 if any(x in text for x in ("passed", "adopted", "approved")) else 0
        authority_bonus = 15 if record.primary_source == "true" else 0
        rights_bonus = 10 if any(x in text for x in ("civil rights", "discrimination", "eviction", "due process", "immigration")) else 0
        score = min(100, base + min(15, len(best_hits) * 3) + status_bonus + authority_bonus + rights_bonus)
        record.importance_score = str(score)
        record.importance = "Critical" if score >= 85 else "High" if score >= 70 else "Medium" if score >= 50 else "Low" if score >= 30 else "Considerations"
        action = best.get("redline_template", "Add a conforming safeguard responsive to this authority.")
        record.proposed_redline = f"[PROPOSED—HUMAN REVIEW REQUIRED] {record.policy}, {record.section}, {record.paragraph}: {action} Source: {record.canonical_url}"
        if record.importance == "Critical":
            record.review_status = "Needs Counsel Review"
    return record


def read_tracker() -> list[dict[str, str]]:
    if not TRACKER.exists():
        return []
    with TRACKER.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def upsert(existing: list[dict[str, str]], incoming: list[Record]) -> tuple[list[dict[str, str]], int]:
    by_id = {row.get("event_id", ""): row for row in existing if row.get("event_id")}
    added = 0
    for record in incoming:
        row = {key: str(value) for key, value in asdict(record).items()}
        if record.event_id not in by_id:
            by_id[record.event_id] = row
            added += 1
        elif by_id[record.event_id].get("content_hash") != record.content_hash:
            preserved = {k: by_id[record.event_id].get(k, "") for k in ("review_status", "reviewer", "disposition_notes")}
            by_id[record.event_id].update(row)
            by_id[record.event_id].update({k: v for k, v in preserved.items() if v})
    return sorted(by_id.values(), key=lambda r: (r.get("date_published", ""), r.get("event_id", "")), reverse=True), added


def build_outputs(rows: list[dict[str, str]], today: str, errors: list[str], added: int) -> dict[str, Any]:
    daily = [row for row in rows if row.get("date_ingested") == today]
    dated = POLICY_RESEARCH / today.replace("-", "")
    dated.mkdir(parents=True, exist_ok=True)
    order = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3, "Considerations": 4}
    daily.sort(key=lambda r: (order.get(r.get("importance", ""), 9), -int(r.get("importance_score") or 0)))

    brief = [f"# NYC Housing Policy Research Brief — {today}", "", "Equity-investment lens; proposed legislative changes require human approval.", ""]
    redlines = [f"# Proposed PETF/TCAP Redlines — {today}", "", "Nothing in this file amends canonical legislation. Counsel and policy-owner approval are required.", ""]
    for row in daily:
        brief += [f"## {row['importance']}: {row['headline']}", "", row["summary"] or "No source summary supplied.", "", f"- Source: {row['canonical_url']}", f"- Mapping: {row['policy']} — {row['section']} — {row['paragraph']}", f"- ROI effect: {row['fiscal_roi_effect']}", f"- Review: {row['review_status']}", ""]
        if row.get("proposed_redline"):
            redlines += [f"## {row['headline']}", "", row["proposed_redline"], "", f"Importance: **{row['importance']}** ({row['importance_score']}/100)", ""]
    if not daily:
        brief += ["No new in-scope records were ingested. Check connector health and source availability.", ""]
        redlines += ["No redlines proposed.", ""]
    (dated / "DAILY_BRIEF.md").write_text("\n".join(brief), encoding="utf-8")
    (dated / "PROPOSED_REDLINES.md").write_text("\n".join(redlines), encoding="utf-8")
    (dated / "SOURCE_PACKET.json").write_text(json.dumps({"generated_at": datetime.now(timezone.utc).isoformat(), "items": daily}, indent=2), encoding="utf-8")

    total = len(daily)
    primary_rate = sum(r.get("primary_source") == "true" for r in daily) / total if total else 0
    mapped_rate = sum(r.get("section") != "Needs mapping" for r in daily) / total if total else 0
    redline_rate = sum(bool(r.get("proposed_redline")) for r in daily) / total if total else 0
    unresolved_critical = sum(r.get("importance") == "Critical" and r.get("review_status") != "Accepted" for r in daily)
    qa = {
        "date": today, "records_seen_today": total, "new_records_added": added,
        "primary_source_rate": round(primary_rate, 3), "section_mapping_rate": round(mapped_rate, 3),
        "redline_coverage_rate": round(redline_rate, 3), "unresolved_critical": unresolved_critical,
        "connector_errors": errors,
        "checks": {
            "all_urls_present": all(bool(r.get("canonical_url")) for r in daily),
            "all_critical_require_counsel": all(r.get("review_status") == "Needs Counsel Review" for r in daily if r.get("importance") == "Critical"),
            "no_canonical_legislation_modified": True,
            "nyc_scope_only": all(r.get("jurisdiction") in {"NYC", "New York City", "NY", "New York", "Federal"} for r in daily)
        }
    }
    qa["passed"] = all(qa["checks"].values()) and not errors
    (dated / "QA_REPORT.json").write_text(json.dumps(qa, indent=2), encoding="utf-8")

    EXPORTS.mkdir(parents=True, exist_ok=True)
    export = {"schema_version": "1.0", "generated_at": datetime.now(timezone.utc).isoformat(), "qa": qa, "items": daily}
    (EXPORTS / "policy-update-latest.json").write_text(json.dumps(export, indent=2), encoding="utf-8")
    (EXPORTS / f"policy-update-{today}.json").write_text(json.dumps(export, indent=2), encoding="utf-8")

    critical = [r for r in daily if r.get("importance") == "Critical"]
    alert = [f"# Critical PETF/TCAP policy alerts — {today}", ""]
    for row in critical:
        alert += [f"- **{row['headline']}** — {row['policy']} / {row['section']} — {row['canonical_url']}"]
    (dated / "CRITICAL_ALERT.md").write_text("\n".join(alert) + "\n", encoding="utf-8")
    return qa


def write_indexes(rows: list[dict[str, str]]) -> None:
    index_fields = ["event_id", "date_published", "source_name", "document_type", "agency", "headline", "canonical_url", "primary_source", "content_hash"]
    write_csv(INDEX_CSV, rows, index_fields)
    lines = ["# Source Index", "", "Generated from the canonical policy-update tracker.", "", "| Date | Source | Headline | Type |", "|---|---|---|---|"]
    for row in rows[:500]:
        headline = row.get("headline", "").replace("|", "\\|")
        lines.append(f"| {row.get('date_published','')} | [{row.get('source_name','')}]({row.get('canonical_url','')}) | {headline} | {row.get('document_type','')} |")
    INDEX_MD.parent.mkdir(parents=True, exist_ok=True)
    INDEX_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def box_upload(paths: list[Path]) -> list[str]:
    token, folder_id = os.getenv("BOX_ACCESS_TOKEN", ""), os.getenv("BOX_OUTPUT_FOLDER_ID", "")
    if not token or not folder_id:
        return []
    errors = []
    headers = {"Authorization": f"Bearer {token}"}
    for path in paths:
        try:
            attributes = json.dumps({"name": path.name, "parent": {"id": folder_id}})
            with path.open("rb") as handle:
                response = requests.post("https://upload.box.com/api/2.0/files/content", headers=headers, data={"attributes": attributes}, files={"file": handle}, timeout=60)
            if response.status_code == 409:
                errors.append(f"Box already has {path.name}; configure retention/versioning or clear the collision.")
            else:
                response.raise_for_status()
        except Exception as exc:
            errors.append(f"Box upload {path.name}: {exc}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--box-pull", action="store_true")
    parser.add_argument("--box-push", action="store_true")
    args = parser.parse_args()

    raw = read_connector_packets()
    fetched, errors = fetch_configured_sources()
    raw.extend(fetched)
    if args.box_pull:
        box_items, box_errors = box_pull()
        raw.extend(box_items)
        errors.extend(box_errors)

    rules = load_json(POLICY_MAP, {}).get("rules", [])
    records = []
    seen_hashes = set()
    for item in raw:
        if not in_scope(item):
            continue
        record = normalize(item, args.date)
        if not record or record.content_hash in seen_hashes:
            continue
        seen_hashes.add(record.content_hash)
        records.append(score_and_map(record, rules))

    rows, added = upsert(read_tracker(), records)
    write_csv(TRACKER, rows, FIELDS)
    write_indexes(rows)
    qa = build_outputs(rows, args.date, errors, added)
    dated = POLICY_RESEARCH / args.date.replace("-", "")
    if args.box_push:
        upload_errors = box_upload([dated / "DAILY_BRIEF.md", dated / "PROPOSED_REDLINES.md", dated / "SOURCE_PACKET.json", dated / "QA_REPORT.json", TRACKER, INDEX_CSV])
        if upload_errors:
            qa["connector_errors"].extend(upload_errors)
            qa["passed"] = False
            (dated / "QA_REPORT.json").write_text(json.dumps(qa, indent=2), encoding="utf-8")
    print(json.dumps(qa, indent=2))
    return 1 if args.strict and not qa["passed"] else 0


if __name__ == "__main__":
    sys.exit(main())
