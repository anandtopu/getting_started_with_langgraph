"""A small assertion contract before graphs. No LLM or external effects.

Run: uv run python modules/00_setup/examples/03_first_gym.py
Expected: water, theft, and unknown labels; input dictionaries stay unchanged.
"""

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


def main() -> None:
    for label in (" Water ", "THEFT", None):
        print_state(run({**DEFAULT_CASE, "claim_type": label}))
    assert run()["label"] == "water", "LARKSPUR: normalize before comparing labels"


if __name__ == "__main__":
    main()
