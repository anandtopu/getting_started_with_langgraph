"""Predict structured logs across the declared cases. Run this file with Python. No live model or network."""

import json

from common.observability import log_record
from common.pretty import print_state

DEFAULT_CASE = {
    "thread_id": "claim-thread",
    "run_id": "review-1",
    "description": "Synthetic contact: 555-0100",
    "api_key": "synthetic-secret",
}


def scenario(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    records = []
    for node in ["normalize", "route", "approve_claim"]:
        record = log_record({**case, "event": "node_finished", "node": node, "status": "ok"})
        records.append(json.loads(record))
    return {
        "records": records,
        "raw_text_logged": any(case["description"] in json.dumps(row) for row in records),
        "credential_logged": any(case["api_key"] in json.dumps(row) for row in records),
    }


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {
            "api_key": "synthetic-secret",
            "description": "Synthetic contact: 555-0100",
            "run_id": "review-1",
            "thread_id": "claim-thread",
        },
        {
            "api_key": "synthetic-secret",
            "description": "Synthetic contact: 555-0100",
            "run_id": "review-2",
            "thread_id": "second-claim",
        },
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {"observations": observations, "cause": None}


if __name__ == "__main__":
    main()
