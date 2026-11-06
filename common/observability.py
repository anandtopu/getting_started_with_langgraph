"""Allowlisted structured logs; raw prompts, customer data, and credentials are excluded."""

import json

ALLOWED = {"event", "thread_id", "run_id", "node", "status", "duration_ms", "error_type"}


def log_record(event: dict) -> str:
    return json.dumps(
        {key: value for key, value in event.items() if key in ALLOWED}, sort_keys=True
    )
