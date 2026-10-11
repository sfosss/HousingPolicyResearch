import csv
import json
from pathlib import Path

import pytest

from scripts.audit_repository_state import (
    build_report,
    inspect_collaboration_manifest,
    render_markdown,
    sanitize_github_items,
)


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
