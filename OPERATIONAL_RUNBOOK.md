# Housing Policy Research Tools - Operational Runbook

**Audience:** Municipal Policy Analyst, Research Team\
**Version:** 1.0\
**Last Updated:** December 26, 2025\
**Status:** Production Ready

______________________________________________________________________

## Quick Reference

| Task              | Command                             | Time   | Frequency  |
| ----------------- | ----------------------------------- | ------ | ---------- |
| **Sweep Bills**   | "Sweep Bills" in Raycast            | 5 min  | Weekly     |
| **Generate Memo** | "Generate Draft Section" in Raycast | 5 min  | As needed  |
| **Add Source**    | "Add Source" in Raycast             | 2 min  | Daily      |
| **Weekly Report** | bash scripts/sweep_bills_weekly.sh  | 10 min | Monday 9am |

______________________________________________________________________

## 1. SWEEP BILLS (Legislative Monitoring)

### Purpose

Monitor new and updated legislation across NYC, NY State, and Federal levels related to housing subsidies and policy.

### When to Use

- **Frequency:** Weekly (recommended Mondays)
- **Time Required:** 5 minutes
- **Output:** CSV file with bill data
- **Integration:** Feeds into policy memo drafting

### Step-by-Step Guide

#### Step 1: Open Raycast

```
Keyboard: Cmd + Space
Result: Raycast search bar opens
```

#### Step 2: Search for Command

```
Type: "Sweep Bills"
Result: "Sweep Bills" command appears
Click: Select the command
```

#### Step 3: Select Jurisdictions

```
You see three checkboxes:
  ✓ NYC
  ✓ New York State  
  ☐ Federal (optional)

Action: Check NYC and NY State (required minimum)
Note: Federal optional for broader context
```

#### Step 4: Set Date Range

```
You see: "Search Since (Optional)" date picker
Action: Click date picker
Select: 7 days ago (for weekly sweeps)
Example: If today is Jan 13, select Jan 6
Note: Leave empty to search all bills
```

#### Step 5: Execute

```
Action: Click "Sweep Bills" button
Status: Loading indicator appears
Wait: 5-30 seconds for results
```

#### Step 6: Review Results

```
You see: Detail view with formatted results
Show: 
  - Bill title
  - Jurisdiction (NYC, NY, Federal)
  - Status (In Committee, Passed, Enacted, etc.)
  - Last action date
  - Summary (if available)
  - URL (if available)

Action: Scroll through all bills
Note: Copy relevant bills for your research
```

#### Step 7: Export to CSV

```
Raycast outputs: bills_sweep_YYYYMMDD.csv
Location: ~/Documents/GitHub/HousingPolicyResearch/data/bills/

Columns:
  - title: Bill name
  - jurisdiction: NYC, NY, or Federal
  - status: Current legislative status
  - last_action: Most recent action date
  - url: Link to bill text (if available)
  - policy_area: Tagged as "housing_subsidy"
  - priority: Manual assignment after review
  - notes: Your analysis notes
```

#### Step 8: Add to Notion Database

```
Action: Open Notion Housing Bills table
Import: Paste bill data from CSV
Tag: By jurisdiction and policy relevance
Priority: Set HIGH/MEDIUM/LOW based on impact
Notes: Add 1-2 sentence policy summary

Example:
Title: "Housing Preservation Act 2025"
Jurisdiction: NY State
Status: In Committee
Priority: HIGH
Notes: "Increases subsidized housing funding by 12%; could affect TCAP model assumptions"
```

#### Step 9: Close Raycast

```
Keyboard: Esc
Result: Raycast closes
Next: Proceed to research or memo drafting
```

### Troubleshooting

**Problem:** Command not found in search\
**Solution:** Ensure extension is loaded (Cmd + Shift + A → "Load Extension" → Select directory)

**Problem:** "Network error. Check your connection and backend URL."\
**Solution:** Verify backend API is running and URL is correct in Raycast preferences (Cmd + ,)

**Problem:** Results show "No new bills found."\
**Solution:** Normal if search period is short; try extending date range or try Federal jurisdiction

**Problem:** Results are loading slowly\
**Solution:** Backend may be under load; wait 30+ seconds or try again later

### Example Output

```
- **Housing Preservation Act 2025** (`NY State`)
  - Status: In Committee
  - Last Action: 2025-01-05
  - Summary: Increases funding for subsidized housing programs

- **Rental Assistance Expansion** (`NYC`)
  - Status: Passed Committee
  - Last Action: 2025-01-10
  - Summary: Expands emergency rental assistance in Bronx and Brooklyn

- **Federal Housing Reform Bill** (`Federal`)
  - Status: In Discussion
  - Last Action: 2025-01-08
  - Summary: Proposes changes to Low-Income Housing Tax Credit program
```

