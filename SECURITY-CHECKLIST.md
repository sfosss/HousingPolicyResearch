# Security incident checklist

**Last reviewed:** 2026-09-20

**Repository remediation:** complete for the current tree

**External credential rotation and history cleanup:** owner verification required

Previously committed credentials must be assumed compromised. Their values are
intentionally omitted from this document; do not copy even partial values into
issues, commits, screenshots, or logs.

## Credential-owner actions

- [ ] Revoke and replace every previously exposed OpenAI, ProPublica Congress,
      NYS Open Legislation, OpenStates, Legistar, and OpenAlex credential.
- [ ] Store replacements in a local ignored `.env` file or GitHub Actions
      secrets, never in a tracked file.
- [ ] Review provider usage and billing logs for activity after first exposure.
- [ ] Record revocation confirmation in a private incident system, not this repo.

## Repository-admin actions

- [x] Remove credential values from the current tree and retain only environment
      variable references in `00_admin/settings.yaml`.
- [x] Enable secret detection as a normal pre-commit hook.
- [x] Ignore common private-key and service-account file formats.
- [x] Restrict workflow permissions and avoid persisted checkout credentials in
      workflows that do not need them.
- [ ] Rewrite all published refs to remove secret-bearing historical blobs, then
      coordinate a force-push and fresh clones. Make a protected backup first.
- [ ] Enable GitHub secret scanning, push protection, Dependabot alerts, and
      private vulnerability reporting in repository settings.
- [ ] Confirm branch protection requires the validation and CodeQL checks.

## Verification

```bash
git grep -nEI 'sk-(proj-)?[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}'
pre-commit run --all-files
python -m pip_audit -r requirements.txt
npm --prefix raycast-extension audit
```

A clean current-tree scan does not prove that Git history is clean. Scan every
reachable ref after history rewriting and rotate credentials regardless of the
scan result.
