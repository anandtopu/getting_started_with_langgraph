"""Extend trajectory evals: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

from langchain_core.messages import AIMessage

from common.pretty import print_state

DEFAULT_CASE = {
    "tools": ["lookup_policy", "check_coverage"],
    "mode": "strict",
    "policy_id": "POL-0001",
}


def messages(names, policy_id):
    return [
        AIMessage(
            content="",
            tool_calls=[{"name": name, "args": {"policy_id": policy_id}, "id": str(index)}],
        )
        for index, name in enumerate(names)
    ]


def run(case: dict | None = None) -> dict:
    from agentevals.trajectory.match import create_trajectory_match_evaluator

    case = DEFAULT_CASE if case is None else case
    evaluator = create_trajectory_match_evaluator(
        trajectory_match_mode=case["mode"], tool_args_match_mode="exact"
    )
    result = evaluator(
        outputs=messages(case["tools"], case["policy_id"]),
        reference_outputs=messages(["lookup_policy", "check_coverage"], "POL-0001"),
    )
    return {"score": result["score"], "key": result["key"]}


def run_batch(cases: list[dict]) -> list[dict]:
    """Preview independent claims in order; one rejected input must not lose its siblings.

    This sequential interface favors isolation over throughput. It is not a shared
    checkpoint thread or a promise of transaction atomicity.
    """
    from copy import deepcopy

    from common.pretty import safe_value

    results = []
    for case in cases:
        try:
            results.append({"value": safe_value(run(deepcopy(case)))})
        except Exception as error:
            results.append({"error": type(error).__name__})
    return results


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
