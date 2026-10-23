# GitHub Actions Node 24 migration — 2026-10-23

Version: 1.0. Proposed follow-up to the CI reconciliation.

## Scope and sequence

Retain the tested checkout v5/setup-python v6 pins from merged #130 and migrate the remaining workflows to verified Node 24 action manifests. Artifact upload/download interoperability is exercised by the existing Linux-staged three-platform preflight workflow. Workflow changes also trigger a read-only Quarto installation and action-reference smoke check.

Merge the reconciliation PR first: it removes publication's direct push to main. This follow-up disables persisted checkout credentials for read-only checkouts and publication. Proposal generation retains checkout authentication solely to push its isolated review branch; its existing token permissions are unchanged. Releases still use the explicit run-scoped GitHub token; generated commits must pass review/checks through a separate branch rather than bypass main's ruleset.

## Verified action manifests

| Action                             | Selected SHA                             | Manifest runtime              |
| ---------------------------------- | ---------------------------------------- | ----------------------------- |
| actions/checkout v5                | fbc6f3992d24b796d5a048ff273f7fcc4a7b6c09 | node24                        |
| actions/setup-python v6            | ece7cb06caefa5fff74198d8649806c4678c61a1 | node24                        |
| actions/upload-artifact v6         | b7c566a772e6b6bfb58ed0dc250532a479d7789f | node24                        |
| actions/download-artifact v7       | 37930b1c2abaa49bbe596cd826c3c89aef350131 | node24                        |
| softprops/action-gh-release v3.0.3 | efb35369e0ad2afab669f228072c1b0d510eae64 | node24                        |
| quarto-dev/quarto-actions/setup v2 | 8a96df13519ee81fd526f2dfca5962811136661b | composite; shell steps        |
| github/codeql-action v4            | cf1bb45a277cb3c205638b2cd5c984db1c46a412 | node24; retained existing pin |

The selected refs were resolved through the official maintainer repositories and their pinned action manifests on October 23, 2026. Checkout/setup-python reuse main's validated majors; this is not a blanket upgrade to the newest action major. Quarto's action is pinned; its existing default CLI release selection is retained.

## Validation limits

Local unit tests, dependency consistency, workflow YAML and immutable-reference checks apply. Hosted preflight validates setup, upload/download and report uploads on Linux, macOS and Windows. The compatibility workflow validates Quarto installation without rendering drafts or creating a release. The release action is verified from its manifest/declared inputs but is not executed in this review. CodeQL's existing language coverage is unchanged. Credentials, integration configuration and research text are unchanged.

## Review fixes

Proposal generation retains its existing Git authentication. Publication has no Git push after the required reconciliation. The immutable-reference guard scans both supported workflow extensions, .yml and .yaml; a local negative fixture confirms it rejects an unpinned .yaml action.

## YAML-aware pin guard

The guard installs the declared validation dependencies and parses both workflow extensions with PyYAML. It checks reusable-job and step action references, including quoted or spaced uses keys and references. Repository actions require full commit SHAs; Docker references require SHA-256 digests. Local negative/positive fixtures cover both extensions, quoted/spaced keys, unpinned tags and immutable references. Combined local suite: 49 tests.
