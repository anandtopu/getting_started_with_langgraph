"""Extend functional resume: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

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


def run_batch(cases: list[dict]) -> list[dict]:
    """Preview independent claims in order; one rejected input must not lose its siblings.

    This sequential interface favors isolation over throughput. It is not a shared
    checkpoint thread or a promise of transaction atomicity.
    """
    from copy import deepcopy

    from common.pretty import safe_value

    results = []
    for case in cases:
        try:
            results.append({"value": safe_value(run(deepcopy(case)))})
        except Exception as error:
            results.append({"error": type(error).__name__})
    return results


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
