# Environment Integration and Documentation Plan

This document captures the setup guidance and project tasks required to connect ChatGPT (OpenAI API), Notion, GitHub, and Zotero securely for the Housing Policy Research environment.

## 1. Prerequisites

- **Node.js and npm**: Install the current LTS release from [nodejs.org](https://nodejs.org/).
- **Python 3.10+**: Required for automation scripts or API clients.
- **Package Managers**: `pipx` (Python) and `npm` (Node.js) are recommended for isolating tooling.
- **Version Control**: Git 2.40+ configured with SSH and/or HTTPS credentials.
- **Secret Storage**: Use a password manager or secret manager (e.g., 1Password, Bitwarden, GitHub Encrypted Secrets) to store API keys.

### OpenAI API Integration

OpenAI's API can be accessed through the official `openai` Python package or Node.js SDK. Install via your preferred package manager:

**Python:**

```bash
pip install openai
```

**Node.js:**

```bash
npm install openai
```

## 2. Secure Connection Architecture

| System     | Purpose                                 | Required Credentials                            | Storage Recommendation                |
| ---------- | --------------------------------------- | ----------------------------------------------- | ------------------------------------- |
| OpenAI API | AI assistance, analysis, and automation | OpenAI API key                                  | Environment variables or secret store |
| Notion     | Knowledge base & documentation          | Notion integration token & database IDs         | Secret manager + local `.env` file    |
| GitHub     | Source control & Actions                | Personal access token (PAT) with minimal scopes | Git credential manager or SSH keys    |
| Zotero     | Reference management                    | Zotero API key and library ID                   | Secret manager + `.env` file          |

The recommended pattern is:

1. Store all secrets in a password manager.
1. Provide each developer with scoped tokens (no shared master tokens).
1. Load tokens into local development environments via `.env` files added to `.gitignore`.
1. Replicate the variables in GitHub repository secrets for CI/CD automation.

## 3. Connection Workflows

### 3.1 OpenAI API

1. Generate an OpenAI API key from the OpenAI dashboard.

1. Export the key as an environment variable:

   ```bash
   export OPENAI_API_KEY="sk-..."
   ```

1. Test the API connection with a simple Python script:

   ```python
   from openai import OpenAI

   try:
       client = OpenAI()
       models = client.models.list()
       print("✓ OpenAI API connection successful")
   except Exception as e:
       print(f"✗ OpenAI API connection failed: {e}")
   ```

1. Document standard prompts, rate limits, and logging practices in the team wiki.

### 3.2 Notion Integration

1. Create a Notion internal integration and capture the secret token.
1. Share the required workspace pages or databases with the integration user.
1. Record database IDs for content synchronization (e.g., research log, literature review).
1. Configure a synchronization script (Python or Node) that reads from GitHub markdown and updates Notion blocks using the Notion API.
1. Log operations with timestamps for auditing.

### 3.3 GitHub Automation

1. Configure Git remotes over SSH for developers; use deploy keys for read-only automation if required.
1. Store PATs with minimal scopes (e.g., `repo`, `workflow`) in GitHub Secrets for Actions.
1. Create GitHub Actions workflows that:
   - Lint documentation (`markdownlint`, `vale`).
   - Sync notes to Notion or Zotero via scheduled jobs.
   - Archive prompts and outputs from ChatGPT sessions to the repo.

### 3.4 Zotero Integration

1. Generate a Zotero API key scoped to the research library.
1. Use the Zotero Web API or `pyzotero` client to fetch and push literature metadata.
1. Maintain a mapping file (e.g., `data/zotero-mapping.json`) that links Zotero items to Notion pages and GitHub issue IDs.
1. Ensure synchronization scripts respect rate limits and handle retries with exponential backoff.

## 4. Reverse Data Flows

- **OpenAI to GitHub**: Archive finalized prompts and responses into version-controlled markdown files.
- **GitHub to Notion**: Publish documentation updates to Notion knowledge bases.
- **Notion to Zotero**: Convert curated reading lists into Zotero collections through the API.
- **Zotero to GitHub**: Export annotations into the repository for reproducibility.

Automate each pipeline with CI jobs or scheduled tasks that authenticate using stored secrets. Include logging to a secure datastore (e.g., CloudWatch, Datadog) for traceability.

### Verification Steps for Secure Connections

1. **Credential Audit** – Confirm each platform token (OpenAI API, Notion, GitHub, Zotero) is present in both the local `.env` file (generated from `.env.template`) and the GitHub Secrets store with matching scopes.
1. **Connection Tests** – Follow the commands listed in [`docs/connection-checks.md`](docs/connection-checks.md) and capture success logs in `logs/connection-checks/`.
1. **Reverse Flow Validation** – Execute the reverse synchronization paths (GitHub→Notion, Notion→Zotero, Zotero→GitHub, OpenAI→GitHub) using the same checklist.
1. **Security Review** – Verify that logs exclude sensitive payloads, rotate tokens post-test, and document findings in the capstone tracker within `capstone/`.

## 5. Security Controls

- **Secret Rotation**: Rotate API keys every 90 days or immediately after role changes.
- **Least Privilege**: Scope each token to the minimal set of permissions.
- **Network Security**: Use VPN or SSO where possible; avoid running integrations from unsecured networks.
- **Audit Trails**: Maintain logs of automation runs and human access to integrations.
- **Dependency Management**: Pin versions in `package.json`/`requirements.txt` and enable Dependabot in GitHub.

## 6. Validation Checklist

- [ ] Document stored in `docs/` and linked from README.
- [ ] All `.env` examples exclude real credentials.
- [ ] GitHub repository secrets mirror local `.env` keys.
- [ ] Integration scripts provide logging and error handling.
- [ ] Backups exist for Notion databases and Zotero libraries.

## 7. Task Breakdown & Next Steps

1. **Documentation Cleanup**

   - Replace corrupted `Capstone alias` file with structured markdown or archive reference details. *(Completed: migrated to `capstone/README.md`.)*
   - Expand README with project overview and integration quick links.

1. **Secret Management Implementation**

   - Select a shared secret manager.
   - Draft `.env.template` covering OpenAI, Notion, GitHub, and Zotero keys.

1. **Automation Scripts**

   - Prototype Node or Python scripts for each data flow (ChatGPT→GitHub, GitHub→Notion, etc.).
   - Add unit tests and linting configuration.

1. **CI/CD Integration**

   - Configure GitHub Actions workflows for linting, synchronization, and backups.
   - Add status badges to the README once pipelines are live.

1. **Security Review**

   - Conduct a quarterly review of access logs and key rotations.
   - Document incident response procedures specific to data integrations.

1. **Governance & Reporting**

   - Establish ownership for each integration and define SLAs.
   - Schedule monthly review meetings; log decisions in Notion.

## 9. Generative Output Roadmap

For the actionable steps, see [`docs/generative-output-tasks.md`](docs/generative-output-tasks.md). Track the summarized workstreams in GitHub Projects and reference them from the `capstone/` documentation:

1. **Prompt Library** – Curate reusable OpenAI prompts aligned to housing policy research goals; version them in `docs/prompts/`.
1. **Evaluation Harness** – Implement scripts that score generative outputs against acceptance criteria (accuracy, citation coverage, compliance).
1. **Human-in-the-Loop Reviews** – Define reviewer roles, review cadences, and escalation paths for questionable outputs.
1. **Data Governance** – Map data sources, retention policies, and redaction requirements before automating publication workflows.
1. **Reporting Automation** – Combine data from GitHub issues, Notion databases, and Zotero annotations into scheduled briefs or dashboards.

## 8. References

- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [Notion API Reference](https://developers.notion.com/reference/intro)
- [GitHub Actions Security Guide](https://docs.github.com/en/actions/security-guides)
- [Zotero Web API](https://www.zotero.org/support/dev/web_api/v3/start)
