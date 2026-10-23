# Clone Inventory & Disposition Plan

**Created:** 2025-12-31\
**Purpose:** Comprehensive audit and tagging of all duplicate clones before consolidating into single repo

______________________________________________________________________

## Executive Summary

Four extra clones/scaffolds exist alongside the main repo. Total footprint: **~1.95GB**. Most are duplicates at older commits; some contain unique dev artifacts that should be archived.

| Item                                 | Size | Status                           | Disposition                                               |
| ------------------------------------ | ---- | -------------------------------- | --------------------------------------------------------- |
| `HousingPolicyResearch/`             | 1.1G | Partial clone (8ad24e3)          | **REVIEW** - has artifacts/ with full policy docs         |
| `HousingPolicyResearch-1/`           | 752M | Older clone (9ee1d5e) + .venv    | **DISCARD** - keep artifacts only                         |
| `Housing Policy Workspace/`          | 24K  | Empty scaffold                   | **DISCARD** - only .gitkeeps                              |
| `workspace/housing_policy_scaffold/` | 73M  | Raycast extension + node_modules | **REVIEW** - extract raycast source, discard node_modules |
| `workspace/*.zip`                    | —    | Archives                         | **DISCARD** - redundant                                   |

______________________________________________________________________

## Detailed Inventory

### 1. `HousingPolicyResearch/` Clone

**Size:** 1.1G | **Commit:** 8ad24e3 (from origin/main)\
**Status:** Recent checkout; contains full policy document artifacts

#### Key Directories:

```
artifacts/                (1.1K total files)
├── LOCAL_LAW_A-D         (4 legal framework docs)
├── PART_V_*              (3 legal framework variants)
├── PET_*                 (15+ policy/template docs) ✅ SUBSTANTIVE
├── pet_deck_*.png        (images - 295K, 196K) ✅ KEEP
├── TCAP_*.md             (2 TCAP overview docs) ✅ KEEP
└── ...DOCX/XLSX          (Word/Excel versions)

docs/                     (26 markdown files)
├── generative-output-*   (AI output tracking) ✅ CORE
├── resources-*           (citation index/CSV) ✅ CORE
├── integration-plan.md   (connection guide) ✅ CORE
├── STYLE-APA.md          (citation standard) ✅ KEEP
├── connection-checks.md  (validation) ✅ KEEP
└── ... (12 more docs)

scripts/                  (some setup/automation) ✅ PARTIAL KEEP
tests/                    (3 test files) ✅ KEEP
src/                      (Python utilities) ✅ KEEP
```

**Verdict:** **KEEP BUT SELECTIVE MERGE**

- Merge `artifacts/` (PET/TCAP docs) into main
- Merge `docs/` (already mostly in main)
- Merge `scripts/` (audit for originals)
- Merge `src/`, `tests/` if not in main

______________________________________________________________________

### 2. `HousingPolicyResearch-1/` Clone

**Size:** 752M | **Commit:** 9ee1d5e (older)\
**Status:** Older clone + full .venv (520M+) + .pytest_cache

#### Key Content Differences:

- Same directory structure as HousingPolicyResearch/
- Contains artifacts/ (duplicate)
- Contains `.venv/` (**BLOAT** - should not be committed)
- Contains `.pytest_cache/` (build artifact)
- Older git history (9ee1d5e vs 8ad24e3)

**Verdict:** **DISCARD CLONE** but extract any unique artifacts

- Archive to `/Desktop/HousingPolicyResearch_Archive/HousingPolicyResearch-1_BACKUP`
- Quick check for uncommitted changes before deleting .git/

______________________________________________________________________

### 3. `Housing Policy Workspace/`

**Size:** 24K | **Status:** Empty scaffold\
**Contents:**

```
Housing Policy Workspace/
└── housing_policy_scaffold/
    ├── 00_admin/
    │   └── .DS_Store
    ├── 10_sources/.gitkeep
    ├── 20_notes/.gitkeep
    ├── 30_drafts/.gitkeep
    ├── 40_outputs/.gitkeep
    ├── 50_data/.gitkeep
    ├── 60_logs/.gitkeep
    └── .DS_Store
```

**Verdict:** **DISCARD** - only directory scaffolds, no content

______________________________________________________________________

### 4. `workspace/housing_policy_scaffold/`

