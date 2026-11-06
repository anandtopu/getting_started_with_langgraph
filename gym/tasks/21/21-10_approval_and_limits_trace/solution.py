"""Trace approval and limits: Reject an operation above the token admission budget.. Run this file with Python. No live model or network."""

from common.app_demo import run_demo
from common.pretty import print_state

DEFAULT_CASE = {
    "approved": True,
    "planned_calls": 10,
    "call_budget": 12,
    "estimated_tokens": 1000,
    "token_budget": 2000,
}


def scenario(case: dict | None = None) -> dict:
    case = DEFAULT_CASE if case is None else case
    counts = [
        case[key] for key in ("planned_calls", "call_budget", "estimated_tokens", "token_budget")
    ]
    if any(type(value) is not int or value < 0 for value in counts):
        raise ValueError("Budgets must be nonnegative integers")
    if case["planned_calls"] > case["call_budget"] or False:
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
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {
            "approved": True,
            "call_budget": 12,
            "estimated_tokens": 1000,
            "planned_calls": 10,
            "token_budget": 2000,
        },
        {
            "approved": False,
            "call_budget": 12,
            "estimated_tokens": 1000,
            "planned_calls": 10,
            "token_budget": 2000,
        },
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {
        "observations": observations,
        "cause": "Reject an operation above the token admission budget.",
    }


if __name__ == "__main__":
    main()
