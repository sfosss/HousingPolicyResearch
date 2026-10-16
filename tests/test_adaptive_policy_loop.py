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
        "source_updated_at": "2026-10-16T12:00:00Z",
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
    item["source_updated_at"] = "2026-10-17T12:00:00Z"
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
    assert errors == ["Box inbox listing: Timeout"]


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
    assert errors == ["Box upload brief.md: HTTPError"]
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


@pytest.mark.parametrize("field", ["source_url", "url"])
@pytest.mark.parametrize(
    "query",
    [
        "access_token=synthetic-secret&id=12",
        "API-Key=synthetic-secret&id=12",
        "%61ccess%255ftoken=synthetic-secret&id=12",
        "X-Amz-Credential=synthetic-secret&"
        "X-Amz-Signature=synthetic-secret&id=12",
        "id=12;token=synthetic-secret&token=synthetic-secret",
        "download=https%3A%2F%2Fexample.com%2Fx%3F"
        "token%3Dsynthetic-secret%26id%3D12",
        "next=id%3D12%26api_key%3Dsynthetic-secret",
    ],
)
def test_secret_queries_are_removed_at_ingestion(item, field, query):
    item.pop("source_url")
    item[field] = f"https://example.com/report?{query}"
    record = module.normalize(item, TODAY)
    assert record is not None
    assert "synthetic-secret" not in json.dumps(asdict(record))
    assert "12" in record.canonical_url
    assert module.sanitize_source_url(record.source_url) == record.source_url


def test_public_query_and_opinion_fragment_survive_sanitization(item):
    item["source_url"] = (
        "https://example.com/opinion?id=12&q=rent&lang=en#holding"
    )
    record = module.normalize(item, TODAY)
    assert record.source_url.endswith("id=12&q=rent&lang=en#holding")
    assert (
        record.canonical_url
        == "https://example.com/opinion?id=12&lang=en&q=rent"
    )


def test_legacy_secret_copies_scrubbed_without_intake_or_review_loss(record):
    row = asdict(record)
    old_url = "https://example.com/report?id=12&token=synthetic-secret"
    row.update(
        source_url=old_url,
        canonical_url=old_url,
        proposed_redline="PROPOSED source: " + old_url,
        review_status="Accepted",
        reviewer="Counsel",
    )
    row["content_hash"] = module.digest(
        row["headline"].lower(), row["summary"].lower(), old_url
    )
    updated, added = module.upsert([row], [])
    assert added == 0
    assert "synthetic-secret" not in json.dumps(updated)
    assert updated[0]["event_id"] == row["event_id"]
    assert updated[0]["review_status"] == "Accepted"
    assert updated[0]["reviewer"] == "Counsel"
    incoming = replace(
        record,
        canonical_url=updated[0]["canonical_url"],
        source_url=updated[0]["source_url"],
        content_hash=updated[0]["content_hash"],
    )
    again, added = module.upsert(updated, [incoming])
    assert added == 0
    assert again[0]["review_status"] == "Accepted"


def test_secrets_absent_from_artifacts_stdout_and_box_bytes(
    sandbox, monkeypatch, item, capsys
):
    item["source_url"] = (
        "https://example.com/report?id=12&token=synthetic-secret"
    )
    monkeypatch.setenv("WEB_RESEARCH_JSON", json.dumps([item]))
    monkeypatch.setattr(module, "fetch_configured_sources", lambda: ([], []))
    mirrored = []

    def upload(paths):
        mirrored.extend(p.read_bytes() for p in paths)
        return []

    monkeypatch.setattr(module, "box_upload", upload)
    run_main(monkeypatch, "--box-push")
    assert "synthetic-secret" not in capsys.readouterr().out
    assert all(b"synthetic-secret" not in content for content in mirrored)
    assert all(
        b"synthetic-secret" not in path.read_bytes()
        for path in sandbox.rglob("*")
        if path.is_file()
    )


def test_feed_failure_diagnostics_do_not_repeat_redirect_secrets(
    sandbox, monkeypatch
):
    sources = sandbox / "sources.json"
    sources.write_text(
        json.dumps(
            {"sources": [{"type": "feed", "url": "https://example.com/rss"}]}
        )
    )
    monkeypatch.setattr(module, "SOURCES", sources)
    error = module.requests.HTTPError(
        "redirect https://example.com/?token=synthetic-secret"
    )
    monkeypatch.setattr(module, "fetch_feed", Mock(side_effect=error))
    _, errors = module.fetch_configured_sources()
    assert errors == ["Official feed 1: HTTPError"]
    assert "synthetic-secret" not in json.dumps(errors)


