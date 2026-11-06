"""Deterministic educational rules, independent of graph or model packages."""

from typing import Any

REQUIRED = ("claim_id", "claim_type", "description", "amount_cents", "loss_date")
CLAIM_TYPES = frozenset({"water", "theft", "fire", "storm", "liability"})


def normalize_claim(claim: dict[str, Any]) -> dict[str, Any]:
    result = dict(claim)
    for key in ("description", "claim_type"):
        if isinstance(result.get(key), str):
            result[key] = result[key].strip()
    if isinstance(result.get("claim_type"), str):
        result["claim_type"] = result["claim_type"].lower()
    return result


def missing_fields(claim: dict[str, Any]) -> list[str]:
    return [key for key in REQUIRED if claim.get(key) is None or claim.get(key) == ""]


def checklist(claim: dict[str, Any]) -> dict[str, Any]:
    normalized = normalize_claim(claim)
    missing = missing_fields(normalized)
    status = (
        "duplicate"
        if normalized.get("duplicate_of")
        else "needs_information"
        if missing
        else "ready"
    )
    return {
        "claim_id": normalized.get("claim_id"),
        "status": status,
        "missing": missing,
        "trace": ["normalize_claim", "check_required_fields", "route_claim"],
    }


def route_claim(claim: dict[str, Any]) -> str:
    normalized = normalize_claim(claim)
    status = checklist(normalized)["status"]
    if status != "ready":
        return status
    amount = normalized["amount_cents"]
    if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
        return "invalid"
    if normalized["claim_type"] not in CLAIM_TYPES:
        return "specialist"
    if normalized.get("fraud_indicators") or amount > 500_000:
        return "specialist"
    if amount <= 100_000 and normalized["claim_type"] in {"water", "theft", "storm"}:
        return "fast_track"
    return "standard"


def calculate_payout(amount_cents: int, limit_cents: int, deductible_cents: int) -> int:
    """Fictional course rule: subtract the deductible, then apply the payout limit."""
    amounts = (amount_cents, limit_cents, deductible_cents)
    if any(isinstance(x, bool) or not isinstance(x, int) or x < 0 for x in amounts):
        raise ValueError("Use nonnegative integer cents.")
    return min(max(amount_cents - deductible_cents, 0), limit_cents)
