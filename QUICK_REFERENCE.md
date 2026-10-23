# Repository Quick Reference

**Repository:** SfosssHousing/HousingPolicyResearch\
**Branch:** main\
**Current Commit:** 2f46cb3\
**Status:** Production-ready, single consolidated instance

______________________________________________________________________

## Directory Structure

```
HousingPolicyResearch/
├── docs/                          # All documentation
│   ├── sections/housing-policy-framework/
│   │   ├── 01-executive-summary-core-problem.md
│   │   ├── 02-theory-of-change-policy-framework.md
│   │   ├── 03-financial-modeling-roi-analysis.md
│   │   └── ... (through 10-complete-works-cited-apa.md)
│   ├── resources-index.md         # Citation index
│   ├── STYLE-APA.md              # Citation standards
│   ├── integration-plan.md        # Architecture guide
│   └── ... (other documentation)
│
├── src/                           # Python utilities
│   └── chatgpt_notion_sync/       # Notion/ChatGPT sync
│
├── scripts/                       # Automation scripts
│   ├── setup.sh                  # Environment setup
│   └── tcap/                     # TCAP automation
│
├── raycast-extension/            # Raycast commands
│   └── src/commands/             # Command implementations
│
├── tests/                         # Test suite
│   └── test_sync.py              # Sync tests
│
├── data/                         # Data files
├── artifacts/                    # Generated outputs
├── TCAP_PET/                    # Policy templates
├── TCAP-COMPLETE-PACKAGE/       # Complete documentation
│
├── pyproject.toml               # Python configuration
├── requirements.txt             # Python dependencies
├── raycast.manifest.json        # Raycast configuration
├── .gitignore                  # Git ignore rules
├── .pre-commit-config.yaml     # Pre-commit hooks
│
└── README.md                    # Project overview
```

______________________________________________________________________

## Key Files & Their Purpose

| File                                      | Purpose                                  |
| ----------------------------------------- | ---------------------------------------- |
| `docs/sections/housing-policy-framework/` | Policy research documents (versioned)    |
| `docs/resources-index.md`                 | Complete resource catalog with citations |
| `docs/STYLE-APA.md`                       | Citation standards for project           |
| `src/chatgpt_notion_sync/sync.py`         | Notion database synchronization          |
| `scripts/setup.sh`                        | Automated environment setup              |
| `raycast-extension/src/`                  | Raycast command implementations          |
| `tests/test_sync.py`                      | Test suite for sync utilities            |
| `pyproject.toml`                          | Python project configuration             |
| `requirements.txt`                        | Python dependencies                      |
| `.env.template`                           | Environment variables template           |

______________________________________________________________________

## Common Tasks

### Environment Setup

```bash
# Clone and setup
git clone git@github.com:SfosssHousing/HousingPolicyResearch.git
cd HousingPolicyResearch
bash scripts/setup.sh
```

### Run Tests

```bash
source .venv/bin/activate
python -m pytest tests/
```

### Run Code Quality Checks

```bash
pre-commit run --all-files
```

### Sync with Notion

```bash
python src/chatgpt_notion_sync/sync.py
```

### Add New Policy Document

```bash
# Create new section doc in docs/sections/housing-policy-framework/
# Use kebab-case naming: "NN-descriptive-name.md"
# Update docs/resources-index.md with citation
# Add to generative-output-version-control.md if AI-generated
# Commit with message: "docs: Add NN-section-name policy document"
```

______________________________________________________________________

## Important Notes

### No Redundant Clones

- ✅ This is the ONLY active clone
- ✅ All backups are at: `/Users/sethadmin/Desktop/HousingPolicyResearch_Archive/`
- ❌ Do NOT create additional clones (use branches instead)

### Node Modules

- ✅ Raycast extension: `npm install` to rebuild if needed
- ❌ Never commit `node_modules/` (use .gitignore)
- ✅ Always commit: `package.json` and `package-lock.json`

### Python Environment

- ✅ Use `python -m venv .venv` to create virtual environment
- ✅ Always activate: `source .venv/bin/activate`
- ❌ Never commit `.venv/` (use .gitignore)
- ✅ Always update: `requirements.txt`

### Documentation Standards

- ✅ All citations in APA 7th format (see `docs/STYLE-APA.md`)
- ✅ Policy docs in `docs/sections/housing-policy-framework/`
- ✅ All resources cataloged in `docs/resources-index.md`
- ✅ Tag generative AI outputs in `docs/generative-output-version-control.md`

______________________________________________________________________

## Backup Archive

**Location:** `/Users/sethadmin/Desktop/HousingPolicyResearch_Archive/`

Contains safe copies of:

- `HousingPolicyResearch_BACKUP/` — Recent clone (1.1G)
- `HousingPolicyResearch-1_BACKUP/` — Older clone (740M)
- `Housing_Policy_Workspace_BACKUP/` — Empty scaffold (24K)
- `workspace_raycast_scaffold_BACKUP/` — Raycast source (73M)

**Status:** Can be deleted once team confirms consolidation is stable.

______________________________________________________________________

## Git Workflow

### Branching

```bash
# Always branch from main
git checkout main
git pull origin main
git checkout -b feature/description

# Make changes, commit
git add .
git commit -m "Clear, descriptive message"

# Push and create PR
git push origin feature/description
# Open PR on GitHub
```

### Commit Message Format

```
[type]: Brief description (50 chars max)

Longer explanation if needed (72 chars per line).

- Bullet points for multiple changes
- Always reference issues/PRs if applicable
```

### Before Pushing

```bash
# Ensure clean state
git status

# Run tests
python -m pytest tests/

# Run code quality checks
pre-commit run --all-files

# Pull latest
git pull origin main

# Then push
git push origin feature/branch-name
```

______________________________________________________________________

## Troubleshooting

### Issue: "Virtual environment not found"

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Issue: "Pre-commit hooks failing"

```bash
# Run linter fixes
black .
flake8 --fix .
pre-commit run --all-files
```

### Issue: "Raycast extension not building"

```bash
cd raycast-extension
rm -rf node_modules package-lock.json
npm install
npm run build
```

### Issue: "Notion sync credentials not working"

```bash
# Verify .env file exists (not in repo!)
cp .env.template .env
# Edit .env with actual API keys
# Never commit .env
```

______________________________________________________________________

## Getting Help

1. **Documentation:** Check `docs/` folder for guides
1. **Architecture:** See `docs/integration-plan.md`
1. **Citations:** Follow `docs/STYLE-APA.md`
1. **Issues:** Create GitHub issue with clear description
1. **Setup:** Run `bash scripts/setup.sh` for automated setup

______________________________________________________________________

**Last Updated:** December 31, 2025\
**Consolidation Commit:** 2f46cb3\
**Archive:** ~/Desktop/HousingPolicyResearch_Archive/
