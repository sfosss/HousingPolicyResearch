#!/bin/bash

echo "=== GIT STATUS ==="
git status

echo ""
echo "=== COMMITS AHEAD/BEHIND ==="
git rev-list --left-right --count origin/main...HEAD

echo ""
echo "=== RECENT COMMITS (last 5) ==="
git log --oneline -5

echo ""
echo "=== CHECKING ARCHIVE LOCATION ==="
if [ -d "/Users/sethadmin/Desktop/HousingPolicyResearch_Archive" ]; then
    echo "✅ Archive exists at ~/Desktop/HousingPolicyResearch_Archive/"
    echo ""
    echo "Archive contents:"
    ls -lh "/Users/sethadmin/Desktop/HousingPolicyResearch_Archive"
    echo ""
    echo "Archive size:"
    du -sh "/Users/sethadmin/Desktop/HousingPolicyResearch_Archive"/*
else
    echo "❌ Archive NOT found at ~/Desktop/HousingPolicyResearch_Archive/"
fi

echo ""
echo "=== CHECKING TAGS ==="
git tag -l "v1.0-consolidated"
