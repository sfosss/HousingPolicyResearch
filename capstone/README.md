# Capstone Documentation

This directory replaces the legacy `Capstone alias` export with structured, version-controlled notes for the Housing Policy Research capstone effort.

## Purpose

- Centralize the research brief, methodology, and deliverable checklist for the capstone track.
- Preserve context that was previously stored in the corrupted `Capstone alias` file.
- Provide clear links back to the integration and security guidance that governs the automation environment.

## Contents

| File        | Description                                                          |
| ----------- | -------------------------------------------------------------------- |
| `README.md` | Entry point with migration notes, environment links, and next steps. |

As additional artifacts (research memos, datasets, automation scripts) are recovered or authored, store them in subdirectories here and update this table accordingly.

## Migration Notes

- The binary `Capstone alias` file has been removed and superseded by this directory to avoid path ambiguity across operating systems.
- All references in the repository now point to `capstone/` to ensure consistent imports and documentation links.
- Follow the environment integration plan in `docs/integration-plan.md` before adding automation code so secrets remain scoped and auditable.

## Next Steps

1. Recover any remaining capstone materials from local backups or cloud storage and convert them to Markdown or structured data files.
1. Document milestones, owners, and timelines for the capstone workstream within this directory (e.g., `capstone/milestones.md`).
1. Cross-link relevant Notion pages and Zotero collections following the secure integration practices outlined in the main documentation.
1. Use GitHub Issues to track capstone-related tasks and reference them from commits within this folder for traceability.

For broader environment setup and automation details, consult the root `README.md` and `docs/integration-plan.md`.
