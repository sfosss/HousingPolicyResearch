"""Check publication prerequisites without rendering or publishing reports."""

import subprocess
from pathlib import Path

import pytest
import yaml


WORKFLOW = Path(__file__).resolve().parents[1] / ".github/workflows/publish-reports.yml"


@pytest.mark.parametrize("draft_name", [None, "brief.md", "brief.qmd"])
def test_drafts_are_required_and_output_exists_before_rendering(tmp_path, draft_name):
    if draft_name:
        drafts = tmp_path / "30_drafts"
        drafts.mkdir()
        (drafts / draft_name).write_text("# Draft\n")
    workflow = yaml.safe_load(WORKFLOW.read_text())
    steps = workflow["jobs"]["validate-and-publish"]["steps"]
    check = next(step for step in steps if step.get("name") == "Check draft inputs")
    result = subprocess.run(
        ["bash", "-e", "-c", check["run"]],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )
    assert result.returncode == (0 if draft_name else 1)
    assert (tmp_path / "40_outputs").is_dir() == bool(draft_name)
    if not draft_name:
        assert "No Markdown or Quarto drafts" in result.stdout
