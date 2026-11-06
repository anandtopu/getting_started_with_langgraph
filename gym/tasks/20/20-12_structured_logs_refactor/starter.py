"""Refactor structured logs: Do not report a successful node as failed during logging refactors.. Run this file with Python. No live model or network."""

import json

from common.observability import log_record
from common.pretty import print_state

DEFAULT_CASE = {
    "thread_id": "claim-thread",
    "run_id": "review-1",
    "description": "Synthetic contact: 555-0100",
    "api_key": "synthetic-secret",
}


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    records = []
    for node in ["normalize", "route", "approve_claim"]:
        record = log_record({**case, "event": "node_finished", "node": node, "status": "failed"})
        records.append(json.loads(record))
    return {
        "records": records,
        "raw_text_logged": any(case["description"] in json.dumps(row) for row in records),
        "credential_logged": any(case["api_key"] in json.dumps(row) for row in records),
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
