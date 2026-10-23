# Quick Reference: Using HousingPolicyResearch with Perplexity

## 30-Second Overview

This repository contains housing policy research documents, analysis, and resources. Use **Perplexity AI** to generate presentations, briefs, and analysis from these materials.

______________________________________________________________________

## Your First Presentation (5 Minutes)

### Step 1: Gather Materials

```bash
cd /Users/sethadmin/Documents/GitHub/HousingPolicyResearch/HousingPolicyResearch-1

# Key files to use:
# - docs/resources-index.md (your bibliography)
# - docs/housing-subsidy-reform-policy-draft-v1.md (policy analysis)
# - exported-assets (1)/PET_Master_Policy_Report_v2025-12-17.md (main report)
# - Any LOCAL_LAW_*.md files (legal frameworks)
```

### Step 2: Open Perplexity

Visit https://www.perplexity.ai

### Step 3: Upload Documents

- Click **Attach** (📎 button)
- Choose files from this repo
- Upload 2-3 key documents

### Step 3: Ask Perplexity

```
"Using these housing policy documents, create a professional 
5-slide presentation on [YOUR TOPIC] for [YOUR AUDIENCE].
Use APA 7th edition citations."
```

### Step 4: Copy & Save

- Copy the output
- Save to: `docs/my-presentation.md`
- Commit: `git add docs/my-presentation.md && git commit -m "Add presentation on [topic]"`

______________________________________________________________________

## Key Documents

| What You Need        | Where to Find                                                 | Example Use                                     |
| -------------------- | ------------------------------------------------------------- | ----------------------------------------------- |
| **Research Index**   | `docs/resources-index.md`                                     | Upload to show Perplexity what sources you have |
| **Policy Analysis**  | `docs/housing-subsidy-reform-policy-draft-v1.md`              | Upload as background/framework                  |
| **Full Reports**     | `exported-assets (1)/PET_Master_Policy_Report_v2025-12-17.md` | Upload for comprehensive reference              |
| **Legal Frameworks** | `exported-assets (1)/LOCAL_LAW_*.md` (4 files)                | Upload for legal/regulatory context             |
| **Citation Style**   | `docs/STYLE-APA.md`                                           | Share with Perplexity for formatting            |

______________________________________________________________________

## Common Prompts

### Executive Briefing (3-5 minutes)

```
"Create a 3-slide executive briefing on [TOPIC] for [AUDIENCE: e.g., city officials].
- Slide 1: Problem statement
- Slide 2: Proposed solution  
- Slide 3: Implementation roadmap
Use citations from the provided documents."
```

### Comparative Analysis

```
"Compare these policy frameworks [upload LOCAL_LAW files].
Create a comparison matrix showing:
- Scope and coverage
- Affordability impact
- Implementation timeline
- Stakeholder effects"
```

### Deep Dive Report

```
"Based on these documents, write a 2,000-word policy brief on [TOPIC].
Include:
- Background and context
- Current approaches
- Proposed improvements
- Implementation recommendations
- References in APA 7th format"
```

### Stakeholder-Specific Versions

```
"Create three versions of a presentation on [TOPIC]:
1. For residents (emphasize affordability, rights, eligibility)
2. For developers (emphasize requirements, incentives, feasibility)
3. For government (emphasize implementation, budget, timeline)
Each 2-3 slides with speaker notes."
```

______________________________________________________________________

## Document Organization

```
HousingPolicyResearch/
├── docs/
│   ├── resources-index.md          ← Your bibliography (upload this!)
│   ├── resources.csv               ← Machine-readable database
│   ├── housing-subsidy-reform-policy-draft-v1.md  ← Policy framework
│   ├── STYLE-APA.md                ← Citation style guide
│   ├── perplexity-integration-guide.md  ← Full guide (you're reading a version!)
│   └── [other documentation]
│
├── exported-assets (1)/
│   ├── PET_Master_Policy_Report_v2025-12-17.md  ← Main report
│   ├── LOCAL_LAW_A_Public_Equity_Transfer_Framework.md
│   ├── LOCAL_LAW_B_SLEC_Classification.md
│   ├── LOCAL_LAW_C_COPA_TCAP_Integration.md
│   ├── LOCAL_LAW_D_TCAP_Implementation_Authority.md
│   └── [20+ additional policy documents]
│
├── src/
│   └── chatgpt_notion_sync/  ← Python utilities (for automation)
│
├── tests/  ← Unit tests (all passing ✅)
└── README.md

```

______________________________________________________________________

## Perplexity Tips

### ✅ DO

- ✅ Upload multiple documents for context
- ✅ Request specific formats (slides, brief, report)
- ✅ Ask for APA 7th citations
- ✅ Specify your audience
- ✅ Iterate: refine tone, depth, focus
- ✅ Upload your style guide
- ✅ Ask for visualization suggestions

### ❌ DON'T

- ❌ Don't assume Perplexity remembers previous uploads
- ❌ Don't expect perfect citations (verify them)
- ❌ Don't use generated content without review
- ❌ Don't forget to document provenance
- ❌ Don't skip verifying facts against source documents

______________________________________________________________________

## Quality Checklist

Before using Perplexity output:

- [ ] Citations verified against original sources
- [ ] No hallucinated statistics or sources
- [ ] Consistent with APA 7th style
- [ ] Appropriate language for audience
- [ ] Key facts match your documents
- [ ] Added to `docs/generative-output-version-control.md`
- [ ] Subject matter expert reviewed (if legal/policy content)

______________________________________________________________________

## Troubleshooting

### "Perplexity isn't citing my documents"

→ Upload more of YOUR documents instead of relying on web search

### "Citations are incomplete or wrong"

→ Share `docs/STYLE-APA.md` explicitly in your prompt

### "The presentation is too generic"

→ Upload specific reports and say "Focus only on these materials"

### "I need a different format"

→ Be explicit: "Format as PowerPoint outline" or "Create HTML slides"

______________________________________________________________________

## System Status

✅ **Everything is working:**

- Python environment: Ready
- Tests: 9/9 passing
- Documentation: Complete
- GitHub issues: Resolved (except #34, which is GitHub's)
- Perplexity guide: Created
- Ready to generate presentations

______________________________________________________________________

## Next Actions

### Today

1. [ ] Review this quick reference
1. [ ] Read `docs/perplexity-integration-guide.md` for full details
1. [ ] Try one Perplexity workflow

### This Week

1. [ ] Generate 2-3 presentations
1. [ ] Document your process
1. [ ] Train team on workflows

### This Month

1. [ ] Build library of 5-10 key presentations
1. [ ] Establish quality/review process
1. [ ] Integrate with your workflow

______________________________________________________________________

## Contact & Questions

- **Full Guide**: See `docs/perplexity-integration-guide.md`
- **System Status**: See `SYSTEM_STATUS_2025-12-30.md`
- **Policy Docs**: See `exported-assets (1)/` folder
- **Resources**: See `docs/resources-index.md`

______________________________________________________________________

**You're all set! Go generate some amazing policy presentations.** 🚀

Generated: 2025-12-30
