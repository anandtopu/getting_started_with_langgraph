"""Claims Copilot v04: Extract claim facts with a model, then route with deterministic rules. No live model or external effects."""

from common.copilot import v04 as copilot
from common.data import load_submission
from common.pretty import print_state


def run() -> dict:
    result = copilot.run(load_submission(1))
    return {
        "extracted": result["extracted"],
        "route": result["route"],
        "approved": result["approved"],
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
