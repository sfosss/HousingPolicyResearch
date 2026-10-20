# Project Roadmap and Next Steps

This roadmap captures actionable follow-up work for the Housing Policy Research project. Update the checklist as milestones are completed.

## 1. Documentation Enhancements

- [ ] Convert the legacy `Capstone alias` document (see `docs/capstone-alias.docx`, a summary of prior project milestones and terminology) into structured Markdown (determine whether to archive or reformat).
- [ ] Expand the datasets section in `README.md` with specific links and access instructions.
- [ ] Draft a citation management guide linking Zotero collections to repository outputs.

## 2. Data and Analysis Pipeline

- [ ] Define the primary research questions and hypotheses in `docs/research-plan.md`.
- [ ] Inventory available datasets (HUD, ACS, local housing authorities) and document access requirements.
- [ ] Prototype an ETL workflow (e.g., Python notebooks or scripts) to normalize housing policy datasets.

## 3. Tool Integrations

- [ ] Implement a GitHub Action that syncs meeting notes from Notion to the `/notes` directory.
- [ ] Create a script or workflow to export Zotero bibliographies automatically into `docs/references.bib`.
- [ ] Establish a secure workflow for capturing ChatGPT outputs and committing summarized insights.

## 4. Quality Assurance

- [ ] Add pre-commit hooks for linting Markdown and Python code (`markdownlint`, `flake8`, `black`).
- [ ] Configure continuous integration tests to run analytical notebooks or scripts when added.
- [ ] Establish a data validation checklist ensuring reproducibility of published results.

## 5. Governance and Security

- [ ] Document onboarding/offboarding steps for collaborators, including GitHub access levels.
- [ ] Set up a secrets rotation calendar for OpenAI, Notion, and Zotero integrations.
- [ ] Draft an incident response plan for data or credential exposure.

______________________________________________________________________

**Last updated:** 2025-12-01
