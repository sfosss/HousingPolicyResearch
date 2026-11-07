# Security policy

## Reporting

Report suspected vulnerabilities privately through GitHub's Security tab when available. If private reporting is unavailable, ask the repository owner for a private channel. Do not post credentials or personal data in issues or pull requests.

## Credentials and configuration

Keep credentials in ignored local configuration or GitHub Actions secrets. Previously committed values require provider-side revocation or rotation; removing text from a branch does not revoke credentials or remove Git history.

The detect-secrets hook currently runs at the manual stage:

```bash
pre-commit run detect-secrets --hook-stage manual --all-files
```

Ordinary pre-commit checks run Black, flake8 and mdformat. Enabling a blocking secret scan or changing its baseline requires separate validation. Repository and provider settings, credential rotation and historical cleanup are not certified by the CI reconciliation.
