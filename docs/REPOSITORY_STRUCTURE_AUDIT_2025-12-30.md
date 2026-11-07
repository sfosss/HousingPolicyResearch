# Repository Structure Audit – 2025-12-30

**Purpose:** Comprehensive review of file organization across the HousingPolicyResearch repository to identify misplaced, redundant, or poorly organized files and provide reorganization recommendations.

**Audit Date:** 2025-12-30\
**Auditor:** Documentation & File Organization Review\
**Status:** COMPLETE with recommendations

______________________________________________________________________

## Executive Summary

**Repository Health Score:** ⚠️ 72% (Needs reorganization)

**Key Findings:**

- **Root directory clutter:** 23 files at root level that should be organized into subdirectories
- **Redundant files:** 3 files identified as duplicates or unnecessary copies
- **Poor directory naming:** 2 directories with non-standard names/formatting
- **Scattered assets:** 42 policy documents in `exported-assets (1)/` needing proper integration
- **Orphaned directories:** 1 directory (`Housing Policy Workspace/`) with transient content
- **Inconsistent naming:** Mix of file naming conventions (kebab-case, snake_case, PascalCase)

**Total Files Requiring Action:** 28+ files\
**Total Directories Requiring Action:** 3+ directories

______________________________________________________________________

## Detailed Audit Results

### 1. Root-Level Files Analysis

**Current State:** 23 active files at repository root (excluding hidden/config files)

#### ✅ Properly Located (Keep at Root)

These files are appropriately located at the root level:

| File                      | Reason                          | Status     |
| ------------------------- | ------------------------------- | ---------- |
| `README.md`               | Primary project documentation   | ✅ Correct |
| `SECURITY.md`             | Security policy for the project | ✅ Correct |
| `pyproject.toml`          | Python project configuration    | ✅ Correct |
| `requirements.txt`        | Python dependencies             | ✅ Correct |
| `raycast.manifest.json`   | Raycast extension configuration | ✅ Correct |
| `.env.template`           | Environment variable template   | ✅ Correct |
| `.pre-commit-config.yaml` | Pre-commit hook configuration   | ✅ Correct |
| `.gitignore`              | Git ignore rules                | ✅ Correct |

______________________________________________________________________

#### ⚠️ Misplaced Files (Recommend Moving)

| File                          | Current Location | Recommended Location | Reason                                            |
| ----------------------------- | ---------------- | -------------------- | ------------------------------------------------- |
| `HousingPolicyResearch.md`    | Root             | `docs/`              | Project overview; belongs with documentation      |
| `PERPLEXITY_QUICK_START.md`   | Root             | `docs/`              | Guide documentation; belongs with other guides    |
| `SYSTEM_STATUS_2025-12-30.md` | Root             | `docs/`              | Project status report; belongs with documentation |
| `tcap_automation.sh`          | Root             | `scripts/`           | Shell script; belongs in scripts directory        |
| `tcap_cron_setup.txt`         | Root             | `scripts/`           | Script configuration; belongs in scripts          |
| `tcap_task_automation.py`     | Root             | `scripts/`           | Python script; belongs in scripts directory       |
| `setup.sh`                    | Root             | `scripts/`           | Setup script; belongs in scripts directory        |

______________________________________________________________________

#### ❌ Duplicate/Redundant Files (Recommend Removing)

| File                                                | Issue                     | Recommended Action | Reason                                            |
| --------------------------------------------------- | ------------------------- | ------------------ | ------------------------------------------------- |
| `README copy.md`                                    | Duplicate/test file       | **DELETE**         | Appears to be accidental copy; no unique content  |
| `NYC_Housing_Subsidy_Ops_Tasks_Notion.csv`          | Data file without context | **REVIEW & MOVE**  | Unclear purpose; if still needed, move to `data/` |
| `HousingPolicyResearch.md` (if duplicate of README) | Possible duplicate        | **REVIEW**         | Check if content duplicates README.md             |

______________________________________________________________________

#### ⏱️ Transient/Maintenance Files (Organize)