@pytest.mark.parametrize(
    "suffix",
    [
        "#access_token%3Dsynthetic-secret",
        "?access_key=synthetic-secret&id=12",
        "?ocp-apim-subscription-key=synthetic-secret&id=12",
        "?next=access_token%3Dsynthetic-secret",
    ],
)
def test_alternate_secret_url_forms(suffix):
    assert "synthetic-secret" not in module.sanitize_source_url(
        "https://example.com/report" + suffix
    )


def test_ambiguous_deep_encoding_is_not_retained():
    from urllib.parse import quote

    nested = "https://example.com/x?token=synthetic-secret"
    for _ in range(10):
        nested = quote(nested, safe="")
    safe = module.sanitize_source_url(
        "https://example.com/?download=" + nested
    )
    assert "synthetic-secret" not in safe


@pytest.mark.parametrize(
    "url",
    [
        "https://example.com/#/opinion?id=12&tab=text",
        "https://example.com/?q=rent%20%26%20income%3Dlow",
        "https://example.com/?return="
        "https%3A%2F%2Fexample.com%2Fx%3Fq%3Da%252Bb",
    ],
)
def test_public_url_semantics_are_preserved(url):
    from urllib.parse import parse_qsl, urlsplit

    safe = module.sanitize_source_url(url)
    assert parse_qsl(urlsplit(safe).query) == parse_qsl(urlsplit(url).query)
    assert urlsplit(safe).fragment == urlsplit(url).fragment


def test_encoded_url_copies_are_scrubbed(item):
    item["summary"] = (
        "Source https%3A%2F%2Fexample.com%2Fx%3Ftoken%3Dsynthetic-secret"
    )
    rows, _ = module.upsert([], [module.normalize(item, TODAY)])
    assert "synthetic-secret" not in json.dumps(rows)


@pytest.mark.parametrize(
    "headline",
    ["NYC tenants visit a courthouse", "NYC housing unsigned memorandum"],
)
def test_mapping_uses_term_boundaries(item, headline):
    item.update(
        headline=headline,
        summary="Tenant community visit",
        agency="",
        document_type="News",
    )
    rules = json.loads(module.POLICY_MAP.read_text())["rules"]
    result = module.score_and_map(module.normalize(item, TODAY), rules)
    assert result.section == "Needs mapping"
    assert result.proposed_redline == ""


def test_primary_promotion_to_critical_reopens_counsel_gate(record, sandbox):
    secondary = replace(
        record,
        primary_source="false",
        importance="High",
        importance_score="75",
    )
    rows, _ = module.upsert([], [secondary])
    rows[0].update(
        review_status="Accepted",
        reviewer="Policy reviewer",
        disposition_notes="Approved high item",
    )
    rows, added = module.upsert(rows, [record])
    assert added == 0
    assert rows[0]["importance"] == "Critical"
    assert rows[0]["review_status"] == "Needs Counsel Review"
    assert rows[0]["reviewer"] == rows[0]["disposition_notes"] == ""
    assert module.build_outputs(rows, TODAY, [], 0)["unresolved_critical"] == 1


def test_missing_jurisdiction_is_diagnosed(item):
    item.pop("jurisdiction")
    errors = []
    assert module.packet_items([item], "web", errors, "packet") == []
    assert "jurisdiction required" in errors[0]


@pytest.mark.parametrize(
    "headline,agency,jurisdiction,expected",
    [
        ("Affordable housing in Albany", "NYS Senate", "NY", False),
        ("Housing funding in Texas", "HUD", "Federal", False),
        ("NYCHA housing funding", "HUD", "Federal", True),
        ("Brooklyn rent rules", "NYS Senate", "NY", True),
        ("Housing rent rules", "HPD", "NY", True),
    ],
)
def test_state_and_federal_items_need_nyc_applicability(
    headline, agency, jurisdiction, expected
):
    assert (
        module.in_scope(
            dict(headline=headline, agency=agency, jurisdiction=jurisdiction)
        )
        is expected
    )


def test_explicit_nyc_applicability_requires_boolean():
    item = dict(
        headline="Federal rental housing funding",
        agency="HUD",
        jurisdiction="Federal",
    )
    assert module.in_scope(dict(item, applies_to_nyc=True))
    assert not module.in_scope(dict(item, applies_to_nyc="true"))


