# Environment Integrations and Documentation

This document captures the current integration points that support the Housing Policy Research project. Data flows are directional and reviewed; cloud drives and AI workspaces are not bidirectional replicas of the repository. Box, ChatGPT exports, and Claude workspace intake follow [`COLLABORATIVE_DATA_INTAKE.md`](COLLABORATIVE_DATA_INTAKE.md).

## 1. System Overview

| Platform                   | Purpose                                                                       | Direction of Sync                                    | Primary Artifacts                     |
| -------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------- |
| ChatGPT / OpenAI workspace | Conversational research assistance, code review, and task planning            | ChatGPT → GitHub, GitHub → ChatGPT (through prompts) | Task instructions, generated analyses |
| Claude workspace           | Collaborative drafting and project instructions                              | Claude export → isolated staging → reviewed GitHub PR | Curated decisions and drafts           |
| Codex automations          | Scripted agents that perform file moves, commit updates, or generate analyses | Codex ↔ GitHub                                       | Automation scripts, commit messages   |
| Box shared folders         | Human collaboration, exchange, and retention                                  | Box → isolated staging; reviewed release → dedicated Box destination | Source packages and release artifacts |
| Notion workspace           | Project management, literature summaries, meeting notes                       | Notion ↔ GitHub (manual exports or API scripts)      | Kanban boards, research briefs        |
| GitHub repository          | Source of truth for datasets, documentation, scripts                          | GitHub ↔ All                                         | Code, data, documentation             |
| Zotero group library       | Reference manager with citation metadata                                      | Zotero → Notion / GitHub (via exports)               | Bibliographies, PDF annotations       |

## 2. Secure Connection Checklist

1. **Account hygiene**
   - Enable multi-factor authentication on GitHub, Notion, and Zotero accounts.
   - Rotate OpenAI API keys and store them in an encrypted vault (e.g., 1Password, Bitwarden).
1. **Network boundaries**
   - Restrict API access by IP where possible (GitHub PATs, Notion integrations).
   - Use SSH for Git operations; add keys with passphrases and review authorized_keys quarterly.
1. **Secret management**
   - Store shared secrets in GitHub Actions as encrypted secrets; never commit plaintext tokens.
   - For local development, place credentials in `.env` files excluded by `.gitignore`.
1. **Audit logging**
   - Enable GitHub organization audit log exports.
   - Subscribe to Notion integration access logs and Zotero API usage summaries.

## 3. Integration Setup Steps

### 3.1 ChatGPT / Codex → GitHub

1. Clone this repository into the approved active root, never inside a Box/iCloud sync tree, and create a dedicated OpenAI API key only when an automation requires API access.
1. Inventory ChatGPT, Claude, or Box sources with an ignored local collaboration manifest before selecting anything for staged import.
1. Prefer the run-scoped `GITHUB_TOKEN`; when a human token is required, use a fine-grained, repository-scoped, expiring token with only the operation-specific permissions documented in [`REPOSITORY_SECURITY_PERMISSIONS.md`](REPOSITORY_SECURITY_PERMISSIONS.md).
1. Run automations inside a hardened environment (container or VM) with read/write access only to the repository workspace.

### 3.2 GitHub ↔ Notion

1. Create a Notion integration and invite it to the workspace pages required for synchronization.
1. Use a sync tool (e.g., Notion2Git, custom Python script) to export Notion databases as Markdown into the `docs/notion-sync/` directory.
1. Schedule weekly sync jobs and review diffs before merging into the default branch.

### 3.3 Zotero → GitHub / Notion

1. Install the Zotero Better BibTeX plugin to generate citation keys.
1. Export collections as `.bib` files into `references/` and commit alongside datasets for reproducibility.
1. Configure Notion with the Zotero API token to embed bibliography entries in project dashboards.

### 3.4 Reverse Sync Validation (GitHub → External Tools)

To guarantee that updates originating in GitHub propagate back to the research tools, validate the following reverse paths at
least once per release cycle:

1. **GitHub → ChatGPT / Codex prompts**
   - Reference commit hashes or permalinks when drafting prompts so conversational agents can cite the latest code state.
   - Store curated prompt templates under `docs/prompts/` (planned) and update them whenever APIs or datasets change.
1. **GitHub → Notion**
   - Configure a Notion database view that mirrors the `docs/` directory; automate Markdown imports via the Notion API and
     confirm timestamps align with the Git commit history.
   - Record the sync status (last import time, actor) in a Notion property to provide traceability back to repository updates.
1. **GitHub → Zotero**
   - Publish release notes that list new or updated bibliography exports so Zotero maintainers know when to refresh
     collections.
   - Keep a `references/CHANGELOG.md` file (planned) that links Zotero collection IDs to the corresponding Git commits.

## 4. Error Corrections and Gaps Filled

- **Missing documentation**: Added this document to capture integration requirements and security expectations.
- **Automation path validation**: Confirmed that automation scripts should reside under `scripts/`; ensure directory exists and is referenced consistently (see follow-up task list).
- **Alias artifacts**: The repository currently contains a macOS alias file (`Capstone alias`). Confirm need; replace with platform-neutral documentation or remove if obsolete.

## 5. Task Breakdown for Next Steps

1. **Documentation hardening**
   - [ ] Expand `README.md` with a quick-start section linking to this guide.
   - [ ] Create architecture diagram illustrating data flows (store under `docs/diagrams/`).
   - [ ] Add `docs/prompts/` with reference templates that describe how to invoke automations from ChatGPT or Codex tools.
1. **Automation stabilization**
   - [ ] Add CI workflow to lint and test shell scripts (e.g., `shellcheck`).
   - [ ] Parameterize source/target paths in automation scripts via environment variables.
   - [ ] Create dry-run modes for automation scripts so they can be exercised in CI without moving sensitive files.
1. **Integration validation**
   - [ ] Implement a health-check script that verifies access to Notion, Zotero, and GitHub APIs.
   - [ ] Document fallback procedures for API outages.
   - [ ] Stand up a nightly job that performs round-trip validation (GitHub → Notion → GitHub) and emits alerts when
     discrepancies are detected.
1. **Security follow-up**
   - [ ] Schedule quarterly credential rotation reminders in Notion.
   - [ ] Review GitHub branch protection rules and enable required reviews for `main`.
   - [ ] Add dependency and secret scanning results to the project Notion dashboard for cross-tool visibility.
1. **Generative output readiness**
   - [ ] Define a publishing pipeline for AI-generated briefs, including manual review checkpoints before GitHub commits.
   - [ ] Capture prompt/response audit logs in Notion or Zotero notes to preserve research provenance.
   - [ ] Map each planned generative artifact (e.g., policy memo, dataset summary) to the repositories and integrations needed
     to produce it so future automation work can be scoped precisely.

## 6. Maintenance Cadence

| Activity                | Frequency                      | Owner               | Notes                                             |
| ----------------------- | ------------------------------ | ------------------- | ------------------------------------------------- |
| Documentation review    | Quarterly                      | Project lead        | Ensure integration steps reflect tooling changes. |
| Secret rotation         | Quarterly or upon staff change | Security POC        | Track via Notion task board.                      |
| Automation script audit | Bi-annually                    | Engineering support | Run `shellcheck` and update dependencies.         |
| Bibliography sync       | Monthly                        | Research analyst    | Export from Zotero and commit updates.            |

______________________________________________________________________

_Last updated: 2025-09-25_
