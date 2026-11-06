"""Executable design constraints; the written rubric remains essential."""

from common.pretty import print_state


def run(case: dict | None = None) -> dict:
    return {
        "amount": "bounded_integer_cents",
        "date": "iso_date_validation",
        "response_address": "interrupt_id",
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
