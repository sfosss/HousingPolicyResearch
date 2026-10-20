# Resource Index and Generative Output Handling

Use this index to quickly locate documentation across the repository and to standardize how previous generative output text files are captured in version control.

## Core Documentation

| Path | Purpose | Notes |
| --- | --- | --- |
| `README.md` | Project overview and quick start steps for the Housing Policy Research repo. | Start here for local setup. |
| `docs/integration-plan.md` | End-to-end environment plan for ChatGPT, Codex, Notion, GitHub, and Zotero. | Includes prerequisites, security controls, and roadmap items. |
| `docs/connection-checks.md` | Checklists for verifying connectivity and reverse data flows. | Reference when running periodic audits. |
| `docs/environment-readiness.md` | End-to-end readiness checklist for secrets, connections, and reverse flows. | Run before automation or CI jobs. |
| `docs/generative-output-tasks.md` | Detailed breakdown of the generative AI workstreams (prompt library, evaluation, governance). | Aligns with Section 8 of the integration plan. |
| `docs/universal-linking-guide.md` | Guidance for deep links across mobile and web clients. | Useful when wiring PRs or briefs to external apps. |
| `logs/generative/README.md` | Canonical guide for archived generative outputs. | Defines naming, metadata, and version control process. |
| `capstone/README.md` | Migration notes and next steps for the capstone documentation track. | Track capstone milestones and recovered artifacts here. |
| `comments/` | Recorded issue-level discussions that inform integration decisions. | Cross-link to related docs when migrating content. |

## How to Use the Index

- Treat this file as the single entry point for onboarding. Each linked document contains deeper implementation details.
- When adding new documentation, update this table with the file path and a short description so contributors can find it without searching.
- Include references back to the integration plan whenever new automation or governance guidance is authored.

## Version-Controlling Generative Output Text Files

Archive previous and future generative outputs (transcripts, drafts, or evaluations) under `logs/generative/` using the following conventions:

1. **File naming**: `YYYY-MM-DD_topic-model.md` (for example, `2024-03-15_zoning-gpt4o.md`).
2. **Frontmatter**: Begin each file with a metadata block:
   ```markdown
   ---
   issue: "#<issue-number>"
   model: "gpt-4o"
   source: "ChatGPT transcript"  # or "Codex CLI", etc.
   reviewer: "Name or GitHub handle"
   status: "draft" | "final"
   ---
   ```
3. **Context section**: Summarize the prompt, objectives, and datasets referenced.
4. **Citations and links**: Add GitHub issue links, Notion pages, or Zotero item IDs that informed the output.
5. **Redaction**: Remove API keys, PII, and sensitive data before committing.
6. **Cross-references**: When a generative output informs another document, add a backlink in that document to the archived file for traceability.

## Backfilling Existing Outputs

- If previous generative outputs exist outside the repository (e.g., local text files or Notion notes), migrate them into `logs/generative/` using the same naming and frontmatter rules.
- Note the original storage location and transfer date in the context section so the provenance is clear.
- Open a short PR summarizing the added archives to keep the audit trail in Git history.
