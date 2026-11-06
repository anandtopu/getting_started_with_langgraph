"""Executable design constraints; the written rubric remains essential."""

from common.pretty import print_state


def run(case: dict | None = None) -> dict:
    return {
        "budget": "bounded_parent_calls",
        "context": "isolated_specialist",
        "delegation": "approval_gated",
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
