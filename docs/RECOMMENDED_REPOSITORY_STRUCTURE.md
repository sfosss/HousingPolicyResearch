# Recommended Repository Structure

This document shows the target organization after implementing the audit recommendations.

## Current vs. Recommended Structure

### Current Root Directory (Cluttered)

```
HousingPolicyResearch-1/
├── HousingPolicyResearch.md              ⚠️ Move to docs/
├── NYC_Housing_Subsidy_Ops_Tasks_Notion.csv  ⚠️ Move to data/
├── PERPLEXITY_QUICK_START.md             ⚠️ Move to docs/
├── README copy.md                        ❌ DELETE
├── README.md                             ✅ Keep
├── SECURITY.md                           ✅ Keep
├── SYSTEM_STATUS_2025-12-30.md           ⚠️ Move to docs/
├── TCAP_*.txt, *.md                      ⚠️ Move to docs/tcap/
├── setup.sh                              ⚠️ Move to scripts/
├── tcap_*.sh, tcap_*.py                  ⚠️ Move to scripts/
├── pyproject.toml                        ✅ Keep
├── requirements.txt                      ✅ Keep
├── raycast.manifest.json                 ✅ Keep
├── .env.template                         ✅ Keep
├── .pre-commit-config.yaml               ✅ Keep
└── [many directories...]
```

### Recommended Root Directory (Clean)

```
HousingPolicyResearch-1/
├── README.md                    ✅ Primary documentation
├── SECURITY.md                  ✅ Security policy
├── pyproject.toml               ✅ Python config
├── requirements.txt             ✅ Dependencies
├── raycast.manifest.json        ✅ Raycast config
├── .env.template                ✅ Environment template
├── .pre-commit-config.yaml      ✅ Pre-commit hooks
│
├── src/                         ✅ Source code (unchanged)
├── tests/                       ✅ Tests (unchanged)
├── scripts/                     ✅ Automation scripts
│   ├── setup.sh
│   ├── tcap-automation.sh
│   ├── tcap-cron-setup.txt
│   ├── tcap-task-automation.py
│   ├── validate-connections.py
│   └── cross-chat-sync.sh
│
├── docs/                        ✅ Documentation (expanded)
│   ├── README.md
│   ├── *.md                     (20+ guide files)
│   │
│   ├── exports/                 📁 NEW: Policy documents
│   │   ├── legal-frameworks/
│   │   │   ├── LOCAL_LAW_A_*.md
│   │   │   ├── LOCAL_LAW_B_*.md
│   │   │   ├── LOCAL_LAW_C_*.md
│   │   │   ├── LOCAL_LAW_D_*.md
│   │   │   ├── PART_V_Legal_*.md
│   │   │   └── PART_V_REVISED_*.md
│   │   │
│   │   ├── policy-reports/
│   │   │   ├── PET_Master_Policy_Report_*.md
│   │   │   ├── PET_Legal_Feasibility_*.md
│   │   │   ├── PET_Milestones_Workplan_*.md
│   │   │   └── MASTER_Works_Cited_APA_7th.md
│   │   │
│   │   ├── templates/
│   │   │   ├── PET_CLT_Ground_Lease_Template.md
│   │   │   ├── PET_Coop_Bylaws_Template.md
│   │   │   ├── PET_Disclosure_And_Consent_Template.md
│   │   │   └── PET_Equity_Share_Agreement_Template.md
│   │   │
│   │   ├── operational-docs/
│   │   │   ├── PET_Operations_Playbook_*.md
│   │   │   ├── PET_One_Pager_*.md
│   │   │   └── PET_Risk_Log_Stakeholders_*.md
│   │   │
│   │   ├── assets/
│   │   │   ├── pet_deck_outline.png
│   │   │   ├── pet_deck_structure.png
│   │   │   ├── pet_deck_structure.png      (only one variant)
│   │   │   └── [other visual assets]
│   │   │
│   │   └── archive/
│   │       ├── Final_Housing_Subsidy_*.docx
│   │       └── [old versions/drafts]
│   │
│   ├── tcap/                    📁 NEW: TCAP documentation
│   │   ├── TCAP_Interactive_Dashboard_README.md
│   │   ├── deployment/
│   │   │   ├── TCAP_DEPLOYMENT_SUMMARY.md
│   │   │   └── TCAP_Status_Report.md
│   │   ├── audit/
│   │   │   ├── TCAP_Version_History_Audit_Log.md
│   │   │   └── TCAP_FILE_MANIFEST.md
│   │   └── tracking/
│   │       └── TCAP_Task_Status_Risk_Tracking.csv
│   │
│   └── prompts/                 ✅ Prompt templates (unchanged)
│
├── data/                        ✅ Data files
│   └── NYC_Housing_Subsidy_Ops_Tasks_Notion.csv
│
├── comments/                    ✅ Issue coordination (unchanged)
├── Capstone/                    ✅ Project milestones (unchanged)
├── backups/                     ✅ Backup files (unchanged)
│
└── .github/                     ✅ GitHub config (unchanged)
```

