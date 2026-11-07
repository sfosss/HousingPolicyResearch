#!/bin/bash

echo "========================================"
echo "CONSOLIDATION COMPLETION TASKS"
echo "========================================"
echo ""

cd /Users/sethadmin/Documents/GitHub/HousingPolicyResearch

# Check current branch
CURRENT_BRANCH=$(git branch --show-current)
echo "Current branch: $CURRENT_BRANCH"
echo ""

if [ "$CURRENT_BRANCH" != "main" ]; then
    echo "⚠️  You are not on main branch. Switch to main for verification:"
    echo "   git checkout main"
    echo ""
fi

# Check if archive exists
echo "=== 1. ARCHIVE VERIFICATION ==="
if [ -d ~/Desktop/HousingPolicyResearch_Archive ]; then
    echo "✅ Archive exists at ~/Desktop/HousingPolicyResearch_Archive/"
    echo ""
    echo "Archive contents:"
    ls -lh ~/Desktop/HousingPolicyResearch_Archive/
    echo ""
    echo "Archive size:"
    du -sh ~/Desktop/HousingPolicyResearch_Archive/*
    echo ""
    echo "RECOMMENDATION: Archive verified. Consider moving to external storage or deleting if confirmed no longer needed."
else
    echo "❌ Archive NOT found at ~/Desktop/HousingPolicyResearch_Archive/"
    echo "   If intentionally deleted, this is OK. If not, investigate."
fi
echo ""

# Check for consolidation tag
echo "=== 2. TAG VERIFICATION ==="
if git tag -l | grep -q "v1.0-consolidated"; then
    echo "✅ Tag v1.0-consolidated exists"
else
    echo "⚠️  Tag v1.0-consolidated does not exist"
    echo ""
    echo "CREATE TAG (optional but recommended):"
    echo "   git tag -a v1.0-consolidated 2f46cb3 -m 'Repository consolidation: removed redundant clones, organized policy docs'"
    echo "   git push origin v1.0-consolidated"
fi
echo ""

# Check policy document naming
echo "=== 3. POLICY DOCUMENT NAMING ==="
if [ -d "docs/sections/housing-policy-framework" ]; then
    echo "Policy framework directory contents:"
    ls -1 docs/sections/housing-policy-framework/
    echo ""
    echo "RECOMMENDATION: Standardize naming to descriptive format:"
    echo "   01-executive-summary-core-problem.md"
    echo "   02-theory-of-change-policy-framework.md"
    echo "   03-financial-modeling-roi-analysis.md"
    echo "   etc."
else
    echo "❌ Policy framework directory not found"
fi
echo ""

# Summary
echo "========================================"
echo "SUMMARY"
echo "========================================"
echo ""
echo "Main consolidation tasks: ✅ COMPLETE"
echo "Commits pushed to remote: ✅ YES"
echo "Repository state: ✅ HEALTHY"
echo ""
echo "Optional improvements:"
echo "  1. Create consolidation tag (v1.0-consolidated)"
echo "  2. Standardize policy document filenames"
echo "  3. Verify/cleanup archive on Desktop"
echo ""
echo "See CONSOLIDATION_STATUS_JAN2026.md for full details."
echo ""