**Size:** 73M | **Status:** Raycast extension + bloat\
**Key Contents:**

```
workspace/housing_policy_scaffold/
├── raycast-extension/        (actual source code) ✅ KEEP
│   ├── src/
│   │   └── commands/         (Raycast commands)
│   ├── tsconfig.json
│   ├── package.json
│   └── node_modules/         (⚠️ 73M bloat - DISCARD)
├── Test.swift                (single file - unclear purpose)
├── 00_admin/settings.yaml    (config)
├── zotero/                   (scaffolds)
├── 30_drafts/                (empty)
└── (other empty dirs)
```

**Verdict:** **EXTRACT RAYCAST SOURCE, DISCARD REST**

- Keep: `workspace/housing_policy_scaffold/raycast-extension/src/`, `.json`, `.yaml` configs
- Discard: `node_modules/`, `.gitkeep` dirs, `Test.swift`
- Archive: Full folder to backup before cleanup

______________________________________________________________________

### 5. Workspace ZIP Files

```
workspace/
├── housing_policy_scaffold.zip     (19K - old archive)
└── housing_policy_scaffold 2.zip   (in parent, also old)
```

**Verdict:** **DISCARD** - redundant archives of above

______________________________________________________________________

## Duplicate Files at Root (Already Identified)

| File                                   | Status                      | Disposition                 |
| -------------------------------------- | --------------------------- | --------------------------- |
| `AUDIT_DOCUMENTATION_INDEX 2.md`       | Duplicate                   | DISCARD                     |
| `AUDIT_FINDINGS_VISUAL 2.txt`          | Duplicate                   | DISCARD                     |
| `REORGANIZATION_ACTION_PLAN 2.md`      | Duplicate                   | DISCARD                     |
| `REORGANIZATION_COMPLETE 2.md`         | Duplicate                   | DISCARD                     |
| `REPOSITORY_ORGANIZATION_SUMMARY 2.md` | Duplicate                   | DISCARD                     |
| `scripts/setup 2.sh`                   | Variant (alt impl)          | **REVIEW** - keep if needed |
| **Section* docs*\*                     | Substantive (not versioned) | **ARCHIVE & COMMIT**        |
| **TCAP-COMPLETE-PACKAGE/**             | Duplicate folder            | **REVIEW**                  |
| **TCAP_PET/**                          | Duplicate folder            | **REVIEW**                  |

______________________________________________________________________

## Commit Status in Each Clone

### Main Repo (current working tree)

```
Current branch: main
HEAD: c3a9293 "Resolve merge conflict in environment-setup"
Untracked: ~50+ files (duplicates, sections, ZIPs, etc.)
```

### HousingPolicyResearch/

```
HEAD: 8ad24e3 "Merge pull request #69..."
Status: Clean (recently cloned)
```

### HousingPolicyResearch-1/

```
HEAD: 9ee1d5e "Merge remote changes..."
Status: Likely clean
.venv/ 520M+ (untracked but present)
```

______________________________________________________________________

## Recommended Consolidation Strategy

### Phase 1: Archive & Backup (Safe)

1. Copy entire `HousingPolicyResearch-1/` to `/Desktop/HousingPolicyResearch_Archive/HousingPolicyResearch-1_BACKUP/`
1. Copy entire `Housing Policy Workspace/` to `/Desktop/HousingPolicyResearch_Archive/Housing_Policy_Workspace_BACKUP/`
1. Copy entire `workspace/housing_policy_scaffold/` to `/Desktop/HousingPolicyResearch_Archive/raycast_scaffold_BACKUP/`
1. Copy all ZIPs to backup folder

### Phase 2: Extract & Merge (Selective)

1. From `HousingPolicyResearch/artifacts/`:
   - Extract PET/TCAP/legal docs if not already in main `docs/exports/`
   - Verify against originals (likely identical)
   - Keep images (pet_deck\_\*.png)
1. From `workspace/housing_policy_scaffold/raycast-extension/`:
   - Extract `src/commands/`, `src/utils/`, `tsconfig.json`, `package.json`
   - Ensure no duplication with main repo's `raycast-extension/`
1. Section docs (Section 1, 2, 3... at root):
   - Move to `docs/sections/housing-policy-framework/`
   - Create version tags/metadata
   - Commit with message noting origin (draft → versioned)

### Phase 3: Cleanup (Delete)

1. Delete `HousingPolicyResearch/` folder (after merge confirmation)
1. Delete `HousingPolicyResearch-1/` folder (after backup)
1. Delete `Housing Policy Workspace/` folder (empty)
1. Delete `workspace/housing_policy_scaffold/node_modules/` and ZIPs
1. Remove root-level duplicate " 2" files
1. Remove root-level duplicate `Section*` folders (after moving to docs/)

### Phase 4: Single Repo Structure

```
HousingPolicyResearch/ (main working repo)
├── docs/
│   ├── sections/                    (NEW: Policy framework drafts)
│   │   ├── housing-policy-framework/
│   │   │   ├── Section 1 - Executive Summary.md
│   │   │   ├── Section 2 - PET Solution Overview.md
│   │   │   └── ... (all section docs)
│   │   └── README.md (versioning notes)
│   ├── exports/                     (Policy docs, templates, etc.)
│   ├── resources-index.md           (Citation index)
│   └── ... (other docs)
├── src/
├── scripts/
├── raycast-extension/               (Raycast commands + source only, no node_modules)
├── tests/
├── data/
├── artifacts/                       (Backup of generated outputs if needed)
├── workspace/                       (Empty scaffold for local work, .gitignore */)
└── README.md
```

______________________________________________________________________

## Disposition Checklist

- [ ] **Archive Phase**: Backup all clones to Desktop/HousingPolicyResearch_Archive/
- [ ] **Audit HousingPolicyResearch/artifacts/**: Check against main docs/exports/ for uniqueness
- [ ] **Extract Raycast**: Copy workspace/.../raycast-extension/src to main repo
- [ ] **Version Sections**: Move Section\* docs to docs/sections/, add metadata
- [ ] **Cleanup Duplicates**: Remove " 2" files at root and in docs/
- [ ] **Delete Clones**: Remove HousingPolicyResearch/, HousingPolicyResearch-1/, Housing Policy Workspace/
- [ ] **Clean workspace/**: Remove node_modules, ZIPs; keep only scaffold structure
- [ ] **Verify Tests**: Run pytest to confirm nothing broke
- [ ] **Commit**: Single "Consolidate clones and organize single repo" commit
- [ ] **Final Status**: One clean repo, one Desktop archive backup

______________________________________________________________________

## File Organization Examples

### Before (Current Root Clutter)

```
HousingPolicyResearch/       ← full 1.1G clone
HousingPolicyResearch-1/     ← full 752M clone
Housing Policy Workspace/    ← empty scaffold
workspace/housing_policy_scaffold/ ← raycast + bloat
Section 1 – Executive Summary & Core Problem Definition
Section 2 – PET Solution Overview
... (10+ section docs)
AUDIT_DOCUMENTATION_INDEX 2.md
AUDIT_FINDINGS_VISUAL 2.txt
... (10+ " 2" duplicates)
```

### After (Single Consolidated Repo)

```
docs/
├── sections/
│   └── housing-policy-framework/
│       ├── executive-summary-core-problem.md
│       ├── pet-solution-overview.md
│       └── ...
├── exports/                    (policy templates, legal frameworks)
├── resources-index.md
├── STYLE-APA.md
└── ...
src/
scripts/
raycast-extension/src/         (source only, no node_modules)
tests/
data/
workspace/                     (local scratch, ignored by git)
```

______________________________________________________________________

## Notes & Caveats

1. **Git History**: HousingPolicyResearch/ and HousingPolicyResearch-1/ are separate git clones (not branches). Merging artifacts doesn't preserve commit history; just extract files.

1. **node_modules Bloat**: 73M of raycast node_modules should NEVER be in version control. Will be discarded.

1. **Section Docs**: Currently named with special characters (e.g., "Section 1 – ..."). Will rename to kebab-case during move.

1. **Stash**: `stash@{0}` still contains node_modules/scaffold files from earlier reset. Can be dropped safely after cleanup.

1. **Raycast Manifest**: Main repo has `raycast.manifest.json` and `raycast-extension/`. Verify no conflicts before merging additional raycast source.

______________________________________________________________________

**Status:** Ready for human review before execution.\
**Next Step:** Confirm disposition plan, then execute phases 1–4.