______________________________________________________________________

## 2. GENERATE DRAFT SECTION (Policy Memo Writing)

### Purpose

Generate AI-assisted draft policy memo sections to accelerate policy document creation.

### When to Use

- **Frequency:** As needed (3-5 times per memo)
- **Time Required:** 5 minutes per section
- **Output:** Markdown text with drafted content
- **Integration:** Copy-paste into policy memo document

### Step-by-Step Guide

#### Step 1: Open Raycast

```
Keyboard: Cmd + Space
Result: Raycast search bar opens
```

#### Step 2: Search for Command

```
Type: "Generate Draft"
Result: "Generate Draft Section" command appears
Click: Select the command
```

#### Step 3: Enter Section Name

```
You see: "Section Name" text field

Common sections:
  - Executive Summary
  - Introduction
  - Key Findings
  - Analysis
  - Recommendations
  - Implementation Roadmap
  - Conclusion

Action: Type your section name
Example: "Key Findings"
```

#### Step 4: Write Your Prompt

```
You see: "Prompt" text area

Prompt structure:
1. What to write (e.g., "Summarize housing subsidy reform findings")
2. Context (e.g., "Based on NYC housing policy analysis 2024-2025")
3. Constraints (e.g., "Target: 500 words, professional tone")
4. Special instructions (e.g., "Focus on equity outcomes")

Example prompt:
"Summarize the key findings from our analysis of NYC housing subsidy programs.
 Focus on:
1. ROI implications of Public Equity Transfer Framework
2. Equity impact on low-income renters
3. Fiscal implications for NYC budget
Target: 400-500 words, professional tone, cite data where available."

Action: Type your detailed prompt
Note: More specific = better output
```

#### Step 5: Submit Request

```
Action: Click "Generate Draft" button
Status: Loading indicator with progress
Wait: 10-60 seconds depending on prompt complexity
```

#### Step 6: Review Generated Content

```
You see: Detail view with generated markdown

Content includes:
  - Formatted section heading
  - Generated paragraph text
  - Metadata (tokens used, model, timestamp)
  - Ready for copy-paste

Review for:
  ✓ Accuracy and relevance
  ✓ Proper structure and formatting
  ✓ Appropriate tone and language
  ☐ Any factual errors or gaps
  ☐ Missing citations or references

Note: AI output is DRAFT ONLY - human review required
```

#### Step 7: Copy to Memo Document

```
Action: Copy generated text (Cmd + C)
Open: Your policy memo document in Word/Google Docs/Markdown editor
Paste: Content into appropriate section
Edit: Refine wording, add citations, adjust as needed
```

#### Step 8: Manual Refinement

```
Tasks:
1. Verify all claims and statistics
2. Add missing citations
3. Adjust tone and language as needed
4. Integrate with surrounding sections
5. Check formatting consistency
6. Flag any questions for further research

Example edit:
Before (AI): "Housing subsidies help low-income residents."
After (You): "The Public Equity Transfer Framework, as described in our analysis,
             could increase owner wealth among low-income NYC households by
             average of $50,000 per unit over 20 years, addressing racial
             wealth gaps documented in Smith et al. (2024)."
```

#### Step 9: Generate Next Section (Repeat)

```
Raycast: Cmd + Space → "Generate Draft" → New section name → New prompt → Execute
Note: You can generate multiple sections in sequence
```

### Tips for Better Output

**DO:**

- ✓ Provide specific context (e.g., "based on NYC housing data 2024")
- ✓ Include constraints (word count, tone, format)
- ✓ Mention key points to cover
- ✓ Request structured output (bullet points, sections, etc.)
- ✓ Reference your research sources

**DON'T:**

- ✗ Use vague prompts ("write about housing")
- ✗ Expect perfectly accurate citations
- ✗ Skip human review of output
- ✗ Use AI text without refinement
- ✗ Trust numbers without verification

### Example Workflow

```
1. Generate "Executive Summary"
   Prompt: "Provide 200-word executive summary of NYC housing subsidy
           reform analysis, emphasizing ROI and equity outcomes"
   Output: 250 words of AI-generated summary

2. Edit manually
   - Verify statistics
   - Add missing citations
   - Adjust phrasing
   - Time: 10 minutes

3. Generate "Key Findings"
   Prompt: "Summarize 5 key findings from our analysis:
           1. Subsidy efficiency gaps
           2. Equity impacts
           3. Fiscal implications
           4. Recommendation framework
           5. Implementation timeline
           Use bullet points, 50-75 words per finding"
   Output: 350 words of structured findings

4. Edit and integrate
   - Match section formatting
   - Add references
   - Connect to recommendations
   - Time: 15 minutes

5. Repeat for Recommendations and Conclusion

Total time: ~2 hours for complete memo with AI assistance
(vs. 6+ hours manual writing)
```

