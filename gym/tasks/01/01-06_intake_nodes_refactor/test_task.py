"""Grade the selected learner file, not the reference implementation."""

import json
from pathlib import Path

import pytest

from common.exercises import observe

CASES = json.loads(Path(__file__).with_name("cases.json").read_text("utf-8"))


@pytest.mark.parametrize("case", CASES, ids=[str(index) for index in range(len(CASES))])
def test_behavior(candidate, case):
    actual = observe(candidate, case["input"])
    assert actual == case["expected"], (
        "LARKSPUR: preserve the declared state, routing, and boundary contracts"
    )


def test_node_returns_a_partial_update_without_mutation(candidate):
    state = dict(candidate.DEFAULT_CASE)
    before = dict(state)
    update = candidate.normalize_description(state)
    assert state == before, "LARKSPUR: a node must not mutate its input"
    assert set(update) == {"description"}, "LARKSPUR: return only the changed field"
