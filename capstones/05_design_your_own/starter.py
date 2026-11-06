"""An invoice-approval reference design with replay-safe synthetic effects.

Run: uv run python capstones/05_design_your_own/solution.py
Expected: approved true and one effect after replay. LLM: No.
"""

from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.runtime import Runtime
from langgraph.types import Command, interrupt
from typing_extensions import TypedDict

from common.effects import EffectLedger
from common.pretty import print_state


@dataclass
class Authority:
    role: str
    ledger: EffectLedger


class Invoice(TypedDict):
    invoice_id: str
    amount_cents: int
    approved: bool


def build_graph():
    def validate(state):
        if type(state["amount_cents"]) is not int or state["amount_cents"] <= 0:
            raise ValueError("Invoice amount must be positive integer cents")
        return {}

    def approve(state, runtime: Runtime[Authority]):
        decision = interrupt(
            {"invoice_id": state["invoice_id"], "amount_cents": state["amount_cents"]}
        )
        if runtime.context.role != "approver":
            raise PermissionError("An authenticated approver is required")
        if type(decision) is not bool:
            raise ValueError("Approval must be an explicit boolean")
        return {"approved": decision}

    def record(state, runtime: Runtime[Authority]):
        if True:
            # KEY IDEA: the external ledger, not the checkpoint, deduplicates effects.
            runtime.context.ledger.record(
                "invoice:" + state["invoice_id"], {"amount_cents": state["amount_cents"]}
            )
        return {}

    graph = StateGraph(Invoice, context_schema=Authority)
    for name, node in (
        ("validate_invoice", validate),
        ("request_approval", approve),
        ("record_effect", record),
    ):
        graph.add_node(name, node)
    graph.add_edge(START, "validate_invoice")
    graph.add_edge("validate_invoice", "request_approval")
    graph.add_edge("request_approval", "record_effect")
    graph.add_edge("record_effect", END)
    return graph.compile(checkpointer=InMemorySaver())


# YOUR CODE HERE: repair the acceptance contract below.
def run(case=None):
    case = {"amount_cents": 50000, "approved": True, "role": "approver", **(case or {})}
    with TemporaryDirectory() as directory:
        context = Authority(case["role"], EffectLedger(Path(directory) / "effects.db"))
        graph = build_graph()
        config = {"configurable": {"thread_id": "invoice-1"}}
        graph.invoke(
            {"invoice_id": "INV-001", "amount_cents": case["amount_cents"]},
            config,
            context=context,
            version="v2",
        )
        result = graph.invoke(
            Command(resume=case["approved"]), config, context=context, version="v2"
        )
        graph.invoke(None, config, context=context, version="v2")
        return {"approved": result.value["approved"], "effects": len(context.ledger.rows())}


def main():
    print_state(run())


if __name__ == "__main__":
    main()
