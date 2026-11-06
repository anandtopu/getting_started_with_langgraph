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


def test_batch_preserves_order_errors_and_input_ownership(candidate):
    from copy import deepcopy

    batch = getattr(candidate, "run_batch", None)
    assert callable(batch), "LARKSPUR: implement the batch extension"
    selected = [CASES[0], CASES[-1], CASES[0]]
    inputs = [deepcopy(row["input"]) for row in selected]
    before = deepcopy(inputs)
    assert batch([]) == [], "LARKSPUR: an empty batch has no observations"
    assert batch(inputs) == [row["expected"] for row in selected], (
        "LARKSPUR: preserve order and isolate each claim"
    )
    assert inputs == before, "LARKSPUR: do not mutate the caller's batch"


@pytest.mark.parametrize(
    "case", json.loads(Path(__file__).with_name("baseline_cases.json").read_text("utf-8"))
)
def test_original_contract_survives_extension(candidate, case):
    from common.exercises import preserves_original

    assert preserves_original(case["expected"], observe(candidate, case["input"])), (
        "LARKSPUR: retain the original fields, list prefix, and errors when adding a feature"
    )
