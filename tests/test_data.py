"""Fixture integrity, reproducible generation, and independent rule boundaries."""

import hashlib
import json
import sqlite3
from contextlib import closing

import pytest

from common.claims import calculate_payout, route_claim
from common.data import (
    DATA,
    claims_connection,
    data_path,
    load_fraud_rules,
    load_jsonl,
    load_submission,
    lookup_claim,
)
from scripts.build_data import build_data


def test_committed_manifest_matches_every_fixture():
    manifest = json.loads((DATA / "manifest.json").read_text("utf-8"))
    assert manifest["counts"] == {"claims": 500, "documents": 30, "emails": 20, "submissions": 60}
    for relative, digest in manifest["sha256"].items():
        assert hashlib.sha256(data_path(relative).read_bytes()).hexdigest() == digest, relative


def test_database_shape_foreign_keys_and_read_only_access():
    with claims_connection() as connection:
        assert connection.execute("SELECT COUNT(*) FROM claims").fetchone()[0] == 500
        assert connection.execute("SELECT COUNT(*) FROM customers").fetchone()[0] == 100
        assert not connection.execute("PRAGMA foreign_key_check").fetchall()
        assert (
            connection.execute("SELECT DISTINCT status FROM payments").fetchall()[0][0]
            == "proposed"
        )
        with pytest.raises(sqlite3.OperationalError):
            connection.execute("DELETE FROM claims")
    with pytest.raises(sqlite3.ProgrammingError):
        connection.execute("SELECT 1")


def test_dataset_has_missing_duplicate_and_review_cases():
    rows = [load_submission(number) for number in range(1, 61)]
    assert {row["claim_type"] for row in rows} == {"water", "theft", "fire", "storm", "liability"}
    assert any(row["loss_date"] is None for row in rows)
    assert any(row["duplicate_of"] for row in rows)
    assert any(row["fraud_indicators"] for row in rows)
    assert load_fraud_rules()["synthetic"] is True
    assert lookup_claim("CLM-0001")["customer_id"] == "CUS-0001"
    with pytest.raises(ValueError):
        lookup_claim("CLM-0001' OR 1=1")


@pytest.mark.parametrize("relative", ["../.env.example", "../../outside", "/outside"])
def test_dataset_traversal_is_rejected(relative):
    with pytest.raises((ValueError, FileNotFoundError)):
        data_path(relative)


def test_generation_is_repeatable_and_matches_logical_database(tmp_path):
    first = build_data(tmp_path / "first")
    second = build_data(tmp_path / "second")
    assert first == second
    committed = json.loads((DATA / "manifest.json").read_text("utf-8"))
    for relative, digest in first["sha256"].items():
        if relative != "claims.db":
            assert digest == committed["sha256"][relative], relative
        if not relative.endswith((".db", ".pdf")):
            assert b"\r\n" not in (tmp_path / "first" / relative).read_bytes()
    # SQLite's writer-version header can differ across Python builds; compare records too.
    with (
        closing(sqlite3.connect(tmp_path / "first/claims.db")) as generated,
        claims_connection() as reference,
    ):
        for table in (
            "customers",
            "policies",
            "claims",
            "claim_documents",
            "payments",
            "adjusters",
        ):
            expected = [
                tuple(row) for row in reference.execute(f"SELECT * FROM {table} ORDER BY 1")
            ]
            actual = generated.execute(f"SELECT * FROM {table} ORDER BY 1").fetchall()
            assert actual == expected


@pytest.mark.parametrize(
    "amount,limit,deductible,result",
    [
        (50_000, 100_000, 75_000, 0),
        (500_000, 200_000, 50_000, 200_000),
        (125_000, 1_000_000, 100_000, 25_000),
    ],
)
def test_payout_independent_examples(amount, limit, deductible, result):
    assert calculate_payout(amount, limit, deductible) == result


@pytest.mark.parametrize("amount", [-1, True, 1.5])
def test_payout_requires_integer_cents(amount):
    with pytest.raises(ValueError):
        calculate_payout(amount, 100_000, 0)


def test_routing_boundaries_and_committed_goldens():
    base = load_submission(1)
    assert route_claim({**base, "amount_cents": 100_000}) == "fast_track"
    assert route_claim({**base, "amount_cents": 100_001}) == "standard"
    assert route_claim({**base, "amount_cents": 500_000}) == "standard"
    assert route_claim({**base, "amount_cents": 500_001}) == "specialist"
    assert route_claim({**base, "amount_cents": True}) == "invalid"
    for case in load_jsonl("eval/routing.jsonl"):
        assert route_claim(case["input"]) == case["expected_route"]
