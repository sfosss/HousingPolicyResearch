import importlib.util
import json
import os
import subprocess
import sys
from dataclasses import asdict, replace
from pathlib import Path
from unittest.mock import Mock

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "adaptive_policy_loop.py"
spec = importlib.util.spec_from_file_location("adaptive_policy_loop", SCRIPT)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
TODAY = "2026-10-16"


@pytest.fixture
def item():
    return {
        "headline": "NYCHA public housing modernization final rule",
        "summary": "NYCHA final rule for public housing modernization.",
        "source_url": "https://www.hud.gov/example?utm_campaign=test",
        "source_name": "HUD",
        "date_published": TODAY,
        "jurisdiction": "Federal",
        "agency": "HUD",
        "document_type": "Final Rule",
        "primary_source": True,
    }


@pytest.fixture
def record(item):
    rules = json.loads(module.POLICY_MAP.read_text())["rules"]
    return module.score_and_map(module.normalize(item, TODAY), rules)


@pytest.fixture
def sandbox(tmp_path, monkeypatch):
    for name, path in {
        "TRACKER": "datasets/ledger.csv",
        "CONNECTORS": "intake/connectors",
        "INDEX_CSV": "indexes/POLICY_SOURCE_INDEX.csv",
        "INDEX_MD": "indexes/POLICY_SOURCE_INDEX.md",
        "EXPORTS": "exports",
        "POLICY_RESEARCH": "policy-research",
    }.items():
        monkeypatch.setattr(module, name, tmp_path / path)
    for name in (
        "WEB_RESEARCH_JSON",
        "MIDPAGE_RESEARCH_JSON",
        "BOX_RESEARCH_JSON",
        "BOX_ACCESS_TOKEN",
        "BOX_INBOX_FOLDER_ID",
        "BOX_OUTPUT_FOLDER_ID",
    ):
        monkeypatch.delenv(name, raising=False)
    return tmp_path


def run_main(monkeypatch, *flags):
    monkeypatch.setattr(sys, "argv", [str(SCRIPT), "--date", TODAY, *flags])
    return module.main()


def read_qa():
    dated = module.POLICY_RESEARCH / TODAY.replace("-", "")
    return json.loads((dated / "QA_REPORT.json").read_text())


def assert_exports_match(qa):
    for name in ("policy-update-latest.json", f"policy-update-{TODAY}.json"):
        assert json.loads((module.EXPORTS / name).read_text())["qa"] == qa


def test_canonicalize_url_removes_tracking_and_fragment():
    url = "HTTPS://Example.COM/report/?b=2&utm_source=x&a=1#section"
    assert module.canonicalize_url(url) == "https://example.com/report?a=1&b=2"


def test_stable_normalization_and_required_review_gate(record):
    assert record.policy == "PETF Master Bill"
    marker = "[PROPOSED—HUMAN REVIEW REQUIRED]"
    assert record.proposed_redline.startswith(marker)
    assert record.importance == "Critical"
    assert record.review_status == "Needs Counsel Review"


def test_unchanged_upsert_preserves_review_and_ingestion_date(record):
    rows, added = module.upsert([], [record])
    assert added == 1
    rows[0].update(review_status="Accepted", reviewer="Counsel")
    unchanged = replace(record, date_ingested="2026-10-17")
    updated, added_again = module.upsert(rows, [unchanged])
    assert added_again == 0
    assert updated == rows
    assert updated[0]["date_ingested"] == TODAY


@pytest.mark.parametrize("changed", ["date_published", "headline", "summary"])
def test_persisted_url_dedup_keeps_identity(item, record, changed):
    rows, _ = module.upsert([], [record])
    rows[0].update(review_status="Accepted", reviewer="Counsel")
    item[changed] = "2026-10-15" if changed == "date_published" else "Revised"
    incoming = module.normalize(item, "2026-10-17")
    assert incoming.event_id != record.event_id or changed == "summary"
    updated, added = module.upsert(rows, [incoming])
    assert added == 0
    assert len(updated) == 1
    assert updated[0]["event_id"] == record.event_id
    if changed == "date_published":
        assert updated[0]["review_status"] == "Accepted"
        assert updated[0]["date_published"] == "2026-10-15"
    else:
        assert updated[0]["review_status"] == "Proposed"
        assert updated[0]["reviewer"] == ""


