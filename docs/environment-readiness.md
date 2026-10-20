# Environment Readiness Checklist

Use this checklist before running any automation so that connections and reverse connections across ChatGPT, Codex, Notion, GitHub, and Zotero are secure and reproducible.

## 1. Secrets and Local Files

- Copy `.env.template` to `.env` and populate every variable.
- Confirm `.env` is ignored by Git and stored in a password manager for backup.
- Mirror the same variable names in GitHub repository **Secrets** and **Variables** for Actions.
- Store SSH keys for GitHub in a secure keychain; restrict file permissions to `600`.

## 2. Platform Credentials

| Platform | Required Values | Scope Guidance | Verification Command |
| --- | --- | --- | --- |
| ChatGPT / OpenAI | `OPENAI_API_KEY`, `OPENAI_ORG_ID` (optional) | No broad organization access unless needed; rotate every 90 days. | `curl https://api.openai.com/v1/models -H "Authorization: Bearer $OPENAI_API_KEY"` |
| Codex CLI | Uses `OPENAI_API_KEY` | Same scope as ChatGPT; avoid shared keys. | `codex --version` |
| Notion | `NOTION_TOKEN`, database IDs | Share target pages with the integration user only. | `python scripts/notion_ping.py` |
| GitHub | `GITHUB_PAT` or SSH keys, webhook secret | PAT scoped to `repo` + `workflow`; deploy keys read-only when possible. | `gh api user` or `git ls-remote git@github.com:<org>/<repo>.git` |
| Zotero | `ZOTERO_API_KEY`, library/collection IDs | Library-specific key; restrict write scope if read-only jobs. | `python scripts/zotero_ping.py` |

## 3. Forward Flows (toward GitHub)

1. **ChatGPT/Codex → GitHub**
   - Save transcripts to `logs/generative/` with metadata from `docs/resource-index.md`.
   - Push sanitized files to a feature branch and open a PR referencing the source issue.

2. **Notion → GitHub**
   - Export relevant databases (tasks, research log) via API.
   - Run ingestion scripts to write markdown summaries into `docs/` or `comments/`.

3. **Zotero → GitHub**
   - Use `python scripts/zotero_to_github.py --dry-run` to generate markdown under `logs/zotero-exports/`.
   - After review, commit redacted exports and link them to related issues.

## 4. Reverse Flows (from GitHub)

1. **GitHub → Notion**
   - Run the Notion sync workflow (`.github/workflows/notion-sync.yml`).
   - Verify the Notion page reflects commit metadata, backlinks, and status updates.

2. **GitHub → Zotero**
   - Publish curated reading lists or citations from markdown to Zotero collections.
   - Confirm Zotero notes include `source=github` and the originating issue/PR URL.

3. **GitHub → ChatGPT/Codex context**
   - Provide issue numbers and file paths when generating outputs.
   - Archive resulting transcripts back into `logs/generative/` for provenance.

## 5. Logging and Evidence

- Store connection test results under `logs/connection-checks/YYYY-MM-DD.md` with timestamps and commands.
- Record reverse-flow validations in the same log file so auditors can trace both directions.
- Add pointers to the log entries inside relevant GitHub issues or the Capstone tracker.

## 6. Security Verification

- Review `.gitattributes` and `.gitignore` to ensure secrets and large restricted files stay out of commits.
- Enable branch protection and required status checks for main branches.
- Rotate credentials after demos, personnel changes, or suspected leaks; document rotations in Notion.

## 7. Readiness Sign-off

Before running scheduled jobs or CI pipelines, confirm:

- [ ] All platform checks in [`docs/connection-checks.md`](connection-checks.md) pass locally.
- [ ] GitHub Actions secrets align with the local `.env` values.
- [ ] Reverse-flow links (GitHub↔Notion↔Zotero; ChatGPT/Codex→GitHub) are documented and tested.
- [ ] Latest generative outputs are archived under `logs/generative/` with reviewers assigned.
