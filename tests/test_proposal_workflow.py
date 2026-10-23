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


def test_generated_proposal_is_committed_to_a_separate_remote_branch(tmp_path):
    remote = tmp_path / "remote.git"
    work = tmp_path / "work"
    env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull)

    def git(*args, cwd=None):
        return subprocess.run(
            ["git", *args],
            cwd=cwd,
            env=env,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()

    git("init", "--bare", str(remote))
    git("init", "-b", "main", str(work))
    git("config", "user.name", "Fixture", cwd=work)
    git("config", "user.email", "fixture@example.invalid", cwd=work)
    git("config", "core.hooksPath", os.devnull, cwd=work)
    (work / ".gitignore").write_text("artifacts/*\n!artifacts/.gitkeep\n")
    (work / "artifacts").mkdir()
    (work / "artifacts/.gitkeep").touch()
    git("add", ".", cwd=work)
    git("commit", "-m", "Fixture baseline", cwd=work)
    git("remote", "add", "origin", str(remote), cwd=work)
    git("push", "-u", "origin", "main", cwd=work)
    baseline = git("--git-dir", str(remote), "rev-parse", "refs/heads/main")
    proposal = "# Fixture proposal\n"
    (work / "artifacts/policy_proposal.md").write_text(proposal)
    workflow = yaml.safe_load(WORKFLOW.read_text())
    checkout = next(
        s
        for s in workflow["jobs"]["build"]["steps"]
        if "actions/checkout@" in s.get("uses", "")
    )
    assert checkout["with"]["ref"] == "main"
    step = next(
        s
        for s in workflow["jobs"]["build"]["steps"]
        if s.get("name") == "Save proposal to a review branch"
    )
    env.update(
        GITHUB_RUN_ID="123",
        GITHUB_RUN_ATTEMPT="2",
        GITHUB_SERVER_URL="https://github.com",
        GITHUB_REPOSITORY="owner/repo",
        GITHUB_STEP_SUMMARY=str(tmp_path / "summary"),
    )
    subprocess.run(
        ["bash", "-e", "-c", step["run"]],
        cwd=work,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )
    assert git("--git-dir", str(remote), "rev-parse", "refs/heads/main") == baseline
    assert (
        git(
            "--git-dir",
            str(remote),
            "show",
            "generated/policy-proposal-123-2:artifacts/policy_proposal.md",
        )
        == proposal.strip()
    )
    assert (
        "compare/main...generated/policy-proposal-123-2"
        in (tmp_path / "summary").read_text()
    )
