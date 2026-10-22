#!/bin/bash
# Housing Policy Research - Automated Setup Script
# ==============================================================================
# This script automates the initial setup of the development environment.
# Run from the repository root: bash setup.sh
# ==============================================================================

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🏠 Housing Policy Research - Setup Script${NC}"
echo -e "${GREEN}==========================================${NC}"
echo ""

# Step 1: Check Python version
echo -e "${YELLOW}Step 1/6: Checking Python version...${NC}"
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python $PYTHON_VERSION"

required_version="3.11"
if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 11) else 1)" 2>/dev/null; then
    echo -e "${RED}✗ Python 3.11+ required. Found: $PYTHON_VERSION${NC}"
    echo "Install with: brew install python@3.11"
    exit 1
fi
echo -e "${GREEN}✓ Python 3.11+ detected${NC}"
echo ""

# Step 2: Check Git
echo -e "${YELLOW}Step 2/6: Checking Git configuration...${NC}"
if ! command -v git &> /dev/null; then
    echo -e "${RED}✗ Git not found. Install with: brew install git${NC}"
    exit 1
fi

GIT_STATUS=$(git status --porcelain 2>/dev/null || true)
if [ ! -z "$GIT_STATUS" ]; then
    echo -e "${YELLOW}⚠ Warning: You have uncommitted changes${NC}"
    echo "Stash them with: git stash"
fi
echo -e "${GREEN}✓ Git is configured${NC}"
echo ""

# Step 3: Create virtual environment
echo -e "${YELLOW}Step 3/6: Creating virtual environment...${NC}"
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${GREEN}✓ Virtual environment already exists${NC}"
fi

source .venv/bin/activate
echo -e "${GREEN}✓ Virtual environment activated${NC}"
echo ""

# Step 4: Install dependencies
echo -e "${YELLOW}Step 4/6: Installing Python dependencies...${NC}"
pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt
echo -e "${GREEN}✓ Dependencies installed${NC}"
echo ""

# Step 5: Configure pre-commit hooks
echo -e "${YELLOW}Step 5/6: Configuring pre-commit hooks...${NC}"
pre-commit install --install-hooks > /dev/null 2>&1
echo -e "${GREEN}✓ Pre-commit hooks installed${NC}"

# Run pre-commit on all files to verify
echo "Running pre-commit validation..."
if pre-commit run --all-files > /dev/null 2>&1; then
    echo -e "${GREEN}✓ Pre-commit validation passed${NC}"
else
    echo -e "${YELLOW}⚠ Pre-commit checks had warnings (this is normal first run)${NC}"
fi
echo ""

# Step 6: Environment configuration
echo -e "${YELLOW}Step 6/6: Checking environment configuration...${NC}"

if [ ! -f ".env" ]; then
    echo -e "${YELLOW}Creating .env file from template...${NC}"
    cp .env.template .env
    echo -e "${GREEN}✓ .env file created${NC}"
    echo ""
    echo -e "${YELLOW}⚠ Important: You must populate .env with your API keys${NC}"
    echo "Edit .env with your keys:"
    echo "  OPENAI_API_KEY=..."
    echo "  NOTION_TOKEN=..."
    echo "  (etc.)"
    echo ""
    echo "Instructions: See docs/environment-setup.md#api-key-acquisition-guide"
else
    if grep -q "your_.*_here" .env; then
        echo -e "${YELLOW}⚠ .env file has placeholder values${NC}"
        echo "Update it with real keys from docs/environment-setup.md"
    else
        echo -e "${GREEN}✓ .env file is configured${NC}"
    fi
fi
echo ""

# Summary
echo -e "${GREEN}==========================================${NC}"
echo -e "${GREEN}✓ Setup Complete!${NC}"
echo -e "${GREEN}==========================================${NC}"
echo ""
echo "Next steps:"
echo ""
echo "1. SECURITY - Populate .env with API keys:"
echo "   - Read: docs/environment-setup.md"
echo "   - Edit: .env (in your editor)"
echo "   - DO NOT commit .env to Git"
echo ""
echo "2. VERIFY environment works:"
echo "   source .venv/bin/activate"
echo "   python --version"
echo "   pip list | grep -E 'black|flake8|openai'"
echo ""
echo "3. CREATE your first policy brief:"
echo "   cp 00_admin/templates/policy_brief_apa7.qmd 30_drafts/my_brief.qmd"
echo "   Edit the file and commit"
echo ""
echo "4. CONFIGURE GitHub (if using CI/CD):"
echo "   Settings → Secrets and variables → Actions"
echo "   Add: OPENAI_API_KEY, NOTION_TOKEN, etc."
echo ""
echo "Questions? See docs/environment-setup.md#troubleshooting"
echo ""
