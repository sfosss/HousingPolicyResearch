# Housing Policy Research Environment Setup

This document records the current understanding of the tools that support the Housing Policy Research project and describes how to configure them securely.

## Table of Contents

- [Quick Start](#quick-start)
- [Goals](#goals)
- [Repository Preparation (GitHub)](#repository-preparation-github)
- [ChatGPT / Codex Integration](#chatgpt--codex-integration)
- [Notion Workspace](#notion-workspace)
- [Zotero Library](#zotero-library)
- [GitHub Integration](#github-integration)
- [Automation and Continuous Integration](#automation-and-continuous-integration)
- [Verifying Your Setup](#verifying-your-setup)
- [Troubleshooting and Error Correction](#troubleshooting-and-error-correction)
- [Documentation Maintenance](#documentation-maintenance)
- [Validation Checklist](#validation-checklist)
- [Related Documentation](#related-documentation)

## Quick Start

For a rapid setup, follow these steps:

1. **Clone and enter the repository:**

   ```bash
   git clone https://github.com/SfosssHousing/HousingPolicyResearch.git
   cd HousingPolicyResearch
   ```

1. **Run the automated setup script:**

   ```bash
   ./setup.sh
   ```

   This script will:

   - Create a Python virtual environment (`.venv`)
   - Install all dependencies from `requirements.txt`
   - Copy `.env.template` to `.env`
   - Set up pre-commit hooks

1. **Configure environment variables:**

   ```bash
   # Edit .env and add your API keys (see sections below for obtaining keys)
   nano .env  # or use your preferred editor
   ```

1. **Activate the virtual environment:**

   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

**Alternative manual setup:**
If you prefer manual steps or need more control:

1. Create Python environment: `python -m venv .venv`
1. Activate it: `source .venv/bin/activate`
1. Install dependencies: `pip install -r requirements.txt`
1. Copy environment template: `cp .env.template .env`
1. Install pre-commit hooks: `pre-commit install`

For detailed setup instructions and integration configuration, continue reading the sections below.

## Goals

- Maintain a reproducible research workspace for the project repository.
- Connect writing and analysis tools (ChatGPT/Codex, Notion, GitHub, and Zotero) while keeping API credentials and personal data secure.
- Provide guidance for validating the links between systems.

## Repository Preparation (GitHub)

**Note:** For automated setup, you can use the provided `setup.sh` script (see [Quick Start](#quick-start)). The steps below provide detailed manual instructions.

1. **Clone the repository**

   ```bash
   git clone git@github.com:SfosssHousing/HousingPolicyResearch.git
   cd HousingPolicyResearch
   ```

   Or use HTTPS if you prefer:

   ```bash
   git clone https://github.com/SfosssHousing/HousingPolicyResearch.git
   cd HousingPolicyResearch
   ```

1. **Create a Python environment (recommended)**
   If analysis notebooks or scripts are added later, create an isolated Python environment so dependencies do not conflict with global packages.

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install --upgrade pip
   ```

1. **Install project dependencies**
   Install the project's Python dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   This includes essential packages like `python-dotenv`, `openai`, `pandas`, `pre-commit`, and code formatting tools.

1. **Set up environment variables**
   Copy the environment template and configure your local settings:

   ```bash
   cp .env.template .env
   ```

   Edit `.env` to add your API keys and credentials. See the [ChatGPT / Codex Integration](#chatgpt--codex-integration) and subsequent sections for details on obtaining these values.

   **Important:** The `.env` file is already excluded by `.gitignore` and should never be committed to version control.

1. **Install tooling dependencies (optional)**
   Additional tools for documentation generation (install as needed):

   - `mkdocs` (for Markdown-based documentation) – `pip install mkdocs`
   - `sphinx` (for reStructuredText-based documentation) – `pip install sphinx`\
     *(Install only one if documentation generation is required.)*

1. **Configure Git hooks**

   ```bash
   pre-commit install
   ```

   Hooks help enforce code quality checks before commits are pushed.

## ChatGPT / Codex Integration

| Task               | Recommended Action                                                                                                                                                                          |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentication     | Generate an OpenAI API key from <https://platform.openai.com/account/api-keys>. Store it in a secrets manager or in your shell profile as `OPENAI_API_KEY`.                                 |
| Secure Storage     | Use environment variables or encrypted secrets (`gh secret set`)—never commit keys to the repository. Add keys to your `.env` file (created from `.env.template`).                          |
| Access             | Ensure the repository has a `.gitignore` file that blocks `.env` or credential files. If it does not exist, create one as shown below.                                                      |
| Reverse Connection | If the project requires feedback from ChatGPT to GitHub, use scripts or GitHub Actions that call the OpenAI API with stored secrets. Log responses in Markdown files committed to the repo. |

**Environment variables for OpenAI:**

- `OPENAI_API_KEY` – Your OpenAI API key (required)
- `OPENAI_ORG_ID` – Your OpenAI organization ID (optional)
- `CHATGPT_ARCHIVE_PATH` – Directory for storing ChatGPT conversation logs (default: `logs/chatgpt`)

**Sample `.gitignore` for sensitive files:**

```gitignore
# Python virtual environments
.venv/
venv/

# Environment variable files
.env
.env.*

# API keys and credentials
*.key
*.pem

# macOS and system files
.DS_Store
```

## Notion Workspace

1. **Create an integration** in Notion via **Settings & Members → Integrations → Develop your own integrations**.
1. **Store the Notion secret** in a password manager or GitHub secret such as `NOTION_TOKEN`.
1. **Share target pages or databases** with the integration to grant access.
1. **Automate sync**
   - Use a scheduled script (Python + `notion-client`) or an automation service (Zapier/Make) to push updates from GitHub documentation into Notion.
   - For reverse sync (Notion → GitHub), export structured data (Markdown/CSV) and commit changes via a bot account or GitHub Action.
1. **Security checklist**
   - Rotate the integration token quarterly.
   - Limit page/database sharing to only what the integration needs.

**Environment variables for Notion:**

- `NOTION_TOKEN` – Your Notion integration secret (required)
- `NOTION_RESEARCH_DB_ID` – Database ID for research tracking (optional)
- `NOTION_ACTION_ITEMS_DB_ID` – Database ID for action items (optional)

## Zotero Library

1. Install the [Zotero desktop application](https://www.zotero.org/).
1. Create a private group library for the project.
1. Generate an API key from **Settings → Feeds/API** with read/write permissions for the project group only.
1. Use the `pyzotero` library (Python) or the Zotero web API to export bibliographies into this repository (for example, `docs/references.bib`).
1. Store the key securely and rotate annually. Do not commit the key.

**Environment variables for Zotero:**

- `ZOTERO_API_KEY` – Your Zotero API key (required)
- `ZOTERO_LIBRARY_ID` – Your library or group ID (required)
- `ZOTERO_COLLECTION_ID` – Specific collection ID (optional)

## GitHub Integration

For automation scripts that interact with GitHub (such as creating issues, updating repositories, or triggering workflows):

1. **Generate a Personal Access Token (PAT)**

   - Go to **Settings → Developer settings → Personal access tokens → Tokens (classic)**
   - Create a token with appropriate scopes (`repo`, `workflow` if using Actions)

1. **Configure SSH keys** (for Git operations)

   - Generate an SSH key if you don't have one: `ssh-keygen -t ed25519 -C "your_email@example.com"`
   - Add the public key to your GitHub account: **Settings → SSH and GPG keys**

1. **Store credentials securely**

   - Add your PAT to `.env` as `GITHUB_PAT`
   - Specify your SSH key path in `.env` as `GITHUB_SSH_KEY_PATH`

**Environment variables for GitHub:**

- `GITHUB_PAT` – Personal Access Token for API operations (required for automation)
- `GITHUB_SSH_KEY_PATH` – Path to your SSH private key (default: `~/.ssh/id_ed25519`)
- `GITHUB_WEBHOOK_SECRET` – Secret for validating webhook payloads (optional, for webhooks)

## Automation and Continuous Integration

- **GitHub Actions:** Use repository secrets (`Settings → Secrets and variables → Actions`) for API keys. Reference them in workflow files using `${{ secrets.OPENAI_API_KEY }}`, `${{ secrets.NOTION_TOKEN }}`, etc.
- **Local scripts:** Read secrets from environment variables or encrypted `.env` files using the `python-dotenv` library (already included in `requirements.txt`). The `.env` file is excluded by `.gitignore`.
- **Validation:** After configuration, run lightweight scripts to confirm each integration can authenticate and exchange data. Create a new file at `docs/integration-status.md` (if it does not exist) and log the results there.

**Additional environment variables:**

- `LOG_LEVEL` – Logging verbosity (default: `info`)
- `SYNC_CHECKPOINT_DIR` – Directory for storing sync state (default: `.sync-state`)

## Verifying Your Setup

After completing the setup, verify that everything is configured correctly:

1. **Check Python environment:**

   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   python --version  # Should show Python 3.x
   pip list  # Should show installed packages
   ```

1. **Verify environment variables:**

   ```bash
   python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('✓ .env loaded' if os.getenv('OPENAI_API_KEY') else '✗ Missing OPENAI_API_KEY')"
   ```

1. **Test pre-commit hooks:**

   ```bash
   pre-commit run --all-files
   ```

1. **Validate API connections** (optional):
   See [Connection Checks](connection-checks.md) for detailed validation procedures for each integration.

If any step fails, consult the [Troubleshooting](#troubleshooting-and-error-correction) section below.

## Troubleshooting and Error Correction

| Issue               | Resolution Steps                                                                                                                                                                  |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Missing API keys    | Generate new keys and update your secrets manager and GitHub Actions secrets.                                                                                                     |
| Unauthorized errors | Ensure the integration has access to the correct Notion pages or Zotero libraries.                                                                                                |
| Sync conflicts      | Adopt a single source of truth per content type (e.g., Zotero for citations, GitHub for documentation) and automate one-way exports with manual review for the reverse direction. |

## Documentation Maintenance

- Update this document whenever new tools are added or access procedures change.
- Document any scripts used to push/pull data between systems.
- Track secret rotation dates in a secure, shared password manager.

## Validation Checklist

- [ ] All API keys stored outside of the repository.
- [ ] GitHub Actions secrets configured for OpenAI, Notion, and Zotero.
- [ ] Automated tests or scripts confirm that read/write operations succeed for each integration.
- [ ] README links to this document.
- [ ] Next steps documented in `docs/project-roadmap.md`.

## Related Documentation

- [Environment Integrations and Documentation](environment-integrations.md) – Detailed integration architecture and bidirectional data flows
- [Workspace Readiness](workspace-readiness.md) – Checklist for Raycast, Quarto, and other workspace setup tasks
- [Connection Checks](connection-checks.md) – Tools for validating API connectivity
- [Project Roadmap](project-roadmap.md) – Outstanding tasks and milestones
- [Security Policy](../SECURITY.md) – Organization-wide security policies and responsible disclosure

______________________________________________________________________

**Last updated:** 2025-12-26\
**Maintainers:** Housing Policy Research team
