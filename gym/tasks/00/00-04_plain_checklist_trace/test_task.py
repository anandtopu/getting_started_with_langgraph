"""Compare a diagnosis with a reproduced state transition."""

from common.gym_fixtures import trace_loss


def test_trace(answer):
    events = trace_loss()
    bad = next(event for event in events if "claim_id" not in event["state"])
    expected = {"first_bad_step": bad["step"], "lost_field": "claim_id", "fix": "preserve_claim_id"}
    assert answer == expected, "LARKSPUR: locate the first state transition that drops claim_id."
