"""Claims Copilot v02: Continue one claim across several adjuster sessions. No live model or external effects."""

from common.copilot import v02 as copilot
from common.data import load_submission
from common.pretty import print_state


def run() -> dict:
    graph = copilot.build_graph()
    claim = load_submission(1)
    config = {"configurable": {"thread_id": claim["claim_id"]}}
    graph.invoke({"claim": claim, "audit": [], "findings": []}, config, version="v2")
    result = graph.invoke({"claim": {**claim, "documents": []}}, config, version="v2").value
    return {"audit": result["audit"], "checkpoints": len(list(graph.get_state_history(config)))}


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
