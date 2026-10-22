#!/usr/bin/env bash
# Housing Policy Research - Project Setup Script
# This script helps set up the development environment for the project

set -e  # Exit on error

echo "=========================================="
echo "Housing Policy Research - Setup Script"
echo "=========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python version
echo "Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo -e "${GREEN}✓ Python $PYTHON_VERSION found${NC}"

# Check if we're in the right directory
if [ ! -f "README.md" ] || [ ! -d ".git" ]; then
    echo -e "${RED}Error: Please run this script from the repository root${NC}"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo ""
    echo "Creating Python virtual environment..."
    python3 -m venv .venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${YELLOW}Virtual environment already exists${NC}"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip -q

# Install dependencies
echo ""
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt -q
echo -e "${GREEN}✓ Dependencies installed${NC}"

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo ""
    echo "Creating .env file from template..."
    cp .env.template .env
    echo -e "${YELLOW}⚠ Please edit .env and add your API keys${NC}"
else
    echo -e "${YELLOW}.env file already exists${NC}"
fi

# Install pre-commit hooks
echo ""
echo "Installing pre-commit hooks..."
if command -v pre-commit &> /dev/null; then
    pre-commit install
    echo -e "${GREEN}✓ Pre-commit hooks installed${NC}"
else
    echo -e "${YELLOW}⚠ pre-commit not found in PATH, skipping hook installation${NC}"
fi

# Create necessary directories (most already exist)
echo ""
echo "Verifying directory structure..."
mkdir -p logs/connection-checks
mkdir -p artifacts
mkdir -p outputs
mkdir -p docs/prompts
mkdir -p docs/outputs
mkdir -p docs/audit-notes
echo -e "${GREEN}✓ Directory structure verified${NC}"

# Check for required environment variables
echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your API keys:"
echo "   - OPENAI_API_KEY (for ChatGPT/Codex)"
echo "   - NOTION_API_KEY (optional, for Notion integration)"
echo "   - ZOTERO_API_KEY (optional, for bibliography management)"
echo ""
echo "2. Activate the virtual environment:"
echo "   source .venv/bin/activate"
echo ""
echo "3. Run validation checks:"
echo "   python scripts/validate_connections.py"
echo ""
echo "4. Read the documentation:"
echo "   - docs/environment-setup.md"
echo "   - docs/project-roadmap.md"
echo "   - docs/rulesets.md"
echo ""
echo -e "${GREEN}Happy coding!${NC}"
