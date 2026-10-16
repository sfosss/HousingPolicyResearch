import importlib.util
import json
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "adaptive_policy_loop.py"
spec = importlib.util.spec_from_file_location("adaptive_policy_loop", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_canonicalize_url_removes_tracking_and_fragment():
    url = "HTTPS://Example.COM/report/?b=2&utm_source=x&a=1#section"
    assert module.canonicalize_url(url) == "https://example.com/report?a=1&b=2"


def test_stable_normalization_and_required_review_gate():
    item = {
        "headline": "NYCHA public housing modernization final rule",
        "summary": "HUD and NYCHA issue a final rule affecting public housing modernization.",
        "source_url": "https://www.hud.gov/example?utm_campaign=test",
        "source_name": "HUD",
        "date_published": "2026-10-16",
        "jurisdiction": "Federal",
        "agency": "HUD",
        "document_type": "Final Rule",
        "primary_source": True,
    }
    record = module.normalize(item, "2026-10-16")
    rules = json.loads((Path(__file__).resolve().parents[1] / "config" / "policy_map.json").read_text())["rules"]
    mapped = module.score_and_map(record, rules)
    assert mapped.policy == "PETF Master Bill"
    assert mapped.proposed_redline.startswith("[PROPOSED—HUMAN REVIEW REQUIRED]")
    if mapped.importance == "Critical":
        assert mapped.review_status == "Needs Counsel Review"


def test_upsert_is_idempotent_and_preserves_review():
    record = module.Record(event_id="abc", headline="One", content_hash="hash", review_status="Proposed")
    rows, added = module.upsert([], [record])
    assert added == 1
    rows[0]["review_status"] = "Accepted"
    rows[0]["reviewer"] = "Counsel"
    replacement = module.Record(event_id="abc", headline="One revised", content_hash="new-hash", review_status="Proposed")
    updated, added_again = module.upsert(rows, [replacement])
    assert added_again == 0
    assert updated[0]["review_status"] == "Accepted"
    assert updated[0]["reviewer"] == "Counsel"
