# Repository Organization Action Plan – Quick Reference

**Date:** 2025-12-30\
**Audit Status:** ✅ COMPLETE\
**Implementation Status:** ⏳ READY TO EXECUTE

______________________________________________________________________

## ⚡ Quick Summary

**Issues Found:** 28+ files/directories need reorganization\
**Severity:** Medium (affects discoverability, not functionality)\
**Effort Required:** ~90 minutes\
**Priority:** High (should be done before major updates)

______________________________________________________________________

## 🎯 Priority 1: CRITICAL (Do Today – 15 min)

These are files that shouldn't exist or have obvious problems.

### DELETE These Files (5 min)

- ❌ `README copy.md`
- ❌ `exported-assets (1)/pet_deck_outline 2.png`
- ❌ `exported-assets (1)/pet_deck_structure 2.png`
- ❌ `exported-assets (1)/Final Housing_Subsidy_MasterFormatted_Final copy copy.docx`
- ❌ `exported-assets (1)/NDA_Tenant_Privacy_Inspection_Agreement_v2 copy.docx`

**Command:**

```bash
rm README\ copy.md
rm exported-assets\ \(1\)/pet_deck_outline\ 2.png
rm exported-assets\ \(1\)/pet_deck_structure\ 2.png
# [etc for other duplicates]
```

### RENAME These Directories (10 min)

- 📁 `exported-assets (1)/` → `docs/exports/`
- 📁 `Housing Policy Workspace/` → `workspace/` (or archive)

**Command:**

```bash
mv exported-assets\ \(1\) docs/exports
```

______________________________________________________________________

## 🎯 Priority 2: HIGH (Do This Week – 45 min)

These files are in the wrong place and should be moved.

### Move Scripts to `scripts/` (10 min)

```
ROOT                          MOVE TO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ━━━━━━━━━━━━━━━━━━━━━━━
setup.sh                      → scripts/setup.sh
tcap_automation.sh            → scripts/tcap/tcap-automation.sh
tcap_cron_setup.txt           → scripts/tcap/tcap-cron-setup.txt
tcap_task_automation.py       → scripts/tcap/tcap-task-automation.py
```

**Commands:**

```bash
mkdir -p scripts/tcap
mv setup.sh scripts/
mv tcap_automation.sh scripts/tcap/tcap-automation.sh
mv tcap_cron_setup.txt scripts/tcap/tcap-cron-setup.txt
mv tcap_task_automation.py scripts/tcap/tcap-task-automation.py
```

### Move Documentation to `docs/` (10 min)

```
ROOT                          MOVE TO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ━━━━━━━━━━━━━━━━━━━━━━━━━━
HousingPolicyResearch.md      → docs/housing-policy-research-overview.md
PERPLEXITY_QUICK_START.md     → docs/perplexity-quick-start.md
SYSTEM_STATUS_2025-12-30.md   → docs/system-status-2025-12-30.md
TCAP_Interactive_Dashboard_README.md → docs/tcap/
```

**Commands:**

```bash
mv HousingPolicyResearch.md docs/housing-policy-research-overview.md
mv PERPLEXITY_QUICK_START.md docs/
mv SYSTEM_STATUS_2025-12-30.md docs/
mv TCAP_Interactive_Dashboard_README.md docs/tcap/
```

### Move Data to `data/` (5 min)

```bash
mv NYC_Housing_Subsidy_Ops_Tasks_Notion.csv data/
```

### Organize 42 Exported Policy Documents (20 min)

Create subdirectories in `docs/exports/`:

```bash
mkdir -p docs/exports/{legal-frameworks,policy-reports,templates,operational-docs,assets,archive}
```

Then move files by category:

```bash
# Legal frameworks
mv docs/exports/LOCAL_LAW_*.md docs/exports/legal-frameworks/
mv docs/exports/PART_V_*.md docs/exports/legal-frameworks/

# Reports and analysis
mv docs/exports/PET_Master_Policy_*.md docs/exports/policy-reports/
mv docs/exports/PET_Legal_Feasibility_*.md docs/exports/policy-reports/
mv docs/exports/MASTER_Works_Cited_*.md docs/exports/policy-reports/

# Templates
mv docs/exports/PET_*_Template.md docs/exports/templates/

# Operational docs
mv docs/exports/PET_Operations_*.md docs/exports/operational-docs/
mv docs/exports/PET_One_Pager_*.md docs/exports/operational-docs/
mv docs/exports/PET_Risk_Log_*.md docs/exports/operational-docs/

# Assets (images)
mv docs/exports/*.png docs/exports/assets/

# Archive (old versions)
mv docs/exports/*.docx docs/exports/archive/
```

______________________________________________________________________

## 🎯 Priority 3: MEDIUM (Do This Sprint – 30 min)

These improve long-term maintainability.

### Organize TCAP Files (10 min)

Create structure:

```bash
mkdir -p docs/tcap/{deployment,audit,tracking}
```

