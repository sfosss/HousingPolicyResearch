# Generative Output Archive

This folder is the canonical location for version-controlled generative outputs (ChatGPT or Codex transcripts, draft narratives, evaluations).

## Folder Structure

- One markdown file per output following `YYYY-MM-DD_topic-model.md`.
- Optional subfolders can group large projects (e.g., `policy-briefs/`, `evaluations/`).
- Attach related assets (CSV exports, screenshots) in the same folder with descriptive names.

## Metadata Template

Start each file with metadata so provenance and review status are clear:

```markdown
---
issue: "#<issue-number>"
model: "gpt-4o"
source: "ChatGPT transcript"
reviewer: "Name or GitHub handle"
status: "draft" # or "final"
updated: "YYYY-MM-DD"
---
```

Follow the metadata with:

1. **Summary** – What the output covers and the decisions it supports.
2. **Prompt/Inputs** – Key prompts or parameters used to generate the text.
3. **Citations** – Links to GitHub issues, Notion pages, or Zotero items.
4. **Risks/Notes** – Any data sensitivity, redactions, or follow-up actions required.

## Version Control Steps

1. Sanitize the text to remove API keys, PII, or internal URLs not meant for publication.
2. Save the file under this directory using the naming convention above.
3. Add a short commit message referencing the related issue (e.g., `Archive ChatGPT transcript for issue #3`).
4. If importing historic outputs, note the original storage location and date migrated in the summary section.
5. Reference the archived file from the related documentation or issue comment to preserve traceability.
