"""Compare tool trajectories with the current agentevals matcher. Requires eval extra.

Run: uv run --extra eval python modules/19_testing_and_evaluation/examples/03_trajectory_evals.py
Expected: strict matching checks order and arguments; unordered matching tolerates parallel order.
"""

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


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
