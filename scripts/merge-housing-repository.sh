#!/bin/bash
# Repository Merge Script: sfosss/Housing → SfosssHousing/HousingPolicyResearch
# This script automates the process of merging the sfosss/Housing repository
# into the housing/ subdirectory while preserving full commit history.
#
# Documentation:
#   - Merge Plan: docs/repository-merge-plan.md
#   - Troubleshooting: docs/repository-merge-troubleshooting.md
#   - Script Documentation: scripts/README.md

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
SOURCE_REPO="https://github.com/sfosss/Housing"
REMOTE_NAME="housing-src"
TARGET_SUBDIR="housing"
SOURCE_BRANCH="main"

echo -e "${GREEN}Repository Merge Script${NC}"
echo "================================"
echo "Source: $SOURCE_REPO"
echo "Target: ./$TARGET_SUBDIR/"
echo "Branch: $SOURCE_BRANCH"
echo ""

# Function to print status messages
print_status() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

# Check if we're in a git repository
if [ ! -d .git ]; then
    print_error "Not in a git repository. Please run this script from the repository root."
    exit 1
fi

print_status "Verified git repository"

# Check if housing directory already exists
if [ -d "$TARGET_SUBDIR" ]; then
    print_error "The '$TARGET_SUBDIR' directory already exists!"
    echo "This script is designed to create a new directory. Please:"
    echo "1. Verify the merge hasn't already been done"
    echo "2. Remove or rename the existing directory if safe to do so"
    exit 1
fi

print_status "Target directory '$TARGET_SUBDIR' does not exist (good)"

# Check for uncommitted changes
if ! git diff-index --quiet HEAD --; then
    print_error "You have uncommitted changes. Please commit or stash them first."
    git status --short
    exit 1
fi

print_status "Working directory is clean"

# Check if remote already exists
if git remote | grep -q "^${REMOTE_NAME}$"; then
    print_warning "Remote '$REMOTE_NAME' already exists, will use existing configuration"
else
    echo "Adding remote '$REMOTE_NAME'..."
    git remote add "$REMOTE_NAME" "$SOURCE_REPO"
    print_status "Added remote '$REMOTE_NAME'"
fi

# Show remote configuration
echo ""
echo "Remote configuration:"
git remote -v | grep "$REMOTE_NAME"
echo ""

# Fetch the source repository
echo "Fetching from $REMOTE_NAME..."
if git fetch "$REMOTE_NAME"; then
    print_status "Successfully fetched from $REMOTE_NAME"
else
    print_error "Failed to fetch from $REMOTE_NAME"
    echo ""
    echo "This usually means:"
    echo "1. The repository is private and you don't have access"
    echo "2. Network connectivity issues"
    echo "3. Invalid repository URL"
    echo ""
    echo "Please verify:"
    echo "- You have access to $SOURCE_REPO"
    echo "- Your git credentials are configured correctly"
    echo "- You can access GitHub"
    echo ""
    echo "For detailed troubleshooting steps, see:"
    echo "  docs/repository-merge-troubleshooting.md"
    exit 1
fi

# List available branches from the remote
echo ""
echo "Available branches from $REMOTE_NAME:"
git branch -r | grep "$REMOTE_NAME"
echo ""

# Verify the source branch exists
if ! git rev-parse --verify "refs/remotes/${REMOTE_NAME}/${SOURCE_BRANCH}" >/dev/null 2>&1; then
    print_error "Branch '$SOURCE_BRANCH' not found in remote '$REMOTE_NAME'"
    echo "Available branches:"
    git branch -r | grep "$REMOTE_NAME"
    exit 1
fi

print_status "Verified branch '$SOURCE_BRANCH' exists in remote"

# Perform the subtree merge
echo ""
echo "Performing subtree merge..."
echo "This will import the entire repository into ./$TARGET_SUBDIR/"
echo "Full commit history will be preserved."
echo ""
read -p "Continue? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_warning "Merge cancelled by user"
    exit 0
fi

# Execute the subtree add command
# Note: --squash is intentionally omitted to preserve full history
if git subtree add --prefix="$TARGET_SUBDIR" "$REMOTE_NAME" "$SOURCE_BRANCH"; then
    print_status "Successfully merged $REMOTE_NAME/$SOURCE_BRANCH into $TARGET_SUBDIR/"
else
    print_error "Subtree merge failed"
    echo ""
    echo "This could be due to:"
    echo "1. Merge conflicts (check git status)"
    echo "2. Invalid branch or remote name"
    echo "3. Network issues during fetch"
    echo ""
    echo "To recover:"
    echo "  git merge --abort  # If merge is in progress"
    echo "  git reset --hard HEAD  # To reset to previous state"
    exit 1
fi

# Verify the merge
echo ""
echo "Verifying merge..."

if [ ! -d "$TARGET_SUBDIR" ]; then
    print_error "Target directory '$TARGET_SUBDIR' was not created!"
    exit 1
fi

print_status "Target directory created"

# Count files in the new directory
FILE_COUNT=$(find "$TARGET_SUBDIR" -type f | wc -l)
print_status "Imported $FILE_COUNT files into $TARGET_SUBDIR/"

# Show summary of what was imported
echo ""
echo "Top-level contents of $TARGET_SUBDIR/ (first 10 items):"
ls -la "$TARGET_SUBDIR/" | head -11  # 11 to account for total line

# Check for merge conflicts
if git ls-files -u | grep -q .; then
    print_error "Merge conflicts detected!"
    echo ""
    echo "Conflicted files:"
    git ls-files -u | cut -f2 | sort -u
    echo ""
    echo "Please resolve conflicts manually:"
    echo "1. Edit conflicted files"
    echo "2. git add <resolved-files>"
    echo "3. git commit"
    exit 1
fi

print_status "No merge conflicts detected"

# Show the merge commit
echo ""
echo "Merge commit:"
git log -1 --oneline
echo ""

# Show how many commits were imported
# Compare against the commit before this merge
COMMIT_COUNT=$(git rev-list --count HEAD ^HEAD~1 2>/dev/null || echo "1")
print_status "Imported $COMMIT_COUNT new commit(s) in this merge"

# Final status
echo ""
echo "================================"
print_status "Merge completed successfully!"
echo ""
echo "Next steps:"
echo "1. Review the imported content in ./$TARGET_SUBDIR/"
echo "2. Verify documentation links still work"
echo "3. Run any tests to ensure compatibility"
echo "4. Commit any additional changes if needed"
echo "5. Push to the feature branch:"
echo "   git push origin $(git branch --show-current)"
echo ""
echo "To undo this merge (if needed):"
echo "   git reset --hard HEAD~1"
echo ""
