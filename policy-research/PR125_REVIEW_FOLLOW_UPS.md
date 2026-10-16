# PR #125 review follow-ups

The initial `9f1d407` changes fixed Python 3.11 collection, persisted identity matching, full-ledger Critical QA, Box versioning, QA/export consistency, strict scheduling, URL structure validation, malformed packets, curated-index preservation and atomic CSV replacement.

## Fresh review of 9f1d407

- [Mapping keyword boundaries](https://github.com/sfosss/HousingPolicyResearch/pull/125#discussion_r4298284281): mapping, status and rights keywords now use whole terms/phrases. A courthouse visit cannot match the court rule.
- [Missing jurisdiction](https://github.com/sfosss/HousingPolicyResearch/pull/125#discussion_r4298284303): missing/unsupported jurisdictions are rejected with a connector diagnostic before scope filtering.
- [Repeated Critical issues](https://github.com/sfosss/HousingPolicyResearch/pull/125#discussion_r4298284321): one persistent open issue is updated across dates.
- [Provenance promotion to Critical](https://github.com/sfosss/HousingPolicyResearch/pull/125#discussion_r4298284349): crossing from High to Critical clears the prior reviewer/disposition and requires fresh counsel review.
- [Named RSS time zones](https://github.com/sfosss/HousingPolicyResearch/pull/125#discussion_r4298284365): RFC date parsing preserves GMT and named-zone publication dates.
- [Strict failure loses ledger](https://github.com/sfosss/HousingPolicyResearch/pull/125#discussion_r4298284378): completed output is retained as workflow artifacts and proposed through a recurring PR even when strict QA fails. The workflow still reports failure. Pending PR artifacts are restored before later intake to preserve reviewed dispositions. A fresh completion marker prevents publication after incomplete runs.
- [Namespaced RSS](https://github.com/sfosss/HousingPolicyResearch/pull/125#discussion_r4298284395): namespace-qualified RSS items and Atom entries are collected; empty/unrecognized feeds produce diagnostics.
- [BOM erases rows](https://github.com/sfosss/HousingPolicyResearch/pull/125#discussion_r4298284417): BOM-aware reads validate headers/row shape and preserve malformed CSVs rather than rewriting them.

## Earlier follow-ups implemented

- Canonical mappings now reference existing sections/paragraphs in the root `NYC-Draft-Legislation.md` package. Configuration and row QA validate these coordinates. Canonical legislation is unchanged.
- Statewide/federal intake requires a city signal, target city agency/program or explicit boolean NYC-applicability assertion. HUD alone and generic housing mentions do not suffice.
- Conflicting content needs a strictly newer timezone-aware source revision timestamp on both snapshots. Stale, equal-version conflicting and unversioned revisions retain stored evidence and produce a QA error.
- Midpage records, including relayed Web/Box records, require completed analysis evidence, a matching opinion URL, timestamp, identifier, proposition and scope limit. External authentication remains limited as described below.
- Artifact publication uses a normal review PR instead of a direct protected-branch push, with downloadable workflow artifacts as a fallback.
- Missing prior dated outputs are recovered from persisted rows. Recovered QA explicitly fails with a note that original connector diagnostics are unavailable.
- Selected transient feed errors get three attempts with one- and two-second backoff. Every available feed entry is processed; the former per-poll truncation is removed.
- Query-credential disclosure is fixed at a shared sanitation boundary before hashing/persistence/export. Known authentication/API-key/token/signature parameters, encoded aliases, nested URL/query forms and credential fragments are removed. Persisted URL copies are scrubbed without losing unchanged approvals. Feed/Box diagnostics omit raw request/redirect exception messages.

## Verification

Files changed: `scripts/adaptive_policy_loop.py`, `tests/test_adaptive_policy_loop.py`, `config/policy_map.json`, `.github/workflows/adaptive-policy-loop.yml`, this follow-up record and `policy-research/README.md`.

1. Syntax/import gate: `python -m py_compile scripts/adaptive_policy_loop.py` and `git diff --check` pass.
1. Security trigger gate: query-credential retention reproduces on `9f1d407` and no longer reproduces in the candidate. `pytest -q tests/test_adaptive_policy_loop.py -k 'secret or public or encoded or legacy or diagnostics'` covers encoded aliases, stored copies, diagnostics, generated files, stdout and captured Box upload bytes. The credential-query disclosure outcome is **fixed** at the shared sanitation boundary.
1. Compatibility and owning checks: public identifiers, search semantics, nested literal-plus values and opinion fragments remain intact. Python 3.11.17 targeted tests (`python -m pytest -q tests/test_adaptive_policy_loop.py`) pass all 118 cases. Python 3.12.14 full suite (`python -m pytest -q`) passes all 127 repository tests. Actionlint 1.7.7 and repository Black, Flake8 and mdformat hooks pass. Workflow tests execute strict-failure readiness, persistent-issue shell paths and actual Git restore pathspecs.

The URL security review used independent read-only boundary investigation and candidate bypass/regression review. Confirmed bypasses and public-link regressions were corrected and covered by tests. Live-integration limits and residual public-link review requirements follow below.

## Remaining limitations and setup

- **Midpage verification remains partial:** operator-supplied analysis evidence is validated locally, but the offline pipeline does not authenticate identifiers against Midpage. Service-backed verification needs an authenticated integration.
- Existing duplicate ledger rows are not automatically merged; conflicting human dispositions need a migration policy. Older unversioned records need reviewer-established source timestamps before automatic revisions can resume.
- Recovery reconstructs the persisted snapshot, not earlier overwritten revisions, original connector errors or feed entries already removed by the publisher.
- Sanitation recognizes credential parameter families. Arbitrary secrets in opaque paths, unknown parameter names or non-URL prose cannot be inferred reliably; public-link review remains necessary. No real credential exposure was observed in the empty live ledger.
- Live Box, feed endpoints, issue creation and artifact-PR publication were not exercised. HTTP and workflow shell/Git behavior are tested locally. Enable the repository setting allowing GitHub Actions to create pull requests and the declared write permissions; enable `POLICY_LOOP_STRICT=true` after source validation.
- If the final Box QA upload fails, local QA and both exports record failure; the remote report can remain stale until a successful upload.
- Historical date-specific Critical issues are not automatically closed during migration to the persistent issue.
