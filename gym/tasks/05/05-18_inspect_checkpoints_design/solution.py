"""Executable design constraints; the written rubric remains essential."""

from common.pretty import print_state


def run(case: dict | None = None) -> dict:
    return {
        "approval": "sync",
        "draft": "async_with_documented_risk",
        "history": "parent_links_and_steps",
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
