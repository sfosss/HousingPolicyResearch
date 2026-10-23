# External repositories for PET/TCAP

Version: 1.0 | Verified: October 23, 2026 | Status: Proposed; human review required

## Purpose and selection

Curated public code and data resources for NYC tenant ownership, preservation, fiscal ROI, and intergenerational equity research. Recommendations are analyst judgments based on repository metadata and maintainer documentation, not endorsements or execution results. No dependencies or datasets are installed by this registry.

Selection favors documented provenance, NYC applicability, inspectable methods, identifiable maintainers, and explicit limitations. Stars are not a quality threshold. Core means first to evaluate; conditional means a specific validation gate remains; historical means context only.

Inspection of HousingPolicyResearch main at `7a0bd7d002f7c40425cf388a316fa3f932e750ed` covered the recursive file tree, README, agent guidance, citation rules and resource/provenance indexes. The tree contains TCAP_PET, TCAP-COMPLETE-PACKAGE and Capstone artifacts; their substantive legal and fiscal claims were not audited. Existing canonical legislation is unchanged.

## Authority boundary

Every entry below is a code/data resource, not legal authority. Agency-hosted software is primary evidence of that agency's implementation methods, not binding law. Model parameters, README statements, derived associations and scraped records cannot establish PET/TCAP enactment, title, eligibility, spending authority, federal approval, or a lawful transfer of funds. Validate such claims separately against current enacted law, regulations, official program documents, appropriations and property records, with legal review where needed.

## Curated registry

### nycdb/nycdb