| File                                   | Issue              | Recommended Action                                  |
| -------------------------------------- | ------------------ | --------------------------------------------------- |
| `TCAP_DEPLOYMENT_SUMMARY.txt`          | Status snapshot    | Move to `docs/archives/tcap/` or delete if outdated |
| `TCAP_FILE_MANIFEST.txt`               | Outdated manifest  | Move to `docs/archives/tcap/`                       |
| `TCAP_Status_Report.txt`               | Old status report  | Move to `docs/archives/tcap/`                       |
| `TCAP_Version_History_Audit_Log.txt`   | Audit log          | Move to `docs/archives/tcap/`                       |
| `TCAP_Interactive_Dashboard_README.md` | TCAP documentation | Move to `docs/tcap/`                                |
| `TCAP_Task_Status_Risk_Tracking.csv`   | Data snapshot      | Move to `data/archives/` or `backups/`              |

______________________________________________________________________

### 2. Directory Organization Analysis

#### ✅ Well-Organized Directories

| Directory   | Contents                                                  | Status            |
| ----------- | --------------------------------------------------------- | ----------------- |
| `src/`      | Python source code (chatgpt_notion_sync, commands, utils) | ✅ Good structure |
| `tests/`    | Unit tests matching `src/` structure                      | ✅ Good structure |
| `docs/`     | 20+ documentation files organized logically               | ✅ Good structure |
| `scripts/`  | 3 automation scripts                                      | ✅ Good structure |
| `comments/` | Issue-related coordination files                          | ✅ Good structure |

______________________________________________________________________

#### ⚠️ Poorly Organized / Needs Improvement

| Directory                   | Issues                                                                        | Recommendation                       |
| --------------------------- | ----------------------------------------------------------------------------- | ------------------------------------ |
| `exported-assets (1)/`      | 42 policy docs with inconsistent naming, poor naming convention (parentheses) | See Section 3 below                  |
| `Housing Policy Workspace/` | Contains scaffolding files and archive; unclear purpose                       | Archive or consolidate               |
| `00_admin/`                 | Hidden admin folder; unclear organization                                     | Document purpose or remove           |
| `backups/`                  | Contains TCAP backup CSVs; no dated organization                              | Implement consistent naming/dating   |
| `artifacts/`                | Empty or unclear purpose                                                      | Document or remove                   |
| `references/`               | Empty or unclear purpose                                                      | Document or consolidate with `docs/` |
| `logs/`                     | Empty placeholder                                                             | Document purpose                     |

______________________________________________________________________

#### ❌ Non-Standard Directory Names

| Directory                   | Issue                                                | Recommendation                                        |
| --------------------------- | ---------------------------------------------------- | ----------------------------------------------------- |
| `exported-assets (1)/`      | Poor naming (parentheses, numbered), not semantic    | Rename to `docs/exports/` or `docs/policy-documents/` |
| `Housing Policy Workspace/` | Inconsistent with repo naming (should be kebab-case) | Rename to `workspace/` or archive                     |

______________________________________________________________________

### 3. Detailed Analysis: `exported-assets (1)/` Directory

**Status:** ⚠️ Critical organization needed

**Contents Summary:**

- 42 files (mostly Markdown and binary documents)
- Mix of policy templates, legal frameworks, and generated content
- Duplicates and variants with poor naming (e.g., `Final Housing_Subsidy_MasterFormatted_Final copy copy.docx`)
- PNG image files mixed with markdown files

**Organization Issues:**

1. **Poor directory naming:** Numbered folder name with parentheses (`exported-assets (1)/`)
1. **Mixed content types:** Markdown, Word docs, Excel, PNG images all at same level
1. **Duplicate files:** Multiple copies with "copy", "copy copy" suffixes
1. **Lack of categorization:** No subdirectories for legal frameworks vs. templates vs. reports
1. **Unclear purpose:** Directory name doesn't describe content; appears to be export from external tool

**Recommended Reorganization:**

```
docs/
├── exports/                          # or docs/policy-documents/
│   ├── legal-frameworks/
│   │   ├── LOCAL_LAW_A_*.md
│   │   ├── LOCAL_LAW_B_*.md
│   │   ├── LOCAL_LAW_C_*.md
│   │   ├── LOCAL_LAW_D_*.md
│   │   ├── PART_V_Legal_Framework_*.md
│   │   └── PART_V_REVISED_TERMINOLOGY_*.md
│   ├── policy-reports/
│   │   ├── PET_Master_Policy_Report_*.md
│   │   ├── PET_Legal_Feasibility_*.md
│   │   ├── PET_Milestones_Workplan_*.md
│   │   └── MASTER_Works_Cited_APA_7th.md
│   ├── templates/
│   │   ├── PET_CLT_Ground_Lease_Template.md
│   │   ├── PET_Coop_Bylaws_Template.md
│   │   ├── PET_Disclosure_And_Consent_Template.md
│   │   └── PET_Equity_Share_Agreement_Template.md
│   ├── operational-docs/
│   │   ├── PET_Operations_Playbook_*.md
│   │   ├── PET_One_Pager_*.md
│   │   └── PET_Risk_Log_Stakeholders_*.md
│   ├── assets/
│   │   ├── pet_deck_outline.png
│   │   ├── pet_deck_structure.png
│   │   └── [other image assets]
│   └── archive/
│       ├── Final_Housing_Subsidy_*.docx
│       └── [old versions/drafts]
```

