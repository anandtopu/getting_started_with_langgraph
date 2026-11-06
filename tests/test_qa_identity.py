"""The QA memory namespace follows trusted context, not graph input."""

from langgraph.store.memory import InMemoryStore

from common.config import ROOT
from common.copilot.v06 import CustomerContext
from common.loading import load_module


def test_qa_input_cannot_substitute_another_customer_identity():
    module = load_module(ROOT / "capstones/02_policy_qa_with_memory/solution.py")
    store = InMemoryStore()
    store.put(("customers", "CUS-0001"), "contact", {"preference": "sms"})
    graph = module.build_graph(store)
    result = graph.invoke(
        {"question": "home deductible", "customer_id": "CUS-0001"},
        {"configurable": {"thread_id": "customer-2"}},
        context=CustomerContext("CUS-0002"),
        version="v2",
    ).value
    assert result["preference"] == "email"
