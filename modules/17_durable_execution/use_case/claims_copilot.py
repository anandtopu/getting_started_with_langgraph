"""Claims Copilot v08: Wait for a contractor estimate and recover after a simulated crash. No live model or external effects."""

from common.copilot import v08 as copilot
from common.data import load_submission
from common.pretty import print_state


def run() -> dict:
    result = copilot.run(load_submission(1), approved=False)
    return {
        "waited_days": result["waited_days"],
        "approved": result["approved"],
        "documents": result["claim"]["documents"],
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
