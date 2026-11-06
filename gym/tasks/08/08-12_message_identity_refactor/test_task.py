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


def test_input_preparation_is_a_separate_owned_boundary(candidate, candidate_path):
    import ast
    from copy import deepcopy

    helper = getattr(candidate, "prepare_case", None)
    assert callable(helper), "LARKSPUR: extract prepare_case(case) from orchestration"
    original = {"nested": {"items": ["original"]}}
    before = deepcopy(original)
    prepared = helper(original)
    assert prepared == before and prepared is not original
    prepared["nested"]["items"].append("changed")
    assert original == before, "LARKSPUR: isolate nested caller-owned inputs"
    defaults = deepcopy(candidate.DEFAULT_CASE)
    prepared = helper()
    assert prepared == defaults and prepared is not candidate.DEFAULT_CASE
    assert helper({}) == {}, "LARKSPUR: an empty input is not a request for defaults"
    tree = ast.parse(candidate_path.read_text("utf-8"))
    run = next(
        node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "run"
    )
    assert any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "prepare_case"
        for node in ast.walk(run)
    ), "LARKSPUR: use the extracted boundary in run"
