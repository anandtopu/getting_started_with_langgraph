"""Extend first gym: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

from common.pretty import print_state

DEFAULT_CASE = {"claim_type": " Water ", "claim_id": "CLM-0001"}


def normalize_label(value: object) -> str:
    normalized = value.strip().lower() if isinstance(value, str) else ""
    return (
        normalized if normalized in {"water", "theft", "fire", "storm", "liability"} else "unknown"
    )


def run(case: dict | None = None) -> dict:
    claim = dict(DEFAULT_CASE if case is None else case)
    return {"claim_id": claim.get("claim_id"), "label": normalize_label(claim.get("claim_type"))}


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
        for label in (" Water ", "THEFT", None):
            print_state(run({**DEFAULT_CASE, "claim_type": label}))
        assert run()["label"] == "water", "LARKSPUR: normalize before comparing labels"
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
