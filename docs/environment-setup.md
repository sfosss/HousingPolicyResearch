# Housing Policy Research Environment Setup

This document provides comprehensive instructions for setting up a secure, reproducible development environment for the Housing Policy Research project. It covers local development setup, integration with external tools (ChatGPT/Codex, Notion, GitHub, and Zotero), and validation procedures.

**Version:** 1.0  
**Last Updated:** 2025-12-26
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

## Overview

### Goals

- Maintain a reproducible research workspace for the project repository
- Connect writing and analysis tools (ChatGPT/Codex, Notion, GitHub, and Zotero) while keeping API credentials and personal data secure
- Provide guidance for validating the links between systems
- Enable automated workflows through continuous integration

### Related Documentation

- [Integration Plan](integration-plan.md) – Detailed architecture and data flow diagrams
- [Connection Checks](connection-checks.md) – Validation procedures for all integrations
- [Project Roadmap](project-roadmap.md) – Planned features and tasks
- [APA Style Guide](STYLE-APA.md) – Citation standards for research documentation
- [Security Policy](../SECURITY.md) – Security practices and incident reporting

## Quick Start

For a rapid setup using the automated script:

```bash
# Clone the repository
git clone git@github.com:SfosssHousing/HousingPolicyResearch.git
cd HousingPolicyResearch

# Run automated setup (creates virtual environment, installs dependencies, sets up hooks)
./setup.sh

# Activate the virtual environment
source .venv/bin/activate

# Copy environment template and configure your credentials
cp .env.template .env
# Edit .env with your API keys (see Environment Variables section below)

# Validate connections (requires configured .env file)
python scripts/validate_connections.py
```

For detailed manual setup instructions, continue reading the sections below.

## Prerequisites

Before beginning, ensure you have the following installed:

- **Python 3.10 or higher** – Check with `python3 --version`
- **Git 2.40+** – Required for version control
- **Text editor** – VS Code, Vim, or your preferred editor
- **Password manager** – For secure storage of API keys (recommended: 1Password, Bitwarden)

