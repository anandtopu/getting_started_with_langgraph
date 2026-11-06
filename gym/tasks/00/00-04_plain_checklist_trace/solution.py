"""Reproduce the recorded bug and locate the first identity loss."""

import json

from common.gym_fixtures import trace_loss


def run() -> dict:
    events = trace_loss()
    bad = next(event for event in events if "claim_id" not in event["state"])
    return {"first_bad_step": bad["step"], "lost_field": "claim_id", "fix": "preserve_claim_id"}


def main() -> None:
    print(json.dumps(run(), sort_keys=True))


if __name__ == "__main__":
    main()
