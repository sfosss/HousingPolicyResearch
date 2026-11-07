# Connection Check Runbook (ChatGPT, Codex, Notion, GitHub, Zotero)

Use this runbook whenever tokens are rotated or new environments are provisioned.

## Prerequisites

- Local `.env` populated with `OPENAI_API_KEY`, `NOTION_TOKEN`, `ZOTERO_API_KEY`, and `GITHUB_TOKEN` (scoped minimally).
- SSH keys or Git credential helper configured.
- `python3` and `node` available for CLI smoke tests.

## Steps

1. **Load Environment**

   - Copy `.env.template` (if available) and fill values; never commit `.env`.
   - Run `source .env` (or your shell equivalent) before executing checks.

1. **ChatGPT / Codex**

   - Run `codex --help` to confirm CLI access.
   - Execute a short prompt and save output to `logs/connection-checks/chatgpt-$(date +%Y%m%d).log`.

1. **GitHub**

   - Run `gh auth status` (if GitHub CLI is installed) or perform a `git ls-remote` against the repo URL to confirm access.
   - Validate that repository secrets mirror local variable names.

1. **Notion**

   - Call a lightweight read API request (e.g., fetch a database title) using `curl` or a script; log response headers to `logs/connection-checks/notion-$(date +%Y%m%d).log`.

1. **Zotero**

   - Use `pyzotero` or the Web API to list collections; save output to `logs/connection-checks/zotero-$(date +%Y%m%d).log`.

1. **Reverse Flows**

   - Push a sample markdown note from GitHub → Notion.
   - Export a Zotero annotation JSON and commit it to a scratch branch to validate Zotero → GitHub.
   - Archive the prompt and response from Step 2 into `logs/chatgpt/` for ChatGPT → GitHub traceability.

1. **Audit & Rotation**

   - Review all logs for credential leakage; redact and delete as needed.
   - Rotate any test tokens; record the rotation date in Notion.

## Success Criteria

- All five services respond with authenticated requests.
- Logs exist under `logs/connection-checks/` with timestamps and without secrets.
- Reverse-flow artifacts are present or referenced in Notion for audit purposes.

## References

- [Environment Integration and Documentation Plan](integration-plan.md)
- [NYC Housing Subsidy Reform Ops Manual](NYC_Housing_Subsidy_Reform_Ops_Manual.md)
- [Report Blueprint](nyc-housing-subsidy-report-blueprint.md)
