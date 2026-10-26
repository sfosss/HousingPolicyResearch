"""Validate the additive housing-policy source registry (Python standard library only)."""
import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REQUIRED = ("source_id", "title", "source_type", "issuing_entity", "jurisdiction",
            "access_date", "authority_level", "verification_status", "research_theme",
            "policy_module", "evidence_summary", "limitations", "fiscal_relevance",
            "last_reviewed")
MULTI = ("jurisdiction", "research_theme", "policy_module")
DATES = ("publication_date", "effective_date", "access_date", "verified_on", "last_reviewed")

def validate(csv_path=ROOT / "sources.csv", taxonomy_path=ROOT / "taxonomy.json"):
    taxonomy = json.loads(Path(taxonomy_path).read_text(encoding="utf-8"))
    errors = []
    with Path(csv_path).open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        columns = reader.fieldnames or []
        missing = sorted(set(REQUIRED) - set(columns))
        if missing:
            return ["Missing columns: " + ", ".join(missing)]
        seen = set()
        for line, row in enumerate(reader, 2):
            for field in REQUIRED:
                if not (row.get(field) or "").strip():
                    errors.append(f"row {line}: missing {field}")
            identifier = (row.get("source_id") or "").strip()
            if identifier and not re.fullmatch(r"HPR-SRC-\d{6}", identifier):
                errors.append(f"row {line}: invalid source_id")
            if identifier in seen:
                errors.append(f"row {line}: duplicate source_id {identifier}")
            seen.add(identifier)
            for field in DATES:
                value = (row.get(field) or "").strip()
                if value:
                    try:
                        if date.fromisoformat(value).isoformat() != value:
                            raise ValueError("noncanonical date")
                    except ValueError:
                        errors.append(f"row {line}: invalid ISO date {field}")
            for field in taxonomy:
                if field not in row:
                    continue
                value = (row.get(field) or "").strip()
                values = [v.strip() for v in value.split("|")] if field in MULTI else [value]
                for item in values:
                    if item and item not in taxonomy[field]:
                        errors.append(f"row {line}: unknown {field}: {item}")
            if row.get(None):
                errors.append(f"row {line}: extra columns")
    return errors

if __name__ == "__main__":
    failures = validate()
    if failures:
        print("\n".join(failures), file=sys.stderr)
        sys.exit(1)
    print("Source registry validation passed")
