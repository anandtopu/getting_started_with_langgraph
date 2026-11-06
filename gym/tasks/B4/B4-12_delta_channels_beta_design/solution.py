"""Executable design constraints; the written rubric remains essential."""

from common.pretty import print_state


def run(case: dict | None = None) -> dict:
    return {"migration": "replay_test_old_threads", "reducer": "batch_invariant", "status": "Beta"}


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