### Troubleshooting

**Problem:** "Please specify a section name"\
**Solution:** Click back and enter section name (required field)

**Problem:** "Please provide a prompt for the draft"\
**Solution:** Click back and enter detailed prompt (required field)

**Problem:** Generated content is irrelevant or inaccurate\
**Solution:** Refine your prompt with more specific context and constraints

**Problem:** Output is too short or too long\
**Solution:** Add word count targets in prompt (e.g., "Target: 400-500 words")

**Problem:** Tone doesn't match your policy memo style\
**Solution:** Add tone instruction in prompt (e.g., "professional, academic tone")

______________________________________________________________________

## 3. ADD SOURCE (Research Management)

### Purpose

Manage your research source inventory with validated URLs and contextual notes.

### When to Use

- **Frequency:** Daily (as sources are discovered)
- **Time Required:** 2 minutes per source
- **Output:** Source added to Notion database
- **Integration:** Referenced in memos and policy documents

### Step-by-Step Guide

#### Step 1: Open Raycast

```
Keyboard: Cmd + Space
Result: Raycast search bar opens
```

#### Step 2: Search for Command

```
Type: "Add Source"
Result: "Add Source" command appears
Click: Select the command
```

#### Step 3: Enter Source Title

```
You see: "Source Title" text field

Examples:
  - "NYC Housing Preservation Database"
  - "Harvard Joint Center for Housing Studies 2024 Report"
  - "New York State Assembly Housing Committee Findings"
  - "HUD Section 8 Program Data Analysis"

Action: Type the source name
Note: Must not be empty
```

#### Step 4: Enter URL

```
You see: "URL" text field

Format required: https://example.com/resource

Examples:
  - https://data.cityofnewyork.us/housing-database
  - https://www.jchs.harvard.edu/research/publications
  - https://assembly.state.ny.us/mem/housing
  - https://www.hud.gov/program_offices/public_indian_housing

Action: Paste or type full URL
Note: URL is validated before submission
Error: Invalid URL format will be rejected
```

#### Step 5: Add Notes (Optional)

```
You see: "Notes" text area

What to include:
  - Key data points or findings
  - Time period covered (e.g., "2020-2024")
  - Relevance to your research
  - Any limitations or caveats
  - Usage rights or access requirements

Example:
"Comprehensive database of NYC subsidized housing units by type and location.
Includes occupancy rates, income distributions, and program outcomes.
Coverage: 2015-2024. Publicly available, updated quarterly.
Note: Some data may be subject to disclosure restrictions."

Action: Type your notes
Note: Optional field, can be empty
Length: Up to 500 characters recommended
```

#### Step 6: Submit

```
Action: Click "Add Source" button
Status: Processing confirmation
Wait: 2-3 seconds
Result: Success notification appears
```

#### Step 7: Verify in Notion

```
Action: Open Notion "Research Sources" table
Verify: Source appears with:
  - Title
  - URL (clickable link)
  - Notes
  - Date added (auto-populated)
  - Source ID (for referencing in memos)

Next steps:
  1. Tag source by policy area
  2. Set confidence level (High/Medium/Low)
  3. Add topic tags
  4. Note if primary or secondary source
```

### Source Categories

Tag your sources appropriately:

**By Type:**

- Government report
- Academic research
- Nonprofit analysis
- News article
- Database/dataset
- Policy document
- Advocacy publication

**By Policy Area:**

- Housing subsidies
- Tenant protection
- Homelessness
- Racial equity
- Fiscal impact
- Implementation

**By Jurisdiction:**

- NYC
- New York State
- Federal
- Comparative (other cities)

### Example Sources

```
✓ NYC Housing Preservation Database
  Type: Database
  Policy Area: Housing Subsidies, Implementation
  Jurisdiction: NYC
  Coverage: 2015-2024
  Status: ACTIVE (quarterly updates)

✓ Harvard Joint Center for Housing Studies Report
  Type: Academic Research
  Policy Area: Housing Subsidies, Fiscal Impact
  Jurisdiction: Comparative
  Year: 2024
  Status: REFERENCED

✓ NYC Comptroller Housing Report
  Type: Government Report
  Policy Area: Fiscal Impact, Racial Equity
  Jurisdiction: NYC
  Year: 2024
  Status: CITED in memo v2.0

✓ NYS Division of Housing Statistics
  Type: Government Database
  Policy Area: All
  Jurisdiction: New York State
  Coverage: 2010-2025
  Status: PRIMARY SOURCE
```

