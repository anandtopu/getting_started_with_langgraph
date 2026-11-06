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


def test_functional_entrypoint_and_task_boundaries(candidate_path):
    import ast

    tree = ast.parse(candidate_path.read_text("utf-8"))
    decorated = {
        node.name: [ast.unparse(item) for item in node.decorator_list]
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }
    assert "entrypoint()" in decorated.get("intake", []), (
        "LARKSPUR: use an entrypoint for orchestration"
    )
    assert all("task" in decorated.get(name, []) for name in ("normalize", "route")), (
        "LARKSPUR: retain task boundaries"
    )