@pytest.mark.parametrize(
    "value,expected",
    [
        ("Fri, 16 Oct 2026 12:00:00 GMT", TODAY),
        ("Fri, 16 Oct 2026 12:00:00 EST", TODAY),
        ("Fri, 16 Oct 2026 12:00:00 +0000", TODAY),
        ("garbage", ""),
    ],
)
def test_rfc_named_zone_dates(value, expected):
    assert module.parse_date(value) == expected


def test_namespaced_rss_and_full_feed_are_processed(monkeypatch):
    response = Mock()
    response.content = b"""<rdf:RDF
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns="http://purl.org/rss/1.0/">
    <item><title>NYC housing one</title>
    <link>https://example.com/1</link></item>
    <item><title>NYC housing two</title>
    <link>https://example.com/2</link></item>
    </rdf:RDF>"""
    monkeypatch.setattr(module.requests, "get", lambda *a, **kw: response)
    items = module.fetch_feed(
        {"url": "https://example.com/rss", "name": "RSS", "max_items": 1}
    )
    assert len(items) == 2
    assert items[0]["headline"] == "NYC housing one"
    assert items[1]["source_url"] == "https://example.com/2"


def test_unrecognized_or_empty_feed_is_diagnosed(monkeypatch):
    response = Mock(content=b"<rss><channel/></rss>")
    monkeypatch.setattr(module.requests, "get", lambda *a, **kw: response)
    with pytest.raises(ValueError, match="no supported RSS/Atom"):
        module.fetch_feed({"url": "https://example.com/rss", "name": "RSS"})


def test_transient_feeds_retry_with_bounded_backoff(sandbox, monkeypatch):
    path = sandbox / "sources.json"
    path.write_text(
        json.dumps(
            {"sources": [{"url": "https://example.com/rss", "type": "feed"}]}
        )
    )
    monkeypatch.setattr(module, "SOURCES", path)
    fetch = Mock(
        side_effect=[
            module.requests.Timeout(),
            module.requests.ConnectionError(),
            [{"headline": "Recovered"}],
        ]
    )
    pause = Mock()
    monkeypatch.setattr(module, "fetch_feed", fetch)
    monkeypatch.setattr(module.time, "sleep", pause)
    items, errors = module.fetch_configured_sources()
    assert items == [{"headline": "Recovered"}]
    assert errors == []
    assert fetch.call_count == 3
    assert [c.args[0] for c in pause.call_args_list] == [1, 2]


def test_bom_csv_preserves_all_persisted_rows(sandbox, record, monkeypatch):
    import csv

    module.TRACKER.parent.mkdir(parents=True)
    with module.TRACKER.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=module.FIELDS)
        writer.writeheader()
        writer.writerow(asdict(record))
    monkeypatch.setattr(module, "fetch_configured_sources", lambda: ([], []))
    run_main(monkeypatch)
    assert module.read_tracker()[0]["event_id"] == record.event_id


@pytest.mark.parametrize(
    "csv_text",
    [
        "wrong,headers\na,b\n",
        "event_id,canonical_url,content_hash\nx,https://example.com\n",
        "event_id,event_id,canonical_url,content_hash\n"
        "x,x,https://example.com,h\n",
        "event_id,canonical_url,content_hash\n,https://example.com,h\n",
    ],
)
def test_malformed_tracker_is_preserved_with_diagnostic_artifacts(
    sandbox, monkeypatch, csv_text
):
    module.TRACKER.parent.mkdir(parents=True)
    module.TRACKER.write_text(csv_text)
    original = module.TRACKER.read_bytes()
    monkeypatch.setattr(module, "fetch_configured_sources", lambda: ([], []))
    assert run_main(monkeypatch) == 1
    assert module.TRACKER.read_bytes() == original
    assert "ledger preserved" in read_qa()["connector_errors"][0]
    assert not (
        module.POLICY_RESEARCH / "20261016" / "RUN_COMPLETE.json"
    ).exists()


def test_missing_prior_daily_outputs_are_recovered(
    sandbox, record, monkeypatch
):
    row = asdict(replace(record, date_ingested="2026-10-15"))
    module.write_csv(module.TRACKER, [row], module.FIELDS)
    monkeypatch.setattr(module, "fetch_configured_sources", lambda: ([], []))
    run_main(monkeypatch)
    recovered = module.POLICY_RESEARCH / "20261015"
    packet = json.loads((recovered / "SOURCE_PACKET.json").read_text())
    assert packet["items"][0]["event_id"] == record.event_id
    assert json.loads((recovered / "RUN_COMPLETE.json").read_text())[
        "recovered_from_ledger"
    ]
    qa = json.loads((recovered / "QA_REPORT.json").read_text())
    assert (
        "original connector diagnostics unavailable"
        in qa["connector_errors"][0]
    )
    assert (
        json.loads((module.EXPORTS / "policy-update-latest.json").read_text())[
            "qa"
        ]["date"]
        == TODAY
    )