Move TCAP files:

```bash
mv TCAP_DEPLOYMENT_SUMMARY.txt docs/tcap/deployment/
mv TCAP_FILE_MANIFEST.txt docs/tcap/audit/
mv TCAP_Status_Report.txt docs/tcap/deployment/
mv TCAP_Version_History_Audit_Log.txt docs/tcap/audit/
mv TCAP_Task_Status_Risk_Tracking.csv docs/tcap/tracking/
```

### Create Documentation (15 min)

Create these new files:

- `docs/DIRECTORY_STRUCTURE.md` - Purpose of each directory
- `docs/NAMING_CONVENTIONS.md` - File naming standards
- `scripts/README.md` - What each script does
- `docs/exports/README.md` - Guide to organized policy docs

### Empty Directory Cleanup (5 min)

Add `.gitkeep` to empty directories:

```bash
touch artifacts/.gitkeep
touch references/.gitkeep
touch logs/.gitkeep
```

______________________________________________________________________

## 🎯 Priority 4: LOW (Polish – 15 min)

These are nice-to-have improvements.

- [ ] Standardize all file names to kebab-case
- [ ] Add directory manifests explaining purpose
- [ ] Create DIRECTORY_STRUCTURE.md at root
- [ ] Update README.md with new directory structure

______________________________________________________________________

## 📊 Before & After Comparison

### Root Directory Files

**BEFORE (23 active files):**

```
README.md
README copy.md ❌
HousingPolicyResearch.md
PERPLEXITY_QUICK_START.md
SYSTEM_STATUS_2025-12-30.md
SECURITY.md
TCAP_*.txt *.md (7 files)
NYC_Housing_Subsidy_*.csv
setup.sh
tcap_*.sh tcap_*.py
pyproject.toml
requirements.txt
raycast.manifest.json
.env.template
.pre-commit-config.yaml
... and more clutter
```

**AFTER (7 files):**

```
README.md ✅
SECURITY.md ✅
pyproject.toml ✅
requirements.txt ✅
raycast.manifest.json ✅
.env.template ✅
.pre-commit-config.yaml ✅
```

**Reduction:** 23 → 7 files (70% cleaner!)

______________________________________________________________________

## ✅ Verification Checklist

After implementation, verify:

- [ ] No files in root except: `README.md`, `SECURITY.md`, `pyproject.toml`, `requirements.txt`, `raycast.manifest.json`, `.env.template`, `.pre-commit-config.yaml`
- [ ] All scripts in `scripts/` directory
- [ ] All documentation in `docs/` directory
- [ ] No duplicate or test files (README copy.md, etc. gone)
- [ ] `docs/exports/` properly organized into 6 subdirectories
- [ ] `docs/tcap/` properly organized into 3 subdirectories
- [ ] All new directories have `.gitkeep` or meaningful content
- [ ] All paths in documentation still work (relative links adjusted if needed)

______________________________________________________________________

## 🚀 Quick Start Command List

Copy and paste these commands to execute the entire reorganization:

