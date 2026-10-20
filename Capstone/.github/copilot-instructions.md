This repository is a policy research capstone composed mainly of Word/PowerPoint documents, PDFs, and reference data files (CSV/PDFs). There is no application code, build system, or CI detected in the workspace.

Key context for AI coding agents working in this repository

- Big picture: This repo contains working drafts, final reports, slide decks, and data sources for a housing subsidy policy project. The primary artifacts are Word docs in the root and several subfolders (e.g., `Final Drafts/`, `FULL PACKAGE FINAL/`, `Research drafts/`, `Visuals/`, `data:sources/`). There are no source-language projects (no package.json, pyproject.toml, Makefile, Dockerfile, or .github/workflows found).

- Primary tasks an agent will be asked to do:

  - Edit, proofread, or reformat Word and PDF documents (docx, pages, pptx).
  - Extract, summarize, or transform data from the `Visuals/` and `data:sources/` folders (CSV, PDFs).
  - Generate or update plain-text artifacts: README, memos, or policy summaries.
  - Prepare presentation slides and visuals; create CSV summaries and charts.

- Project-specific conventions and notes:

  - Filenames are entitled with natural language and dates; preserve original filenames when producing revised copies (use a suffix like `_edited_v1.docx`).
  - The repository stores final and draft documents in separate folders: prefer editing files in `Research drafts/` or `Final Drafts/` rather than the `FULL PACKAGE FINAL/` unless the user asks to update the final package.
  - Visual assets (charts and PNGs) are in `Visuals/` — keep image sizes and aspect ratios consistent when creating new visuals.

- Useful examples (explicit files to reference):

  - Root documents: `Housing_Subsidy_MasterFormatted_Final.docx`, `Comprehensive_Housing_Subsidy_Reform_Proposal_CITED.docx`
  - Data/visuals: `Visuals/10-Year Cost vs. Family Wealth Generation by Housing Model.png`, `Visuals/Cost_Savings_and_Wealth_Generation_Comparison.csv`
  - Notes: `Housing_Subsidy_Data_Sourcing_Desktop_Notes.txt`

- How to operate safely and usefully here:

  - Do not attempt to run build or test commands — there are none. If you need to transform a Word/PPTX/PDF file, propose a clear plan (tools to use: pandoc, python-docx, pypandoc, PyPDF2) and ask for permission before modifying original files.
  - When producing derived artifacts (summaries, CSV extracts, slide decks), create new files in a clearly named folder such as `Generated/` and include a short README explaining inputs and transformation steps.

- Integration points and external dependencies:

  - External sources are referenced in `data:sources/` (news clippings, reports). Cite any source file you used in a short metadata file next to derived outputs.

- Quick checklist for common requests:

  - "Summarize all drafts": list files in `Research drafts/`, extract headings from `.docx` files, and produce a 1–2 page executive summary.
  - "Create slides": locate the most recent `Housing_Policy_Stakeholder_Update*` slide deck and propose a 6–8 slide executive summary before creating a new `.pptx`.
  - "Extract CSVs": validate column headers and produce a short README and sample plotting script (Python/matplotlib or R) when asked.

- When uncertain about which document is "current": prefer to ask the user. If forced to pick, prefer files in `Final Drafts/` over root files and prefer filenames with `_Final` or `FINAL`.

If you (human) want a merged or more code-oriented instructions file (for example, if new code or CI is added), tell the agent where the source code lives and what languages/build tools to expect. Otherwise, confirm if you want an initial `Generated/` folder created for outputs.
