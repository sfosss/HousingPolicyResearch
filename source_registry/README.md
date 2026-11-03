# Housing Policy Source Registry v1.0

**Status:** Additive foundation; not a completed source migration. Existing research inventories remain authoritative for their original content until reviewed and reconciled.

## Files
- `sources.csv`: UTF-8 canonical source records; initially header-only to avoid inventing bibliographic facts.
- `taxonomy.json`: controlled vocabularies.
- `validate.py`: dependency-free structural and vocabulary validation.
- `legacy-inventory.md`: pre-existing source locations and migration policy.

## Data rules
Use stable IDs `HPR-SRC-000001` onward. Never reuse or renumber an ID. Dates use YYYY-MM-DD. Multi-select values are separated with `|`. Preserve the original source and exact version; record supersession as a link, never an overwrite. Source verification and individual claim verification are distinct. `CONTENT VERIFIED` requires a reviewer, review date, and source-specific citation locator for downstream drafting.

Required on each populated row: source_id, title, source_type, issuing_entity, jurisdiction, access_date, authority_level, verification_status, research_theme, policy_module, evidence_summary, limitations, fiscal_relevance, last_reviewed. Unknown values must be investigated, not guessed. Do not commit personal case records or restricted materials.

## Validation
```sh
python source_registry/validate.py
```

## Migration workflow
1. Inventory legacy references without moving or deleting anything.
2. Extract bibliographic metadata; compare titles, canonical URLs, versions, and file hashes where practical.
3. Assign IDs only after deduplication and provenance review.
4. Mark each record UNREVIEWED until source-level validation.
5. Create separate claim, legislative, fiscal, and proposal relation tables in a subsequent reviewed change. Do not infer legal effect from bill titles or secondary reporting.

Generated documentation prepared with AI assistance on 2026-10-26; human review required before treating it as an approved research baseline.
