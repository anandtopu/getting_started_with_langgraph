"""Grade observable checklist behavior against the selected learner file."""

from copy import deepcopy

import pytest

from common.gym_fixtures import REQUIRED, TRACE, checklist_cases


@pytest.mark.parametrize(
    "index,status,missing",
    [
        (0, "ready", []),
        (1, "needs_information", ["loss_date"]),
        (2, "duplicate", []),
    ],
)
def test_checklist_acceptance(candidate, index, status, missing):
    claim = checklist_cases()[index]
    before = deepcopy(claim)
    actual = candidate.run(claim)
    assert actual["claim_id"] == claim["claim_id"], "LARKSPUR: preserve claim identity."
    assert actual["status"] == status, (
        "LARKSPUR: route incomplete and duplicate submissions explicitly."
    )
    assert actual["missing"] == missing, "LARKSPUR: list missing fields in the documented order."
    assert actual["trace"] == TRACE, "LARKSPUR: normalize, check required fields, then route."
    assert claim == before, "LARKSPUR: do not mutate the caller's dictionary."


def test_zero_is_not_missing(candidate):
    claim = {**checklist_cases()[0], "amount_cents": 0}
    assert candidate.run(claim)["missing"] == [], (
        "LARKSPUR: zero is present; do not use a truthiness check."
    )


def test_whitespace_and_missing_fields(candidate):
    actual = candidate.run({"claim_id": "CLM-0042", "description": "   "})
    assert actual["missing"] == list(REQUIRED[1:]), (
        "LARKSPUR: normalize whitespace before validation."
    )
