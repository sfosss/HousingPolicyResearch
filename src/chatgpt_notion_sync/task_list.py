"""Generate CSV task trackers for ChatGPT project and chat workflows.

This module provides a small automation that organises tasks by ChatGPT project
or chat, writes them to a CSV table with interactive checkboxes, and stores the
result in a predictable ``<Tasks>`` directory. The goal is to keep a unified
view of pending work regardless of whether the user opens ChatGPT on iOS,
macOS, or the web interface.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List, Sequence

DEFAULT_TASKS_DIR = Path.home() / "ChatGPT" / "Projects" / "Tasks"
DEFAULT_TASKS_FILE = "chat_tasks.csv"

CATEGORY_ORDER = {"project": 0, "unassigned": 1, "unknown": 2}
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


@dataclass
class ChatTask:
    """Representation of a task extracted from a chat thread."""

    description: str
    priority: str = "medium"
    status: str | bool | None = None

    def normalised_priority(self) -> str:
        return normalise_priority(self.priority)

    def checkbox(self) -> str:
        return "☑" if task_is_complete(self.status) else "☐"

    def status_label(self) -> str:
        return "done" if task_is_complete(self.status) else "open"


@dataclass
class ChatEntry:
    """Aggregate tasks for a single chat thread."""

    chat_title: str
    last_updated: str
    project: str | None = None
    subject: str | None = None
    tasks: List[ChatTask] = field(default_factory=list)

    def category(self) -> str:
        if self.project:
            return "project"
        if self.subject:
            return "unassigned"
        return "unknown"

    def last_updated_date(self) -> datetime:
        try:
            return datetime.fromisoformat(self.last_updated)
        except (ValueError, TypeError):
            return datetime.min

    def sorted_tasks(self) -> List[ChatTask]:
        return sorted(
            self.tasks,
            key=lambda task: (
                PRIORITY_ORDER.get(task.normalised_priority(), 99),
                task.description.lower(),
            ),
        )


CSV_HEADERS = [
    "category",
    "project",
    "subject",
    "chat_title",
    "last_updated",
    "task",
    "priority",
    "status",
    "checkbox",
]


def normalise_priority(priority: str | None) -> str:
    """Return a canonical priority label."""

    if not priority:
        return "medium"
    cleaned = "".join(
        char for char in priority.lower() if char.isalpha() or char.isspace()
    ).strip()
    if cleaned in {"urgent", "critical", "high"}:
        return "high"
    if cleaned in {"low", "minor"}:
        return "low"
    return "medium"


def task_is_complete(status: str | bool | None) -> bool:
    """Determine whether a task should be treated as complete."""

    if isinstance(status, bool):
        return status
    if not status:
        return False
    return status.strip().lower() in {
        "done",
        "complete",
        "closed",
        "resolved",
        "yes",
    }


def load_chat_tasks(path: Path) -> List[ChatEntry]:
    """Load chat tasks from a JSON export.

    The loader accepts either a list of chat dictionaries or a mapping with a
    ``chats`` key containing that list.
    """

    payload = json.loads(path.read_text())
    chats = (
        payload["chats"]
        if isinstance(payload, dict) and "chats" in payload
        else payload
    )
    entries: List[ChatEntry] = []
    for chat in chats:
        tasks: List[ChatTask] = []
        for task_data in chat.get("tasks", []):
            tasks.append(
                ChatTask(
                    description=task_data.get("description", ""),
                    priority=task_data.get("priority"),
                    status=task_data.get("status"),
                )
            )
        entries.append(
            ChatEntry(
                chat_title=chat.get("chat_title")
                or chat.get("title")
                or "Untitled chat",
                last_updated=(chat.get("last_updated") or chat.get("updated") or ""),
                project=chat.get("project"),
                subject=chat.get("subject"),
                tasks=tasks,
            )
        )
    return entries


def _chat_sort_key(entry: ChatEntry) -> tuple:
    return (
        CATEGORY_ORDER.get(entry.category(), 99),
        entry.project or entry.subject or "",
        -entry.last_updated_date().timestamp(),
        entry.chat_title.lower(),
    )


def build_rows(entries: Sequence[ChatEntry]) -> List[List[str]]:
    """Flatten chat entries into ordered CSV rows."""

    rows: List[List[str]] = []
    for chat in sorted(entries, key=_chat_sort_key):
        for task in chat.sorted_tasks():
            rows.append(
                [
                    chat.category(),
                    chat.project or "",
                    chat.subject or "",
                    chat.chat_title,
                    chat.last_updated,
                    task.description,
                    task.normalised_priority(),
                    task.status_label(),
                    task.checkbox(),
                ]
            )
    return rows


def ensure_tasks_directory(base_dir: Path | None = None) -> Path:
    """Ensure the <Tasks> directory exists."""

    target_dir = base_dir or DEFAULT_TASKS_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    return target_dir


def write_task_table(entries: Sequence[ChatEntry], output_path: Path) -> Path:
    """Write the task table to CSV."""

    ensure_tasks_directory(output_path.parent)
    rows = build_rows(entries)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(CSV_HEADERS)
        writer.writerows(rows)
    return output_path


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a ChatGPT tasks CSV table")
    parser.add_argument(
        "--chat-export",
        type=Path,
        required=True,
        help="Path to a JSON file with chat tasks",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_TASKS_DIR,
        help=(
            "Directory to write the <Tasks> CSV into "
            "(defaults to ChatGPT/Projects/Tasks)"
        ),
    )
    parser.add_argument(
        "--filename", default=DEFAULT_TASKS_FILE, help="Name of the generated CSV file"
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> Path:
    args = parse_args(argv)
    entries = load_chat_tasks(args.chat_export)
    output_path = ensure_tasks_directory(args.output_dir) / args.filename
    return write_task_table(entries, output_path)


if __name__ == "__main__":  # pragma: no cover - CLI passthrough
    main()
