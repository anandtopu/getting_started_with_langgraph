"""Executable design constraints; the written rubric remains essential."""

from common.pretty import print_state


def run(case: dict | None = None) -> dict:
    return {
        "checkpoint": "copied_state_and_position",
        "pause": "single_node_teaching_contract",
        "thread": "isolated",
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
