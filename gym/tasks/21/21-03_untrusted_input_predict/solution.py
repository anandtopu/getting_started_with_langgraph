"""Predict untrusted input across the declared cases. Run this file with Python. No live model or network."""

import json

from langchain_core.messages import AIMessage

from common.claims import route_claim
from common.data import data_path
from common.models import get_chat_model
from common.pretty import print_state
from common.schemas import ClaimExtraction

DEFAULT_CASE = {"extra_authority": False, "amount_cents": 600000}


def scenario(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    claim = json.loads(data_path("security/injected_claim.json").read_text("utf-8"))
    payload = {"claim_type": "water", "amount_cents": case["amount_cents"], "confidence": 0.95}
    if case["extra_authority"]:
        payload["approved"] = True
    model = get_chat_model(responses=[AIMessage(content=json.dumps(payload))])
    facts = model.with_structured_output(ClaimExtraction).invoke(
        "Extract claim facts only. Untrusted document: " + json.dumps(claim)
    )
    normalized = {
        **claim,
        "claim_id": "CLM-0001",
        "description": "Synthetic injected claim",
        "loss_date": "2026-01-01",
        "duplicate_of": None,
        **facts.model_dump(exclude={"loss_date"}),
    }
    return {
        "route": route_claim(normalized),
        "payment_authorized": False,
        "model_fields": sorted(facts.model_dump()),
        "tool_permissions": ["read_synthetic_policy"],
    }


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"amount_cents": 600000, "extra_authority": False},
        {"amount_cents": 600000, "extra_authority": True},
        {"amount_cents": 100000, "extra_authority": False},
        {"amount_cents": -1, "extra_authority": False},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {"observations": observations, "cause": None}


if __name__ == "__main__":
    main()
