#!/usr/bin/env python3
"""Refined markdown link checker.

- Scans .md files in the repo (excluding .git and node_modules)
- Strips fenced code blocks (```...```) and inline code (`...`)
- Extracts external links (markdown and bare URLs)
- Performs HEAD (then GET if needed) requests and records status
- Writes results to logs/link-check/YYYY-MM-DD.json and prints a summary
"""

from __future__ import annotations

import re
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Tuple

try:
    import requests
except Exception:
    print("This script requires the 'requests' package.")
    print("Install with: pip install requests")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = ROOT / "logs" / "link-check"
IGNORED_DIRS = {".git", "node_modules", "venv", ".venv"}

MD_EXT = ".md"

FENCE_RE = re.compile(r"```.*?```", re.S)
INLINE_CODE_RE = re.compile(r"`[^`]+`")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(" r"(https?://[^)\s]+)\)")
BARE_URL_RE = re.compile(r"(?<!\()https?://" r"[\w\-./?=&%#]+")
BARE_URL_RE2 = re.compile(r"https?://" r"[\w\-./?=&%#]+")

TIMEOUT = 10


def gather_md_files(root: Path) -> List[Path]:
    files: List[Path] = []
    for p in root.rglob("*.md"):
        if any(part in IGNORED_DIRS for part in p.parts):
            continue
        files.append(p)
    return files


def strip_code(text: str) -> str:
    text = FENCE_RE.sub("", text)
    text = INLINE_CODE_RE.sub("", text)
    return text


def extract_links(text: str) -> Set[str]:
    links: Set[str] = set()
    for m in MARKDOWN_LINK_RE.finditer(text):
        links.add(m.group(1))
    for m in BARE_URL_RE2.finditer(text):
        links.add(m.group(0))
    return links


def check_url(url: str) -> Tuple[str, int | None, str | None]:
    """Return (url, status_code or None, error_message or None)"""
    headers = {"User-Agent": "HousingPolicyResearch-link-check/1.0"}
    try:
        r = requests.head(
            url,
            allow_redirects=True,
            timeout=TIMEOUT,
            headers=headers,
        )
        code = r.status_code
        if code >= 400 or code == 405:
            # try GET
            r = requests.get(
                url,
                allow_redirects=True,
                timeout=TIMEOUT,
                headers=headers,
            )
            code = r.status_code
        return url, code, None
    except requests.RequestException as exc:
        return url, None, str(exc)


def main() -> int:
    files = gather_md_files(ROOT)
    if not LOG_DIR.exists():
        LOG_DIR.mkdir(parents=True, exist_ok=True)

    discovered: Dict[str, Dict] = {}
    for p in files:
        try:
            content = p.read_text(encoding="utf-8")
        except Exception:
            continue
        stripped = strip_code(content)
        links = extract_links(stripped)
        for url in links:
            if url not in discovered:
                discovered[url] = {"checked": False, "files": set()}
            discovered[url]["files"].add(str(p.relative_to(ROOT)))

    # Check links
    results = []
    for url, meta in sorted(discovered.items()):
        print(f"Checking: {url}")
        u, code, err = check_url(url)
        results.append(
            {
                "url": u,
                "status_code": code,
                "error": err,
                "files": sorted(list(meta["files"])),
            }
        )

    now = datetime.utcnow().strftime("%Y-%m-%dT%H%M%SZ")
    out_path = LOG_DIR / f"link-check-{now}.json"
    payload = {"timestamp": now, "results": results}
    out_path.write_text(
        json.dumps(payload, indent=2),
        encoding="utf-8",
    )

    # Summary
    total = len(results)
    failures = []
    for r in results:
        if r["status_code"] is None or r["status_code"] >= 400:
            failures.append(r)
    print("\nSummary:")
    print(f"  Files scanned: {len(files)}")
    print(f"  Unique external links found: {total}")
    print(f"  Failures (None or >=400): {len(failures)}")

    if failures:
        print("\nTop failures:")
        for f in failures[:25]:
            url = f["url"]
            code = f["status_code"]
            err = f["error"]
            seen = len(f["files"])
            print(f"- {url}")
            print(f"  -> {code} / {err} (seen in {seen} file(s))")

    print(f"Results written to: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