______________________________________________________________________

## Detailed Directory Purposes

### Root Level Files (Kept at Root)

**Why at root?**

- Entry points for developers and CI/CD systems
- Quick access to critical project information and configuration

```
README.md              → Project overview, quick start, key links
SECURITY.md            → Access controls, vulnerability disclosure
pyproject.toml         → Python project metadata and dependencies
requirements.txt       → Package list for pip install
raycast.manifest.json  → Raycast extension configuration
.env.template          → Template for environment variables
.pre-commit-config.yaml → Git hook configuration
```

______________________________________________________________________

### `src/` Directory ✅ (Well-Organized, No Changes)

```
src/
├── chatgpt_notion_sync/
│   ├── sync.py
│   ├── config.py
│   ├── job_app_manager.py
│   └── task_list.py
│
├── commands/           → Raycast command implementations
├── utils/
│   └── api.ts         → API client functions
```

______________________________________________________________________

### `tests/` Directory ✅ (Well-Organized, No Changes)

```
tests/
├── test_sync.py
├── test_job_app_manager.py
└── test_task_list.py
```

______________________________________________________________________

### `scripts/` Directory ✅ (Expanded with Root Files)

```
scripts/
├── .gitkeep
├── setup.sh                    ← Moved from root
├── validate-connections.py     ✅ Already here
├── cross-chat-sync.sh          ✅ Already here
│
├── tcap/                       📁 NEW: TCAP automation
│   ├── tcap-automation.sh      ← Moved from root (renamed)
│   ├── tcap-cron-setup.txt     ← Moved from root (renamed)
│   └── tcap-task-automation.py ← Moved from root (renamed)
│
└── README.md                   📁 NEW: Script documentation
    (Documenting what each script does and how to use)
```

______________________________________________________________________

### `docs/` Directory ✅ (Expanded Significantly)

#### Core Documentation (20+ files, already at root of `docs/`)

