"""Extend first gym: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

from common.pretty import print_state

DEFAULT_CASE = {"claim_type": " Water ", "claim_id": "CLM-0001"}


def normalize_label(value: object) -> str:
    normalized = value.strip().lower() if isinstance(value, str) else ""
    return (
        normalized if normalized in {"water", "theft", "fire", "storm", "liability"} else "unknown"
    )


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    claim = dict(DEFAULT_CASE if case is None else case)
    return {"claim_id": claim.get("claim_id"), "label": normalize_label(claim.get("claim_type"))}


def run_batch(cases: list[dict]) -> list[dict]:
    return []


def main() -> None:
    try:
        for label in (" Water ", "THEFT", None):
            print_state(run({**DEFAULT_CASE, "claim_type": label}))
        assert run()["label"] == "water", "LARKSPUR: normalize before comparing labels"
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
