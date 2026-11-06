"""Claims Copilot v05: Look up policies and calculate a synthetic payout through controlled tools. No live model or external effects."""

from common.copilot import v05 as copilot
from common.data import load_submission
from common.pretty import print_state


def run() -> dict:
    result = copilot.run(load_submission(1))
    return {
        "tools": [item["tool"] for item in result["policy_evidence"]],
        "explanation": result["agent_explanation"],
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