```
docs/
├── README.md                                    ✅ Documentation index
├── STYLE-APA.md                                ✅ Citation guide
├── integration-plan.md                         ✅ System setup
├── connection-checks.md                        ✅ Validation procedures
├── environment-setup.md                        ✅ Environment guide
├── environment-integrations.md                 ✅ Integration details
├── project-roadmap.md                          ✅ Roadmap
├── generative-output-version-control.md        ✅ AI output tracking
├── generative-output-tasks.md                  ✅ AI workflow guide
├── agent-instructions-verification.md          ✅ Agent verification
├── agent-status-2025-12-02.md                  ✅ Status report
├── workspace-readiness.md                      ✅ Readiness checklist
├── housing-subsidy-reform-policy-draft-v1.md   ✅ Policy draft
├── tenant-toolkit-v1.md                        ✅ Toolkit documentation
├── resources-index.md                          ✅ Resource catalog
├── resources-summary.md                        ✅ Resource summary
├── resources.csv                               ✅ Resource data
├── FILE_PATH_FIXES_2025-12-30.md               ✅ Fix documentation
├── REPOSITORY_STRUCTURE_AUDIT_2025-12-30.md    ✅ This audit
├── universal-linking-guide.md                  ✅ Apple linking guide
├── perplexity-integration-guide.md             ✅ Perplexity guide
│
├── DIRECTORY_STRUCTURE.md                      📁 NEW: Structure guide
├── NAMING_CONVENTIONS.md                       📁 NEW: Naming guide
│
├── exports/                                    📁 NEW: Policy exports
│   ├── README.md
│   ├── legal-frameworks/
│   ├── policy-reports/
│   ├── templates/
│   ├── operational-docs/
│   ├── assets/
│   └── archive/
│
├── tcap/                                       📁 NEW: TCAP docs
│   ├── README.md
│   ├── TCAP_Interactive_Dashboard_README.md
│   ├── deployment/
│   ├── audit/
│   └── tracking/
│
├── prompts/                                    ✅ Already organized
│   ├── [prompt templates]
│   └── README.md
│
└── archives/                                   📁 OPTIONAL: Old docs
    └── [deprecated files]
```

______________________________________________________________________

### `data/` Directory ✅ (Organized)

```
data/
├── .gitkeep
├── NYC_Housing_Subsidy_Ops_Tasks_Notion.csv   ← Moved from root
│
└── [other data files as project grows]
```

______________________________________________________________________

### `comments/` Directory ✅ (Coordination, Unchanged)

```
comments/
├── issue-2.txt
└── issue-34-coordination.md
```

______________________________________________________________________

### `Capstone/` Directory ✅ (Project Tracking, Unchanged)

```
Capstone/
├── README.md
├── indexes/
│   └── [index files]
```

______________________________________________________________________

### `backups/` Directory ✅ (Backup Storage)

```
backups/
├── .gitkeep
├── TCAP_Tasks_v20251224_032344.csv  ✅ Backup file
└── [other backups as needed]
```

______________________________________________________________________

### `.github/` Directory ✅ (GitHub Config, Unchanged)

```
.github/
├── workflows/
├── copilot-instructions.md         ✅ Recently fixed
└── [other GitHub configs]
```

______________________________________________________________________

### Empty/Placeholder Directories

```
artifacts/              → PURPOSE: Store generated artifacts (currently unused)
references/             → PURPOSE: Reference materials (consolidate or remove)
logs/                   → PURPOSE: Runtime logs and outputs (currently unused)
00_admin/               → PURPOSE: Admin settings and templates
```

**Recommendation:** Document purpose of each in root `DIRECTORY_STRUCTURE.md`

______________________________________________________________________

## Migration Steps (Priority Order)

### Phase 1: DELETE (Cleanup - 5 minutes)

```bash
# Remove duplicate/test files
rm README\ copy.md
rm exported-assets\ \(1\)/pet_deck_outline\ 2.png
rm exported-assets\ \(1\)/pet_deck_structure\ 2.png
rm exported-assets\ \(1\)/Final\ Housing_Subsidy_*copy\ copy.docx
rm exported-assets\ \(1\)/NDA_Tenant_*copy.docx
```

______________________________________________________________________

### Phase 2: RENAME (Directory Structure - 10 minutes)

```bash
# Rename poorly named directory
mv exported-assets\ \(1\) docs/exports

# Optionally rename/archive Housing Policy Workspace
# mv Housing\ Policy\ Workspace workspace
# OR remove if content is not needed
```

______________________________________________________________________

### Phase 3: CREATE (New Directories - 15 minutes)

```bash
# Create subdirectories within docs/exports/
mkdir -p docs/exports/{legal-frameworks,policy-reports,templates,operational-docs,assets,archive}

# Create TCAP structure
mkdir -p docs/tcap/{deployment,audit,tracking}

# Create scripts/tcap directory
mkdir -p scripts/tcap
```