@pytest.mark.parametrize(
    "updated", ["2026-10-15T12:00:00Z", "", "2026-10-16T12:00:00Z"]
)
def test_old_or_unversioned_revisions_do_not_overwrite_evidence(
    record, updated
):
    rows, _ = module.upsert([], [record])
    rows[0].update(review_status="Accepted", reviewer="Counsel")
    incoming = replace(
        record,
        summary="Older snapshot",
        content_hash="older",
        source_updated_at=updated,
    )
    errors = []
    rows, added = module.upsert(rows, [incoming], errors)
    assert added == 0
    assert rows[0]["summary"] == record.summary
    assert rows[0]["reviewer"] == "Counsel"
    assert "conflicting evidence" in errors[0]


def analyzed_packet(item):
    return dict(
        item,
        opinion_analysis={
            "tool": "analyzeOpinion",
            "status": "completed",
            "analysis_id": "analysis-123",
            "opinion_url": item["source_url"],
            "analyzed_at": "2026-10-16T12:00:00Z",
            "proposition": "Supported legal proposition",
            "scope_limit": "NYC circumstances only",
        },
    )


@pytest.mark.parametrize(
    "origin,claimed",
    [("midpage", "web"), ("box", "midpage"), ("web", "Midpage")],
)
def test_unanalyzed_midpage_items_do_not_enter_mapping(item, origin, claimed):
    errors = []
    assert (
        module.packet_items(
            [dict(item, source_type=claimed)], origin, errors, "packet"
        )
        == []
    )
    assert "analyzeOpinion" in errors[0]


def test_completed_opinion_metadata_is_preserved(item):
    packet = analyzed_packet(item)
    errors = []
    items = module.packet_items([packet], "midpage", errors, "packet")
    assert not errors
    record = module.normalize(items[0], TODAY)
    assert json.loads(record.opinion_analysis)["analysis_id"] == "analysis-123"
    assert record.source_type == "midpage"
    assert "Supported legal proposition" in record.summary
    assert "Scope limit: NYC circumstances only" in record.summary


def test_all_mapping_targets_exist_in_selected_local_bill():
    rules = json.loads(module.POLICY_MAP.read_text())["rules"]
    errors = []
    assert module.validated_rules(rules, errors) == rules
    assert errors == []
    invalid = dict(rules[0], section="Article made up")
    assert module.validated_rules([invalid], errors) == []
    assert "canonical target not found" in errors[0]


def workflow_job():
    import yaml

    return yaml.safe_load(
        (ROOT / ".github/workflows/adaptive-policy-loop.yml").read_text()
    )["jobs"]["research-update"]