def test_persisted_hash_dedup_and_official_provenance(record):
    secondary = replace(record, primary_source="false", source_name="News")
    rows, _ = module.upsert([], [secondary])
    rows[0].update(review_status="Accepted", reviewer="Counsel")
    incoming = replace(record, event_id="different-provider-id")
    rows[0]["canonical_url"] = "https://example.com/legacy-link"
    updated, added = module.upsert(rows, [incoming])
    assert added == 0
    assert len(updated) == 1
    assert updated[0]["source_name"] == "HUD"
    assert updated[0]["primary_source"] == "true"
    assert updated[0]["reviewer"] == "Counsel"


def test_same_batch_dedup(record):
    duplicate = replace(record, event_id="another-id")
    rows, added = module.upsert([], [record, duplicate])
    assert len(rows) == added == 1


@pytest.mark.parametrize("published", ["", "unknown", "2026-99-99"])
def test_undated_items_keep_stable_identity(item, published):
    item["date_published"] = published
    first = module.normalize(item, TODAY)
    second = module.normalize(item, "2026-10-17")
    assert first.date_published == second.date_published == ""
    assert first.event_id == second.event_id


def test_pending_critical_persists_in_next_day_qa(sandbox, record):
    row = asdict(record)
    next_day = "2026-10-17"
    qa = module.build_outputs([row], next_day, [], 0)
    assert qa["records_seen_today"] == 0
    assert qa["unresolved_critical"] == 1
    assert not qa["passed"]
    alert = module.POLICY_RESEARCH / "20261017" / "CRITICAL_ALERT.md"
    assert record.headline in alert.read_text()


def test_named_acceptance_resolves_critical_qa(sandbox, record):
    row = asdict(record)
    row.update(review_status="Accepted", reviewer="Counsel")
    qa = module.build_outputs([row], TODAY, [], 0)
    assert qa["unresolved_critical"] == 0
    assert qa["passed"]
    row["reviewer"] = ""
    qa = module.build_outputs([row], TODAY, [], 0)
    assert qa["unresolved_critical"] == 1
    assert not qa["passed"]


def test_unmapped_items_fail_qa(sandbox):
    row = asdict(module.Record(canonical_url="https://example.com/"))
    row["date_ingested"] = TODAY
    qa = module.build_outputs([row], TODAY, [], 1)
    assert not qa["checks"]["all_daily_records_mapped"]
    assert not qa["checks"]["all_daily_records_have_redlines"]
    assert not qa["passed"]


@pytest.mark.parametrize("jurisdiction", ["nyc", "new york city", "federal"])
def test_lowercase_jurisdiction_passes_qa(sandbox, record, jurisdiction):
    row = asdict(record)
    row.update(jurisdiction=jurisdiction, importance="High")
    assert module.build_outputs([row], TODAY, [], 1)["passed"]


@pytest.mark.parametrize(
    "url",
    [
        "not-a-url",
        "ftp://example.com/evidence",
        "https:///evidence",
        "https://",
        "https://[broken",
        "https://bad host/evidence",
        "https://example.com:bad/evidence",
        "https://user:password@example.com/evidence",
        "https://-invalid.example/evidence",
    ],
)
def test_invalid_urls_rejected_and_fail_persisted_qa(sandbox, item, url):
    item["source_url"] = url
    assert module.normalize(item, TODAY) is None
    row = asdict(module.Record(canonical_url=url))
    qa = module.build_outputs([row], TODAY, [], 0)
    assert not qa["checks"]["all_urls_present"]
    assert not qa["passed"]


@pytest.mark.parametrize(
    "url",
    [
        "https://example.com/report",
        "http://localhost:8080/x",
        "https://[::1]/",
    ],
)
def test_http_urls_accepted(url):
    assert module.valid_source_url(url)


@pytest.mark.parametrize(
    "headline", ["Current state budget", "Parental leave"]
)
def test_scope_terms_do_not_match_substrings(headline):
    assert not module.in_scope({"headline": headline, "jurisdiction": "NY"})


def test_scope_phrase_boundaries():
    assert module.in_scope(
        {"headline": "NYC rent budget", "jurisdiction": "NY"}
    )


