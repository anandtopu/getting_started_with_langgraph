"""Claims Copilot v07: Coordinate intake, policy, fraud, and communication specialists. No live model or external effects."""

from common.copilot import v07 as copilot
from common.data import load_submission
from common.pretty import print_state


def run() -> dict:
    result = copilot.run(load_submission(1))
    return {"specialists": result["specialist_reports"], "approved": result["approved"]}


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
