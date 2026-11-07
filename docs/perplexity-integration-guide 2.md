# Using HousingPolicyResearch Repo with Perplexity for Policy Presentation Generation

This guide shows you how to leverage Perplexity AI to research, synthesize, and generate policy presentations using resources in this repository.

## Overview

Perplexity AI is particularly effective for policy research because it:

- Searches real-time web sources and academic databases
- Synthesizes information from multiple sources
- Generates well-structured, citation-aware content
- Integrates findings with your local documentation

## Quick Start: Three Ways to Use Perplexity

### Method 1: Upload Documents for Context (Recommended for Presentations)

**Best for:** Generating presentations grounded in your existing research

1. **Prepare Your Context**

   - Go to `docs/resources-index.md` - your annotated resource library
   - Go to `docs/resources.csv` - your machine-readable resource database
   - Go to `exported-assets (1)/` - export your policy documents (PET, LOCAL_LAW, etc.)

1. **In Perplexity**

   - Click "Attach" (📎 icon) in the chat
   - Upload key documents:
     - `docs/resources-index.md` (shows what's available)
     - Relevant exported policy documents from `exported-assets (1)/`
     - Your `docs/project-roadmap.md` for scope/goals

1. **Generate Your Presentation**

   - Ask Perplexity to "Create a policy presentation on \[topic\] using the provided resources"
   - Request specific formats: "Structure this as a 5-minute executive summary" or "Create presentation slides"
   - Perplexity will cite your sources and integrate them

**Example prompts:**

```
"Using the resources I've uploaded about housing policy reform, 
create a 3-slide executive presentation on the Public Equity Transfer framework. 
Include key statistics, stakeholder impacts, and implementation timeline."

"Based on these housing documents, draft a 10-minute policy brief 
on tenant protections and TCAP implementation for City Council."
```

### Method 2: Reference GitHub Repository (Research + Generation)

**Best for:** Real-time research synthesis with your documented work

1. **Share Your Repository**

   - In Perplexity, paste your GitHub repo URL: `https://github.com/SfosssHousing/HousingPolicyResearch`
   - Perplexity can browse public repo documentation

1. **Search the Repo + Web**

   - Ask: "Summarize housing subsidy reform best practices from research and from the HousingPolicyResearch repo, then create presentation slides"
   - Perplexity combines your repo's findings with current web research

1. **Cross-Reference Your Work**

   - Use specific file references: "Based on `docs/housing-subsidy-reform-policy-draft-v1.md` and current policies, create comparison slides"

**Example prompts:**

```
"Review the HousingPolicyResearch repo documentation. Create a 
presentation comparing NYC's LOCAL_LAW approaches with best practices 
from the broader US housing policy landscape."

"Using the TCAP_Implementation_Authority document from this repo 
and recent state housing policy trends, draft a policy innovation brief."
```

### Method 3: Interactive Research Sessions (Iterative Refinement)

**Best for:** Building presentations through conversation

1. **Start Research**

   - Upload your `docs/resources-index.md`
   - Ask Perplexity to "Find gaps in my housing policy research"
   - Request recommendations for additional sources

1. **Synthesize Findings**

   ```
   "Based on the 21 resources in my repo:
   - What are the three most important trends?
   - Which stakeholders are underrepresented?
   - What policy recommendations emerge?"
   ```

1. **Generate Presentation Content**

   - Ask Perplexity to draft specific sections
   - Request citations in APA 7th format (see `docs/STYLE-APA.md`)
   - Iterate on tone, depth, and audience

## Organizing Your Repository for Perplexity

### Key Resources to Reference

| Path                                                          | Use in Perplexity            | Content                                     |
| ------------------------------------------------------------- | ---------------------------- | ------------------------------------------- |
| `docs/resources-index.md`                                     | Upload as context            | Annotated bibliography with relevance notes |
| `docs/resources.csv`                                          | Reference structure          | Machine-readable resource database          |
| `docs/housing-subsidy-reform-policy-draft-v1.md`              | Upload for presentation base | Policy analysis framework                   |
| `exported-assets (1)/PET_Master_Policy_Report_v2025-12-17.md` | Upload for reference         | Comprehensive policy report                 |
| `exported-assets (1)/LOCAL_LAW_*.md`                          | Upload for legal framework   | Legal/statutory documents                   |
| `docs/STYLE-APA.md`                                           | Share with Perplexity        | Citation formatting requirements            |

### Before Each Perplexity Session

1. **Clarify Your Goal**

   - Executive presentation?
   - Policy brief?
   - Stakeholder memo?
   - Research synthesis?

1. **Gather Your Materials**

   ```bash
   # List resources to upload
   ls -la docs/
   ls -la exported-assets\ \(1\)/*.md
   ```

1. **Identify Scope**

   - Single policy (e.g., TCAP implementation)
   - Comparative analysis (e.g., LOCAL_LAW A vs B)
   - Sector overview (e.g., NYC housing policy landscape)

## Example Workflows

### Workflow 1: Generate a 5-Minute Executive Briefing

```
1. Upload: resources-index.md + PET_Master_Policy_Report
2. Prompt: "Create a 5-minute briefing on the Public Equity Transfer 
   framework for non-expert stakeholders. Include:
   - What it is (1 min)
   - Why it matters (1 min)
   - Key implementation steps (2 min)
   - Risks and mitigations (1 min)"
3. Request format: PowerPoint outline or slide notes
4. Ask for citations in APA 7th
5. Refine tone/audience
```

### Workflow 2: Comparative Policy Analysis Presentation

```
1. Upload: LOCAL_LAW_A, LOCAL_LAW_B, LOCAL_LAW_C, LOCAL_LAW_D
2. Prompt: "Compare these four NYC housing policy frameworks.
   Create a presentation matrix showing:
   - Jurisdiction scope (citywide vs specific zones)
   - Affordability impact (estimated units)
   - Implementation timeline
   - Stakeholder winners/losers"
3. Request format: Comparison table + summary slides
4. Ask for visualization recommendations
5. Suggest policy synthesis recommendations
```

### Workflow 3: Stakeholder-Specific Presentation

```
1. Upload: housing-subsidy-reform-policy-draft-v1.md + resources-index.md
2. Prompt: "Create three versions of a housing policy presentation:
   - For city government (focus: implementation, budget, timeline)
   - For residents (focus: affordability, rights, eligibility)
   - For developers (focus: requirements, incentives, feasibility)"
3. Each version: 3 slides, distinct messaging
4. Include speaker notes for each
```

## Advanced Techniques

### Asking for APA Citations

```
"When citing sources, use APA 7th edition format. 
Here's my citation style guide: [paste from STYLE-APA.md]
Make sure all sources are cited."
```

### Integrating New Research

```
"I've updated my resource index with 5 new studies on [topic].
Based on my repo documentation + these new sources, 
please revise the presentation on [topic]."
```

### Validating Against Your Framework

```
"Here's my policy evaluation matrix from [docs/file.md].
Generate a presentation that scores each policy option 
against these criteria."
```

### Cross-Referencing Documents

```
"The TCAP_Implementation_Authority document mentions coordination 
with LOCAL_LAW_C. Create a presentation showing how these 
two policies complement each other."
```

## Output Formats

Perplexity can generate presentations in several formats:

| Format                 | Request                                                            |
| ---------------------- | ------------------------------------------------------------------ |
| **Markdown Slides**    | "Create presentation as markdown with `---` separators for slides" |
| **PowerPoint Outline** | "Format as a PowerPoint outline I can import"                      |
| **HTML Presentation**  | "Generate as HTML/reveal.js for web viewing"                       |
| **Speaker Notes**      | "Include detailed speaker notes under each slide"                  |
| **Executive Summary**  | "Create a one-page executive summary"                              |
| **Research Brief**     | "Draft as a policy research brief (2000 words)"                    |

## Tips for Best Results

### 1. **Be Specific About Audience**

```
"Create this for [city planners/residents/city council/investors].
What would this audience care most about?"
```

### 2. **Request Structure Upfront**

```
"Structure the presentation with:
- Problem statement
- Current approaches
- Proposed solution
- Implementation roadmap
- Risks & mitigation"
```

### 3. **Use Your Citation Standard**

```
"Use APA 7th edition citations throughout. 
Reference documents from my uploaded files and web sources."
```

### 4. **Ask for Visuals**

```
"What charts or infographics would best illustrate [concept]?
Describe what I should create to accompany this content."
```

### 5. **Iterate on Tone**

```
"Revise for [urgent/formal/accessible/technical] tone."
```

## Saving Your Work

1. **Copy Perplexity Output**

   - Copy generated content from Perplexity
   - Paste into a new `.md` file in your repo

1. **Track Provenance**

   - Add header: `Generated with Perplexity [date]`
   - Add prompt used
   - List uploaded source documents
   - Add to `docs/generative-output-version-control.md`

1. **Update Your Repo**

   ```bash
   git add docs/my-presentation.md
   git commit -m "Add Perplexity-generated presentation on [topic]"
   git push
   ```

## Quality Checklist

Before using Perplexity output in a presentation:

- [ ] All citations verified (cross-check with source documents)
- [ ] No hallucinated sources or statistics
- [ ] Consistent with your APA style guide
- [ ] Audience-appropriate language
- [ ] Key facts align with your uploaded documents
- [ ] Provenance documented (`generative-output-version-control.md`)
- [ ] For legal/policy content: reviewed by subject matter expert

## Troubleshooting

| Issue                                        | Solution                                                   |
| -------------------------------------------- | ---------------------------------------------------------- |
| Perplexity cites non-existent sources        | Upload more of YOUR documents to anchor the response       |
| Generated content doesn't match my framework | Be more explicit: "Use ONLY the uploaded documents"        |
| Citations are incomplete                     | Provide your citation style guide upfront                  |
| Too generic for my project                   | Upload specific reports and say "Focus on these materials" |
| Format doesn't match what you need           | Request specific markdown/HTML/slide format explicitly     |

## Next Steps

1. **Try it now**: Upload `docs/resources-index.md` to Perplexity and ask "What presentation would you recommend based on these resources?"
1. **Build iteratively**: Generate a rough outline, refine through conversation, export final version
1. **Document your process**: Add notes to `docs/generative-output-version-control.md`
1. **Contribute back**: Share what worked in your team's workflow

______________________________________________________________________

**Last updated:** 2025-12-30\
**Maintained by:** Housing Policy Research Team