______________________________________________________________________

### Phase 4: MOVE FILES (Reorganization - 20 minutes)

**Move documentation:**

```bash
mv HousingPolicyResearch.md docs/housing-policy-research-overview.md
mv PERPLEXITY_QUICK_START.md docs/
mv SYSTEM_STATUS_2025-12-30.md docs/
mv TCAP_Interactive_Dashboard_README.md docs/tcap/
```

**Move scripts:**

```bash
mv setup.sh scripts/
mv tcap_automation.sh scripts/tcap/tcap-automation.sh
mv tcap_cron_setup.txt scripts/tcap/tcap-cron-setup.txt
mv tcap_task_automation.py scripts/tcap/tcap-task-automation.py
```

**Move data:**

```bash
mv NYC_Housing_Subsidy_Ops_Tasks_Notion.csv data/
```

**Move exported assets:**

```bash
# Legal frameworks
mv docs/exports/LOCAL_LAW_*.md docs/exports/legal-frameworks/
mv docs/exports/PART_V_*.md docs/exports/legal-frameworks/

# Reports
mv docs/exports/PET_Master_Policy_*.md docs/exports/policy-reports/
mv docs/exports/PET_Legal_Feasibility_*.md docs/exports/policy-reports/
mv docs/exports/MASTER_Works_Cited_*.md docs/exports/policy-reports/

# Templates
mv docs/exports/PET_*_Template.md docs/exports/templates/

# Operational
mv docs/exports/PET_Operations_*.md docs/exports/operational-docs/
mv docs/exports/PET_One_Pager_*.md docs/exports/operational-docs/
mv docs/exports/PET_Risk_Log_*.md docs/exports/operational-docs/

# Assets
mv docs/exports/*.png docs/exports/assets/

# Archive old docs
mv docs/exports/*.docx docs/exports/archive/
mv docs/exports/index.html docs/exports/archive/  # unless needed elsewhere
```

**Move TCAP files:**

```bash
mv TCAP_DEPLOYMENT_SUMMARY.txt docs/tcap/deployment/
mv TCAP_FILE_MANIFEST.txt docs/tcap/audit/
mv TCAP_Status_Report.txt docs/tcap/deployment/
mv TCAP_Version_History_Audit_Log.txt docs/tcap/audit/
mv TCAP_Task_Status_Risk_Tracking.csv docs/tcap/tracking/
```

______________________________________________________________________

### Phase 5: DOCUMENTATION (Create guides - 15 minutes)

Create new documentation files:

- `docs/DIRECTORY_STRUCTURE.md` - Directory purposes and guidelines
- `docs/NAMING_CONVENTIONS.md` - Naming standards
- `scripts/README.md` - Script documentation
- `docs/exports/README.md` - Exports directory guide

______________________________________________________________________

## Total Estimated Effort

- **Phase 1 (Delete):** 5 minutes
- **Phase 2 (Rename):** 10 minutes
- **Phase 3 (Create dirs):** 15 minutes
- **Phase 4 (Move files):** 20 minutes
- **Phase 5 (Documentation):** 15 minutes

**Total:** ~60-90 minutes for complete reorganization

______________________________________________________________________

## Benefits After Reorganization

✅ **Root directory cleaner** - Only 7 files at root (down from 23)
✅ **Better discoverability** - Files organized by category and domain
✅ **Easier navigation** - Clear directory purposes with documentation
✅ **Scalable structure** - Ready for project growth
✅ **Standards established** - Naming conventions prevent future clutter
✅ **Reduced confusion** - Clear where files belong
✅ **CI/CD friendly** - Consistent structure for automation

______________________________________________________________________

**Recommended Implementation:** During next development sprint or dedicated maintenance window
**Review Schedule:** Quarterly (every 3 months) to prevent clutter re-accumulation
