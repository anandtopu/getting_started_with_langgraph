"""Convert a public claim schema to a private investigation schema. No LLM.

Run: uv run python modules/13_subgraphs/examples/02_schema_adapters.py
Expected: the public result includes risk, but no private investigator notes.
"""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001", "amount_cents": 600000}


class Claim(TypedDict):
    claim_id: str
    amount_cents: int
    risk: str


class Investigation(TypedDict):
    case_number: str
    value: int
    private_notes: str
    finding: str


def build_graph():
    def investigate(state: Investigation) -> dict:
        return {
            "private_notes": "Synthetic rule assessment, not evidence of wrongdoing.",
            "finding": "review" if state["value"] > 500000 else "routine",
        }

    child = StateGraph(Investigation)
    child.add_node("investigate", investigate)
    child.add_edge(START, "investigate")
    child.add_edge("investigate", END)
    investigation = child.compile()

    def adapt(state: Claim) -> dict:
        result = investigation.invoke(
            {"case_number": state["claim_id"], "value": state["amount_cents"]}, version="v2"
        )
        # KEY IDEA: only the reviewed finding crosses the child output boundary.
        return {"risk": result.value["finding"]}

    parent = StateGraph(Claim)
    parent.add_node("fraud_adapter", adapt)
    parent.add_edge(START, "fraud_adapter")
    parent.add_edge("fraud_adapter", END)
    return parent.compile()


def run(case: dict | None = None) -> dict:
    result = build_graph().invoke(dict(DEFAULT_CASE if case is None else case), version="v2").value
    return {"fields": sorted(result), **result}


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
