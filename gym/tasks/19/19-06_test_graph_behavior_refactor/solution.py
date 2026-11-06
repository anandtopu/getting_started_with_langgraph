"""Refactor test graph behavior: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.. Run this file with Python. No live model or network."""

from common.claims import route_claim
from common.copilot import v01
from common.data import load_submission
from common.pretty import print_state

DEFAULT_CASE = {"amounts": [100000, 100001, 500001, True]}


def prepare_case(case: dict | None = None) -> dict:
    """Own a fresh input snapshot; do not mutate the caller or shared defaults."""
    from copy import deepcopy

    return deepcopy(DEFAULT_CASE if case is None else case)


def run(case: dict | None = None) -> dict:
    case = prepare_case(case)
    rows = []
    for amount in case["amounts"]:
        claim = {**load_submission(1), "amount_cents": amount, "claim_type": "water"}
        expected = (
            "invalid"
            if type(amount) is not int or amount < 0
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
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