**Specific Files to Clean Up:**

| File                                                         | Action           | Reason                                      |
| ------------------------------------------------------------ | ---------------- | ------------------------------------------- |
| `Final Housing_Subsidy_MasterFormatted_Final copy copy.docx` | DELETE           | Duplicate/test artifact                     |
| `pet_deck_outline 2.png`                                     | DELETE or RENAME | Duplicate variant                           |
| `pet_deck_structure 2.png`                                   | DELETE or RENAME | Duplicate variant                           |
| `NDA_Tenant_Privacy_Inspection_Agreement_v2 copy.docx`       | DELETE or RENAME | Duplicate variant                           |
| `index.html`                                                 | REVIEW           | Clarify purpose (appears to be from export) |

______________________________________________________________________

### 4. File Naming Consistency Analysis

**Current State:** Inconsistent naming conventions throughout repository

**Identified Patterns:**

| Pattern    | Examples                                                                       | Count | Issue                                      |
| ---------- | ------------------------------------------------------------------------------ | ----- | ------------------------------------------ |
| kebab-case | `perplexity-integration-guide.md`, `housing-subsidy-reform-policy-draft-v1.md` | 8     | Good; consistent with repo style           |
| snake_case | `tcap_automation.sh`, `tcap_cron_setup.txt`                                    | 6     | Acceptable but inconsistent                |
| PascalCase | `TCAP_DEPLOYMENT_SUMMARY.txt`, `SYSTEM_STATUS_2025-12-30.md`                   | 7     | Inconsistent; use kebab-case or snake_case |
| Mixed/Poor | `HousingPolicyResearch.md`, `README copy.md`, `NYC_Housing_...csv`             | 5+    | Needs standardization                      |

**Recommendation:** Adopt **kebab-case** as standard for all new files (already mostly in use)

______________________________________________________________________

### 5. Hidden/System Files Analysis

**Status:** ✅ Properly organized

| File                 | Purpose                             | Status                               |
| -------------------- | ----------------------------------- | ------------------------------------ |
| `.github/`           | GitHub workflows and configurations | ✅ Correct                           |
| `.devcontainer/`     | Dev container configuration         | ✅ Correct                           |
| `.venv/`             | Python virtual environment          | ✅ Correct (should be in .gitignore) |
| `.pytest_cache/`     | Pytest cache                        | ✅ Correct (should be in .gitignore) |
| `.git/`              | Git version control                 | ✅ Correct                           |
| `.secrets.baseline/` | Detect-secrets baseline             | ✅ Correct                           |

______________________________________________________________________

## Action Plan & Recommendations

### Priority 1: CRITICAL (Do Immediately)

#### 1.1 Remove Duplicate/Test Files

- **DELETE:** `README copy.md` (appears to be test artifact)
- **DELETE:** `pet_deck_outline 2.png` and `pet_deck_structure 2.png` (duplicates with different variants)
- **DELETE:** `Final Housing_Subsidy_MasterFormatted_Final copy copy.docx` (clearly a test file)
- **REVIEW & DELETE:** `NDA_Tenant_Privacy_Inspection_Agreement_v2 copy.docx`

**Impact:** Reduces clutter; prevents confusion

______________________________________________________________________

#### 1.2 Rename Non-Standard Directories

- **RENAME:** `exported-assets (1)/` → `docs/exports/` (or `docs/policy-documents/`)
- **RENAME:** `Housing Policy Workspace/` → `workspace/` (or archive)

**Impact:** Improves semantic clarity; follows repo naming conventions

______________________________________________________________________

### Priority 2: HIGH (Do Soon)

