# Housing Policy Research Resources Index

**Version:** 1.0\
**Last Updated:** 2025-12-02\
**Maintained by:** Housing Policy Research Librarian & Doc Ops agent

> **Directory note:** This file should ideally be located at `/docs/resources/index.md` once directory creation is supported. The companion CSV file is at `/docs/resources.csv`.

## Overview

This index catalogs all research sources, datasets, tools, and references used in the Housing Policy Research project. Each entry includes:

- **APA-formatted citation** following guidelines in [`docs/STYLE-APA.md`](STYLE-APA.md)
- **Brief annotations** (1-2 sentences) explaining relevance and application
- **Quality flags** indicating source type and access status
- **Cross-references** to documentation sections, issues, and PRs where the source is used

## Table of Contents

- [Technical Resources](#technical-resources)
  - [APIs and Integration Platforms](#apis-and-integration-platforms)
  - [Development Tools](#development-tools)
  - [Documentation Tools](#documentation-tools)
- [Housing Policy Research Resources](#housing-policy-research-resources)
  - [Government Sources](#government-sources)
  - [Academic Literature](#academic-literature)
  - [Data Sources](#data-sources)
  - [Policy Examples](#policy-examples)
- [Project Management Resources](#project-management-resources)
- [Version Control and Generative Output](#version-control-and-generative-output)

______________________________________________________________________

## Technical Resources

### APIs and Integration Platforms

#### OpenAI API

**Citation:**
OpenAI. (n.d.). *OpenAI API documentation*. https://platform.openai.com/docs/

**Annotation:**
API documentation for ChatGPT and Codex integration. Essential for implementing automated analysis and code generation workflows in the research environment.

**Quality:** `[Primary source]` `[Technical documentation]`\
**Used in:** [`docs/integration-plan.md`](integration-plan.md#31-chatgpt--codex), [`docs/connection-checks.md`](connection-checks.md)\
**Relevance:** Enables AI-assisted policy analysis and document generation

______________________________________________________________________

#### Notion API

**Citation:**
Notion. (n.d.). *Notion API reference*. Notion Developers. https://developers.notion.com/reference/intro

**Annotation:**
Official API documentation for Notion integration. Required for synchronizing research notes, literature reviews, and task tracking between GitHub and Notion knowledge bases.

**Quality:** `[Primary source]` `[Technical documentation]`\
**Used in:** [`docs/integration-plan.md`](integration-plan.md#32-notion-integration), [`docs/connection-checks.md`](connection-checks.md)\
**Relevance:** Facilitates centralized knowledge management and cross-platform documentation sync

______________________________________________________________________

#### GitHub Actions

**Citation:**
GitHub. (n.d.). *GitHub Actions documentation*. GitHub Docs. https://docs.github.com/en/actions

**Annotation:**
Official documentation for GitHub's CI/CD platform. Used for automating documentation linting, synchronization workflows, and security scanning in the project repository.

**Quality:** `[Primary source]` `[Technical documentation]`\
**Used in:** [`docs/integration-plan.md`](integration-plan.md#33-github-automation)\
**Relevance:** Automates quality gates and data flows between integrated systems

______________________________________________________________________

#### Zotero Web API

**Citation:**
Corporation for Digital Scholarship. (n.d.). *Zotero Web API v3*. Zotero. https://www.zotero.org/support/dev/web_api/v3/start

**Annotation:**
API specification for programmatic access to Zotero reference libraries. Enables automated citation synchronization and annotation export for reproducible research workflows.

**Quality:** `[Primary source]` `[Technical documentation]`\
**Used in:** [`docs/integration-plan.md`](integration-plan.md#34-zotero-integration), [`docs/connection-checks.md`](connection-checks.md)\
**Relevance:** Maintains traceability of research sources and enables automated bibliography generation

______________________________________________________________________

### Development Tools

#### Node.js

**Citation:**
OpenJS Foundation. (n.d.). *Node.js documentation*. Node.js. https://nodejs.org/

**Annotation:**
JavaScript runtime required for npm-based automation tools and OpenAI Node.js SDK. Prerequisite for development environment setup.

**Quality:** `[Primary source]` `[Technical documentation]`\
**Used in:** [`docs/integration-plan.md`](integration-plan.md#1-prerequisites), [`README.md`](../README.md)\
**Relevance:** Core dependency for automation scripts and integration tooling

______________________________________________________________________

#### Python 3.11+

**Citation:**
Python Software Foundation. (n.d.). *Python 3.11 documentation*. Python.org. https://docs.python.org/3.11/

**Annotation:**
Python runtime required for API clients, data synchronization scripts, and automation workflows. Minimum version 3.11 specified for project compatibility.

**Quality:** `[Primary source]` `[Technical documentation]`\
**Used in:** [`docs/integration-plan.md`](integration-plan.md#1-prerequisites)\
**Relevance:** Primary scripting language for data pipeline automation

______________________________________________________________________

### Documentation Tools

#### Markdownlint

**Citation:**
Markdown Lint Tool. (n.d.). *markdownlint*. GitHub. https://github.com/DavidAnson/markdownlint

**Annotation:**
Markdown linting tool for enforcing consistent documentation formatting. Proposed for GitHub Actions workflows to maintain documentation quality.

**Quality:** `[Secondary source]` `[Tool documentation]`\
**Used in:** [`docs/integration-plan.md`](integration-plan.md#33-github-automation)\
**Relevance:** Ensures documentation consistency and readability

______________________________________________________________________

## Housing Policy Research Resources

### Government Sources

*Note: As the project develops, this section will be populated with specific HUD reports, Census data, and regulatory documents referenced in policy proposals. Each entry will follow the APA format specified in [`docs/STYLE-APA.md`](STYLE-APA.md#2-government-documents).*

**Placeholder entries (examples from STYLE-APA.md):**

#### U.S. Department of Housing and Urban Development Reports

**Citation:**
U.S. Department of Housing and Urban Development. (2021). *Barriers to the production and preservation of affordable housing* (Report to Congress). https://www.huduser.gov/portal/publications/Barriers-to-Production-and-Preservation-of-Affordable-Housing.html

**Annotation:**
Comprehensive federal analysis of regulatory and market barriers to affordable housing production. Primary source for understanding federal policy context and identifying intervention points.

**Quality:** `[Primary source]` `[Government document]`\
**Used in:** *To be linked to policy proposals*\
**Relevance:** Establishes federal baseline for housing barrier analysis

______________________________________________________________________

### Academic Literature

*Note: Academic sources will be added as they are cited in research memos and policy proposals. Priority will be given to peer-reviewed articles with DOIs.*

**Placeholder entries (examples from STYLE-APA.md):**

#### Zoning Economics

**Citation:**
Fischel, W. A. (2015). *Zoning rules! The economics of land use regulation*. Lincoln Institute of Land Policy.

**Annotation:**
Foundational text explaining economic theory of zoning and land use regulation. Essential for understanding homeowner voting behavior and regulatory capture dynamics.

**Quality:** `[Primary source]` `[Academic book]`\
**Used in:** *To be linked to zoning reform proposals*\
**Relevance:** Provides theoretical framework for regulatory reform advocacy

______________________________________________________________________

#### Housing Supply Economics

**Citation:**
Glaeser, E. L., & Gyourko, J. (2018). *The economic implications of housing supply* (Working Paper No. 24815). National Bureau of Economic Research. https://doi.org/10.3386/w24815

**Annotation:**
Quantifies housing supply elasticity effects and price responses to regulatory changes. Critical empirical basis for understanding market impacts of zoning reforms.

**Quality:** `[Primary source]` `[Academic working paper]`\
**Used in:** *To be linked to supply-side policy proposals*\
**Relevance:** Provides data-driven evidence for supply-focused interventions

______________________________________________________________________

### Data Sources

*Note: Dataset entries will include version numbers and access dates for reproducibility. Priority given to authoritative sources like Census Bureau and HUD.*

**Placeholder entry (example from STYLE-APA.md):**

#### American Housing Survey

**Citation:**
U.S. Census Bureau. (2020). *American Housing Survey (AHS) 2019 national file* \[Data set\]. https://www.census.gov/programs-surveys/ahs/data.html

**Annotation:**
Authoritative federal dataset on housing conditions, costs, and demographics. Used for baseline market analysis and trend identification.

**Quality:** `[Primary source]` `[Government data]`\
**Used in:** *To be linked to quantitative analysis sections*\
**Relevance:** Provides nationally representative housing market data

______________________________________________________________________

### Policy Examples

*Note: Municipal code citations and policy case studies will be added as examples are researched for the proposal. Each will include jurisdiction, date, and implementation context.*

**Placeholder entry (example from STYLE-APA.md):**

#### Minneapolis Zoning Reform

**Citation:**
City of Minneapolis. (2020). *Minneapolis Code of Ordinances § 520. Zoning Code*. https://library.municode.com/mn/minneapolis/codes/code_of_ordinances

**Annotation:**
Example of ADU legalization and incremental zoning reform. Model for analyzing implementation pathways and political feasibility.

**Quality:** `[Primary source]` `[Municipal code]`\
**Used in:** *To be linked to reform strategy sections*\
**Relevance:** Demonstrates practical application of supply-side reforms

______________________________________________________________________

## Project Management Resources

### Security and Access Management

#### GitHub Security Guide

**Citation:**
GitHub. (n.d.). *Security guides for GitHub Actions*. GitHub Docs. https://docs.github.com/en/actions/security-guides

**Annotation:**
Official guidance for securing CI/CD pipelines and managing secrets in GitHub Actions. Referenced for establishing project security controls.

**Quality:** `[Primary source]` `[Technical documentation]`\
**Used in:** [`docs/integration-plan.md`](integration-plan.md#5-security-controls), [`SECURITY.md`](../SECURITY.md)\
**Relevance:** Ensures secure automation and protects sensitive credentials

______________________________________________________________________

### Apple Universal Linking

#### Apple Developer Documentation

**Citation:**
Apple Inc. (n.d.). *Allowing apps and websites to link to your content*. Apple Developer Documentation. https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content/

**Annotation:**
Official specification for configuring universal links in iOS/macOS apps. Adapted for housing policy research mobile/web integration in the universal linking guide.

**Quality:** `[Primary source]` `[Technical documentation]`\
**Used in:** [`docs/universal-linking-guide.md`](universal-linking-guide.md)\
**Relevance:** Enables seamless cross-platform documentation access

______________________________________________________________________

## Version Control and Generative Output

### Generative AI Output Management

This section documents version-controlled generative outputs from ChatGPT, Codex, and other AI tools used in the research process.

#### Integration Plan

**Source:** Generated via AI-assisted documentation (ChatGPT/Codex)\
**File:** [`docs/integration-plan.md`](integration-plan.md)\
**Created:** Prior to 2025-12-02\
**Last verified:** 2025-12-02\
**Status:** `[Active]` `[Generative output]`

**Description:**
Comprehensive environment setup and integration architecture document. Covers secure connection patterns for ChatGPT, Codex, Notion, GitHub, and Zotero with automation workflows.

**Verification notes:**

- All external links tested 2025-12-02
- References to OpenAI, Notion, GitHub, and Zotero APIs verified against current documentation
- Security recommendations align with current best practices

______________________________________________________________________

#### Generative Output Task Breakdown

**Source:** Generated via AI-assisted documentation (ChatGPT/Codex)\
**File:** [`docs/generative-output-tasks.md`](generative-output-tasks.md)\
**Created:** Prior to 2025-12-02\
**Last verified:** 2025-12-02\
**Status:** `[Active]` `[Generative output]`

**Description:**
Operational runbook expanding Section 9 of integration-plan.md. Defines actionable steps for prompt library, evaluation harness, human-in-loop reviews, data governance, and reporting automation.

**Verification notes:**

- Task breakdown aligns with integration-plan.md structure
- References to other project files verified
- Implementation tracker approach compatible with GitHub Projects

______________________________________________________________________

#### Connection Checks Documentation

**Source:** Generated via AI-assisted documentation (ChatGPT/Codex)\
**File:** [`docs/connection-checks.md`](connection-checks.md)\
**Created:** Prior to 2025-12-02\
**Last verified:** 2025-12-02\
**Status:** `[Active]` `[Generative output]`

**Description:**
Step-by-step procedures for validating secure connections to all integrated platforms. Includes reverse-flow validation and security controls checklist.

**Verification notes:**

- Connection test commands verified for syntax
- API endpoint patterns checked against current platform documentation
- Security control checklist comprehensive for stated scope

______________________________________________________________________

#### Universal Linking Guide

**Source:** Generated via AI-assisted documentation (ChatGPT/Codex)\
**File:** [`docs/universal-linking-guide.md`](universal-linking-guide.md)\
**Created:** Prior to 2025-12-02\
**Last verified:** 2025-12-02\
**Status:** `[Active]` `[Generative output]`

**Description:**
Adaptation of Apple's universal linking specification for housing policy research mobile/web clients. Includes AASA file configuration and testing procedures.

**Verification notes:**

- Apple Developer Documentation reference verified
- JSON example syntax validated
- Cross-references to other project docs accurate

______________________________________________________________________

#### Issue Comments

**Source:** User-generated comment\
**File:** [`comments/issue-2.txt`](../comments/issue-2.txt)\
**Created:** Prior to 2025-12-02\
**Last verified:** 2025-12-02\
**Status:** `[Active]` `[Project artifact]`

**Description:**
Comment suggesting integration of citations into CSV for Issue #2 (Building a Resources Database with citations). Proposes consolidating resources and citations in unified structure.

**Note:** This comment informed the design of the current resources index and CSV structure, which integrates citation management with resource tracking.

______________________________________________________________________

## Maintenance and Update Log

### Change History

| Date       | Change                                | Author                                  | PR/Issue       |
| ---------- | ------------------------------------- | --------------------------------------- | -------------- |
| 2025-12-02 | Initial resources index created       | Housing Policy Research Librarian agent | *Current task* |
| 2025-12-02 | APA style guide established           | Housing Policy Research Librarian agent | *Current task* |
| 2025-12-02 | Existing generative outputs cataloged | Housing Policy Research Librarian agent | *Current task* |

### Pending Updates

- [ ] Add housing policy-specific research sources as policy proposals are developed
- [ ] Populate government data sources section with Census and HUD datasets
- [ ] Add peer-reviewed academic articles as literature review progresses
- [ ] Link municipal code examples as case studies are researched
- [ ] Create automated citation validation workflow
- [ ] Establish quarterly review process for resource currency

### Quality Gates

Before merging updates to this index:

1. ✅ All citations verified against original sources
1. ✅ APA format compliance checked against [`docs/STYLE-APA.md`](STYLE-APA.md)
1. ✅ Annotations include relevance and application statements
1. ✅ Quality flags assigned appropriately
1. ✅ Cross-references to documentation tested
1. ✅ Verification notes documented

______________________________________________________________________

## How to Use This Index

### For Researchers

1. Search this index before adding new citations to avoid duplicates
1. Copy APA-formatted citations directly into policy documents
1. Use annotations to assess source relevance quickly
1. Follow cross-references to see how sources are applied in context

### For Contributors

1. Review [`docs/STYLE-APA.md`](STYLE-APA.md) before adding entries
1. Complete all required fields (citation, annotation, quality flags, cross-references)
1. Verify citations against original sources before submission
1. Update the CSV file ([`docs/resources.csv`](resources.csv)) in parallel with this index
1. Open a PR with the label `documentation` for review

### For Automation

- Parse [`docs/resources.csv`](resources.csv) for structured data access
- Use quality flags to filter by source type
- Extract cross-references for automated link checking
- Generate bibliographies by filtering entries used in specific documents

______________________________________________________________________

## Verification Notes

**Last comprehensive review:** 2025-12-02

### Technical Resources Verification

- All API documentation links tested and active
- Version numbers current as of review date
- Integration patterns align with current platform capabilities

### Existing Documentation Verification

- All internal cross-references tested
- Generative output files cataloged and dated
- File paths verified against repository structure

### Outstanding Items

- Housing policy research sources to be added as research progresses
- Government data sources pending policy proposal development
- Academic literature section to be populated with specific citations
- Municipal code examples to be added as case studies are identified

### Next Verification Due

**2025-03-02** (Quarterly review cycle)

______________________________________________________________________

**Questions or suggestions?** Open an issue with the label `documentation` to propose additions or corrections to this index.

**Citation style questions?** Refer to [`docs/STYLE-APA.md`](STYLE-APA.md) or open an issue for clarification.

## PET/TCAP external repositories — proposed 2026-10-23

See the [curated registry](external-repositories.md) and [filterable CSV](external-repositories.csv). All entries are code/data tools, not legal authority. Proposed applications and quality limits follow; all links and pinned README snapshots were retrieved on October 23, 2026.

- NYCDB contributors. (n.d.). *nycdb* \[Source code\]. GitHub. Retrieved October 23, 2026, from [nycdb/nycdb](https://github.com/nycdb/nycdb). Load property and enforcement baselines for candidate screening. Quality: Community ETL; Core; not legal authority. Third-party transformations; NYCHA BBL coverage is not household eligibility; validate dataset vintages and BBL joins.
- JustFix. (n.d.). *who-owns-what* \[Source code\]. GitHub. Retrieved October 23, 2026, from [JustFixNYC/who-owns-what](https://github.com/JustFixNYC/who-owns-what). Map ownership associations to investigate acquisition candidates. Quality: Tenant advocacy tool; Core; not legal authority. Associations are investigative leads rather than verified title or beneficial ownership; verify against underlying records.
- New York City Department of City Planning. (n.d.). *data-engineering* \[Source code\]. GitHub. Retrieved October 23, 2026, from [NYCPlanning/data-engineering](https://github.com/NYCPlanning/data-engineering). Inspect DCP data production and source lineage before building parcel baselines. Quality: Agency data pipelines; Core; not legal authority. Build output may be draft; use approved published releases and record dataset vintage. Replaces archived db-pluto.
- NYC Planning Labs. (n.d.). *labs-community-profiles* \[Source code\]. GitHub. Retrieved October 23, 2026, from [NYCPlanning/labs-community-profiles](https://github.com/NYCPlanning/labs-community-profiles). Use community district indicator patterns to design neighborhood distributional reporting. Quality: Agency visualization code; Supporting; not legal authority. README references a 202402 table and legacy services; do not infer current demographic estimates from repository activity.
- City of New York. (n.d.). *ACCESS-NYC* \[Source code\]. GitHub. Retrieved October 23, 2026, from [CityOfNewYork/ACCESS-NYC](https://github.com/CityOfNewYork/ACCESS-NYC). Study multilingual resident navigation and benefits screening interfaces for implementation planning. Quality: City service website code; Supporting; not legal authority. Website code is not HRA administrative rules or a complete eligibility engine; program information and screening services are separate dependencies.
- PolicyEngine. (n.d.). *policyengine-us* \[Source code\]. GitHub. Retrieved October 23, 2026, from [PolicyEngine/policyengine-us](https://github.com/PolicyEngine/policyengine-us). Explore NY household resource changes with explicit policy-year and parameter assumptions. Quality: Independent tax-benefit model; Conditional; not legal authority. README deprecates direct aggregate microsimulation in favor of policyengine.py; separately vet that package before use. NYC program coverage and calibration remain unverified; not an agency budget model.
- Kyle Walker and contributors. (n.d.). *tidycensus* \[Source code\]. GitHub. Retrieved October 23, 2026, from [walkerke/tidycensus](https://github.com/walkerke/tidycensus). Retrieve ACS and decennial baselines for NYC geographies. Quality: Independent Census API client; Supporting; not legal authority. Not Census-endorsed; retain margins of error and survey vintage; avoid household inference from area averages.
- JustFix. (n.d.). *nycha-scraper* \[Source code\]. GitHub. Retrieved October 23, 2026, from [JustFixNYC/nycha-scraper](https://github.com/JustFixNYC/nycha-scraper). Understand provenance of a historical NYCHA block-and-lot crosswalk. Quality: PDF extraction utility; Historical only; not legal authority. README targets August 27, 2018 guide; do not use as current NYCHA inventory or evidence of transfer eligibility.
- BetaNYC. (n.d.). *New-York-City-Budget* \[Source code\]. GitHub. Retrieved October 23, 2026, from [BetaNYC/New-York-City-Budget](https://github.com/BetaNYC/New-York-City-Budget). Inspect structured Council designations and their provenance when assessing funding streams. Quality: Civic fiscal data extraction; Conditional; not legal authority. Use structured 2.0 sources only; retired PDF extracts have known errors. Designations are not expenditure actuals or proof of reusable HPD/HRA/NYCHA appropriations. Independently reconcile relied-on figures.
