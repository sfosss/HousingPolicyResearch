import csv
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import urllib.request

import pytest

from scripts.audit_repository_state import (
    build_report,
    find_task_files,
    github_get,
    inspect_collaboration_manifest,
    render_markdown,
    sanitize_github_items,
)


@pytest.fixture(autouse=True)
def git_inventory_root(tmp_path):
    subprocess.run(
        ["git", "init", "--quiet", str(tmp_path)], check=True, capture_output=True
    )


def test_task_inventory_does_not_follow_symlinks_or_ignored_trees(tmp_path):
    root = tmp_path / "repo"
    root.mkdir()
    outside = tmp_path / "private_tasks.csv"
    outside.write_text("Task,Status\nPrivate,Open\n")
    (root / "linked_tasks.csv").symlink_to(outside)
    (root / "linked-directory").symlink_to(tmp_path, target_is_directory=True)
    ignored = root / "node_modules"
    (root / ".gitignore").write_text("node_modules/\n")
    ignored.mkdir()
    (ignored / "nested_tasks.csv").write_text("Task,Status\nIgnored,Open\n")
    retained = root / "project_tasks.csv"
    retained.write_text("Task,Status\nReview,Open\n")

    assert find_task_files(root) == [retained]


def test_build_report_summarizes_local_statuses_without_github_token(tmp_path: Path):
    task_file = tmp_path / "project_tasks.csv"
    with task_file.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["Task", "Status"])
        writer.writeheader()
        writer.writerows(
            [{"Task": "Review", "Status": "Open"}, {"Task": "Ship", "Status": "Done"}]
        )

    report = build_report(tmp_path, "owner/repo", None)

    assert report["local_task_files"][0]["statuses"] == {"Done": 1, "Open": 1}
    assert "authentication" in report["github_errors"]
    assert "project_tasks.csv" in render_markdown(report)


def test_secret_alert_sanitization_never_emits_secret_or_locations():
    alerts = [
        {
            "number": 7,
            "state": "open",
            "secret_type": "example_token",
            "secret": "must-not-leak",
            "locations_url": "https://example.invalid/locations",
        }
    ]

    result = sanitize_github_items("secret_scanning_alerts", alerts)

    assert result == [
        {
            "number": 7,
            "state": "open",
            "updated_at": None,
            "url": None,
            "secret_type": "example_token",
        }
    ]
    assert "must-not-leak" not in str(result)


def test_collaboration_manifest_reports_readiness_without_disclosing_path(tmp_path):
    shared = tmp_path / "Box Shared Project"
    shared.mkdir()
    manifest = tmp_path / "sources.json"
    manifest.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "sources": [
                    {
                        "id": "team-box",
                        "kind": "box_shared_folder",
                        "path": str(shared),
                        "mode": "reference_only",
                        "data_owner": "project lead",
                    }
                ],
            }
        )
    )

    result = inspect_collaboration_manifest(manifest)

    assert result[0]["available"] is True
    assert result[0]["readable"] is True
    assert str(shared) not in str(result)


def test_collaboration_manifest_rejects_credentials(tmp_path):
    manifest = tmp_path / "sources.json"
    manifest.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "sources": [
                    {
                        "id": "unsafe",
                        "kind": "chatgpt_export",
                        "path": "/staging/export",
                        "mode": "staged_import",
                        "token": "do-not-store-this",
                    }
                ],
            }
        )
    )

    with pytest.raises(ValueError, match="forbidden"):
        inspect_collaboration_manifest(manifest)


@pytest.mark.parametrize(
    "field", ["access_token", "api_key", "shared_url", "credentials"]
)
def test_manifest_rejects_undeclared_source_fields(tmp_path, field):
    manifest = tmp_path / "sources.json"
    manifest.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "sources": [
                    {
                        "id": "source",
                        "kind": "chatgpt_export",
                        "mode": "staged_import",
                        "path": str(tmp_path),
                        field: {"nested_secret": "must-not-leak"},
                    }
                ],
            }
        )
    )
    with pytest.raises(ValueError, match="forbidden or unsupported"):
        inspect_collaboration_manifest(manifest)


