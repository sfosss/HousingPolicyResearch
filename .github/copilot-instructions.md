source .venv/bin/activate
python -m pytest tests/          # Run tests
pre-commit run --all-files       # Run code quality checks
python <script>                  # Execute any Python script# Housing Policy Research – Copilot Instructions

Purpose: give AI agents the minimum project-specific context to ship safe, accurate changes fast. Keep instructions short and actionable.

## Big Picture

- Docs-first repo: key sources live in [docs](../docs) (integration plan, connection checks, APA style, resources index/CSV, universal linking). New AI text must be tracked in [docs/generative-output-version-control.md](../docs/generative-output-version-control.md).
- Two code areas: Python utilities for ChatGPT/Notion task hygiene in [src/chatgpt_notion_sync](../src/chatgpt_notion_sync) and Raycast extension commands in [src/commands](../src/commands) calling a backend via [src/utils/api.ts](../src/utils/api.ts).
- Security baseline: see [SECURITY.md](../SECURITY.md) and [docs/environment-setup.md](../docs/environment-setup.md); secrets live in env vars per [.env.template](../.env.template). Detect-secrets baseline is enforced via [.pre-commit-config.yaml](../.pre-commit-config.yaml).

## Python utilities

- [src/chatgpt_notion_sync/sync.py](../src/chatgpt_notion_sync/sync.py) pulls Notion pages, builds an LLM prompt, updates the `NOTION_SUMMARY_PROPERTY_NAME`, and optionally appends to a changelog page. Config comes from [src/chatgpt_notion_sync/config.py](../src/chatgpt_notion_sync/config.py) (env var names documented there).
- [src/chatgpt_notion_sync/job_app_manager.py](../src/chatgpt_notion_sync/job_app_manager.py) CLI: reads job postings/profile JSON, writes reminders CSVs to iCloud and GitHub mirrors, and can init a git repo. Progress/status values are normalised; deadlines bucket into overdue/due_soon/scheduled.
- [src/chatgpt_notion_sync/task_list.py](../src/chatgpt_notion_sync/task_list.py) flattens ChatGPT chat exports into a priority-sorted CSV with checkbox markers.
- Tests live in [tests](../tests); run `python -m pytest` from repo root (pyproject sets `src` on PYTHONPATH). Keep changes testable without hitting live services; mock clients like in [tests/test_sync.py](../tests/test_sync.py).

## Raycast extension

- Commands: Add Source, Bill Sweep, Draft Section in [src/commands](../src/commands); all POST to the assistant backend defined in Raycast prefs `assistant_base_url` and optional `api_timeout_ms` (see [raycast.manifest.json](../raycast.manifest.json)).
- API client: [src/utils/api.ts](../src/utils/api.ts) wraps `/sweep_bills`, `/generate_section`, `/add_source` with abortable fetch + error surfacing. Respect expected payloads (jurisdictions list; section/prompt strings; title/url/notes).
- Build/test: no package.json yet; when editing commands, keep JSX minimal and toasts/validation consistent with existing patterns. Ensure URLs are validated client-side (AddSource) and selections non-empty (BillSweep).

## Docs, citations, and data hygiene

- APA 7th is mandatory: follow [docs/STYLE-APA.md](../docs/STYLE-APA.md). Every new source goes in tandem to [docs/resources-index.md](../docs/resources-index.md) (annotated) and [docs/resources.csv](../docs/resources.csv) (tabular) with relevance, application note, quality flags, and DOI/URL.
- Generative output provenance: log new AI-authored docs in [docs/generative-output-version-control.md](../docs/generative-output-version-control.md) with creation/update dates and verification notes.
- Roadmap/context: [docs/project-roadmap.md](../docs/project-roadmap.md) lists pending work; [docs/integration-plan.md](../docs/integration-plan.md) and [docs/connection-checks.md](../docs/connection-checks.md) describe platform wiring and validation steps.

## Quality and safety gates

- Run `pre-commit run --all-files` if available; hooks include black, flake8, mdformat, detect-secrets.
- Keep secrets out of the repo; never hardcode tokens or URLs with keys. Use `.env` (ignored) and GitHub secrets.
- Prefer deterministic inputs/fixtures for tests and scripts; avoid network calls in unit tests.
- If adding new AI outputs or citations, validate links, DOI resolution, and flag paywalled items as `[Paywalled]` in both index and CSV.

## PR expectations

- Small, scoped changes with docs updates alongside code.
- Reference roadmap items/issues and list checks run (pytest, manual command exercise).
- Describe any backend assumptions for Raycast commands (endpoint paths/auth) and sample payloads.

## Version

- Maintainer: Housing Policy Research team
- Last updated: 2025-12-30
- Review cadence: Quarterly or as major changes occur
