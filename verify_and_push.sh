#!/bin/bash

echo "========================================"
echo "REPOSITORY CONSOLIDATION VERIFICATION"
echo "Date: $(date)"
echo "========================================"
echo ""

cd /Users/sethadmin/Documents/GitHub/HousingPolicyResearch

echo "=== 1. GIT STATUS ==="
git status
echo ""

echo "=== 2. COMMITS AHEAD OF ORIGIN/MAIN ==="
AHEAD=$(git rev-list --count origin/main..HEAD)
echo "Commits ahead: $AHEAD"
echo ""

echo "=== 3. RECENT LOCAL COMMITS ==="
git log origin/main..HEAD --oneline
echo ""

echo "=== 4. LAST 5 COMMITS (with details) ==="
git log -5 --pretty=format:"%h - %an, %ar : %s" --graph
echo ""
echo ""

echo "=== 5. CHECKING FOR CONSOLIDATION COMMIT ==="
if git log --oneline | grep -q "2f46cb3"; then
    echo "✅ Found consolidation commit 2f46cb3"
    git log --oneline | grep "2f46cb3"
else
    echo "⚠️  Consolidation commit 2f46cb3 not found in recent history"
fi
echo ""

echo "=== 6. ARCHIVE VERIFICATION ==="
if [ -d "/Users/sethadmin/Desktop/HousingPolicyResearch_Archive" ]; then
    echo "✅ Archive exists at ~/Desktop/HousingPolicyResearch_Archive/"
    echo ""
    echo "Archive contents:"
    ls -lh "/Users/sethadmin/Desktop/HousingPolicyResearch_Archive/" 2>/dev/null || echo "Unable to list contents"
    echo ""
    echo "Archive sizes:"
    du -sh "/Users/sethadmin/Desktop/HousingPolicyResearch_Archive"/* 2>/dev/null || echo "Unable to calculate sizes"
else
    echo "❌ Archive NOT found at ~/Desktop/HousingPolicyResearch_Archive/"
fi
echo ""

echo "=== 7. TAG VERIFICATION ==="
if git tag -l | grep -q "v1.0-consolidated"; then
    echo "✅ Tag v1.0-consolidated exists"
else
    echo "⚠️  Tag v1.0-consolidated does not exist"
fi
echo ""

echo "=== 8. POLICY DOCUMENTS VERIFICATION ==="
if [ -d "docs/sections/housing-policy-framework" ]; then
    echo "✅ Policy framework directory exists"
    echo ""
    echo "Contents:"
    ls -1 docs/sections/housing-policy-framework/
else
    echo "❌ Policy framework directory not found"
fi
echo ""

echo "========================================"
echo "VERIFICATION COMPLETE"
echo "========================================"
