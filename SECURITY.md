# Security policy

## Supported versions

This repository is a research workspace rather than a versioned service. Security
fixes are applied only to the current default branch. Snapshots, exports, and
archived materials are not independently supported.

## Report a vulnerability

Do **not** open a public issue or include credentials, personal data, or exploit
details in a pull request. Use GitHub's **Report a vulnerability** button under
the repository Security tab to submit a private report. If private reporting is
unavailable, contact the repository owner through their GitHub profile and ask
for a private disclosure channel without including the sensitive details.

Please include the affected path and revision, impact, reproduction steps, and a
suggested mitigation when possible. Expect acknowledgement within seven days and
a status update within fourteen days. Timelines for a fix depend on severity and
whether a credential owner or third-party service must act.

## Secrets and local configuration

* Store secrets only in an ignored `.env` file or the GitHub Actions secrets
  store; committed configuration must contain environment-variable references.
* Treat every credential ever committed as compromised. Removing its text from
  the current branch is not revocation: rotate it at the provider and purge it
  from reachable Git history before publishing rewritten refs.
* Run `pre-commit run --all-files` before submitting changes. The configured
  `detect-secrets` hook blocks newly detected credentials.
