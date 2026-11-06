"""Executable design constraints; the written rubric remains essential."""

from common.pretty import print_state


def run(case: dict | None = None) -> dict:
    # YOUR CODE HERE: choose and justify each policy.
    return {"identities": "unreviewed", "hosting": "unreviewed", "schedule": "unreviewed"}


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
