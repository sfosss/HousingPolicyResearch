import csv
import json
from pathlib import Path

import pytest

from scripts.audit_repository_state import (
    build_report,
    find_task_files,
    inspect_collaboration_manifest,
    render_markdown,
    sanitize_github_items,
)


def test_task_inventory_does_not_follow_symlinks_or_ignored_trees(tmp_path):
    root = tmp_path / "repo"
    root.mkdir()
    outside = tmp_path / "private_tasks.csv"
    outside.write_text("Task,Status\nPrivate,Open\n")
    (root / "linked_tasks.csv").symlink_to(outside)
    (root / "linked-directory").symlink_to(tmp_path, target_is_directory=True)
    ignored = root / "node_modules"
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