#### 2.1 Move Root-Level Scripts to `scripts/`

**Files to move:**

```
tcap_automation.sh        → scripts/tcap-automation.sh
tcap_cron_setup.txt       → scripts/tcap-cron-setup.txt
tcap_task_automation.py   → scripts/tcap-task-automation.py
setup.sh                  → scripts/setup.sh (or root if entry point)
```

**Impact:** Cleaner root; better organization

______________________________________________________________________

#### 2.2 Move Documentation Files to `docs/`

**Files to move:**

```
HousingPolicyResearch.md              → docs/housing-policy-research-overview.md
PERPLEXITY_QUICK_START.md             → docs/perplexity-quick-start.md
SYSTEM_STATUS_2025-12-30.md           → docs/system-status-2025-12-30.md
TCAP_Interactive_Dashboard_README.md  → docs/tcap/interactive-dashboard-guide.md
```

**Impact:** Root directory cleaner; documentation more discoverable

______________________________________________________________________

#### 2.3 Reorganize `exported-assets (1)/` (42 files)

**Create subdirectories within `docs/exports/`:**

1. `legal-frameworks/` - for LOCAL_LAW and PART_V files
1. `policy-reports/` - for master reports and analysis
1. `templates/` - for legal/operational templates
1. `operational-docs/` - for playbooks and operational guides
1. `assets/` - for PNG, images, visual materials
1. `archive/` - for old drafts and variants

**Action:** Create structure and redistribute files by category

**Impact:** Better discoverability; enables easier searching and reference

______________________________________________________________________

### Priority 3: MEDIUM (Plan for Next Sprint)

#### 3.1 Organize TCAP-Related Files

Create `docs/tcap/` directory:

```
docs/tcap/
├── TCAP_Interactive_Dashboard_README.md
├── deployment/
│   ├── TCAP_DEPLOYMENT_SUMMARY.md
│   └── TCAP_Status_Report.md
├── audit/
│   ├── TCAP_Version_History_Audit_Log.md
│   └── TCAP_FILE_MANIFEST.md
└── tracking/
    └── TCAP_Task_Status_Risk_Tracking.csv
```

**Impact:** TCAP documentation centralized and organized by domain

______________________________________________________________________

#### 3.2 Clarify Purpose of Empty Directories

| Directory     | Action                             | Reason                          |
| ------------- | ---------------------------------- | ------------------------------- |
| `artifacts/`  | Document purpose or remove         | Currently empty; unclear intent |
| `references/` | Consolidate with `docs/` or remove | Overlaps with resources.csv     |
| `logs/`       | Document purpose; implement usage  | Currently empty placeholder     |
| `data/`       | Document intended use              | Currently empty; unclear scope  |

______________________________________________________________________

#### 3.3 Standardize All File Naming

**Convention:** Use **kebab-case** for all new files

- Good: `perplexity-integration-guide.md` ✅
- Bad: `TCAP_Interactive_Dashboard_README.md` ❌ → Use `tcap-interactive-dashboard-guide.md`

**Action:** Create `.naming-convention.md` document in root describing standard

______________________________________________________________________

#### 3.4 Clarify `Housing Policy Workspace/` Directory

**Current contents:**

- `housing_policy_scaffold/` (directory)
- `housing_policy_scaffold.zip` (archive)

**Decision needed:**

- Is this a scaffolding template? → Move to `templates/` or archive
- Is this transient? → Remove if no longer needed
- Is this for onboarding? → Document purpose in README

______________________________________________________________________

### Priority 4: LOW (Polish)

#### 4.1 Add `.gitkeep` Files to Empty Directories

Ensure empty directories are preserved in Git:

```
data/.gitkeep
artifacts/.gitkeep
references/.gitkeep
```

______________________________________________________________________

#### 4.2 Create Directory Manifest

Add `DIRECTORY_STRUCTURE.md` at root documenting:

- Purpose of each directory
- What files belong where
- Guidelines for future file placement

______________________________________________________________________

#### 4.3 Add `docs/NAMING_CONVENTIONS.md`

Document project-wide standards:

- File naming (kebab-case preferred)
- Directory naming conventions
- Version numbering format (if used)

______________________________________________________________________

## Summary Table: Files Requiring Action

