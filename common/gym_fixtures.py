"""Small deterministic claim scenarios used by the introductory gym tasks."""

from copy import deepcopy
from typing import Any

REQUIRED = ("claim_id", "claim_type", "description", "amount_cents", "loss_date")
TRACE = ["normalize_claim", "check_required_fields", "route_claim"]


def checklist_cases() -> list[dict[str, Any]]:
    complete = {
        "claim_id": "CLM-0001",
        "claim_type": " Water ",
        "description": " Burst pipe. ",
        "amount_cents": 125_000,
        "loss_date": "2026-01-01",
    }
    missing = {**complete, "claim_id": "CLM-0007", "loss_date": None}
    duplicate = {**complete, "claim_id": "CLM-0010", "duplicate_of": "CLM-0001"}
    return deepcopy([complete, missing, duplicate])


def trace_loss() -> list[dict[str, Any]]:
    claim = checklist_cases()[1]
    # Deliberate observed bug: this step reconstructs state without the identity.
    after_normalize = {"description": claim["description"].strip(), "loss_date": claim["loss_date"]}
    after_check = {
        **after_normalize,
        "missing": ["claim_id", "claim_type", "amount_cents", "loss_date"],
    }
    return [
        {"step": "input", "state": claim},
        {"step": "normalize_claim", "state": after_normalize},
        {"step": "check_required_fields", "state": after_check},
    ]
