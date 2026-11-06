"""Extend test graph behavior: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

from common.claims import route_claim
from common.copilot import v01
from common.data import load_submission
from common.pretty import print_state

DEFAULT_CASE = {"amounts": [100000, 100001, 500001, True]}


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
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


def run_batch(cases: list[dict]) -> list[dict]:
    """Preview independent claims in order; one rejected input must not lose its siblings.

    This sequential interface favors isolation over throughput. It is not a shared
    checkpoint thread or a promise of transaction atomicity.
    """
    from copy import deepcopy

    from common.pretty import safe_value

    results = []
    for case in cases:
        try:
            results.append({"value": safe_value(run(deepcopy(case)))})
        except Exception as error:
            results.append({"error": type(error).__name__})
    return results


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
