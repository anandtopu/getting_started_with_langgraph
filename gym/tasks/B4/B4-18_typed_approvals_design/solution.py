"""Executable design constraints; the written rubric remains essential."""

from common.pretty import print_state


def run(case: dict | None = None) -> dict:
    return {
        "decisions": "approve_or_reject",
        "granularity": "per_tool_call",
        "validation": "response_schema",
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
