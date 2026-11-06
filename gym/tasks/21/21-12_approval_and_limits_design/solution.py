"""Executable design constraints; the written rubric remains essential."""

from common.pretty import print_state


def run(case: dict | None = None) -> dict:
    return {
        "admission": "call_and_token_limits",
        "decision": "authenticated_adjuster",
        "effect": "idempotent_ledger",
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
