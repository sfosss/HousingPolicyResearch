"""Exercise the proposal workflow's credential gate without live API calls."""

import os
import shutil
import subprocess
from pathlib import Path

import pytest
import yaml

pytestmark = pytest.mark.skipif(
    os.name == "nt" or shutil.which("bash") is None,
    reason="Exercises Bash steps from an ubuntu-latest GitHub Actions job",
)


WORKFLOW = (
    Path(__file__).resolve().parents[1]
    / ".github/workflows/generate_policy_proposal.yml"
)


@pytest.mark.parametrize(
    "event,configured,exit_code,ready",
    [
        ("schedule", False, 0, False),
        ("workflow_dispatch", False, 1, False),
        ("schedule", True, 0, True),
        ("workflow_dispatch", True, 0, True),
    ],
)
def test_missing_credentials_skip_schedules_but_fail_manual_requests(
    tmp_path, event, configured, exit_code, ready
):
    workflow = yaml.safe_load(WORKFLOW.read_text())
    gate = workflow["jobs"]["build"]["steps"][0]
    output = tmp_path / "output"
    summary = tmp_path / "summary"
    env = dict(os.environ)
    env.update(
        OPENAI_API_KEY="configured-test-value" if configured else "",
        GITHUB_EVENT_NAME=event,
        GITHUB_OUTPUT=str(output),
        GITHUB_STEP_SUMMARY=str(summary),
    )
    result = subprocess.run(
        ["bash", "-e", "-c", gate["run"]], env=env, capture_output=True, text=True
    )
    assert result.returncode == exit_code, result.stdout + result.stderr
    assert output.read_text().strip() == "ready=" + str(ready).lower()
    assert "configured-test-value" not in result.stdout + result.stderr
    if not configured:
        assert "was not run" in summary.read_text()
