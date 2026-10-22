"""Application configuration helpers.

This module currently offers a tiny settings container that mirrors the
environment variables used by the sync command.  The implementation is
intentionally lightweight so that tests can instantiate the settings with
explicit values while the production code can still rely on the environment.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Optional
import os


@dataclass
class Settings:
    """Container for configuration flags.

    The attributes mirror the environment variables that would normally be set
    when the synchronisation script is executed.  Only the pieces that are
    needed by the tests are modelled here which keeps the code portable and
    dependency free.
    """

    # Names of the environment variables.  These act as both documentation and
    # defaults for :meth:`from_env`.
    ENV_NOTION_TOKEN: ClassVar[str] = "NOTION_TOKEN"
    ENV_NOTION_DATABASE_ID: ClassVar[str] = "NOTION_DATABASE_ID"
    ENV_NOTION_SUMMARY_PROPERTY_NAME: ClassVar[str] = "NOTION_SUMMARY_PROPERTY_NAME"
    ENV_NOTION_CHANGELOG_PAGE_ID: ClassVar[str] = "NOTION_CHANGELOG_PAGE_ID"

    # Actual configuration values.  They intentionally use the same naming as
    # the environment variables to reduce the amount of translation needed in
    # the rest of the code base.
    NOTION_TOKEN: str = ""
    NOTION_DATABASE_ID: str = ""
    NOTION_SUMMARY_PROPERTY_NAME: str = "Summary"
    NOTION_CHANGELOG_PAGE_ID: Optional[str] = None

    @classmethod
    def from_env(cls) -> "Settings":
        """Create a :class:`Settings` instance from environment variables."""

        return cls(
            NOTION_TOKEN=os.getenv(cls.ENV_NOTION_TOKEN, ""),
            NOTION_DATABASE_ID=os.getenv(cls.ENV_NOTION_DATABASE_ID, ""),
            NOTION_SUMMARY_PROPERTY_NAME=os.getenv(
                cls.ENV_NOTION_SUMMARY_PROPERTY_NAME,
                "Summary",
            ),
            NOTION_CHANGELOG_PAGE_ID=os.getenv(cls.ENV_NOTION_CHANGELOG_PAGE_ID)
            or None,
        )
