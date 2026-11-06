"""The deployment plan must match the actual exported graph input schema."""

from langgraph.checkpoint.memory import InMemorySaver

from common.config import ROOT
from common.copilot.v03 import build_graph
from common.loading import load_module


def test_managed_plan_contains_an_executable_claim_state():
    lesson = load_module(ROOT / "modules/22_deployment/examples/03_managed_deployment.py")
    plan = lesson.run()
    result = build_graph(InMemorySaver()).invoke(
        plan["run"]["input"],
        {"configurable": {"thread_id": plan["thread"]["thread_id"]}},
        version="v2",
    )
    assert result.value["claim"]["claim_id"] == "CLM-0001"
    assert result.value["route"]
