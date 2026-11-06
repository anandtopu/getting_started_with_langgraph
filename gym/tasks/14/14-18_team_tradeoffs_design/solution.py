"""Executable design constraints; the written rubric remains essential."""

from common.pretty import print_state


def run(case: dict | None = None) -> dict:
    return {
        "budget": "explicit_call_count",
        "comparison": "single_agent_baseline",
        "routing": "active_role",
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
