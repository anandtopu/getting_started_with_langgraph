"""Replay an entrypoint while reusing a completed task result. No LLM.

Run: uv run python modules/15_functional_api/examples/03_functional_resume.py
Expected: entrypoint starts twice but the completed evidence task executes only once.
"""

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.func import entrypoint, task
from langgraph.types import Command, interrupt

from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001", "approved": True}


def build_workflow(counts: dict):
    @task
    def collect_evidence(claim_id: str) -> dict:
        counts["task"] += 1
        return {"claim_id": claim_id, "documents": ["estimate"]}

    @entrypoint(checkpointer=InMemorySaver())
    def review(claim: dict) -> dict:
        counts["entrypoint"] += 1
        evidence = collect_evidence(claim["claim_id"]).result()
        decision = interrupt({"evidence": evidence})
        if type(decision) is not bool:
            raise ValueError("Approval must be a boolean")
        return {"claim_id": evidence["claim_id"], "approved": decision}

    return review


def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    counts = {"entrypoint": 0, "task": 0}
    workflow = build_workflow(counts)
    config = {"configurable": {"thread_id": case["claim_id"]}}
    paused = workflow.invoke({"claim_id": case["claim_id"]}, config, version="v2")
    result = workflow.invoke(Command(resume=case["approved"]), config, version="v2")
    return {"interrupts": len(paused.interrupts), "result": result.value, "counts": counts}


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
