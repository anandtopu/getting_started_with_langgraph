"""Exact-budget completion differs from a still-pending cycle."""

import pytest

from common.mini_graph import MiniGraph


def test_final_step_can_complete_at_the_budget_boundary():
    graph = MiniGraph({"done": lambda state, resume: {"result": 1}}, {}, ["done"])
    result = graph.run({}, limit=1)
    assert result.values == {"result": 1} and result.pending == []
    assert graph.latest("claim") == result


def test_budget_still_stops_a_cycle_and_preserves_recovery_state():
    graph = MiniGraph(
        {"loop": lambda state, resume: {"n": state["n"] + 1}}, {"loop": ["loop"]}, ["loop"]
    )
    with pytest.raises(RuntimeError, match="budget"):
        graph.run({"n": 0}, limit=2)
    assert graph.latest("claim").values == {"n": 2}
