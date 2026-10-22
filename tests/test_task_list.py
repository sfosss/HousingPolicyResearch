from pathlib import Path
import json
import csv

from chatgpt_notion_sync import task_list


def write_export(tmp_path: Path, data) -> Path:
    path = tmp_path / "chat_export.json"
    path.write_text(json.dumps(data))
    return path


def sample_data():
    return {
        "chats": [
            {
                "chat_title": "Housing policy project",
                "project": "HousingPolicyResearch",
                "last_updated": "2024-05-10",
                "tasks": [
                    {
                        "description": "Draft outline",
                        "priority": "urgent",
                        "status": "open",
                    },
                    {
                        "description": "Sync Zotero notes",
                        "priority": "low",
                        "status": True,
                    },
                ],
            },
            {
                "chat_title": "Zotero quick chat",
                "subject": "Zotero",
                "last_updated": "2024-05-09",
                "tasks": [
                    {
                        "description": "Tag sources",
                        "priority": "medium",
                        "status": "done",
                    }
                ],
            },
            {
                "chat_title": "Misc scratchpad",
                "last_updated": "2024-05-11",
                "tasks": [
                    {
                        "description": "Clarify scope",
                        "priority": "unknown",
                        "status": "open",
                    }
                ],
            },
        ]
    }


def test_write_task_table_orders_by_category_and_priority(tmp_path):
    export = write_export(tmp_path, sample_data())
    entries = task_list.load_chat_tasks(export)
    output = task_list.write_task_table(entries, tmp_path / "tasks.csv")

    content = list(csv.reader(output.read_text().splitlines()))
    header = content[0]
    rows = content[1:]

    assert header == task_list.CSV_HEADERS

    # Project rows come first, ordered by priority within the chat
    project_rows = [row for row in rows if row[0] == "project"]
    assert project_rows[0][5] == "Draft outline"
    assert project_rows[0][6] == "high"
    assert project_rows[0][-1] == "☐"
    assert project_rows[1][5] == "Sync Zotero notes"
    assert project_rows[1][6] == "low"
    assert project_rows[1][-1] == "☑"

    # Unassigned subject chat follows
    assert rows[2][0] == "unassigned"
    assert rows[2][2] == "Zotero"

    # Unknown category appears last
    assert rows[-1][0] == "unknown"
    assert rows[-1][5] == "Clarify scope"


def test_normalise_priority_maps_synonyms():
    assert task_list.normalise_priority("Urgent!!!") == "high"
    assert task_list.normalise_priority("LOW") == "low"
    assert task_list.normalise_priority(None) == "medium"
