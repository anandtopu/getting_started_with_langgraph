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


def test_typescript_structure(candidate_path):
    source = candidate_path.with_suffix(".ts").read_text("utf-8")
    assert "createAgent({ model: model(), tools: [lookup] })" in source, (
        "LARKSPUR: implement the requested TypeScript construction boundary"
    )
    assert "new StateGraph(" not in source, "LARKSPUR: remove the manual agent loop"