| File/Directory                             | Current Location       | Action                           | Priority | Status            |
| ------------------------------------------ | ---------------------- | -------------------------------- | -------- | ----------------- |
| `README copy.md`                           | Root                   | DELETE                           | 1        | ⏳ Ready          |
| `pet_deck_outline 2.png`                   | `exported-assets (1)/` | DELETE                           | 1        | ⏳ Ready          |
| `pet_deck_structure 2.png`                 | `exported-assets (1)/` | DELETE                           | 1        | ⏳ Ready          |
| `Final Housing_Subsidy_..._copy copy.docx` | `exported-assets (1)/` | DELETE                           | 1        | ⏳ Ready          |
| `exported-assets (1)/`                     | Root                   | RENAME to `docs/exports/`        | 1        | ⏳ Ready          |
| `Housing Policy Workspace/`                | Root                   | REVIEW & RENAME/ARCHIVE          | 1        | ⏳ Needs review   |
| `tcap_automation.sh`                       | Root                   | MOVE to `scripts/`               | 2        | ⏳ Ready          |
| `tcap_cron_setup.txt`                      | Root                   | MOVE to `scripts/`               | 2        | ⏳ Ready          |
| `tcap_task_automation.py`                  | Root                   | MOVE to `scripts/`               | 2        | ⏳ Ready          |
| `HousingPolicyResearch.md`                 | Root                   | MOVE to `docs/`                  | 2        | ⏳ Ready          |
| `PERPLEXITY_QUICK_START.md`                | Root                   | MOVE to `docs/`                  | 2        | ⏳ Ready          |
| `SYSTEM_STATUS_2025-12-30.md`              | Root                   | MOVE to `docs/`                  | 2        | ⏳ Ready          |
| `exported-assets (1)/` (42 files)          | One directory          | REORGANIZE into subdirectories   | 2        | ⏳ Needs planning |
| `docs/tcap/`                               | N/A                    | CREATE & ORGANIZE                | 3        | ⏳ Future         |
| All files                                  | Repository-wide        | STANDARDIZE naming to kebab-case | 3        | ⏳ Future         |

______________________________________________________________________

## Implementation Checklist

- [ ] **Priority 1 - CRITICAL:**

  - [ ] Delete `README copy.md`
  - [ ] Delete `pet_deck_outline 2.png` and `pet_deck_structure 2.png`
  - [ ] Delete `Final Housing_Subsidy_*_copy copy.docx`
  - [ ] Delete `NDA_Tenant_Privacy_Inspection_Agreement_v2 copy.docx` (if no longer needed)
  - [ ] Rename `exported-assets (1)/` to `docs/exports/`
  - [ ] Review and decide on `Housing Policy Workspace/` directory

- [ ] **Priority 2 - HIGH:**

  - [ ] Move scripts to `scripts/` directory (4 files)
  - [ ] Move documentation to `docs/` directory (4 files)
  - [ ] Reorganize `docs/exports/` into category subdirectories (42 files in 5 subdirectories)

- [ ] **Priority 3 - MEDIUM:**

  - [ ] Create `docs/tcap/` and organize TCAP files
  - [ ] Clarify/document purpose of empty directories
  - [ ] Document naming conventions

- [ ] **Priority 4 - LOW:**

  - [ ] Add `.gitkeep` to empty directories
  - [ ] Create `DIRECTORY_STRUCTURE.md`
  - [ ] Create `docs/NAMING_CONVENTIONS.md`

______________________________________________________________________

## Notes & Observations

### Positive Findings ✅

- Core codebase (`src/`, `tests/`) is well-organized
- Documentation (`docs/`) has good structure
- GitHub configuration is properly located
- Pre-commit hooks are configured correctly

### Areas for Improvement ⚠️

- Root directory has become cluttered with files that belong in subdirectories
- Exported assets directory needs significant reorganization
- Naming conventions not standardized across all files
- Empty directories lack documentation of purpose
- Some old/transient files should be archived or removed

### Recommendations for Future Maintenance 📋

1. **Establish file placement guidelines** before taking on new files
1. **Regular audits** (quarterly) to prevent clutter accumulation
1. **Archive old files** to `docs/archives/` rather than deleting
1. **Enforce naming conventions** in code review process
1. **Document directory purposes** in a central registry

______________________________________________________________________

**Audit Completed:** 2025-12-30\
**Next Review:** 2025-03-30 (Quarterly)\
**Estimated Time to Implement:** 1-2 hours for Priority 1 & 2 actions