@pytest.mark.parametrize("complete", [False, True])
def test_strict_failed_research_publishes_only_complete_artifacts(
    tmp_path, complete
):
    job = workflow_job()
    step = next(s for s in job["steps"] if s.get("id") == "research")
    today = module.datetime.now(module.timezone.utc).strftime("%Y%m%d")
    dated = tmp_path / "policy-research" / today
    dated.mkdir(parents=True)
    (dated / "RUN_COMPLETE.json").write_text("stale marker")
    output = tmp_path / "github-output"
    stub = "python() { "
    if complete:
        stub += (
            'mkdir -p "policy-research/$(date -u +%Y%m%d)"; '
            'echo completed > "policy-research/$(date -u +%Y%m%d)/'
            'RUN_COMPLETE.json"; '
        )
    stub += "return 1; }\n"
    result = subprocess.run(
        ["bash", "-e", "-c", stub + step["run"]],
        cwd=tmp_path,
        env={
            "PATH": os.environ["PATH"],
            "STRICT_MODE": "true",
            "GITHUB_OUTPUT": str(output),
        },
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert output.exists() is complete
    if complete:
        assert output.read_text() == "artifacts_ready=true\n"
    publish = next(
        s
        for s in job["steps"]
        if s.get("uses", "").startswith("peter-evans/create-pull-request")
    )
    assert "!cancelled()" in publish["if"]
    assert "outputs.artifacts_ready == 'true'" in publish["if"]
    assert "git push" not in "\n".join(s.get("run", "") for s in job["steps"])
    assert publish["with"]["branch"] == "${{ env.OUTPUT_BRANCH }}"


def test_alerts_update_one_persistent_issue_across_days(tmp_path):
    job = workflow_job()
    step = next(
        s for s in job["steps"] if "Critical items" in s.get("name", "")
    )
    log = tmp_path / "calls"
    stub = """date() { echo "$TEST_DAY"; }
    gh() {
      printf '%s\\n' "$*" >> "$CALL_LOG"
      if [ "$1" = "issue" ] && [ "$2" = "list" ]; then echo 123; fi
    }
    """
    for day in ("20261016", "20261017"):
        dated = tmp_path / "policy-research" / day
        dated.mkdir(parents=True)
        (dated / "CRITICAL_ALERT.md").write_text(
            "# Alerts\n- unresolved event\n"
        )
        subprocess.run(
            ["bash", "-e", "-c", stub + step["run"]],
            cwd=tmp_path,
            env={
                "PATH": os.environ["PATH"],
                "TEST_DAY": day,
                "CALL_LOG": str(log),
            },
            check=True,
        )
    calls = log.read_text()
    assert calls.count("issue edit 123 --body-file") == 2
    assert "issue create" not in calls
    assert "Critical PETF/TCAP policy review" in calls


def test_restoring_pending_pr_keeps_reviewed_ledger(tmp_path):
    # Exercise the actual git pathspecs rather than only inspecting the YAML.
    job = workflow_job()
    restore = next(
        s for s in job["steps"] if "Restore pending" in s.get("name", "")
    )
    assert "--state open" in restore["run"]
    assert '--head "$OUTPUT_BRANCH"' in restore["run"]
    paths = [
        "datasets/NYC_Housing_Subsidy_Policy_News_LIVE.csv",
        "indexes/POLICY_SOURCE_INDEX.csv",
        "indexes/POLICY_SOURCE_INDEX.md",
        "policy-research/20261016/QA_REPORT.json",
        "exports-for-chatgpt/policy-update-latest.json",
    ]
    repo = tmp_path / "repo"
    repo.mkdir()

    def git(*args):
        subprocess.run(
            ["git", "-C", str(repo), *args], check=True, capture_output=True
        )

    git("init")
    for name in paths:
        path = repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("reviewed")
    git("add", ".")
    git(
        "-c",
        "user.name=Test",
        "-c",
        "user.email=test@example.com",
        "commit",
        "-m",
        "reviewed outputs",
    )
    for name in paths:
        (repo / name).write_text("old default snapshot")
    git(
        "restore",
        "--source=HEAD",
        "--worktree",
        "--",
        paths[0],
        paths[1],
        paths[2],
        ":(glob)policy-research/[0-9]*/**",
        "exports-for-chatgpt",
    )
    assert all((repo / name).read_text() == "reviewed" for name in paths)


def test_strict_critical_intake_is_persisted_and_ready_for_review(
    sandbox, monkeypatch, item
):
    monkeypatch.setenv("WEB_RESEARCH_JSON", json.dumps([item]))
    monkeypatch.setattr(module, "fetch_configured_sources", lambda: ([], []))
    assert run_main(monkeypatch, "--strict") == 1
    assert module.read_tracker()[0]["importance"] == "Critical"
    assert read_qa()["unresolved_critical"] == 1
    assert (
        module.POLICY_RESEARCH / "20261016" / "RUN_COMPLETE.json"
    ).is_file()
    assert_exports_match(read_qa())


def test_box_redirect_failure_does_not_expose_query_credentials(
    sandbox, monkeypatch
):
    monkeypatch.setenv("BOX_ACCESS_TOKEN", "test-token")
    monkeypatch.setenv("BOX_INBOX_FOLDER_ID", "123")
    listing = Mock()
    listing.json.return_value = {
        "entries": [{"id": "456", "name": "packet.json", "type": "file"}],
        "total_count": 1,
    }
    error = module.requests.HTTPError(
        "redirect https://example.com/?token=synthetic-secret"
    )
    monkeypatch.setattr(
        module.requests, "get", Mock(side_effect=[listing, error])
    )
    _, errors = module.box_pull()
    assert errors == ["Box file packet.json: HTTPError"]
    assert "synthetic-secret" not in json.dumps(errors)
