# Security incident checklist

Reviewed: 2026-10-23. Status: owner verification pending.

This update removes credential-bearing incident instructions from the current documentation. It does not establish that all tracked files or Git history are free of credentials. Never repeat credential values or identifying fragments in reports, issues, commits or screenshots.

## Remaining verification

- [ ] Identify affected credentials privately and revoke or rotate them at their providers.
- [ ] Review relevant provider usage and billing records.
- [ ] Check current tracked configuration and documentation with a secret scanner.
- [ ] Confirm GitHub secret scanning and push-protection settings.
- [ ] Verify required checks on the default branch after saving the proposed CI ruleset.
- [ ] Review a coordinated historical-cleanup plan if sensitive blobs remain reachable.

Do not rewrite published history or force-push as part of routine CI repair. Any historical cleanup requires a separately agreed preservation and collaborator recovery plan.

## Existing check

```bash
pre-commit run detect-secrets --hook-stage manual --all-files
```

This hook is manual. Passing ordinary pre-commit checks does not mean a secret scan ran.
