# GitHub Actions Maintenance Guide

## Security Policy: Pinned Action Versions

This repository requires all GitHub Actions to be pinned to **full-length commit SHAs** instead of version tags (e.g., `@v4`). This ensures supply chain security by preventing malicious updates to actions from affecting the repository.

## Current Action Versions

### CodeQL Workflow (`.github/workflows/codeql.yml`)

Last updated: 2025-12-10

| Action | Workflow | Version Tag | Commit SHA | Notes |
|--------|----------|-------------|------------|-------|
| actions/checkout | codeql.yml | v4.3.1 | `34e114876b0b11c390a56381ad16ebd13914f8d5` | Latest stable v4 release |
| actions/checkout | blank.yml | v4.3.1 | `34e114876b0b11c390a56381ad16ebd13914f8d5` | Synced with CodeQL workflow |
| github/codeql-action/init | codeql.yml | v4 | `cf1bb45a277cb3c205638b2cd5c984db1c46a412` | CodeQL initialization |
| github/codeql-action/analyze | codeql.yml | v4 | `cf1bb45a277cb3c205638b2cd5c984db1c46a412` | CodeQL analysis |

## How to Update Actions

When a new version of an action is released and you want to update:

1. **Find the latest release tag** for the action on GitHub
   - For `actions/checkout`: https://github.com/actions/checkout/tags
   - For `github/codeql-action`: https://github.com/github/codeql-action/tags

2. **Identify the commit SHA** for that tag
   - Use the GitHub API:  
     - Template: `https://api.github.com/repos/{owner}/{repo}/git/refs/tags/{tag}`  
     - Example: `https://api.github.com/repos/actions/checkout/git/refs/tags/v4.3.1`
   - Or browse the repository tags page

3. **Update the workflow file** with the new commit SHA
   - Add a comment above the `uses:` line documenting the version tag
   - Example:
     ```yaml
     - name: Checkout repository
       # actions/checkout@v4.3.1
       uses: actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5
     ```

4. **Update this documentation** with the new version information

5. **Test the workflow** by triggering it manually or waiting for the scheduled run

## Verification

After updating action versions, verify the workflow runs successfully:

- Check the Actions tab in GitHub: https://github.com/SfosssHousing/HousingPolicyResearch/actions
- Review job logs for any errors or warnings
- Ensure CodeQL analysis completes without issues

## Troubleshooting

### Error: "actions must be pinned to a full-length commit SHA"

This error occurs when an action uses a version tag (e.g., `@v4`) instead of a commit SHA. Follow the update process above to resolve.

### Finding Commit SHAs via GitHub CLI

If you have the GitHub CLI installed:

```bash
# Get the commit SHA for a specific tag
gh api /repos/actions/checkout/git/refs/tags/v4

# List recent tags
gh api /repos/actions/checkout/tags
```

### Finding Commit SHAs via Browser

1. Navigate to the action's GitHub repository
2. Click on the "Tags" section
3. Find the desired tag (e.g., `v4`)
4. Click on the tag to view the commit
5. Copy the full commit SHA from the URL or commit page

## Security Rationale

Pinning actions to commit SHAs provides:

- **Immutability**: Commit SHAs cannot be changed, unlike tags which can be force-pushed
- **Auditability**: Clear record of exactly what code is running in workflows
- **Supply chain security**: Protection against tag hijacking or malicious updates
- **Compliance**: Meets security requirements for sensitive repositories

## Related Documentation

- [GitHub Actions Security Best Practices](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
- [Project Security Policy](../SECURITY.md)
- [Environment Setup Guide](environment-setup.md)

---

**Version:** 1.0  
**Last Updated:** 2025-12-10  
**Maintained by:** Housing Policy Research team
