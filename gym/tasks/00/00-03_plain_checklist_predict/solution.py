"""Compute the prediction answer from real deterministic runs. No LLM is needed."""

import json

from common.claims import checklist
from common.gym_fixtures import checklist_cases


def run() -> dict:
    outcomes = [checklist(claim) for claim in checklist_cases()]
    return {
        "statuses": [item["status"] for item in outcomes],
        "missing": [item["missing"] for item in outcomes],
        "trace": outcomes[0]["trace"],
    }


def main() -> None:
    print(json.dumps(run(), sort_keys=True))


if __name__ == "__main__":
    main()
