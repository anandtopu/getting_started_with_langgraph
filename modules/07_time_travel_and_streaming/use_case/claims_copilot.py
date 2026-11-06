"""Claims Copilot v03: Replay a disputed decision and fork it with corrected evidence. No live model or external effects."""

from common.copilot import v03 as copilot
from common.data import load_submission
from common.pretty import print_state


def run() -> dict:
    graph = copilot.build_graph()
    claim = {**load_submission(1), "amount_cents": 600000}
    config = {"configurable": {"thread_id": claim["claim_id"]}}
    paused = graph.invoke({"claim": claim, "audit": [], "findings": []}, config, version="v2")
    history = list(graph.get_state_history(config))
    return {
        "requests": [item.value for item in paused.interrupts],
        "pending": list(graph.get_state(config).next),
        "steps": sorted(item.metadata["step"] for item in history),
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
