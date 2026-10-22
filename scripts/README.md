# Scripts Directory

This directory contains automation scripts for repository management and maintenance tasks.

## Available Scripts

### `merge-housing-repository.sh`

**Purpose:** Automates the process of merging the `sfosss/Housing` repository into this repository's `housing/` subdirectory while preserving full commit history.

**Requirements:**

- Git installed and configured
- Access to the source repository (`sfosss/Housing`)
- Clean working directory (no uncommitted changes)

**Usage:**

```bash
# From the repository root:
./scripts/merge-housing-repository.sh
```

The script will:

1. Verify prerequisites (git repo, clean working directory)
1. Configure remote for the source repository (if not already configured)
1. Fetch the source repository
1. Perform a git subtree merge into the `housing/` subdirectory
1. Verify the merge completed successfully
1. Provide next steps for review and pushing changes

**Interactive Mode:**
The script will ask for confirmation before performing the merge. This allows you to review the configuration before making changes.

**Error Handling:**
If the script encounters an error, it will:

- Display a clear error message
- Suggest recovery steps
- Exit without making partial changes (where possible)

**Troubleshooting:**

If the fetch fails with an authentication error:

```
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/sfosss/Housing/'
```

This means you need access to the source repository. Solutions:

1. **Grant access:** Repository owner should grant read access to your GitHub account
1. **Use SSH:** Change the remote URL to use SSH instead of HTTPS
1. **Use a token:** Configure a personal access token with repo read permissions

**Related Documentation:**

- See [docs/repository-merge-plan.md](../docs/repository-merge-plan.md) for detailed planning documentation
- See [docs/environment-setup.md](../docs/environment-setup.md) for general setup instructions

## Adding New Scripts

When adding new automation scripts to this directory:

1. **Make scripts executable:**

   ```bash
   chmod +x scripts/your-script.sh
   ```

1. **Add a header comment** with:

   - Script purpose
   - Author/maintainer
   - Date created
   - Usage instructions
   - Prerequisites

1. **Use error handling:**

   ```bash
   set -e  # Exit on error
   set -u  # Exit on undefined variable
   ```

1. **Include help text:**

   ```bash
   if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
       echo "Usage: $0 [options]"
       exit 0
   fi
   ```

1. **Update this README** with:

   - Script name and purpose
   - Usage example
   - Any important notes or warnings

1. **Test thoroughly** before committing

## Script Conventions

- Use `.sh` extension for shell scripts
- Use `.py` extension for Python scripts
- Use descriptive, kebab-case names (e.g., `merge-housing-repository.sh`)
- Include error checking and clear error messages
- Provide usage help with `--help` flag
- Use relative paths when possible
- Never commit secrets or credentials in scripts
- Document any required environment variables

## Security Notes

- Never hardcode credentials, API keys, or tokens in scripts
- Use environment variables or configuration files for sensitive data
- Add sensitive config files to `.gitignore`
- Review scripts for security issues before committing
- See [SECURITY.md](../SECURITY.md) for security policies

## Future Scripts (Planned)

Based on the project roadmap, future scripts may include:

- Data export/import automation
- Zotero bibliography synchronization
- Notion integration scripts
- ChatGPT conversation export
- Automated testing and validation
- Documentation generation

See [docs/project-roadmap.md](../docs/project-roadmap.md) for more details.

______________________________________________________________________

**Last Updated:** 2025-12-12\
**Maintainer:** Housing Policy Research team
