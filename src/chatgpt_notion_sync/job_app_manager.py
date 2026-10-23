"""Utilities for managing local job application repositories and reminders.

This module provides a CLI that automates the creation of a local Git
repository for job applications and exports a Reminders.app compatible CSV
template summarising each job posting.  The template focuses on progress
tracking and on capturing the metadata that is frequently needed when
submitting applications.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple


DEFAULT_ICLOUD_DIR = (
    Path.home()
    / "Library"
    / "Mobile Documents"
    / "com~apple~CloudDocs"
    / "JobApplications"
)
DEFAULT_GITHUB_DIR = Path.home() / "Documents" / "GitHub" / "JobApplications"
DEFAULT_REPO_NAME = "JobApplications"


PROGRESS_STATUSES = (
    "not_started",
    "drafted",
    "needs_revisions",
    "complete",
)

REMINDERS_SUBDIR = "Reminders"
APPLICATIONS_SUBDIR = "Applications"
REFERENCE_SUBDIR = "Reference"

DEADLINE_SOON_THRESHOLD_DAYS = 7


def normalise_status(value: str | None) -> str:
    """Return a canonical progress status string."""

    if not value:
        return PROGRESS_STATUSES[0]
    value = value.strip().lower().replace(" ", "_")
    return value if value in PROGRESS_STATUSES else PROGRESS_STATUSES[0]


def tokenise(text: str | None) -> List[str]:
    if not text:
        return []
    return re.findall(r"[A-Za-z]+", text.lower())


def derive_keywords(*texts: str | None) -> str:
    tokens: List[str] = []
    for text in texts:
        tokens.extend(tokenise(text))
    unique = sorted({token for token in tokens if len(token) > 3})
    return ", ".join(unique[:25])


def estimate_match(prerequisites: str | None, profile_tokens: Sequence[str]) -> float:
    job_tokens = set(tokenise(prerequisites))
    if not job_tokens:
        return 0.0
    if not profile_tokens:
        return 0.0
    matches = len(job_tokens.intersection(profile_tokens))
    return round((matches / len(job_tokens)) * 100, 2)


def parse_deadline(deadline: str | None) -> date | None:
    if not deadline:
        return None
    try:
        return datetime.strptime(deadline, "%Y-%m-%d").date()
    except ValueError:
        return None


def describe_deadline(
    deadline: str | None, today: date | None = None
) -> Tuple[str, str]:
    parsed = parse_deadline(deadline)
    if not parsed:
        return "", "unspecified"
    today = today or date.today()
    delta = (parsed - today).days
    if delta < 0:
        label = "overdue"
    elif delta <= DEADLINE_SOON_THRESHOLD_DAYS:
        label = "due_soon"
    else:
        label = "scheduled"
    return str(delta), label


def ensure_directory(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def initialise_git_repository(path: Path) -> None:
    if (path / ".git").exists():
        return
    subprocess.run(["git", "init", str(path)], check=True)


@dataclass
class JobApplicationRecord:
    company: str
    job_title: str
    department: str | None = None
    description_summary: str | None = None
    responsibilities: str | None = None
    required_documents: List[str] = field(default_factory=list)
    local_files: List[str] = field(default_factory=list)
    web_links: List[str] = field(default_factory=list)
    application_file: str | None = None
    submission_method: str | None = None
    prerequisites: str | None = None
    salary: str | None = None
    date_posted: str | None = None
    submission_deadline: str | None = None
    tags: List[str] = field(default_factory=list)
    resume_status: str | None = None
    cover_letter_status: str | None = None
    writing_sample_status: str | None = None
    references_status: str | None = None

    def pending_components(self) -> List[str]:
        labels = {
            "resume": self.resume_status,
            "cover_letter": self.cover_letter_status,
            "writing_sample": self.writing_sample_status,
            "references": self.references_status,
        }
        return [
            label
            for label, status in labels.items()
            if normalise_status(status) != "complete"
        ]

    def to_row(self, profile_tokens: Sequence[str]) -> List[str]:
        keywords = derive_keywords(self.description_summary, self.responsibilities)
        match_score = estimate_match(self.prerequisites, profile_tokens)
        days_until_deadline, deadline_status = describe_deadline(
            self.submission_deadline
        )
        attention_flags = self.pending_components()
        if deadline_status in {"overdue", "due_soon"}:
            attention_flags.append(f"deadline_{deadline_status}")
        attention_summary = ", ".join(attention_flags)
        return [
            normalise_status(self.resume_status),
            normalise_status(self.cover_letter_status),
            normalise_status(self.writing_sample_status),
            normalise_status(self.references_status),
            self.company,
            self.department or "",
            self.job_title,
            self.description_summary or "",
            self.responsibilities or "",
            "; ".join(self.required_documents),
            "; ".join(self.local_files),
            "; ".join(self.web_links),
            self.application_file or "",
            self.submission_method or "",
            self.prerequisites or "",
            f"{match_score}",
            self.salary or "",
            self.date_posted or "",
            self.submission_deadline or "",
            keywords,
            "; ".join(self.tags),
            days_until_deadline,
            deadline_status,
            attention_summary,
        ]


CSV_HEADERS = [
    "resume_status",
    "cover_letter_status",
    "writing_sample_status",
    "references_status",
    "company",
    "department",
    "job_title",
    "job_summary",
    "key_responsibilities",
    "required_documents",
    "local_files",
    "web_links",
    "application_file",
    "submission_method",
    "prerequisites",
    "match_percent",
    "salary",
    "date_posted",
    "submission_deadline",
    "keywords",
    "tags",
    "days_until_deadline",
    "deadline_status",
    "attention_summary",
]


def load_job_records(path: Path) -> List[JobApplicationRecord]:
    data = json.loads(path.read_text())
    records: List[JobApplicationRecord] = []
    for entry in data:
        records.append(
            JobApplicationRecord(
                company=entry["company"],
                job_title=entry["job_title"],
                department=entry.get("department"),
                description_summary=entry.get("summary"),
                responsibilities=entry.get("responsibilities"),
                required_documents=entry.get("required_documents", []),
                local_files=entry.get("local_files", []),
                web_links=entry.get("web_links", []),
                application_file=entry.get("application_file"),
                submission_method=entry.get("submission_method"),
                prerequisites=entry.get("prerequisites"),
                salary=entry.get("salary"),
                date_posted=entry.get("date_posted"),
                submission_deadline=entry.get("submission_deadline"),
                tags=entry.get("tags", []),
                resume_status=entry.get("resume_status"),
                cover_letter_status=entry.get("cover_letter_status"),
                writing_sample_status=entry.get("writing_sample_status"),
                references_status=entry.get("references_status"),
            )
        )
    return records


def load_profile_tokens(profile_path: Path | None) -> List[str]:
    if not profile_path:
        return []
    profile_data = json.loads(profile_path.read_text())
    texts: List[str] = []
    for key in ("skills", "education", "interests", "goals"):
        value = profile_data.get(key)
        if isinstance(value, str):
            texts.append(value)
        elif isinstance(value, Iterable):
            texts.extend(str(item) for item in value)
    tokens = []
    for text in texts:
        tokens.extend(tokenise(text))
    return tokens


def write_reminders_template(
    records: Sequence[JobApplicationRecord],
    profile_tokens: Sequence[str],
    output_path: Path,
) -> Path:
    ensure_directory(output_path.parent)
    ordered_records = sorted(
        records,
        key=lambda record: parse_deadline(record.submission_deadline) or date.max,
    )
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(CSV_HEADERS)
        for record in ordered_records:
            writer.writerow(record.to_row(profile_tokens))
    return output_path


def resolve_github_repo_path(github_dir: Path, repo_name: str) -> Path:
    """Return the concrete path to the JobApplications repository."""

    # Allow callers to either pass the parent directory along with a repo name
    # or the fully qualified repository path inside ``github_dir``.  The goal is
    # to ensure the automation never leaves the JobApplications tree while still
    # supporting existing environment setups.
    if github_dir.name == repo_name:
        return github_dir
    return github_dir / repo_name


def _declutter_workspace(base_dir: Path) -> Path:
    ensure_directory(base_dir / APPLICATIONS_SUBDIR)
    ensure_directory(base_dir / REFERENCE_SUBDIR)
    reminders_dir = ensure_directory(base_dir / REMINDERS_SUBDIR)
    return reminders_dir


def configure_repository_structure(
    icloud_dir: Path, github_dir: Path, repo_name: str, init_repo: bool = True
) -> List[Path]:
    icloud_repo = ensure_directory(icloud_dir)
    github_repo = ensure_directory(resolve_github_repo_path(github_dir, repo_name))
    if init_repo:
        initialise_git_repository(github_repo)
    return [_declutter_workspace(icloud_repo), _declutter_workspace(github_repo)]


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Manage job application reminders template"
    )
    parser.add_argument(
        "--job-data",
        type=Path,
        required=True,
        help="Path to a JSON file with job postings",
    )
    parser.add_argument(
        "--profile", type=Path, help="Path to a JSON profile for estimating job match"
    )
    parser.add_argument(
        "--output-name",
        default="job_application_reminders.csv",
        help="Name of the CSV template file",
    )
    parser.add_argument("--icloud-dir", type=Path, default=DEFAULT_ICLOUD_DIR)
    parser.add_argument("--github-dir", type=Path, default=DEFAULT_GITHUB_DIR)
    parser.add_argument("--repo-name", default=DEFAULT_REPO_NAME)
    parser.add_argument(
        "--skip-git", action="store_true", help="Do not initialise Git repository"
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> List[Path]:
    args = parse_args(argv)
    targets = configure_repository_structure(
        icloud_dir=args.icloud_dir,
        github_dir=args.github_dir,
        repo_name=args.repo_name,
        init_repo=not args.skip_git,
    )
    records = load_job_records(args.job_data)
    profile_tokens = load_profile_tokens(args.profile)
    written_paths = []
    for directory in targets:
        output_path = directory / args.output_name
        written_paths.append(
            write_reminders_template(records, profile_tokens, output_path)
        )
    return written_paths


if __name__ == "__main__":  # pragma: no cover - CLI passthrough
    main()