- **Citation:** NYCDB contributors. (n.d.). *nycdb* \[Source code\]. GitHub. Retrieved October 23, 2026, from [repository](https://github.com/nycdb/nycdb).
- **Selection:** Core; Community ETL. Topics: HPD; NYCHA; DOF; preservation.
- **Proposed use:** Load property and enforcement baselines for candidate screening.
- **Limits:** Third-party transformations; NYCHA BBL coverage is not household eligibility; validate dataset vintages and BBL joins.
- **Verification:** Public repository and maintainer README retrieved; archived: false; last pushed (UTC): 2026-10-15T13:41:13Z. Repository activity is not data freshness or runtime validation.
- **Evidence snapshot:** [README at inspected head](https://github.com/nycdb/nycdb/blob/1d4f35365979f2470aff19e8fc9fdd6d3607af09/README.md); commit `1d4f35365979f2470aff19e8fc9fdd6d3607af09`.
- **License signal:** AGPL-3.0. Code licensing does not establish rights in upstream datasets.

### JustFixNYC/who-owns-what

- **Citation:** JustFix. (n.d.). *who-owns-what* \[Source code\]. GitHub. Retrieved October 23, 2026, from [repository](https://github.com/JustFixNYC/who-owns-what).
- **Selection:** Core; Tenant advocacy tool. Topics: Tenant ownership; preservation.
- **Proposed use:** Map ownership associations to investigate acquisition candidates.
- **Limits:** Associations are investigative leads rather than verified title or beneficial ownership; verify against underlying records.
- **Verification:** Public repository and maintainer README retrieved; archived: false; last pushed (UTC): 2026-09-25T16:38:19Z. Repository activity is not data freshness or runtime validation.
- **Evidence snapshot:** [README at inspected head](https://github.com/JustFixNYC/who-owns-what/blob/1ebd47cbe62d327ef41dd67332ba08458ee83dec/README.md); commit `1ebd47cbe62d327ef41dd67332ba08458ee83dec`.
- **License signal:** GPL-3.0. Code licensing does not establish rights in upstream datasets.

### NYCPlanning/data-engineering

- **Citation:** New York City Department of City Planning. (n.d.). *data-engineering* \[Source code\]. GitHub. Retrieved October 23, 2026, from [repository](https://github.com/NYCPlanning/data-engineering).
- **Selection:** Core; Agency data pipelines. Topics: Land use; housing stock; local planning.
- **Proposed use:** Inspect DCP data production and source lineage before building parcel baselines.
- **Limits:** Build output may be draft; use approved published releases and record dataset vintage. Replaces archived db-pluto.
- **Verification:** Public repository and maintainer README retrieved; archived: false; last pushed (UTC): 2026-10-22T20:49:24Z. Repository activity is not data freshness or runtime validation.
- **Evidence snapshot:** [README at inspected head](https://github.com/NYCPlanning/data-engineering/blob/d902377eeecbc4f75ca32212f3bb765f78cab061/README.md); commit `d902377eeecbc4f75ca32212f3bb765f78cab061`.
- **License signal:** MIT. Code licensing does not establish rights in upstream datasets.

### NYCPlanning/labs-community-profiles

- **Citation:** NYC Planning Labs. (n.d.). *labs-community-profiles* \[Source code\]. GitHub. Retrieved October 23, 2026, from [repository](https://github.com/NYCPlanning/labs-community-profiles).
- **Selection:** Supporting; Agency visualization code. Topics: Local demographics; equity.
- **Proposed use:** Use community district indicator patterns to design neighborhood distributional reporting.
- **Limits:** README references a 202402 table and legacy services; do not infer current demographic estimates from repository activity.
- **Verification:** Public repository and maintainer README retrieved; archived: false; last pushed (UTC): 2026-01-21T23:45:58Z. Repository activity is not data freshness or runtime validation.
- **Evidence snapshot:** [README at inspected head](https://github.com/NYCPlanning/labs-community-profiles/blob/0a4e60811b2d7f464d1fe9e91d35965eb59040e7/README.md); commit `0a4e60811b2d7f464d1fe9e91d35965eb59040e7`.
- **License signal:** Unresolved by GitHub metadata; inspect repository terms before reuse. Code licensing does not establish rights in upstream datasets.

### CityOfNewYork/ACCESS-NYC

- **Citation:** City of New York. (n.d.). *ACCESS-NYC* \[Source code\]. GitHub. Retrieved October 23, 2026, from [repository](https://github.com/CityOfNewYork/ACCESS-NYC).
- **Selection:** Supporting; City service website code. Topics: HRA interface; resident access.
- **Proposed use:** Study multilingual resident navigation and benefits screening interfaces for implementation planning.
- **Limits:** Website code is not HRA administrative rules or a complete eligibility engine; program information and screening services are separate dependencies.
- **Verification:** Public repository and maintainer README retrieved; archived: false; last pushed (UTC): 2026-10-05T20:56:38Z. Repository activity is not data freshness or runtime validation.
- **Evidence snapshot:** [README at inspected head](https://github.com/CityOfNewYork/ACCESS-NYC/blob/9541edb236bdda5a80761d3d33e123d56b9b5d32/README.md); commit `9541edb236bdda5a80761d3d33e123d56b9b5d32`.
- **License signal:** Unresolved by GitHub metadata; inspect repository terms before reuse. Code licensing does not establish rights in upstream datasets.

### PolicyEngine/policyengine-us

- **Citation:** PolicyEngine. (n.d.). *policyengine-us* \[Source code\]. GitHub. Retrieved October 23, 2026, from [repository](https://github.com/PolicyEngine/policyengine-us).
- **Selection:** Conditional; Independent tax-benefit model. Topics: Fiscal scenarios; household resources.
- **Proposed use:** Explore NY household resource changes with explicit policy-year and parameter assumptions.
- **Limits:** README deprecates direct aggregate microsimulation in favor of policyengine.py; separately vet that package before use. NYC program coverage and calibration remain unverified; not an agency budget model.
- **Verification:** Public repository and maintainer README retrieved; archived: false; last pushed (UTC): 2026-10-23T06:38:03Z. Repository activity is not data freshness or runtime validation.
- **Evidence snapshot:** [README at inspected head](https://github.com/PolicyEngine/policyengine-us/blob/c5837fb00b3db253a2a1725917b97abf185e065f/README.md); commit `c5837fb00b3db253a2a1725917b97abf185e065f`.
- **License signal:** AGPL-3.0. Code licensing does not establish rights in upstream datasets.

### walkerke/tidycensus

- **Citation:** Kyle Walker and contributors. (n.d.). *tidycensus* \[Source code\]. GitHub. Retrieved October 23, 2026, from [repository](https://github.com/walkerke/tidycensus).
- **Selection:** Supporting; Independent Census API client. Topics: Local demographics; equity.
- **Proposed use:** Retrieve ACS and decennial baselines for NYC geographies.
- **Limits:** Not Census-endorsed; retain margins of error and survey vintage; avoid household inference from area averages.
- **Verification:** Public repository and maintainer README retrieved; archived: false; last pushed (UTC): 2026-10-20T16:09:58Z. Repository activity is not data freshness or runtime validation.
- **Evidence snapshot:** [README at inspected head](https://github.com/walkerke/tidycensus/blob/cc5aac2eccf7757dfaeb876dcc63ceb3062d88db/README.md); commit `cc5aac2eccf7757dfaeb876dcc63ceb3062d88db`.
- **License signal:** Unresolved by GitHub metadata; inspect repository terms before reuse. Code licensing does not establish rights in upstream datasets.

### JustFixNYC/nycha-scraper

- **Citation:** JustFix. (n.d.). *nycha-scraper* \[Source code\]. GitHub. Retrieved October 23, 2026, from [repository](https://github.com/JustFixNYC/nycha-scraper).
- **Selection:** Historical only; PDF extraction utility. Topics: NYCHA property identifiers.
- **Proposed use:** Understand provenance of a historical NYCHA block-and-lot crosswalk.
- **Limits:** README targets August 27, 2018 guide; do not use as current NYCHA inventory or evidence of transfer eligibility.
- **Verification:** Public repository and maintainer README retrieved; archived: false; last pushed (UTC): 2024-08-29T19:40:29Z. Repository activity is not data freshness or runtime validation.
- **Evidence snapshot:** [README at inspected head](https://github.com/JustFixNYC/nycha-scraper/blob/04decd5887d8101b20dc6ceca226386245bb8121/README.md); commit `04decd5887d8101b20dc6ceca226386245bb8121`.
- **License signal:** No detected license; inspect terms before reuse. Code licensing does not establish rights in upstream datasets.

### BetaNYC/New-York-City-Budget

- **Citation:** BetaNYC. (n.d.). *New-York-City-Budget* \[Source code\]. GitHub. Retrieved October 23, 2026, from [repository](https://github.com/BetaNYC/New-York-City-Budget).
- **Selection:** Conditional; Civic fiscal data extraction. Topics: Council designations; local fiscal context.
- **Proposed use:** Inspect structured Council designations and their provenance when assessing funding streams.
- **Limits:** Use structured 2.0 sources only; retired PDF extracts have known errors. Designations are not expenditure actuals or proof of reusable HPD/HRA/NYCHA appropriations. Independently reconcile relied-on figures.
- **Verification:** Public repository and maintainer README retrieved; archived: false; last pushed (UTC): 2026-10-23T06:03:18Z. Repository activity is not data freshness or runtime validation.
- **Evidence snapshot:** [README at inspected head](https://github.com/BetaNYC/New-York-City-Budget/blob/fc1c9e6761adf3c585085eca8bc309eb7f2bfc3c/README.md); commit `fc1c9e6761adf3c585085eca8bc309eb7f2bfc3c`.
- **License signal:** Unresolved by GitHub metadata; inspect repository terms before reuse. Code licensing does not establish rights in upstream datasets.

## Coverage gaps and exclusions

- **HUD:** No HUD-maintained repository was accepted in this bounded search. A name match for HUDUSER resolved to an unrelated user repository and was excluded. HUD datasets, funding restrictions and program rules require separate official-source research; this is a coverage gap, not evidence that no suitable repository exists.
- **HRA:** ACCESS NYC supports interface research, not verification of CityFHEPS, HASA or other HRA eligibility/operational rules. No HRA administrative engine was validated.
- **Tenant ownership:** No NYC cooperative or community land trust implementation repository passed this pass. Generic smart-contract land-trust results and unrelated multi-tenant software were excluded for weak NYC applicability. Acquisition, resale restrictions, governance and credit-union finance need separate vetted sources and an explicit model.
- **Preservation:** NYCDB and JustFix are candidate-screening tools; no entry proves acquisition suitability, tenancy rights or building financial viability.
- **Fiscal ROI:** BetaNYC covers Council designations, while PolicyEngine provides household rules. Neither establishes full agency operating budgets, cash savings or transferability. Reconcile baseline expenditures, actual payments, legal restrictions, administrative costs, credit risk and time horizon before modeling returns. Do not add construction capital unless tenants are investors, consistent with project scope.
- **Superseded:** [NYCPlanning/db-pluto](https://github.com/NYCPlanning/db-pluto) is archived and its README directs readers to data-engineering. Retain for provenance only.

## Adoption and reproducibility checklist

1. Review this PR and approve individual proposed uses before implementation.
1. Pin code SHA/release and upstream dataset URL, release date, retrieval date, geography, schema and checksum in each analysis manifest.
1. Verify source terms separately from software license; resolve NOASSERTION before copying code or redistributing data.
1. Validate a small NYC sample against original agency records; audit BBL/BIN joins, missingness, duplicates, survey uncertainty and temporal alignment.
1. Separate observed baseline data, model assumptions, scenario outputs and statutory authority in every resulting fact table. Compare continuation of existing equity investments with ownership conversion using explicit costs and distributional outcomes.
1. Record checks, unresolved gaps and human approval in the project log. Recheck links and upstream status quarterly or before reliance; no monitor is installed.

## Verification scope

GitHub's connected account was used for repository discovery, metadata and README retrieval on October 23, 2026. The cited repository/README endpoints resolved; pinned heads were recorded. Selected archived status was checked directly. This pass did not execute upstream code, independently reproduce data, audit security, verify every README outbound link, or certify legal compliance. License labels are GitHub metadata signals, not legal opinions. See the companion CSV for filtering and the project resource/provenance indexes for cross-references.
