# Security remediation record

This file supersedes the 2025 incident instructions, which themselves repeated
live credential values and therefore prolonged the exposure.

## Current status (2026-09-20)

The current tree uses environment-variable references in tracked configuration.
Credential literals have been removed from current documentation, secret
screening runs during pre-commit, dependency update automation covers Python,
npm, and GitHub Actions, and workflow permissions have been tightened.

Two administrator-controlled actions cannot be completed from a detached local
checkout:

1. **Rotate credentials at each provider.** Every value ever committed must be
   revoked even if it no longer appears in the current files.
2. **Clean published Git history.** After backing up and coordinating with all
   contributors, use `git filter-repo` (or the hosting provider's documented
   sensitive-data removal process), force-push every affected ref, invalidate
   caches/forks where possible, and require fresh clones.

Track those confirmations privately. Never place old/new keys or identifying
fragments in this repository. See `SECURITY-CHECKLIST.md` for the remaining
owner and administrator checklist.