def test_manifest_rejects_nested_values_in_declared_text_fields(tmp_path):
    manifest = tmp_path / "sources.json"
    manifest.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "sources": [
                    {
                        "id": "source",
                        "kind": "chatgpt_export",
                        "mode": "staged_import",
                        "path": str(tmp_path),
                        "data_owner": {"api_key": "must-not-leak"},
                    }
                ],
            }
        )
    )
    with pytest.raises(ValueError, match="must be strings"):
        inspect_collaboration_manifest(manifest)


def test_manifest_rejects_undeclared_document_fields(tmp_path):
    manifest = tmp_path / "sources.json"
    manifest.write_text(
        json.dumps({"schema_version": 1, "sources": [], "credentials": {}})
    )
    with pytest.raises(ValueError, match="forbidden or unsupported"):
        inspect_collaboration_manifest(manifest)


def test_manifest_rejects_nested_document_metadata(tmp_path):
    manifest = tmp_path / "sources.json"
    manifest.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "sources": [],
                "authoritative_repository": {"api_key": "must-not-leak"},
            }
        )
    )
    with pytest.raises(ValueError, match="must be a string"):
        inspect_collaboration_manifest(manifest)


def test_unavailable_alert_families_are_not_rendered_as_zero(tmp_path):
    report = build_report(tmp_path, None, None)
    report["github"] = {"issues": []}
    report["github_errors"] = {"secret_scanning_alerts": "HTTPError: 403"}
    markdown = render_markdown(report)
    assert "**Issues:** 0" in markdown
    assert "**Secret Scanning Alerts:** Unavailable (not assessed)" in markdown
    assert "**Dependabot Alerts:** Unavailable (not assessed)" in markdown
    assert "**Secret Scanning Alerts:** 0" not in markdown


def test_status_table_escapes_pipes_and_normalizes_newlines(tmp_path):
    path = tmp_path / "project_tasks.csv"
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["Task", "Status"])
        writer.writeheader()
        writer.writerow({"Task": "Review", "Status": "Blocked | waiting\nowner"})
    markdown = render_markdown(build_report(tmp_path, None, None))
    assert "Blocked \\| waiting owner: 1" in markdown
    assert "Blocked | waiting\nowner" not in markdown


def test_git_inventory_respects_ignore_patterns_and_negations(tmp_path):
    (tmp_path / ".gitignore").write_text(
        "workspace/\n*_BACKUP/\n*.csv\n!project_tasks.csv\n"
    )
    (tmp_path / "project_tasks.csv").write_text("Task,Status\n")
    (tmp_path / "private_tasks.csv").write_text("Task,Status\n")
    for directory in ["workspace", "old_BACKUP"]:
        path = tmp_path / directory
        path.mkdir()
        (path / "project_tasks.csv").write_text("Task,Status\n")
    assert find_task_files(tmp_path) == [tmp_path / "project_tasks.csv"]


def test_empty_tracker_preserves_status_header(tmp_path):
    (tmp_path / "empty_tasks.csv").write_text("Task,Status\n")
    report = build_report(tmp_path, None, None)
    assert report["local_task_files"][0]["status_column"] == "Status"
    assert report["local_task_files"][0]["rows"] == 0
    assert "No rows" in render_markdown(report)


def test_total_github_failure_keeps_all_endpoint_coverage(tmp_path):
    report = build_report(tmp_path, None, None)
    report["github_errors"] = {
        "issues": "HTTPError: 403",
        "secret_scanning_alerts": "HTTPError: 403",
    }
    markdown = render_markdown(report)
    assert "provide both" not in markdown
    assert markdown.count("Unavailable (not assessed)") == 5


