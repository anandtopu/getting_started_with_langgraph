"""Executable design constraints; the written rubric remains essential."""

from common.pretty import print_state


def run(case: dict | None = None) -> dict:
    return {
        "acceptance": "known_and_unknown_labels",
        "evidence": "passing_assertions",
        "whitespace": "strip_then_lower",
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