@pytest.mark.parametrize("strict, expected", [(False, 0), (True, 1)])
def test_malformed_packets_continue_with_valid_sources(
    sandbox, monkeypatch, item, strict, expected
):
    folder = module.CONNECTORS / "web"
    folder.mkdir(parents=True)
    (folder / "broken.json").write_text("{broken")
    (folder / "valid.json").write_text(json.dumps([item]))
    monkeypatch.setenv("MIDPAGE_RESEARCH_JSON", "{broken")
    monkeypatch.setattr(module, "fetch_configured_sources", lambda: ([], []))
    flags = ["--strict"] if strict else []
    assert run_main(monkeypatch, *flags) == expected
    qa = read_qa()
    assert qa["records_seen_today"] == 1
    assert len(qa["connector_errors"]) == 2
    assert not qa["passed"]
    assert_exports_match(qa)
    assert len(module.read_tracker()) == 1


@pytest.mark.parametrize(
    "payload", [None, 42, {}, {"items": None}, {"items": {}}]
)
def test_bad_packet_shapes_are_reported(payload):
    errors = []
    assert module.packet_items(payload, "web", errors, "packet") == []
    assert len(errors) == 1


def test_invalid_packet_items_are_reported_without_losing_siblings(item):
    errors = []
    payload = [None, {}, {"headline": "One", "source_url": "not-a-url"}, item]
    result = module.packet_items(payload, "web", errors, "packet")
    assert len(result) == 1
    assert len(errors) == 3


def test_string_false_is_not_primary(item):
    item["primary_source"] = "false"
    assert module.normalize(item, TODAY).primary_source == "false"


def test_box_listing_failure_is_reported(sandbox, monkeypatch):
    monkeypatch.setenv("BOX_ACCESS_TOKEN", "test-token")
    monkeypatch.setenv("BOX_INBOX_FOLDER_ID", "123")
    monkeypatch.setattr(
        module.requests,
        "get",
        Mock(side_effect=module.requests.Timeout("timeout")),
    )
    items, errors = module.box_pull()
    assert items == []
    assert errors == ["Box inbox listing: timeout"]


@pytest.mark.parametrize("conflict_list", [False, True])
def test_box_conflicts_upload_a_new_version(
    sandbox, monkeypatch, conflict_list
):
    monkeypatch.setenv("BOX_ACCESS_TOKEN", "test-token")
    monkeypatch.setenv("BOX_OUTPUT_FOLDER_ID", "123")
    path = sandbox / "DAILY_BRIEF.md"
    path.write_bytes(b"latest brief")
    conflict = {"id": "456", "name": path.name, "type": "file"}
    conflicts = [conflict] if conflict_list else conflict
    response = Mock(status_code=409)
    response.json.return_value = {"context_info": {"conflicts": conflicts}}
    sent = []

    def post(url, **kwargs):
        sent.append((url, kwargs["files"]["file"].read()))
        return response if len(sent) == 1 else Mock(status_code=201)

    monkeypatch.setattr(module.requests, "post", post)
    assert module.box_upload([path]) == []
    assert sent == [
        ("https://upload.box.com/api/2.0/files/content", b"latest brief"),
        ("https://upload.box.com/api/2.0/files/456/content", b"latest brief"),
    ]


def test_box_version_failure_records_error_and_continues(sandbox, monkeypatch):
    monkeypatch.setenv("BOX_ACCESS_TOKEN", "test-token")
    monkeypatch.setenv("BOX_OUTPUT_FOLDER_ID", "123")
    first = sandbox / "brief.md"
    second = sandbox / "packet.json"
    first.write_text("brief")
    second.write_text("{}")
    conflict = Mock(status_code=409)
    conflict.json.return_value = {
        "context_info": {
            "conflicts": {"id": "456", "name": first.name, "type": "file"}
        }
    }
    failed_version = Mock(status_code=403)
    failed_version.raise_for_status.side_effect = module.requests.HTTPError(
        "version denied"
    )
    post = Mock(side_effect=[conflict, failed_version, Mock(status_code=201)])
    monkeypatch.setattr(module.requests, "post", post)
    errors = module.box_upload([first, second])
    assert errors == ["Box upload brief.md: version denied"]
    assert post.call_count == 3


