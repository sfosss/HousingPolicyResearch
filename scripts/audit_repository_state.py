#!/usr/bin/env python3
"""Create one sanitized assessment of local task files and hosted GitHub work."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
from html import escape
import json
import os
from pathlib import Path
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

STATUS_COLUMNS = ("status", "current status", "state")
TASK_NAME_PARTS = ("task", "status", "checklist")
GITHUB_ENDPOINTS = {
    "issues": "/issues?state=open&per_page=100",
    "pull_requests": "/pulls?state=open&per_page=100",
    "dependabot_alerts": "/dependabot/alerts?state=open&per_page=100",
    "code_scanning_alerts": "/code-scanning/alerts?state=open&per_page=100",
    "secret_scanning_alerts": "/secret-scanning/alerts?state=open&per_page=100",
}
COLLABORATION_KINDS = {
    "box_shared_folder",
    "chatgpt_export",
    "claude_workspace",
    "cloud_drive_reference",
}
COLLABORATION_MODES = {"reference_only", "staged_import"}
MANIFEST_FIELDS = {"schema_version", "sources", "authoritative_repository"}
SOURCE_FIELDS = {
    "id",
    "kind",
    "path",
    "mode",
    "data_owner",
    "contains_chat_exports",
    "contains_personal_data",
}


def find_task_files(root: Path) -> list[Path]:
    if not root.is_dir() or not os.access(root, os.R_OK | os.X_OK):
        raise ValueError("audit root must be an existing readable directory")
    try:
        listing = subprocess.run(
            [
                "git",
                "-c",
                "core.fsmonitor=false",
                "-c",
                "core.hooksPath=/dev/null",
                "-C",
                str(root),
                "ls-files",
                "--cached",
                "--others",
                "--exclude-standard",
                "--deduplicate",
                "-z",
                "--",
                ".",
            ],
            check=True,
            capture_output=True,
            timeout=30,
        ).stdout
    except (OSError, subprocess.SubprocessError) as exc:
        raise ValueError(
            "audit root must be inside an accessible Git working tree"
        ) from exc
    found = []
    for name in listing.split(b"\0"):
        if not name:
            continue
        relative = Path(os.fsdecode(name))
        path = root / relative
        if (
            not any(
                root.joinpath(*relative.parts[:i]).is_symlink()
                for i in range(1, len(relative.parts) + 1)
            )
            and path.is_file()
            and path.suffix.lower() in {".csv", ".tsv"}
            and any(part in path.name.lower() for part in TASK_NAME_PARTS)
        ):
            found.append(path)
    return sorted(found)


def summarize_task_file(path: Path, root: Path) -> dict[str, object]:
    delimiter = "\t" if path.suffix.lower() == ".tsv" else ","
    with path.open(encoding="utf-8-sig", errors="replace", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
        columns = [column for column in (reader.fieldnames or []) if column]
        rows = list(reader)
    status_column = next(
        (column for column in columns if column.strip().lower() in STATUS_COLUMNS), None
    )
    statuses: dict[str, int] = {}
    if status_column:
        for row in rows:
            status = (row.get(status_column) or "(blank)").strip() or "(blank)"
            statuses[status] = statuses.get(status, 0) + 1
    return {
        "path": str(path.relative_to(root)),
        "rows": len(rows),
        "status_column": status_column,
        "statuses": dict(sorted(statuses.items())),
    }


def github_get(repo: str, endpoint: str, token: str) -> list[dict[str, object]]:
    url = f"https://api.github.com/repos/{repo}{endpoint}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "housing-policy-repository-audit",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    result = []
    while url:
        origin = urllib.parse.urlsplit(url)
        if origin.scheme != "https" or origin.netloc != "api.github.com":
            raise ValueError("GitHub pagination returned an unexpected URL")
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request, timeout=30) as response:
            page = json.load(response)
            link_header = response.headers.get("Link", "")
        if not isinstance(page, list):
            raise ValueError(f"GitHub returned an unexpected response for {endpoint}")
        result.extend(page)
        url = next(
            (
                part[part.find("<") + 1 : part.find(">")]
                for part in link_header.split(",")
                if 'rel="next"' in part
            ),
            "",
        )
    return result


def sanitize_github_items(
    kind: str, items: list[dict[str, object]]
) -> list[dict[str, object]]:
    sanitized = []
    for item in items:
        if kind == "issues" and "pull_request" in item:
            continue
        record = {
            "number": item.get("number"),
            "state": item.get("state"),
            "updated_at": item.get("updated_at"),
            "url": item.get("html_url"),
        }
        if kind in {"issues", "pull_requests"}:
            record["title"] = item.get("title")
        elif kind == "dependabot_alerts":
            dependency = item.get("dependency") or {}
            advisory = item.get("security_advisory") or {}
            record.update(
                package=(dependency.get("package") or {}).get("name"),
                ecosystem=(dependency.get("package") or {}).get("ecosystem"),
                severity=advisory.get("severity"),
            )
        elif kind == "code_scanning_alerts":
            rule = item.get("rule") or {}
            record.update(
                rule=rule.get("id"), severity=rule.get("security_severity_level")
            )
        elif kind == "secret_scanning_alerts":
            # Never emit the secret, locations, or validity metadata.
            record.update(
                secret_type=item.get("secret_type_display_name")
                or item.get("secret_type")
            )
        sanitized.append(record)
    return sanitized


def collect_github(repo: str, token: str) -> tuple[dict[str, object], dict[str, str]]:
    data: dict[str, object] = {}
    errors: dict[str, str] = {}
    for kind, endpoint in GITHUB_ENDPOINTS.items():
        try:
            data[kind] = sanitize_github_items(kind, github_get(repo, endpoint, token))
        except (
            urllib.error.HTTPError,
            urllib.error.URLError,
            TimeoutError,
            ValueError,
        ) as exc:
            errors[kind] = f"{type(exc).__name__}: {exc}"
    return data, errors


def inspect_collaboration_manifest(path: Path) -> list[dict[str, object]]:
    """Validate declared external sources without reading their contents."""
    document = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(document, dict):
        raise ValueError("collaboration manifest must be an object")
    if set(document) - MANIFEST_FIELDS:
        raise ValueError("forbidden or unsupported collaboration manifest fields")
    if "authoritative_repository" in document and not isinstance(
        document["authoritative_repository"], str
    ):
        raise ValueError("authoritative_repository must be a string")
    if (
        type(document.get("schema_version")) is not int
        or document.get("schema_version") != 1
        or not isinstance(document.get("sources"), list)
    ):
        raise ValueError("collaboration manifest must use schema_version 1 and sources")
    results = []
    seen_ids = set()
    for source in document["sources"]:
        if not isinstance(source, dict):
            raise ValueError("each collaboration source must be an object")
        if set(source) - SOURCE_FIELDS:
            raise ValueError("forbidden or unsupported collaboration source fields")
        for field in SOURCE_FIELDS - {"contains_chat_exports"}:
            if field in source and not isinstance(source[field], str):
                raise ValueError("collaboration source text fields must be strings")
        if (
            "contains_chat_exports" in source
            and type(source["contains_chat_exports"]) is not bool
        ):
            raise ValueError("contains_chat_exports must be a boolean")
        source_id = source.get("id")
        kind = source.get("kind")
        mode = source.get("mode")
        raw_path = source.get("path")
        if not source_id or source_id in seen_ids:
            raise ValueError("collaboration source IDs must be present and unique")
        if kind not in COLLABORATION_KINDS:
            raise ValueError(f"unsupported collaboration source kind: {kind}")
        if mode not in COLLABORATION_MODES:
            raise ValueError(f"unsupported collaboration source mode: {mode}")
        if not isinstance(raw_path, str) or not raw_path:
            raise ValueError(f"collaboration source {source_id} requires a path")
        seen_ids.add(source_id)
        source_path = Path(os.path.expandvars(raw_path)).expanduser()
        exists = source_path.exists()
        results.append(
            {
                "id": source_id,
                "kind": kind,
                "mode": mode,
                "data_owner_declared": bool(source.get("data_owner")),
                "personal_data_classification": source.get(
                    "contains_personal_data", "unknown"
                ),
                "available": exists,
                "is_directory": source_path.is_dir() if exists else None,
                "readable": os.access(source_path, os.R_OK) if exists else False,
            }
        )
    return results


def markdown_cell(value: object) -> str:
    text = " ".join(escape(str(value), quote=False).splitlines())
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("`", "\\`")


def render_markdown(report: dict[str, object]) -> str:
    lines = [
        "# Unified repository assessment",
        "",
        f"Generated: {report['generated_at']}",
        "",
        "## Local task/status artifacts",
        "",
        "| Path | Rows | Status summary |",
        "| --- | ---: | --- |",
    ]
    for item in report["local_task_files"]:
        statuses = ", ".join(
            f"{key}: {value}" for key, value in item["statuses"].items()
        )
        empty = "No rows" if item["status_column"] else "No status column"
        lines.append(
            f"| {markdown_cell(item['path'])} | {item['rows']} | {markdown_cell(statuses or empty)} |"
        )
    lines.extend(["", "## Hosted GitHub state", ""])
    github = report.get("github") or {}
    errors = report.get("github_errors") or {}
    if not github and "authentication" in errors:
        lines.append(
            "Not assessed: provide both `--repo OWNER/REPO` and `GITHUB_TOKEN`."
        )
    else:
        for kind in GITHUB_ENDPOINTS:
            status = (
                "Unavailable (not assessed)"
                if kind in errors or kind not in github
                else str(len(github[kind]))
            )
            lines.append(f"* **{kind.replace('_', ' ').title()}:** {status}")
    if errors:
        lines.extend(["", "### Permission or API failures", ""])
        for kind, message in errors.items():
            lines.append(f"* **{markdown_cell(kind)}:** {markdown_cell(message)}")
    lines.extend(["", "## Declared collaboration sources", ""])
    collaboration = report.get("collaboration_sources") or []
    if not collaboration:
        supplied = report.get("collaboration_manifest_supplied")
        if supplied is True:
            lines.append(
                "0 declared collaboration sources (manifest supplied and validated)."
            )
        elif supplied is False:
            lines.append("Not assessed: no local collaboration manifest was supplied.")
        else:
            lines.append("Not assessed: manifest coverage was not recorded.")
    else:
        lines.extend(
            [
                "| ID | Kind | Mode | Available | Readable | Owner declared |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
        )
        for source in collaboration:
            lines.append(
                f"| {markdown_cell(source['id'])} | {markdown_cell(source['kind'])} | {markdown_cell(source['mode'])} | "
                f"{source['available']} | {source['readable']} | "
                f"{source['data_owner_declared']} |"
            )
    lines.extend(
        [
            "",
            "## Comprehensive disposition rule",
            "",
            "Reconcile local rows and hosted issues by evidence, not title alone. Keep one hosted issue",
            "for each still-relevant outcome; link its source row, assign an owner and acceptance",
            "criteria, then archive the source tracker. Close duplicates or completed work only after",
            "recording the superseding issue, pull request, commit, or deliverable.",
            "",
        ]
    )
    return "\n".join(lines)


def build_report(
    root: Path,
    repo: str | None,
    token: str | None,
    collaboration_manifest: Path | None = None,
) -> dict[str, object]:
    report: dict[str, object] = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "collaboration_manifest_supplied": collaboration_manifest is not None,
        "local_task_files": [
            summarize_task_file(path, root) for path in find_task_files(root)
        ],
    }
    if repo and token:
        report["github"], report["github_errors"] = collect_github(repo, token)
    else:
        report["github"] = {}
        report["github_errors"] = {
            "authentication": "Set --repo OWNER/REPO and GITHUB_TOKEN to assess hosted state."
        }
    if collaboration_manifest:
        report["collaboration_sources"] = inspect_collaboration_manifest(
            collaboration_manifest
        )
    else:
        report["collaboration_sources"] = []
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--repo", default=os.getenv("GITHUB_REPOSITORY"))
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--markdown-output", type=Path)
    parser.add_argument(
        "--collaboration-manifest",
        type=Path,
        help="Local JSON manifest; source contents are not read",
    )
    args = parser.parse_args()
    report = build_report(
        args.root.resolve(),
        args.repo,
        os.getenv("GITHUB_TOKEN"),
        args.collaboration_manifest,
    )
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(
            json.dumps(report, indent=2) + "\n", encoding="utf-8"
        )
    markdown = render_markdown(report)
    if args.markdown_output:
        args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_output.write_text(markdown, encoding="utf-8")
    else:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