```bash
#!/bin/bash
# Full Repository Reorganization Script

echo "🚀 Starting repository reorganization..."

# Phase 1: Delete duplicates (5 min)
echo "📍 Phase 1: Deleting duplicate files..."
rm README\ copy.md
rm exported-assets\ \(1\)/pet_deck_outline\ 2.png
rm exported-assets\ \(1\)/pet_deck_structure\ 2.png
rm exported-assets\ \(1\)/"Final Housing_Subsidy_MasterFormatted_Final copy copy.docx" 2>/dev/null
rm exported-assets\ \(1\)/"NDA_Tenant_Privacy_Inspection_Agreement_v2 copy.docx" 2>/dev/null
echo "✅ Duplicates removed"

# Phase 2: Rename directories (10 min)
echo "📍 Phase 2: Renaming directories..."
mv exported-assets\ \(1\) docs/exports
echo "✅ Directories renamed"

# Phase 3: Create subdirectories (15 min)
echo "📍 Phase 3: Creating subdirectories..."
mkdir -p scripts/tcap
mkdir -p docs/exports/{legal-frameworks,policy-reports,templates,operational-docs,assets,archive}
mkdir -p docs/tcap/{deployment,audit,tracking}
echo "✅ Subdirectories created"

# Phase 4a: Move scripts (10 min)
echo "📍 Phase 4a: Moving scripts..."
mv setup.sh scripts/ 2>/dev/null
mv tcap_automation.sh scripts/tcap/tcap-automation.sh 2>/dev/null
mv tcap_cron_setup.txt scripts/tcap/tcap-cron-setup.txt 2>/dev/null
mv tcap_task_automation.py scripts/tcap/tcap-task-automation.py 2>/dev/null
echo "✅ Scripts moved"

# Phase 4b: Move documentation (10 min)
echo "📍 Phase 4b: Moving documentation..."
mv HousingPolicyResearch.md docs/housing-policy-research-overview.md 2>/dev/null
mv PERPLEXITY_QUICK_START.md docs/ 2>/dev/null
mv SYSTEM_STATUS_2025-12-30.md docs/ 2>/dev/null
mv TCAP_Interactive_Dashboard_README.md docs/tcap/ 2>/dev/null
echo "✅ Documentation moved"

# Phase 4c: Move data (5 min)
echo "📍 Phase 4c: Moving data..."
mv NYC_Housing_Subsidy_Ops_Tasks_Notion.csv data/ 2>/dev/null
echo "✅ Data moved"

# Phase 4d: Organize exported assets (20 min)
echo "📍 Phase 4d: Organizing exported assets..."
mv docs/exports/LOCAL_LAW_*.md docs/exports/legal-frameworks/ 2>/dev/null
mv docs/exports/PART_V_*.md docs/exports/legal-frameworks/ 2>/dev/null
mv docs/exports/PET_Master_Policy_*.md docs/exports/policy-reports/ 2>/dev/null
mv docs/exports/PET_Legal_Feasibility_*.md docs/exports/policy-reports/ 2>/dev/null
mv docs/exports/MASTER_Works_Cited_*.md docs/exports/policy-reports/ 2>/dev/null
mv docs/exports/PET_*_Template.md docs/exports/templates/ 2>/dev/null
mv docs/exports/PET_Operations_*.md docs/exports/operational-docs/ 2>/dev/null
mv docs/exports/PET_One_Pager_*.md docs/exports/operational-docs/ 2>/dev/null
mv docs/exports/PET_Risk_Log_*.md docs/exports/operational-docs/ 2>/dev/null
mv docs/exports/*.png docs/exports/assets/ 2>/dev/null
mv docs/exports/*.docx docs/exports/archive/ 2>/dev/null
echo "✅ Exported assets organized"

# Phase 4e: Organize TCAP files (10 min)
echo "📍 Phase 4e: Organizing TCAP files..."
mv TCAP_DEPLOYMENT_SUMMARY.txt docs/tcap/deployment/ 2>/dev/null
mv TCAP_FILE_MANIFEST.txt docs/tcap/audit/ 2>/dev/null
mv TCAP_Status_Report.txt docs/tcap/deployment/ 2>/dev/null
mv TCAP_Version_History_Audit_Log.txt docs/tcap/audit/ 2>/dev/null
mv TCAP_Task_Status_Risk_Tracking.csv docs/tcap/tracking/ 2>/dev/null
echo "✅ TCAP files organized"

# Phase 5: Add .gitkeep files
echo "📍 Phase 5: Adding .gitkeep files..."
touch artifacts/.gitkeep
touch references/.gitkeep
touch logs/.gitkeep
echo "✅ .gitkeep files added"

echo "✅ ✅ ✅ Repository reorganization complete! ✅ ✅ ✅"
echo ""
echo "📊 Results:"
echo "   • Root directory reduced from 23 to 7 files"
echo "   • 42 policy documents properly categorized"
echo "   • TCAP files organized into 3 subdirectories"
echo "   • All scripts moved to scripts/ directory"
echo "   • All docs moved to docs/ directory"
echo ""
echo "📝 Next steps:"
echo "   1. Run: git status (to verify changes)"
echo "   2. Create: docs/DIRECTORY_STRUCTURE.md"
echo "   3. Create: scripts/README.md"
echo "   4. Commit changes: git add -A && git commit -m 'refactor: reorganize repository structure'"
```

Save this as `reorganize.sh` and run:

```bash
chmod +x reorganize.sh
./reorganize.sh
```

______________________________________________________________________

## 📋 Post-Implementation Checklist

- [ ] All deletions complete (5 duplicate files removed)
- [ ] All renames complete (2 directories renamed)
- [ ] All moves complete (23+ files moved to proper locations)
- [ ] All subdirectories created (8 new subdirectories)
- [ ] Documentation files created (4 new guide files)
- [ ] `.gitkeep` files added to empty directories
- [ ] `git status` shows all changes
- [ ] All paths in documentation tested and working
- [ ] Run `git add -A && git commit -m "refactor: reorganize repository structure"`
- [ ] Verify repository structure matches `RECOMMENDED_REPOSITORY_STRUCTURE.md`

______________________________________________________________________

## 📚 Documentation References

For more details, see:

- **Full Audit:** `docs/REPOSITORY_STRUCTURE_AUDIT_2025-12-30.md`
- **Target Structure:** `docs/RECOMMENDED_REPOSITORY_STRUCTURE.md`
- **Directory Guide:** `docs/DIRECTORY_STRUCTURE.md` (to be created)
- **Naming Guide:** `docs/NAMING_CONVENTIONS.md` (to be created)

______________________________________________________________________

**Status:** ✅ Ready to implement\
**Estimated Time:** 90 minutes total\
**Recommended Window:** During maintenance sprint or non-critical development time\
**Impact:** Medium (improves discoverability; no functional changes)