def test_github_pagination_accepts_canonical_repository_urls(monkeypatch):
    first, second = io.StringIO('[{"number": 1}]'), io.StringIO('[{"number": 2}]')
    first.headers = {
        "Link": '<https://api.github.com/repositories/123/issues?page=2>; rel="next"'
    }
    second.headers = {}
    responses = iter([first, second])
    monkeypatch.setattr(
        urllib.request, "urlopen", lambda request, timeout: next(responses)
    )
    assert github_get("owner/repo", "/issues?per_page=100", "fixture-token") == [
        {"number": 1},
        {"number": 2},
    ]


@pytest.mark.parametrize(
    "url",
    [
        "https://evil.invalid/issues",
        "http://api.github.com/repos/o/r/issues",
        "https://api.github.com@evil.invalid/issues",
    ],
)
def test_github_pagination_rejects_untrusted_origins(monkeypatch, url):
    first = io.StringIO("[]")
    first.headers = {"Link": f'<{url}>; rel="next"'}
    requests = []

    def respond(request, timeout):
        requests.append(request)
        return first

    monkeypatch.setattr(urllib.request, "urlopen", respond)
    with pytest.raises(ValueError, match="unexpected URL"):
        github_get("owner/repo", "/issues?per_page=100", "fixture-token")
    assert len(requests) == 1


@pytest.mark.parametrize("kind", ["missing", "file"])
def test_invalid_audit_roots_are_unavailable(tmp_path, kind):
    root = tmp_path / "unavailable"
    if kind == "file":
        root.write_text("not a directory")
    with pytest.raises(ValueError, match="existing readable directory"):
        build_report(root, None, None)


def test_cli_writes_unicode_reports_under_a_non_utf8_locale(tmp_path):
    (tmp_path / "project_tasks.csv").write_text(
        "Task,Status\nReview,🟢 Open\n", encoding="utf-8"
    )
    env = dict(
        os.environ, LC_ALL="C", LANG="C", PYTHONUTF8="0", PYTHONCOERCECLOCALE="0"
    )
    env.pop("GITHUB_TOKEN", None)
    env.pop("GITHUB_REPOSITORY", None)
    markdown = tmp_path / "reports/report.md"
    output = tmp_path / "json/report.json"
    script = Path(__file__).resolve().parents[1] / "scripts/audit_repository_state.py"
    result = subprocess.run(
        [
            sys.executable,
            str(script),
            "--root",
            str(tmp_path),
            "--markdown-output",
            str(markdown),
            "--json-output",
            str(output),
        ],
        env=env,
        capture_output=True,
    )
    assert result.returncode == 0, result.stderr.decode("utf-8", errors="replace")
    assert "🟢 Open" in markdown.read_text(encoding="utf-8")
    assert json.loads(output.read_text(encoding="utf-8"))["local_task_files"][0][
        "statuses"
    ] == {"🟢 Open": 1}


def test_default_stdout_is_utf8_under_a_non_utf8_locale(tmp_path):
    (tmp_path / "project_tasks.csv").write_text(
        "Task,Status\nReview,🟢 Open\n", encoding="utf-8"
    )
    env = dict(
        os.environ, LC_ALL="C", LANG="C", PYTHONUTF8="0", PYTHONCOERCECLOCALE="0"
    )
    env.pop("GITHUB_TOKEN", None)
    env.pop("GITHUB_REPOSITORY", None)
    script = Path(__file__).resolve().parents[1] / "scripts/audit_repository_state.py"
    result = subprocess.run(
        [sys.executable, str(script), "--root", str(tmp_path)],
        env=env,
        capture_output=True,
    )
    assert result.returncode == 0, result.stderr.decode("utf-8", errors="replace")
    assert "🟢 Open" in result.stdout.decode("utf-8")


def test_empty_manifest_preserves_evidence_it_was_supplied(tmp_path):
    manifest = tmp_path / "sources.json"
    manifest.write_text(json.dumps({"schema_version": 1, "sources": []}))
    report = build_report(tmp_path, None, None, manifest)
    assert report["collaboration_manifest_supplied"] is True
    markdown = render_markdown(report)
    assert (
        "0 declared collaboration sources (manifest supplied and validated)" in markdown
    )
    assert "no local collaboration manifest was supplied" not in markdown
