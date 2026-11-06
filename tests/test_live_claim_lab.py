"""Deterministic teaching contracts; real inference is an explicit optional experiment."""

import pytest

from scripts.live_claim_lab import run


def test_provider_lab_has_offline_extraction_tools_and_memory():
    result = run()
    assert result["extract"]["amount_cents"] == 125000
    assert result["tools"]["tool_names"] == ["lookup_policy"]
    assert result["memory"] == {"answer": "Your contact preference is sms.", "messages": 4}


@pytest.mark.live
def test_optional_live_extraction_has_a_valid_schema():
    result = run("extract", live=True)
    assert result["extract"]["claim_type"] == "water"
    assert result["extract"]["amount_cents"] == 125000
