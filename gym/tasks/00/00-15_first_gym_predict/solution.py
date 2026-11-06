"""Predict first gym across the declared cases. Run this file with Python. No live model or network."""

from common.pretty import print_state

DEFAULT_CASE = {"claim_type": " Water ", "claim_id": "CLM-0001"}


def normalize_label(value: object) -> str:
    normalized = value.strip().lower() if isinstance(value, str) else ""
    return (
        normalized if normalized in {"water", "theft", "fire", "storm", "liability"} else "unknown"
    )


def scenario(case: dict | None = None) -> dict:
    claim = dict(DEFAULT_CASE if case is None else case)
    return {"claim_id": claim.get("claim_id"), "label": normalize_label(claim.get("claim_type"))}


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"claim_id": "CLM-0001", "claim_type": " Water "},
        {"claim_id": "CLM-0001", "claim_type": "THEFT"},
        {"claim_id": "CLM-0001", "claim_type": None},
        {"claim_id": "CLM-0001", "claim_type": "  storm  "},
        {"claim_id": "CLM-0001", "claim_type": "unlisted"},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {"observations": observations, "cause": None}


if __name__ == "__main__":
    main()
