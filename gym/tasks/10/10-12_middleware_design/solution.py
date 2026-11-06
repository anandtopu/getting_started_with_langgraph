"""Executable design constraints; the written rubric remains essential."""

from common.pretty import print_state


def run(case: dict | None = None) -> dict:
    return {"budgets": "model_and_tool", "hooks": "ordered", "state": "declared_schema"}


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
