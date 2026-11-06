"""Executable design constraints; the written rubric remains essential."""

from common.pretty import print_state


def run(case: dict | None = None) -> dict:
    return {
        "effects": "idempotent_boundary",
        "replay": "entrypoint_restarts",
        "task_results": "checkpoint_reuse",
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
