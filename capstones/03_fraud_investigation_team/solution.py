"""Compose a reusable fraud subgraph, scoped specialists, and real local MCP evidence.

Run: uv run --extra mcp python capstones/03_fraud_investigation_team/solution.py
Expected: two specialists and correlated evidence. LLM: local scripted fakes.
"""

from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict

from common.config import ROOT
from common.copilot import v07
from common.data import load_submission
from common.loading import load_module
from common.pretty import print_state


class Investigation(TypedDict):
    amount_cents: int
    claim_id: str
    evidence: dict
    risk_flags: list[str]
    specialists: list[str]


def build_graph():
    def collect_evidence(state):
        adapter = load_module(
            ROOT / "modules/16_external_systems_and_mcp/examples/03_mcp_adapter.py"
        )
        return {"evidence": adapter.run({"claim_id": state["claim_id"]})["claim"]}

    def investigate(state):
        claim = {**load_submission(1), "amount_cents": state["amount_cents"]}
        if state["evidence"].get("claim_id") != claim["claim_id"]:
            raise ValueError("MCP evidence belongs to a different claim")
        result = v07.run(claim, approved=False)
        return {
            "risk_flags": result["risk_flags"],
            "specialists": [row["specialist"] for row in result["specialist_reports"]],
        }

    graph = StateGraph(Investigation)
    graph.add_node("collect_mcp_evidence", collect_evidence)
    graph.add_node("supervise_scoped_team", investigate)
    graph.add_edge(START, "collect_mcp_evidence")
    graph.add_edge("collect_mcp_evidence", "supervise_scoped_team")
    graph.add_edge("supervise_scoped_team", END)
    return graph.compile()


def run(case=None):
    case = {"amount_cents": 600000, "claim_id": "CLM-0001", **(case or {})}
    result = build_graph().invoke(case, version="v2").value
    return {key: result[key] for key in ("risk_flags", "specialists", "evidence")}


def main():
    print_state(run())


if __name__ == "__main__":
    main()
