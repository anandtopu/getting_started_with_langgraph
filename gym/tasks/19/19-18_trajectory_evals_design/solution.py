"""Executable design constraints; the written rubric remains essential."""

from common.pretty import print_state


def run(case: dict | None = None) -> dict:
    return {"arguments": "exact", "order": "business_contract", "trajectory": "tool_requests"}


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
