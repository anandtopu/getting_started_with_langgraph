"""Independent end-to-end contracts for the progressively composed claim workflow."""

import pytest
from langgraph.types import Command

from common.copilot import v03, v04, v05, v06, v07
from common.data import load_submission


@pytest.mark.parametrize("module", [v03, v04, v05, v06])
def test_high_value_claim_cannot_finish_before_a_human_decision(module):
    claim = {**load_submission(1), "amount_cents": 600000}
    graph = module.build_graph()
    config = {"configurable": {"thread_id": "approval-test"}}
    kwargs = {"context": v06.CustomerContext(claim["customer_id"])} if module is v06 else {}
    result = graph.invoke(
        {"claim": claim, "audit": [], "findings": []}, config, version="v2", **kwargs
    )
    assert len(result.interrupts) == 1
    assert result.interrupts[0].value["amount_cents"] == 600000
    result = graph.invoke(Command(resume={"approved": False}), config, version="v2", **kwargs)
    assert result.value["approved"] is False
    assert result.value["approval_reason"] == "human_rejected"


def test_policy_agent_exposes_all_four_read_only_tools():
    result = v05.run()
    assert {item["tool"] for item in result["policy_evidence"]} == {
        "lookup_policy",
        "get_claim_history",
        "check_coverage",
        "calculate_payout",
    }
    assert result["claim"]["claim_id"] == load_submission(1)["claim_id"]


@pytest.mark.parametrize("number", [19, 20, 38, 57])
def test_incomplete_fixture_reaches_intake_without_invented_model_facts(number):
    result = v07.run(load_submission(number))
    assert result["approved"] is False
    assert result["route"] in {"needs_information", "duplicate"}
    assert result["claim"]["amount_cents"] is None
    assert result["extracted"] == {} and result["policy_evidence"] == []
    assert "not approved" in result["letter"]


@pytest.mark.parametrize("amount", [-1, True, "100"])
def test_invalid_amount_reaches_rejection_instead_of_model_validation(amount):
    result = v07.run({**load_submission(1), "amount_cents": amount})
    assert result["route"] == "invalid" and not result["approved"]


def test_unknown_category_is_preserved_for_specialist_review():
    result = v04.run({**load_submission(1), "claim_type": " JEWELRY "}, approved=False)
    assert result["extracted"]["claim_type"] == "unknown"
    assert result["claim"]["claim_type"] == "jewelry"
    assert result["route"] == "specialist"


def test_letter_respects_rejection_and_customer_preference():
    result = v06.run(
        {**load_submission(1), "amount_cents": 600000}, approved=False, preference="sms"
    )
    assert result["preference"] == "sms"
    assert result["letter_accepted"]
    assert "not approved" in result["letter"]
    assert result["letter_attempts"] == 2


def test_customer_context_cannot_read_another_customers_memory(monkeypatch):
    def forbidden(*args, **kwargs):
        pytest.fail("Authorization must precede model extraction and policy reads")

    monkeypatch.setattr(v04, "get_chat_model", forbidden)
    graph = v06.build_graph()
    claim = {**load_submission(1), "amount_cents": 10000, "claim_type": "water"}
    with pytest.raises(PermissionError, match="does not own"):
        graph.invoke(
            {"claim": claim, "audit": [], "findings": []},
            {"configurable": {"thread_id": "wrong-owner"}},
            context=v06.CustomerContext("CUS-OTHER"),
            version="v2",
        )