Optional but recommended:
- **Node.js LTS** – Required for Codex CLI and JavaScript-based automation
- **SSH keys** – For GitHub authentication (see [GitHub SSH setup](https://docs.github.com/en/authentication/connecting-to-github-with-ssh))

## Repository Setup

### Method 1: Automated Setup (Recommended)

The repository includes an automated setup script that handles most configuration:

```bash
./setup.sh
```

This script will:
1. Verify Python 3 is installed
2. Create a virtual environment at `.venv/`
3. Upgrade pip and install dependencies from `requirements.txt`
4. Copy `.env.template` to `.env` (if not already present)
5. Install pre-commit hooks for code quality checks
6. Create necessary directories (`logs/`, `artifacts/`, `docs/prompts/`)

For CI environments, use:
```bash
./setup.sh --ci
```

### Method 2: Manual Setup

If you prefer manual control or need to troubleshoot the automated setup:

#### 1. Clone the Repository

```bash
git clone git@github.com:SfosssHousing/HousingPolicyResearch.git
cd HousingPolicyResearch
```

> **Note:** Replace `git@github.com:SfosssHousing/HousingPolicyResearch.git` with the HTTPS URL if you haven't configured SSH keys.

#### 2. Create Python Virtual Environment

Create an isolated Python environment to avoid conflicts with system packages:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
```

**Verify your environment:**
```bash
which python  # Should show path inside .venv/
python --version  # Should be 3.10 or higher
```

#### 3. Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

**Current dependencies include:**
- `black` – Code formatter
- `flake8` – Linter for Python code
- `mdformat` – Markdown formatter
- `openai` – OpenAI API client
- `pandas` – Data analysis library
- `pre-commit` – Git hook manager
- `python-dotenv` – Environment variable loader
- `requests` – HTTP library

#### 4. Configure Pre-commit Hooks

Pre-commit hooks automatically check code quality before each commit:

```bash
pre-commit install
```

**Test the hooks:**
```bash
pre-commit run --all-files
```

This will run linting checks on all files. Address any issues before committing.

## Environment Variables

The project uses environment variables for sensitive configuration. All credentials must be stored securely and never committed to the repository.

### Setup Environment File

1. **Copy the template:**
   ```bash
   cp .env.template .env
   ```

2. **Edit `.env`** and populate with your credentials (see sections below for obtaining each key)

3. **Verify `.env` is gitignored:**
   ```bash
   git check-ignore .env  # Should output: .env
   ```

### Required Environment Variables

Based on `.env.template`, configure the following:

**OpenAI / ChatGPT / Codex:**
- `OPENAI_API_KEY` – API key from [OpenAI Platform](https://platform.openai.com/account/api-keys)
- `OPENAI_ORG_ID` – Organization ID (optional, for team accounts)
- `CHATGPT_ARCHIVE_PATH` – Local path for archiving ChatGPT sessions (default: `logs/chatgpt`)

**Notion:**
- `NOTION_TOKEN` – Integration secret from Notion workspace
- `NOTION_RESEARCH_DB_ID` – Database ID for research tracking
- `NOTION_ACTION_ITEMS_DB_ID` – Database ID for action items

**GitHub:**
- `GITHUB_PAT` – Personal Access Token with `repo` and `workflow` scopes
- `GITHUB_SSH_KEY_PATH` – Path to SSH key (default: `~/.ssh/id_ed25519`)
- `GITHUB_WEBHOOK_SECRET` – Secret for webhook validation (if using webhooks)

**Zotero:**
- `ZOTERO_API_KEY` – API key from [Zotero Settings](https://www.zotero.org/settings/keys)
- `ZOTERO_LIBRARY_ID` – Library ID (user or group)
- `ZOTERO_COLLECTION_ID` – Collection ID for project-specific references

**Automation Settings:**
- `LOG_LEVEL` – Logging verbosity (default: `info`)
- `SYNC_CHECKPOINT_DIR` – Directory for sync state tracking (default: `.sync-state`)

### Security Best Practices for Credentials

✅ **Do:**
- Store API keys in a password manager
- Use scoped tokens with minimal required permissions
- Rotate credentials every 90 days
- Use different credentials for development and production
- Store GitHub Actions secrets separately in repository settings

❌ **Don't:**
- Commit `.env` files to version control
- Share credentials via email or chat
- Use production credentials in development
- Store credentials in plaintext files
- Reuse credentials across multiple projects

## Integration Configuration

### ChatGPT / Codex Integration

### ChatGPT / Codex Integration

#### 1. Obtain OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/account/api-keys)
2. Create a new API key with appropriate usage limits
3. Copy the key immediately (it won't be shown again)
4. Add to your `.env` file: `OPENAI_API_KEY=sk-...`

#### 2. Test API Connection

```bash
# Verify API key works
python -c "import openai, os; openai.api_key = os.getenv('OPENAI_API_KEY'); print('✓ OpenAI API configured')"

# Or use the validation script
python scripts/validate_connections.py
```

#### 3. Configure ChatGPT Output Archiving

The project maintains a record of ChatGPT sessions for reproducibility:

1. Ensure `CHATGPT_ARCHIVE_PATH` is set in `.env` (default: `logs/chatgpt`)
2. When using ChatGPT, export conversations as Markdown
3. Store in the archive directory with naming convention: `YYYY-MM-DD-topic-name.md`
4. Include metadata header:
   ```markdown
   ---
   date: 2025-12-26
   model: gpt-4
   purpose: Research question analysis
   ---
   ```

See [Generative Output Version Control](generative-output-version-control.md) for tracking guidelines.

#### 4. Codex CLI (Optional)

For command-line code generation:

```bash
# Install Node.js if not already present
# Then install Codex CLI
npm install -g @openai/codex

# Configure with your API key
export OPENAI_API_KEY="sk-..."

# Test
codex --version
```

**Note:** As of 2024, OpenAI Codex has been superseded by ChatGPT code capabilities. The Codex CLI may not be actively maintained.

### Notion Workspace Integration

Notion serves as the project's knowledge base and task management system.

#### 1. Create Notion Integration

1. Navigate to **Settings & Members → Integrations** in your Notion workspace
2. Click **Develop your own integrations** or **New integration**
3. Name it "Housing Policy Research Bot"
4. Select the workspace and grant appropriate permissions:
   - Read content
   - Update content
   - Insert content
5. Copy the **Internal Integration Token** (starts with `secret_...`)
6. Add to `.env`: `NOTION_TOKEN=secret_...`

#### 2. Share Databases with Integration

1. Open each database you want to sync (Research DB, Action Items, etc.)
2. Click **Share** in the top-right
3. Search for your integration name and add it
4. Copy the database ID from the URL:
   - URL format: `https://notion.so/workspace/{workspace_id}/{database_id}?v=...`
   - Database ID is the 32-character hex string before the `?`
5. Add to `.env`:
   ```
   NOTION_RESEARCH_DB_ID=abc123...
   NOTION_ACTION_ITEMS_DB_ID=def456...
   ```
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

#### 3. Test Notion Connection

```bash
# Verify Notion API access
python scripts/validate_connections.py

# Or test manually
curl https://api.notion.com/v1/users \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Notion-Version: 2022-06-28"
```

#### 4. Automation Scripts (Future)

Planned automation includes:
- Syncing GitHub issues to Notion action items
- Publishing documentation updates to Notion pages
- Exporting reading lists from Notion to Zotero

See [Integration Plan](integration-plan.md) for implementation roadmap.

### Zotero Library Integration

Zotero manages research references and citations for the project.

#### 1. Install Zotero Desktop

Download and install from [zotero.org](https://www.zotero.org/download/)

#### 2. Create Project Library

1. Create a **Group Library** for the project (recommended for collaboration):
   - Visit [zotero.org/groups/new](https://www.zotero.org/groups/new)
   - Name: "Housing Policy Research"
   - Type: Private or Public (depending on requirements)
2. Or use your **Personal Library** for individual work

#### 3. Generate API Key

1. Go to [Zotero Settings → Feeds/API](https://www.zotero.org/settings/keys)
2. Click **Create new private key**
3. Configure permissions:
   - **Personal Library:** Read/Write (if using personal library)
   - **Group Permissions:** Select your project group, grant Read/Write access
   - **Notes:** Allow library access, file access
4. Save the key and add to `.env`: `ZOTERO_API_KEY=...`

#### 4. Find Library and Collection IDs

**Library ID:**
- Personal library: Your user ID (visible in API key settings)
- Group library: Group ID from URL: `https://www.zotero.org/groups/{group_id}/...`

**Collection ID (optional):**
1. In Zotero, right-click a collection
2. Copy collection link
3. Extract the 8-character ID from the URL

Add to `.env`:
```
ZOTERO_LIBRARY_ID=12345678
ZOTERO_COLLECTION_ID=ABCD1234
```
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

#### 5. Test Zotero Connection

```bash
# Test API access
curl https://api.zotero.org/users/$ZOTERO_LIBRARY_ID/items \
  -H "Zotero-API-Key: $ZOTERO_API_KEY"

# Or use validation script
python scripts/validate_connections.py
```

#### 6. Citation Management Workflow

1. **Add sources to Zotero:**
   - Use browser extensions to capture citations
   - Import DOIs, ISBNs, or BibTeX entries
   - Manually add government reports and grey literature

2. **Follow APA 7th edition:**
   - See [APA Style Guide](STYLE-APA.md) for formatting requirements
   - Use Zotero's APA citation style for exports
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

3. **Export to repository:**
   - Future automation will sync Zotero → `docs/resources-index.md`
   - Manual export: File → Export Library → Format: Markdown or BibTeX

4. **Annotate citations:**
   - Add notes in Zotero explaining relevance and application
   - Export annotations for research transparency

### GitHub Integration

Most GitHub interaction happens through Git, but some features require API access.

#### 1. Personal Access Token (PAT)

For GitHub Actions and automation scripts:

1. Go to [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Click **Generate new token (classic)**
3. Select scopes:
   - `repo` – Full repository access
   - `workflow` – Update GitHub Actions workflows
   - `read:org` – Read organization data (if applicable)
4. Generate and copy the token (starts with `ghp_...`)
5. Add to `.env`: `GITHUB_PAT=ghp_...`

**For GitHub CLI:**
```bash
gh auth login
# Follow prompts to authenticate
```

#### 2. SSH Keys (Recommended for Git)

If not already configured:

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your-email@example.com"

# Add to SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy public key
cat ~/.ssh/id_ed25519.pub
# Add to GitHub: Settings → SSH and GPG keys → New SSH key
```

Update `.env`:
```
GITHUB_SSH_KEY_PATH=~/.ssh/id_ed25519
```

#### 3. Configure Git Identity

```bash
git config user.name "Your Name"
git config user.email "your-email@example.com"

# Verify
git config --list | grep user
```

## Validation and Testing

After completing setup, validate all integrations.

### Run Validation Script

The repository includes an automated validation tool:

```bash
# Activate virtual environment if not already active
source .venv/bin/activate

# Run validation
python scripts/validate_connections.py
```

**Expected output:**
```
2025-12-26 12:00:00 INFO [OpenAI] OK
2025-12-26 12:00:01 INFO [Notion] OK
2025-12-26 12:00:02 INFO [Zotero] OK
```

If any service fails, check:
- Environment variable is set correctly in `.env`
- API key is valid and not expired
- Network connectivity
- Service-specific permissions (Notion database sharing, Zotero library access)

### Manual Connection Tests

**OpenAI:**
```bash
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

**Notion:**
```bash
curl https://api.notion.com/v1/users \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Notion-Version: 2022-06-28"
```

**Zotero:**
```bash
curl https://api.zotero.org/users/$ZOTERO_LIBRARY_ID/items?limit=1 \
  -H "Zotero-API-Key: $ZOTERO_API_KEY"
```

**GitHub:**
```bash
curl https://api.github.com/user \
  -H "Authorization: token $GITHUB_PAT"
```

### Detailed Connection Checks

For comprehensive validation procedures, see [Connection Checks](connection-checks.md).

## GitHub Actions Configuration

To enable automation in CI/CD:

### 1. Add Repository Secrets

1. Navigate to repository **Settings → Secrets and variables → Actions**
2. Click **New repository secret**
3. Add each secret from your `.env` file:
   - `OPENAI_API_KEY`
   - `NOTION_TOKEN`
   - `NOTION_RESEARCH_DB_ID`
   - `NOTION_ACTION_ITEMS_DB_ID`
   - `GITHUB_PAT` (if needed for cross-repo operations)
   - `ZOTERO_API_KEY`
   - `ZOTERO_LIBRARY_ID`
   - `ZOTERO_COLLECTION_ID`

### 2. Reference Secrets in Workflows

In `.github/workflows/*.yml`:

```yaml
env:
  OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
  NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}
```

### 3. Test Workflow

```bash
# Trigger a workflow manually
gh workflow run <workflow-name>

# Check status
gh run list
```

## Troubleshooting

### Common Issues and Solutions

#### Missing API Keys

**Symptom:** Validation script fails or scripts raise `KeyError`/`None` exceptions

**Solution:**
1. Verify `.env` file exists: `ls -la .env`
2. Check all required variables are set: `cat .env | grep -v "^#" | grep "="`
3. Ensure `.env` is being loaded by scripts (uses `python-dotenv`)
4. Generate new keys if expired or revoked

#### Unauthorized Errors

**Symptom:** HTTP 401 or 403 responses from APIs

**Solution:**
- **OpenAI:** Check billing status, verify key hasn't expired
- **Notion:** Confirm database is shared with integration, check token scopes
- **Zotero:** Verify library/group access permissions, check API key configuration
- **GitHub:** Regenerate PAT with correct scopes

#### Python Environment Issues

**Symptom:** `ModuleNotFoundError` or import errors

**Solution:**
```bash
# Verify virtual environment is active
which python  # Should show .venv/bin/python

# If not active
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt

# Clear cache if persistent issues
pip cache purge
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### Pre-commit Hook Failures

**Symptom:** Commits blocked by failing hooks

**Solution:**
```bash
# Run hooks manually to see detailed errors
pre-commit run --all-files

# Fix reported issues (usually formatting)
black .
mdformat docs/

# Skip hooks temporarily (use sparingly)
git commit --no-verify -m "message"

# Update hooks
pre-commit autoupdate
```

#### Git Authentication Issues

**Symptom:** `Permission denied (publickey)` or `Authentication failed`

**Solution:**
- **SSH:** Check key is added to SSH agent: `ssh-add -l`
- **SSH:** Verify key is added to GitHub account
- **HTTPS:** Use `gh auth login` or configure credential helper
- **HTTPS:** Use PAT as password when prompted

#### Network/Connectivity Issues

**Symptom:** Timeouts or connection refused errors

**Solution:**
1. Check internet connectivity
2. Verify firewall/VPN settings
3. Test with `curl` to isolate the problem
4. Check service status pages:
   - [OpenAI Status](https://status.openai.com/)
   - [Notion Status](https://status.notion.so/)
   - [GitHub Status](https://www.githubstatus.com/)

#### Sync Conflicts

**Symptom:** Data inconsistencies between systems

**Solution:**
- Establish single source of truth per content type:
  - Zotero: Citations and references
  - GitHub: Documentation and code
  - Notion: Meeting notes and task tracking
- Use one-way syncs with manual review for reverse direction
- Document sync procedures in automation scripts

### Getting Help

If issues persist:

1. **Check documentation:**
   - [Integration Plan](integration-plan.md)
   - [Connection Checks](connection-checks.md)
   - [Project Roadmap](project-roadmap.md)

2. **Search existing issues:**
   ```bash
   gh issue list --search "your error message"
   ```

3. **Open a new issue:**
   ```bash
   gh issue create --title "Setup issue: brief description" \
     --body "Detailed description, error messages, steps to reproduce"
   ```

4. **Security issues:** See [Security Policy](../SECURITY.md) for responsible disclosure

## Maintenance and Best Practices

### Regular Maintenance Tasks

**Weekly:**
- Review logs for integration errors
- Check for dependency updates: `pip list --outdated`

**Monthly:**
- Rotate API keys (follow 90-day policy)
- Update pre-commit hooks: `pre-commit autoupdate`
- Review GitHub Actions usage and costs

**Quarterly:**
- Full security audit of credentials
- Review and update this documentation
- Archive old ChatGPT conversation exports
- Clean up unused Notion databases

### Credential Rotation Schedule

Track rotation in your password manager with reminders:

| Service | Rotation Period | Last Rotated | Next Due |
|---------|----------------|--------------|----------|
| OpenAI API Key | 90 days | - | - |
| Notion Integration Token | 90 days | - | - |
| GitHub PAT | 90 days | - | - |
| Zotero API Key | 365 days | - | - |

### Documentation Updates

Update this document when:
- New tools are added to the stack
- API authentication methods change
- New automation scripts are created
- Security policies are updated
- Common issues and solutions are discovered

## Validation Checklist

Before considering setup complete:

- [ ] Repository cloned and accessible
- [ ] Python 3.10+ virtual environment created and activated
- [ ] All dependencies installed from `requirements.txt`
- [ ] Pre-commit hooks installed and tested
- [ ] `.env` file created from `.env.template`
- [ ] All required API keys obtained and added to `.env`
- [ ] `.env` file confirmed in `.gitignore`
- [ ] Connection validation script runs successfully
- [ ] GitHub Actions secrets configured (if applicable)
- [ ] Git identity configured (name and email)
- [ ] SSH keys or HTTPS authentication working
- [ ] Zotero desktop application installed
- [ ] Notion integration created and databases shared
- [ ] ChatGPT conversation archiving procedure understood
- [ ] Documentation reviewed: Integration Plan, Connection Checks
- [ ] Next steps reviewed in [Project Roadmap](project-roadmap.md)

## Next Steps

After completing setup:

1. **Review research goals** in [Project Roadmap](project-roadmap.md)
2. **Explore resources** in [Resources Index](resources-index.md)
3. **Understand citation standards** in [APA Style Guide](STYLE-APA.md)
4. **Set up automation** following [Integration Plan](integration-plan.md)
5. **Run connection checks** per [Connection Checks](connection-checks.md)
6. **Start contributing** following repository contribution guidelines

---

**Document version:** 1.0  
**Last updated:** 2025-12-26  
**Maintained by:** Housing Policy Research team  
**Review schedule:** Quarterly or when major changes occur

For questions or issues with this setup, please [open an issue](https://github.com/SfosssHousing/HousingPolicyResearch/issues/new) with the `documentation` label.

## Related Documentation

- [Environment Integrations and Documentation](environment-integrations.md) – Detailed integration architecture and bidirectional data flows
- [Workspace Readiness](workspace-readiness.md) – Checklist for Raycast, Quarto, and other workspace setup tasks
- [Connection Checks](connection-checks.md) – Tools for validating API connectivity
- [Project Roadmap](project-roadmap.md) – Outstanding tasks and milestones
- [Security Policy](../SECURITY.md) – Organization-wide security policies and responsible disclosure

______________________________________________________________________

**Last updated:** 2025-12-26\
**Maintainers:** Housing Policy Research team
