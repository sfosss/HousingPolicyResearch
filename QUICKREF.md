# Quick Reference Guide

This guide provides quick commands and references for common tasks in the Housing Policy Research project.

## Initial Setup

```bash
# Clone and setup
git clone https://github.com/SfosssHousing/HousingPolicyResearch.git
cd HousingPolicyResearch
./setup.sh

# Configure environment
cp .env.template .env
# Edit .env with your API keys

# Activate virtual environment
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows
```

## Daily Development

```bash
# Activate virtual environment
source .venv/bin/activate

# Update dependencies (if needed)
pip install -r requirements.txt

# Before committing
pre-commit run --all-files

# Format code
black .
flake8 .
```

## Common Commands

### Git Workflow

```bash
# Create a new branch
git checkout -b feature/your-feature-name

# Check status
git status

# Stage and commit
git add .
git commit -m "Your commit message"

# Push to remote
git push origin your-branch-name
```

### Python Scripts

```bash
# Validate API connections
python scripts/validate_connections.py

# Generate policy proposal
python scripts/generate_policy_proposal.py

# Evaluate policy proposal
python evaluation/evaluate_policy_proposal.py
```

### Code Quality

```bash
# Run all pre-commit hooks
pre-commit run --all-files

# Format Python code
black .

# Lint Python code
flake8 .

# Format Markdown
mdformat *.md docs/*.md
```

## Environment Variables

Required in `.env` file:

```bash
# Required
OPENAI_API_KEY=sk-...

# Optional
NOTION_API_KEY=secret_...
NOTION_DATABASE_ID=...
ZOTERO_API_KEY=...
ZOTERO_LIBRARY_ID=...
```

## Directory Structure

```
├── .github/workflows/    # CI/CD workflows
├── artifacts/            # Generated outputs
├── docs/                 # Documentation
│   ├── prompts/         # AI prompt templates
│   ├── outputs/         # AI-generated archives
│   └── audit-notes/     # Security logs
├── evaluation/          # Evaluation scripts
├── logs/                # Application logs
├── scripts/             # Automation scripts
└── .env                 # Your local config (not in git)
```

## Troubleshooting

### Virtual Environment Issues

```bash
# Remove and recreate
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Pre-commit Hook Failures

```bash
# Update hooks
pre-commit autoupdate

# Clean cache
pre-commit clean

# Reinstall
pre-commit uninstall
pre-commit install
```

### API Connection Issues

```bash
# Test connections
python scripts/validate_connections.py

# Check logs
cat logs/connection-checks/*.json
```

## Getting Help

1. Check [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines
1. Review [docs/environment-setup.md](docs/environment-setup.md) for setup help
1. Open a GitHub issue for problems or questions
1. Review [docs/project-roadmap.md](docs/project-roadmap.md) for project status

## Quick Links

- [Main README](README.md) - Project overview
- [Setup Guide](docs/environment-setup.md) - Detailed setup instructions
- [Contributing](CONTRIBUTING.md) - Contribution guidelines
- [Roadmap](docs/project-roadmap.md) - Project plans
- [Security Rules](docs/rulesets.md) - Security practices