@pytest.mark.parametrize("qa_upload_fails", [False, True])
def test_box_failures_finalize_local_exports_and_upload_qa_last(
    sandbox, monkeypatch, qa_upload_fails
):
    monkeypatch.setattr(module, "fetch_configured_sources", lambda: ([], []))
    batches = []

    def upload(paths):
        batches.append([p.name for p in paths])
        if len(batches) == 1:
            assert "QA_REPORT.json" not in batches[0]
            return ["Box tracker upload failed"]
        assert read_qa()["connector_errors"] == ["Box tracker upload failed"]
        assert_exports_match(read_qa())
        return ["Box QA upload failed"] if qa_upload_fails else []

    monkeypatch.setattr(module, "box_upload", upload)
    assert run_main(monkeypatch, "--box-push", "--strict") == 1
    assert batches[-1] == ["QA_REPORT.json"]
    qa = read_qa()
    assert not qa["passed"]
    assert len(qa["connector_errors"]) == 1 + qa_upload_fails
    assert_exports_match(qa)


def test_successful_box_upload_preserves_success(sandbox, monkeypatch):
    monkeypatch.setattr(module, "fetch_configured_sources", lambda: ([], []))
    monkeypatch.setattr(module, "box_upload", lambda paths: [])
    assert run_main(monkeypatch, "--box-push", "--strict") == 0
    assert read_qa()["passed"]
    assert_exports_match(read_qa())


def test_rss_text_nodes_are_not_discarded(monkeypatch):
    response = Mock()
    response.content = b"""<rss><channel><item><title>NYC housing</title>
    <link>https://example.com/report</link>
    <description>NYCHA rent</description>
    <pubDate>Fri, 16 Oct 2026 12:00:00 +0000</pubDate>
    </item></channel></rss>"""
    monkeypatch.setattr(module.requests, "get", lambda *a, **kw: response)
    source = {"name": "Official", "url": "https://example.com/rss"}
    result = module.fetch_feed(source)
    assert result[0]["headline"] == "NYC housing"
    assert result[0]["source_url"] == "https://example.com/report"
    assert result[0]["summary"] == "NYCHA rent"


def test_csv_failure_leaves_previous_ledger_intact(sandbox, monkeypatch):
    path = sandbox / "ledger.csv"
    path.write_text("original ledger")

    def fail_replace(*args):
        raise OSError("interrupted write")

    monkeypatch.setattr(module.os, "replace", fail_replace)
    with pytest.raises(OSError, match="interrupted write"):
        module.write_csv(path, [{"event_id": "one"}], ["event_id"])
    assert path.read_text() == "original ledger"
    assert list(sandbox.iterdir()) == [path]


def test_generated_indexes_preserve_curated_catalog(sandbox, record):
    index_dir = module.INDEX_CSV.parent
    index_dir.mkdir(parents=True)
    for name in ("SOURCE_INDEX.csv", "SOURCE_INDEX.md"):
        (index_dir / name).write_text("curated catalog")
    module.write_indexes([asdict(record)])
    for name in ("SOURCE_INDEX.csv", "SOURCE_INDEX.md"):
        assert (index_dir / name).read_text() == "curated catalog"
    assert record.headline in module.INDEX_MD.read_text()


@pytest.mark.parametrize("strict", ["true", "false", ""])
def test_workflow_passes_strict_flag_from_environment(strict):
    import yaml

    workflow = yaml.safe_load(
        (ROOT / ".github/workflows/adaptive-policy-loop.yml").read_text()
    )
    job = workflow["jobs"]["research-update"]
    assert "vars.POLICY_LOOP_STRICT" in job["env"]["STRICT_MODE"]
    step = next(s for s in job["steps"] if s.get("id") == "research")
    script = 'python() { printf "%s\\n" "$@"; }\n' + step["run"]
    result = subprocess.run(
        ["bash", "-e", "-c", script],
        env={"PATH": os.environ["PATH"], "STRICT_MODE": strict},
        check=True,
        capture_output=True,
        text=True,
    )
    assert ("--strict" in result.stdout) == (strict == "true")
    alert = next(
        s for s in job["steps"] if "Critical items" in s.get("name", "")
    )
    assert "steps.research.outcome == 'failure'" in alert["if"]
