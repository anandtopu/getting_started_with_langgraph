"""Diagnose test graph behavior from execution evidence. Run this file with Python. No live model or network."""

from common.claims import route_claim
from common.copilot import v01
from common.data import load_submission
from common.pretty import print_state

DEFAULT_CASE = {"amounts": [100000, 100001, 500001, True]}


def scenario(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    rows = []
    for amount in case["amounts"]:
        claim = {**load_submission(1), "amount_cents": amount, "claim_type": "water"}
        expected = (
            "invalid"
            if not isinstance(amount, int) or amount < 0
            else "fast_track"
            if amount <= 100000
            else "standard"
            if amount <= 500000
            else "specialist"
        )
        rows.append(
            {
                "amount": amount,
                "expected": expected,
                "rule": route_claim(claim),
                "graph": v01.run(claim)["route"],
            }
        )
    return {
        "rows": rows,
        "passed": all(row["expected"] == row["rule"] == row["graph"] for row in rows),
    }


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [{"amounts": [100000, 100001, 500001, True]}, {"amounts": [0, -1, 500000]}]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {
        "observations": observations,
        "cause": "Include boolean cents in invalid-input coverage.",
    }


if __name__ == "__main__":
    main()