### Troubleshooting

**Problem:** "Please enter a source title"\
**Solution:** Go back and enter title (required field)

**Problem:** "Please enter a valid URL"\
**Solution:** Ensure URL format is correct (must start with https:// or http://)

**Problem:** "Invalid URL format"\
**Solution:** Check URL is complete and correct (copy-paste recommended)

**Problem:** Source doesn't appear in Notion after adding\
**Solution:** Refresh Notion page or check that Raycast preference has Notion API key

**Problem:** Duplicate sources in database\
**Solution:** Check URL before adding; use Notion search to find existing entries

______________________________________________________________________

## 4. WEEKLY AUTOMATION

### Automated Bill Sweep (Monday Morning)

```bash
# Run automated weekly bill sweep
bash scripts/sweep_bills_weekly.sh

# This script:
# 1. Runs Raycast sweep_bills command
# 2. Exports to CSV: data/bills/bills_sweep_YYYYMMDD.csv
# 3. Imports to Notion database
# 4. Generates summary report
# 5. Creates task for policy review

# Output:
# - CSV file with bills
# - Notion entries
# - Summary report in logs/
```

### Task Checklist (Weekly)

```
MONDAY:
  [ ] 9:00 AM - Run bill sweep: bash scripts/sweep_bills_weekly.sh
  [ ] Review results (10 min)
  [ ] Tag bills in Notion by priority (15 min)
  [ ] Create research task for relevant bills (5 min)

TUESDAY-WEDNESDAY:
  [ ] Add new sources as discovered (2 min/source)
  [ ] Review research findings (30 min)
  [ ] Plan policy memo sections

THURSDAY:
  [ ] Generate memo drafts using DraftSection (5 min/section)
  [ ] Manual review and editing (30 min/memo)
  [ ] Add citations and references (20 min)

FRIDAY:
  [ ] Final review and fact-checking (30 min)
  [ ] Prepare briefing memo for stakeholders (15 min)
  [ ] Archive memo in Git (5 min)
  [ ] Plan next week's research (10 min)

TOTAL TIME: ~3 hours/week for full research cycle
```

______________________________________________________________________

## 5. ERROR HANDLING & SUPPORT

### Common Issues

| Error                                  | Cause                      | Fix                             |
| -------------------------------------- | -------------------------- | ------------------------------- |
| "Assistant backend URL not configured" | Missing preference setting | Cmd + , → Set URL               |
| "Network error"                        | Backend down or wrong URL  | Check backend status            |
| "API error: 404"                       | Endpoint doesn't exist     | Verify endpoint path            |
| "Request timeout"                      | Slow backend response      | Increase timeout in preferences |
| "Invalid URL format"                   | Malformed URL in AddSource | Verify URL format               |

### Getting Help

**For technical issues:**

- Check RAYCAST_IMPLEMENTATION_REVIEW.md
- Verify Raycast extension is loaded
- Check backend API is running
- Review logs in ~/Documents/GitHub/HousingPolicyResearch/logs/

**For workflow questions:**

- Refer to relevant section in this runbook
- Review examples and use cases
- Check Space instructions for patterns

______________________________________________________________________

## 6. PERFORMANCE METRICS

Track your productivity gains:

```
Weekly Metrics:
  - Bills identified: __ bills
  - Sources added: __ sources
  - Memo sections generated: __ sections
  - Time to complete memo: __ hours
  - AI output usability: __%

Compare to baseline (manual process):
  - Previous time per memo: 6-8 hours
  - New time per memo: 2-3 hours
  - Time saved: 50-65% reduction
```

______________________________________________________________________

## 7. KEYBOARD SHORTCUTS

```
Raycast:
  Cmd + Space     Open Raycast
  Cmd + ,         Open Preferences
  Cmd + K         Clear search
  Cmd + [         Go back
  Cmd + ]         Go forward
  Esc             Close/cancel

Within Extension:
  Tab             Move to next field
  Shift + Tab     Move to previous field
  Enter           Submit form
  Esc             Go back
```

______________________________________________________________________

## Quick Links

- **Setup:** START_HERE.md
- **Technical Details:** RAYCAST_IMPLEMENTATION_REVIEW.md
- **Integration Plan:** SPACE_INTEGRATION_PLAN.md
- **Output Files:** ~/Documents/GitHub/HousingPolicyResearch/data/
- **Logs:** ~/Documents/GitHub/HousingPolicyResearch/logs/

______________________________________________________________________

**Need Help?** Refer to the relevant documentation file or review examples in this runbook.

**Status:** Production Ready\
**Last Updated:** December 26, 2025
