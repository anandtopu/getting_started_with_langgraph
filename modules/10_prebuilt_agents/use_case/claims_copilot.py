"""Claims Copilot v05: Use create_agent while retaining deterministic claim controls. No live model or external effects."""

from common.copilot import v05 as copilot
from common.data import load_submission
from common.pretty import print_state


def run() -> dict:
    result = copilot.run({**load_submission(1), "amount_cents": 600000}, approved=False)
    return {
        "approved": result["approved"],
        "route": result["route"],
        "explanation": result["agent_explanation"],
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
