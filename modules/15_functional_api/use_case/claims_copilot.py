"""Claims Copilot v07: Rewrite intake with ordinary control flow while preserving durable behavior. No live model or external effects."""

from common.copilot import v07 as copilot
from common.data import load_submission
from common.pretty import print_state


def run() -> dict:
    result = copilot.run(load_submission(1))
    return {
        "route": result["route"],
        "letter": result["letter"],
        "risk_flags": result["risk_flags"],
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
