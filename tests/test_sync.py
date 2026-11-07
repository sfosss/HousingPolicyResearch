from unittest.mock import MagicMock, patch

from chatgpt_notion_sync.config import Settings
from chatgpt_notion_sync.sync import sync_database


def make_page(page_id: str, title: str, content: str):
    return {
        "id": page_id,
        "title": title,
        "content": content,
        "properties": {
            "Name": {
                "title": [
                    {
                        "plain_text": title,
                    }
                ]
            }
        },
    }


def test_sync_database_updates_summary_and_appends_change_log():
    notion_client = MagicMock()
    page = make_page("page-123", "Test page", "Some detailed content")
    notion_client.databases.query.return_value = {"results": [page]}

    llm_client = MagicMock()
    llm_client.summarize.return_value = "A compact summary"

    settings = Settings(
        NOTION_TOKEN="token",
        NOTION_DATABASE_ID="db-id",
        NOTION_SUMMARY_PROPERTY_NAME="Summary",
        NOTION_CHANGELOG_PAGE_ID="page-change-log",
    )

    with patch("chatgpt_notion_sync.sync.append_change_log") as mock_append:
        sync_database(notion_client, llm_client, settings)

    notion_client.databases.query.assert_called_once_with(database_id="db-id")
    notion_client.pages.update.assert_called_once()
    update_kwargs = notion_client.pages.update.call_args.kwargs
    assert update_kwargs["page_id"] == "page-123"
    content = update_kwargs["properties"]["Summary"]["rich_text"][0]["text"]["content"]
    assert content == "A compact summary"

    mock_append.assert_called_once()
    change_log_page_id = mock_append.call_args.kwargs["change_log_page_id"]
    assert change_log_page_id == "page-change-log"


def test_sync_database_skips_change_log_when_id_missing():
    notion_client = MagicMock()
    page = make_page("page-999", "Other page", "Different content")
    notion_client.databases.query.return_value = {"results": [page]}

    llm_client = MagicMock()
    llm_client.summarize.return_value = "Summary"

    settings = Settings(NOTION_DATABASE_ID="db-id")

    with patch("chatgpt_notion_sync.sync.append_change_log") as mock_append:
        sync_database(notion_client, llm_client, settings)

    mock_append.assert_not_called()
