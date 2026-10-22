# Contributing to Housing Policy Research

Thank you for your interest in contributing to the Housing Policy Research project! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Code Standards](#code-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Pull Request Process](#pull-request-process)
- [Security](#security)

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Git
- A GitHub account

### Initial Setup

1. Fork the repository on GitHub

1. Clone your fork locally:

   ```bash
   git clone https://github.com/YOUR-USERNAME/HousingPolicyResearch.git
   cd HousingPolicyResearch
   ```

1. Run the setup script:

   ```bash
   ./setup.sh
   ```

1. Configure your environment variables:

   ```bash
   cp .env.template .env
   # Edit .env and add your API keys
   ```

1. Activate the virtual environment:

   ```bash
   source .venv/bin/activate
   ```

## Development Workflow

### Creating a Branch

Create a descriptive branch name for your work:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
# or
git checkout -b docs/documentation-update
```

### Making Changes

1. Make your changes in focused, logical commits

1. Write clear commit messages following the format:

   ```
   Short summary (50 chars or less)

   More detailed explanation if needed. Wrap at 72 characters.

   - Bullet points are okay
   - Reference issues: Fixes #123
   ```

1. Test your changes locally

1. Run code quality checks before committing

### Running Quality Checks

Before committing, ensure your code passes all checks:

```bash
# Run pre-commit hooks manually
pre-commit run --all-files

# Format Python code
black .

# Lint Python code
flake8 .

# Format Markdown (if modified)
mdformat *.md docs/*.md
```

## Code Standards

### Python Style

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Maximum line length: 100 characters
- Use descriptive variable and function names
- Add docstrings to all public functions and classes

Example:

```python
def analyze_housing_data(data: pd.DataFrame, metric: str) -> dict:
    """
    Analyze housing data for a specific metric.
    
    Args:
        data: DataFrame containing housing data
        metric: Name of the metric to analyze
        
    Returns:
        Dictionary with analysis results
    """
    # Implementation here
    pass
```

### Markdown Style

- Use proper heading hierarchy (h1 → h2 → h3)
- Wrap lines at 80 characters for readability
- Use code blocks with language specifications
- Include alt text for images

## Testing

Currently, the project is in development and does not have a formal test suite. When adding tests:

1. Use pytest as the testing framework
1. Place tests in a `tests/` directory mirroring the source structure
1. Name test files with `test_` prefix
1. Write descriptive test names that explain what is being tested

Example:

```python
def test_policy_proposal_generation_includes_required_sections():
    """Test that generated proposals contain all required sections."""
    # Test implementation
    pass
```

## Documentation

### When to Update Documentation

Update documentation when you:

- Add new features or functionality
- Change existing behavior
- Add new configuration options
- Create new scripts or tools
- Modify API integrations

### Documentation Locations

- `README.md` - Overview and quick start
- `docs/environment-setup.md` - Setup and configuration
- `docs/project-roadmap.md` - Project plans and milestones
- `docs/rulesets.md` - Security and integration rules
- Code docstrings - Function and class documentation

### Writing Good Documentation

- Write for your audience (assume they're new to the project)
- Use examples where helpful
- Keep it concise but complete
- Update related documentation when making changes
- Use proper markdown formatting

## Pull Request Process

### Before Submitting

1. Ensure your branch is up to date with `main`:

   ```bash
   git fetch origin
   git rebase origin/main
   ```

1. Run all quality checks:

   ```bash
   pre-commit run --all-files
   ```

1. Test your changes thoroughly

1. Update documentation as needed

1. Review your own changes before submitting

### Submitting a Pull Request

1. Push your branch to your fork:

   ```bash
   git push origin your-branch-name
   ```

1. Go to the repository on GitHub and create a pull request

1. Fill out the PR template with:

   - Clear description of changes
   - Link to related issues (if any)
   - Screenshots for UI changes
   - Testing performed
   - Checklist of completed items

1. Request review from appropriate team members

### PR Review Process

- Address reviewer feedback promptly
- Make requested changes in new commits (don't force-push during review)
- Mark conversations as resolved once addressed
- Be open to suggestions and alternative approaches

### After Approval

Once approved:

1. Squash commits if requested
1. Ensure CI passes
1. A maintainer will merge your PR

## Security

### Reporting Security Issues

**Do not open public issues for security vulnerabilities.**

Instead:

1. Email the maintainers directly
1. Include detailed information about the vulnerability
1. Wait for acknowledgment before disclosing publicly

### Security Best Practices

- Never commit secrets, API keys, or credentials
- Use environment variables for sensitive configuration
- Keep dependencies up to date
- Review security advisories for dependencies
- Follow the principle of least privilege for API scopes

## Questions?

If you have questions about contributing:

1. Check existing documentation first
1. Look for similar issues or discussions
1. Open a GitHub discussion for general questions
1. Open an issue for specific problems or feature requests

## Code of Conduct

This project follows a code of conduct to ensure a welcoming environment:

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Respect different viewpoints and experiences
- Prioritize the project's best interests

Thank you for contributing to housing policy research!
