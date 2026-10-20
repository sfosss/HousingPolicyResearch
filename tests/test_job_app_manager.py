from pathlib import Path
import json
import csv
from datetime import date

from chatgpt_notion_sync import job_app_manager as jam


def write_json(tmp_path: Path, name: str, data) -> Path:
    path = tmp_path / name
    path.write_text(json.dumps(data))
    return path


def sample_job_record():
    return {
        "company": "Civic Tech",
        "job_title": "Policy Analyst",
        "department": "Housing",
        "summary": "Analyse housing policy",
        "responsibilities": "Research, writing reports",
        "required_documents": ["resume", "cover letter"],
        "local_files": ["/tmp/resume.pdf"],
        "web_links": ["https://example.com"],
        "application_file": "application.pdf",
        "submission_method": "portal",
        "prerequisites": "Research, writing, housing",
        "salary": "$80k-$95k",
        "date_posted": "2024-01-15",
        "submission_deadline": "2024-02-15",
        "tags": ["analysis", "policy"],
        "resume_status": "drafted",
        "cover_letter_status": "needs revisions",
        "writing_sample_status": "not started",
        "references_status": "complete",
    }


def test_generate_template_creates_csv(tmp_path):
    job_file = write_json(tmp_path, "jobs.json", [sample_job_record()])
    profile = write_json(
        tmp_path, "profile.json", {"skills": ["research", "policy", "writing"]}
    )
    records = jam.load_job_records(job_file)
    profile_tokens = jam.load_profile_tokens(profile)
    output = tmp_path / "template.csv"
    jam.write_reminders_template(records, profile_tokens, output)
    content = list(csv.reader(output.read_text().splitlines()))
    header = content[0]
    assert header[-3:] == [
        "days_until_deadline",
        "deadline_status",
        "attention_summary",
    ]
    row = content[1]
    assert "drafted" in row[0]
    assert "policy" in ",".join(content[1])
    assert row[-2] in {
        "due_soon",
        "overdue",
        "scheduled",
        "unspecified",
    }


def test_configure_repository_structure_initialises_directories(tmp_path, monkeypatch):
    icloud = tmp_path / "icloud"
    github_parent = tmp_path / "github"
    github = github_parent / "JobApps"

    called = {}

    def fake_init(path):
        called["path"] = Path(path)

    monkeypatch.setattr(jam, "initialise_git_repository", fake_init)

    results = jam.configure_repository_structure(icloud, github_parent, "JobApps")
    reminders_icloud = icloud / jam.REMINDERS_SUBDIR
    reminders_github = github / jam.REMINDERS_SUBDIR
    assert reminders_icloud.exists()
    assert reminders_github.exists()
    assert (github / jam.APPLICATIONS_SUBDIR).exists()
    assert called["path"] == github
    assert results == [
        icloud / jam.REMINDERS_SUBDIR,
        github / jam.REMINDERS_SUBDIR,
    ]


def test_resolve_github_repo_path_accepts_full_path(tmp_path):
    repo = tmp_path / "JobApps"
    repo.mkdir()
    assert jam.resolve_github_repo_path(repo, "JobApps") == repo


def test_describe_deadline_handles_overdue_and_pending():
    overdue, label = jam.describe_deadline("2023-01-01", today=date(2023, 1, 10))
    assert overdue == "-9"
    assert label == "overdue"

    soon, label = jam.describe_deadline("2023-01-15", today=date(2023, 1, 10))
    assert soon == "5"
    assert label == "due_soon"


def test_cli_returns_written_paths(tmp_path, monkeypatch):
    job_file = write_json(tmp_path, "jobs.json", [sample_job_record()])
    profile = write_json(tmp_path, "profile.json", {"skills": ["research"]})
    args = [
        "--job-data",
        str(job_file),
        "--profile",
        str(profile),
        "--icloud-dir",
        str(tmp_path / "icloud"),
        "--github-dir",
        str(tmp_path / "github"),
        "--repo-name",
        "Repo",
        "--skip-git",
    ]
    written = jam.main(args)
    assert len(written) == 2
    for path in written:
        assert path.exists()
