"""Executable design constraints; the written rubric remains essential."""

from common.pretty import print_state


def run(case: dict | None = None) -> dict:
    return {
        "retries": "transient_only",
        "shutdown": "cooperative_drain",
        "timeout": "async_attempt",
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
