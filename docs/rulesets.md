# Repository Rulesets and Integration Controls

This ruleset consolidates security, connectivity, and documentation expectations for the Housing Policy Research environment. It applies to all workstreams that rely on ChatGPT/Codex, Notion, GitHub, and Zotero.

## Core Principles

- **Security first**: Secrets stay out of version control and are stored in encrypted managers or GitHub Secrets.
- **Traceability**: Every automated sync must write minimal, non-sensitive logs for auditing.
- **Reproducibility**: Document configuration steps, validation results, and failure modes alongside the code that depends on them.
- **Least privilege**: Tokens and integrations must use the smallest scopes that support the workflow.
- **Dual flows**: Forward and reverse data paths (e.g., GitHub→Notion and Notion→GitHub) require mirrored validation checks.

## Platform Rules

### ChatGPT / Codex

- API keys are exported as `OPENAI_API_KEY` only in local shells or CI environments; never hard-code keys in scripts.
- CLI usage (`codex ...`) must be wrapped with rate-limit handling and time-stamped logs saved under `logs/`.
- Model prompts and outputs that influence research deliverables are archived in versioned Markdown (`docs/prompts/` and `docs/outputs/`).
- Reverse connection: When ChatGPT generates content that is committed to GitHub, record the prompt, model version, and reviewer in the commit description or linked issue.

### Notion

- Integration tokens are stored as `NOTION_API_KEY` and granted access only to required databases/pages.
- Database IDs used by scripts belong in `.env` (ignored by Git) or GitHub Secrets; document friendly names in `docs/notion-mapping.md`.
- Sync scripts must log the Notion page IDs touched, the source file, and the timestamp. Logs cannot include raw content.
- Reverse connection: Changes pulled from Notion into GitHub require a reviewer to confirm formatting and data classification before merging.

### GitHub

- Enable branch protection for default branches and require reviews for automation-generated pull requests.
- Use deploy keys or fine-scoped PATs for automation; avoid reusing human credentials in CI.
- Store all secret variables in `Settings → Secrets and variables → Actions`; mirror the names used in local `.env` files.
- Reverse connection: When external systems (Notion, Zotero, ChatGPT) push updates, the corresponding workflows must open pull requests rather than direct pushes.

### Zotero

- API keys live in `ZOTERO_API_KEY`; library IDs are stored separately (e.g., `ZOTERO_LIBRARY_ID`).
- Scripts must respect rate limits and include retry logic with exponential backoff.
- Exported bibliographies belong in `docs/references/` with dates and source library references.
- Reverse connection: GitHub→Zotero writes should be staged (dry-run first) and logged with item keys and collection names.

## Documentation and Error Handling

- Update `docs/environment-setup.md` and `docs/integration-plan.md` whenever new credentials, scopes, or workflows are introduced.
- Log connection checks in `logs/connection-checks/` (create if missing) with timestamps and anonymized results.
- Any script failure must capture: platform, endpoint, HTTP status/error code, retry count, and whether secrets were rotated.
- Replace corrupted or duplicated documentation assets; keep a pointer to the authoritative source (GitHub for code/docs, Zotero for citations, Notion for meeting notes).

## Validation Rules

Run these checks after configuration changes or quarterly:

1. **Credential audit** – Confirm `.env` and GitHub Secrets contain aligned keys for ChatGPT, Codex CLI, Notion, GitHub automation, and Zotero.
1. **Forward flow tests** – GitHub→Notion, GitHub→Zotero, and ChatGPT→GitHub scripts run without errors and log success entries.
1. **Reverse flow tests** – Notion→GitHub and Zotero→GitHub syncs execute in a staging branch and open pull requests with reviewers assigned.
1. **Access review** – Verify tokens remain scoped to intended resources; revoke unused credentials and rotate active keys.
1. **Log hygiene** – Ensure logs omit secrets and sensitive personal data; archive quarterly summaries in `docs/audit-notes/`.

## Generative Output Governance

- Maintain acceptance criteria for AI-generated content (accuracy, citation coverage, tone) in `docs/prompts/README.md`.
- All generative outputs must include provenance metadata: prompt ID, model, date, reviewer, and verification status.
- High-risk outputs (policy recommendations, legal drafts) require human review and sign-off before publication.
- Store evaluation results from scoring harnesses in `docs/outputs/evaluations/` and link them to issues or pull requests.

## Task Breakdown and Next Steps

1. **Create secret templates** – Add `.env.template` entries for OpenAI, Notion, GitHub, and Zotero keys; include comments on required scopes.
1. **Stand up logging folders** – Add `logs/connection-checks/` with a sample log format; ensure `.gitignore` permits committed, redacted logs.
1. **Document reverse syncs** – Write minimal runbooks for Notion→GitHub and Zotero→GitHub pipelines (staging branch usage, dry-run steps).
1. **Add validation scripts** – Implement smoke tests that hit each API with a dry-run and write structured results to `logs/connection-checks/`.
1. **Set review policy** – Configure branch protection and PR templates that require reviewers for automation-originated changes.

Track completion of these items in GitHub issues or the project roadmap, linking back to this ruleset for traceability.
