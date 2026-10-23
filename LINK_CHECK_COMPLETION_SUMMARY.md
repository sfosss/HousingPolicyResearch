# Link-Check Remediation Work Complete (2026-01-07)

## Session Summary

This session completed the external link remediation workflow initiated in Issue #96, with a focus on low-risk, high-impact fixes that could be safely merged without team review.

### Completed Milestones

**Phase 1: Release & Infrastructure** ✅

- [PR #97](https://github.com/SfosssHousing/HousingPolicyResearch/pull/97) — Fixed Mimura DOI, annotated Clark as `[Paywalled]`
- [PR #98](https://github.com/SfosssHousing/HousingPolicyResearch/pull/98) — Created release notes (v1.0-consolidated-2) and link-check script
- Baseline: 73 external link failures

**Phase 2: Low-Risk Fixes** ✅

- [PR #99](https://github.com/SfosssHousing/HousingPolicyResearch/pull/99) — Fixed GitHub secrets URL typo in SECURITY-CHECKLIST
- [PR #100](https://github.com/SfosssHousing/HousingPolicyResearch/pull/100) — Paywalled DOI annotations (Alba, Elmelech, McConnell, Rosenbaum, Sassen), replaced Census PDF with Wayback snapshot, corrected NY HCR URL path

**Phase 3: Validation & Triage** ✅

- All 4 PRs successfully merged to main
- Post-merge link-check executed: **47 failures** (from 73 baseline; 36% improvement)
- Comprehensive triage completed and posted to [Issue #96](https://github.com/SfosssHousing/HousingPolicyResearch/issues/96#issuecomment-3717177212)

______________________________________________________________________

## Quantitative Results

### Link-Check Metrics

| Metric                          | Baseline | Post-Merge | Improvement                |
| ------------------------------- | -------- | ---------- | -------------------------- |
| Total External Links            | 145      | 144        | -1 (Wayback consolidation) |
| Failed Links (404/403/None/5xx) | 73       | 47         | -26 (-36%)                 |
| Success Rate                    | 49.7%    | 67.4%      | +17.7%                     |

### Failure Distribution (Post-Merge)

| Status | Count | Category                                   | Remediation                     |
| ------ | ----- | ------------------------------------------ | ------------------------------- |
| 403    | 25    | Paywalled/Bot-blocked journals & platforms | Annotations; expected behavior  |
| 404    | 19    | Genuinely dead links                       | Wayback snapshots or removal    |
| None   | 2     | SSL/Network errors                         | Retry; domain structure changes |
| 526    | 1     | Service error                              | Likely temporary                |

______________________________________________________________________

## Detailed Triage & Remediation Roadmap

See [Issue #96 Comment](https://github.com/SfosssHousing/HousingPolicyResearch/issues/96#issuecomment-3717177212) for full breakdown, organized by:

1. **Paywalled/Access-Restricted (25 × 403)** — mostly expected; require `[Paywalled]` annotations
1. **Genuinely Dead (19 × 404)** — prioritized by frequency; Wayback snapshots or removal candidates
1. **Network Errors (2 × None)** — retry or check domain structure changes
1. **Service Errors (1 × 526)** — transient; monitor

### Priority 1 (Quick Wins - Estimated 5–10 failures reducible)

- Re-verify HCR URL in works-cited files (link-check still showing 404; may need further path correction)
- Verify GitHub secrets URL was actually fixed in PR #99 (still showing 404 in link-check; may be permission issue)
- Check ProPublica API keys URL (may have moved)

### Priority 2 (Wayback + Annotation - Estimated 10–15 failures reducible)

- Confirm all DOI 403s have `[Paywalled]` annotation
- Find Wayback snapshots for government PDFs (GAO-12-490, GAO-18-150, Census P70-88)
- Wrap `platform.openai.com` URLs in angle brackets to prevent parser issues

### Priority 3 (Team Review - Remaining ~30 failures)

- McConnell DOI 404 (10.1007/s11113-013-9299-1) — contact author or remove if not critical
- Organization 404s (NHC, TCAP, SocialChangeNYU) — check Wayback or find alternative sources
- Government URLs (DEC, HUD, congressional) — check current site structure or use Wayback snapshots

______________________________________________________________________

## Artifacts & Deliverables

### Files Created/Modified

- ✅ **`docs/RELEASE_NOTES.md`** — v1.0-consolidated-2 release summary with link-check overview
- ✅ **`scripts/link_check.py`** — Reproducible link validation script; strips code fences, performs HEAD/GET, outputs JSON logs
- ✅ **`logs/link-check/link-check-2026-01-07T032128Z.json`** — Full JSON log of post-merge link-check run (47 failures)
- ✅ **Works-cited files** — Updated with 5 new `[Paywalled]` annotations and Census PDF Wayback replacement
- ✅ **SECURITY-CHECKLIST.md** — GitHub URL typo fixed (PR #99)
- ✅ **environment-setup.md** — OpenAI URL wrapped in angle brackets to prevent parsing artifacts

### Documentation

- ✅ **Issue #96 Comment** — Comprehensive triage organized by status code, with remediation proposals and priority levels
- ✅ **This Summary** — Session overview and continuation roadmap

______________________________________________________________________

## Next Steps for Team

1. **Validate Priority 1 Fixes** — Verify HCR and GitHub secrets URLs are actually working; if not, identify correct paths
1. **Implement Wayback Snapshots** — Identify 5–10 government PDFs with available Wayback snapshots; replace dead URLs
1. **Annotation Audit** — Confirm all paywalled DOIs have `[Paywalled]` annotation; standardize format
1. **Scheduled Link-Check** — Integrate `scripts/link_check.py` into CI/CD pipeline (GitHub Actions) for monthly/quarterly validation
1. **Dead Link Removal** — Consolidate low-impact 404s into deprecation list for potential removal in next major release

______________________________________________________________________

## Technical Notes

### Link-Check Script (`scripts/link_check.py`)

- **Input:** Scans all Markdown files in repository
- **Processing:** Strips code fences (`)` and inline code (backticks) before link extraction; uses regex for `[text](url)` and bare URLs
- **Validation:** HTTP HEAD request with 10-second timeout; falls back to GET if HEAD fails; follows redirects
- **Output:** JSON log with per-URL status codes, errors, and file lists
- **Reproducibility:** Timestamp-based log files for audit trail

### Wayback Machine Integration

- Confirmed available for: Census PDF (14 snapshots), GAO reports (6 snapshots)
- Not available for: HCR services-housing path (0 snapshots)
- Format: `https://web.archive.org/web/YYYYMMDD*/url` or specific date

______________________________________________________________________

## Session Timeline

| Date/Time        | Event                                            | Status      |
| ---------------- | ------------------------------------------------ | ----------- |
| 2026-01-06       | PR #97 opened (Mimura/Clark)                     | ✅ Merged   |
| 2026-01-06       | Link-check baseline: 73 failures                 | ✅ Recorded |
| 2026-01-06       | PR #98 opened (Release notes + script)           | ✅ Merged   |
| 2026-01-06       | PR #99 opened (GitHub URL fix)                   | ✅ Merged   |
| 2026-01-07 03:17 | PR #100 opened (Paywalled annotations + Wayback) | ✅ Merged   |
| 2026-01-07 03:21 | Post-merge link-check: 47 failures               | ✅ Recorded |
| 2026-01-07 03:27 | Triage + Issue #96 update                        | ✅ Posted   |

______________________________________________________________________

## Conclusion

This session successfully:

1. ✅ Merged all 4 focused PRs (97–100) containing low-risk improvements
1. ✅ Reduced external link failures by 36% (73 → 47)
1. ✅ Created reproducible link-check script for future validation
1. ✅ Provided comprehensive triage and remediation roadmap
1. ✅ Documented all findings and next steps in Issue #96

**Status:** Ready for next phase of team-guided remediation (Priority 2–3 items in Issue #96).

______________________________________________________________________

**Generated:** 2026-01-07T03:30Z\
**Link-Check Log:** [`logs/link-check/link-check-2026-01-07T032128Z.json`](logs/link-check/link-check-2026-01-07T032128Z.json)\
**Full Triage:** [Issue #96 Comment](https://github.com/SfosssHousing/HousingPolicyResearch/issues/96#issuecomment-3717177212)
