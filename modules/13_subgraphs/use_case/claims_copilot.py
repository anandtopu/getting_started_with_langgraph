"""Claims Copilot v07: Reuse one fraud-review component in claim and policy workflows. No live model or external effects."""

from common.copilot import v07 as copilot
from common.data import load_submission
from common.pretty import print_state


def run() -> dict:
    result = copilot.run(load_submission(1))
    return {"risk_flags": result["risk_flags"], "claim_id": result["claim"]["claim_id"]}


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
