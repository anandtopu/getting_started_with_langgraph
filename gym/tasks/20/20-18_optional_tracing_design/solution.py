"""Executable design constraints; the written rubric remains essential."""

from common.pretty import print_state


def run(case: dict | None = None) -> dict:
    return {"correction": "retained_branch", "evidence": "local_checkpoints", "tracing": "optional"}


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
