"""Reference checklist. Run this file with Python; no LLM is used."""

from typing import Any

from common.gym_fixtures import REQUIRED, TRACE, checklist_cases
from common.pretty import print_state


def run(claim: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(claim)
    for key in ("description", "claim_type"):
        if isinstance(normalized.get(key), str):
            normalized[key] = normalized[key].strip()
    missing = [key for key in REQUIRED if normalized.get(key) is None or normalized.get(key) == ""]
    if normalized.get("duplicate_of"):
        status = "duplicate"
    elif missing:
        status = "needs_information"
    else:
        status = "ready"
    # YOUR CODE HERE: add a reason without changing existing outputs.
    return {
        "claim_id": normalized.get("claim_id"),
        "status": status,
        "missing": missing,
        "trace": list(TRACE),
    }


def main() -> None:
    print_state(run(checklist_cases()[1]))


if __name__ == "__main__":
    main()
