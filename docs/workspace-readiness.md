# Workspace Readiness and Outstanding Setup

Use this checklist to finish configuring the Housing Policy Research workspace, with emphasis on the Raycast extension toolchain, Quarto authoring stack, and secure cross-platform links between ChatGPT/Codex, Notion, GitHub, and Zotero.

## 1) Raycast Extension Build Path

**Observed issue:** `npm run build` fails with TS2786 errors due to React type mismatches between `@raycast/api` and globally installed React types.

**Preferred workaround (Raycast tooling):**

1. Install the Raycast Extension Developer Tools.
1. From inside your extension directory (for example `raycast-extension/`):
   ```bash
   ray run .
   ```
   This uses Raycast's own compiler, which supports async components and the API's bundled types.

**Optional direct TypeScript compilation:**

1. Pin `typescript` to `4.9.x` in `package.json` and reinstall dependencies.
1. Add `"typeRoots": ["./node_modules/@types"]` to `tsconfig.json` to avoid duplicate React definitions.
1. Re-run `npm run build`.

Record the chosen approach and results in a short log (e.g., `docs/logs/raycast-build.md`) so future runs use the same toolchain.

## 2) Publishing Stack (Quarto + APA)

1. Install [Quarto](https://quarto.org) locally.
1. In the project root, enable APA 7 templates:
   ```bash
   quarto add wjschne/apaquarto
   ```
1. Confirm that Quarto sees the APA format with `quarto check`. Capture the output in `docs/logs/quarto-install.md`.
1. Update `docs/policy_brief_apa7.qmd` and the bill drafting shell template with project metadata (title, authors, date, and contact email). Track any custom filters or CSL files alongside the QMD files.

## 3) Configuration Secrets

- Create `00_admin/settings.yaml` (not present in the repository) with the following placeholders replaced by real values stored outside Git:
  ```yaml
  openai_api_key: <your key>
  notion_token: <your token>
  zotero_api_key: <your key>
  github_pat: <your token>
  assistant_base_url: <backend URL>
  ```
- Add `00_admin/settings.yaml` to `.gitignore` so credentials never enter version control.
- Mirror the same keys in GitHub Actions secrets for CI jobs.

## 4) Raycast Extension Installation

1. After a successful build, open Raycast → **Extensions → Developer → Install Extension…** and select the `raycast-extension` folder.
1. Validate commands load without errors; note any missing environment variables in `docs/logs/raycast-install.md`.
1. Set up a minimal smoke test command (e.g., `hello-world`) to confirm Raycast can call the backend configured via `assistant_base_url`.

## 5) Shortcuts Automation

1. Create a `shortcuts/` folder in this repository to store exported `.shortcut` files and usage notes.
1. Build the following Apple Shortcuts following the instructions in `shortcuts/`:
   - **Add Source** – captures a URL, notes, and pushes to Notion/Zotero queues.
   - **Draft Section** – prompts ChatGPT/Codex to outline or draft a policy section and saves results to GitHub.
   - **Bill Sweep** – monitors legislation feeds and posts updates to GitHub Issues.
1. Export each shortcut to `shortcuts/` and document triggers and required permissions.

## 6) Secure Connections and Reverse Links

- Follow the security controls in `docs/environment-setup.md` and `docs/connection-checks.md` to harden API usage.
- Validate forward and reverse flows:
  - ChatGPT/Codex ↔ GitHub: use archived transcripts and bot commits with scoped PATs.
  - GitHub ↔ Notion: scheduled Markdown exports/imports with audit timestamps.
  - Zotero → GitHub/Notion and GitHub → Zotero release notes.
- Log each validation run with date, tool versions, and any remediation applied.

## 7) Generative Output Next Actions

- Map generative deliverables (policy briefs, bill drafts, source annotations) to the required integrations and owners.
- Add review checkpoints (human-in-the-loop) before publishing generated content, referencing `docs/generative-output-tasks.md` and `docs/generative-output-version-control.md`.
- Capture errors or gaps in `docs/logs/generative-readiness.md` and open GitHub issues for any blockers.

Keeping this document updated ensures the workspace remains reproducible, secure, and ready for the drafting pipeline.
