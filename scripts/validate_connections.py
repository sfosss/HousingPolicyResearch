"""Validate connectivity to configured third-party services."""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import Callable, Dict, Iterable, Tuple

import requests
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

load_dotenv()


def _get_timeout() -> float:
    try:
        return float(os.getenv("REQUEST_TIMEOUT", "5"))
    except ValueError:
        return 5.0


TIMEOUT = _get_timeout()


@dataclass
class ServiceCheck:
    name: str
    url: str
    headers: Dict[str, str] | None
    enabled: Callable[[], bool]

    def run(self) -> Tuple[bool, str]:
        if not self.enabled():
            return False, "Skipping (credentials not configured)"

        try:
            response = requests.get(self.url, timeout=TIMEOUT, headers=self.headers)
            response.raise_for_status()
        except (
            requests.exceptions.HTTPError
        ) as exc:  # pragma: no cover - network dependent
            return False, f"HTTP error: {exc}"
        except (
            requests.exceptions.RequestException
        ) as exc:  # pragma: no cover - network dependent
            return False, f"Connection failed: {exc}"
        return True, "OK"


def env_present(*keys: str) -> bool:
    return all(os.getenv(key) for key in keys)


def notion_headers() -> Dict[str, str]:
    token = os.getenv("NOTION_TOKEN", "")
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28",
    }


SERVICES: Iterable[ServiceCheck] = (
    ServiceCheck(
        name="OpenAI",
        url="https://api.openai.com/v1/models",
        headers={"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY', '')}"},
        enabled=lambda: env_present("OPENAI_API_KEY"),
    ),
    ServiceCheck(
        name="Notion",
        url="https://api.notion.com/v1/users",
        headers=notion_headers(),
        enabled=lambda: env_present("NOTION_TOKEN"),
    ),
    ServiceCheck(
        name="Zotero",
        url="https://api.zotero.org/",
        headers=None,
        enabled=lambda: env_present("ZOTERO_API_KEY", "ZOTERO_LIBRARY_ID"),
    ),
)


def main() -> None:
    success = True
    for service in SERVICES:
        status, detail = service.run()
        message = f"[{service.name}] {detail}"
        if status:
            logging.info(message)
        else:
            success = False if service.enabled() else success
            log_fn = logging.warning if service.enabled() else logging.info
            log_fn(message)

    if not success:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
