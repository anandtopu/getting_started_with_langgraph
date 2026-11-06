"""Predict trajectory evals across the declared cases. Run this file with Python. No live model or network."""

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


def scenario(case: dict | None = None) -> dict:
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


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"mode": "strict", "policy_id": "POL-0001", "tools": ["lookup_policy", "check_coverage"]},
        {"mode": "strict", "policy_id": "POL-0001", "tools": ["check_coverage", "lookup_policy"]},
        {
            "mode": "unordered",
            "policy_id": "POL-0001",
            "tools": ["check_coverage", "lookup_policy"],
        },
        {"mode": "strict", "policy_id": "POL-0002", "tools": ["lookup_policy", "check_coverage"]},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {"observations": observations, "cause": None}


if __name__ == "__main__":
    main()
