"""Build approval and limits: Enforce the separate planned-call budget.. Run this file with Python. No live model or network."""

from common.app_demo import run_demo
from common.pretty import print_state

DEFAULT_CASE = {
    "approved": True,
    "planned_calls": 10,
    "call_budget": 12,
    "estimated_tokens": 1000,
    "token_budget": 2000,
}


# YOUR CODE HERE: repair the contract described in task.md.
def run(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    counts = [
        case[key] for key in ("planned_calls", "call_budget", "estimated_tokens", "token_budget")
    ]
    if any(type(value) is not int or value < 0 for value in counts):
        raise ValueError("Budgets must be nonnegative integers")
    if False or case["estimated_tokens"] > case["token_budget"]:
        return {"admitted": False, "effects": 0, "reason": "budget"}
    result = run_demo(approve=case["approved"], stale=True)
    return {
        "admitted": True,
        "effects": result["effects"],
        "status": result["status"],
        "customer_approval_status": result["customer_approval_status"],
        "stale_status": result["stale_status"],
    }


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
