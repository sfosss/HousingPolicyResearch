# Connection & Reverse-Flow Checklists

Use these procedures to confirm that OpenAI API, Notion, GitHub, and Zotero remain securely linked in both directions. Incorporate the steps into CI jobs or scheduled automations.

## 1. Shared Preparation

1. Copy `.env.template` to `.env` and populate the required tokens.
1. Run `scripts/connection-checks.sh` (placeholder) or the equivalent automation runner.
1. Store logs in `logs/connection-checks/YYYY-MM-DD.md` with timestamps and command output.

## 2. Individual Connection Tests

| Integration | Command or API Call                                                                       | Expected Result                    | Remediation                                             |
| ----------- | ----------------------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------- |
| OpenAI API  | `curl https://api.openai.com/v1/models -H "Authorization: Bearer $OPENAI_API_KEY"`        | HTTP 200 with model list           | Rotate key; verify billing status.                      |
| Notion      | `python scripts/notion_ping.py`                                                           | HTTP 200 from `/v1/databases/{id}` | Confirm database sharing and token scopes.              |
| GitHub      | `gh api user` or `curl https://api.github.com/user -H "Authorization: token $GITHUB_PAT"` | Returns authenticated user         | Regenerate PAT with `repo` scope or switch to SSH auth. |
| Zotero      | `python scripts/zotero_ping.py`                                                           | HTTP 200 with library metadata     | Reissue API key; verify library ID.                     |

## 3. Reverse-Flow Validation

### GitHub → Notion

1. Trigger the documentation sync workflow (GitHub Action `notion-sync.yml`).
1. Confirm the Notion database reflects the latest commit metadata.
1. Add a test issue link and ensure the Notion page includes the backlink.

### Notion → Zotero

1. Export a reading list view as JSON using the Notion API.
1. Run the Zotero sync script to ingest the entries.
1. Validate that Zotero collections show the new citations with `source=notion` in the extra field.

### Zotero → GitHub

1. Execute `python scripts/zotero_to_github.py --dry-run`.
1. Inspect the generated markdown in `logs/zotero-exports/`.
1. Open a PR or issue draft that includes the exported annotations, ensuring sensitive notes are redacted.

### OpenAI → GitHub

1. Archive the most recent session transcript into `logs/openai/`.
1. Run the lint workflow to ensure transcripts contain metadata headers (prompt, timestamp, model).
1. Reference the archive from the related GitHub issue for traceability.

## 4. Security Controls to Verify

- `.env` file is excluded via `.gitignore`.
- GitHub Secrets mirror local variable names for CI.
- Logs omit API keys and personally identifiable information.
- Key rotation dates are tracked in Notion's security dashboard.

## 5. Reporting

Summarize each run in the Capstone tracker:

1. Status (pass/fail) for every integration and reverse flow.
1. Action items with owners and deadlines.
1. Links to GitHub issues raised during the checks.

Maintaining this checklist guarantees that integrations stay aligned with the automation roadmap and security posture described elsewhere in the repository.
