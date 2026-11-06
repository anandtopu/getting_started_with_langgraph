"""Executable design constraints; the written rubric remains essential."""

from common.pretty import print_state


def run(case: dict | None = None) -> dict:
    return {
        "payout_write": "idempotency_before_retry",
        "policy_read": "retry_and_scoped_cache",
        "ttl_test": "injected_clock",
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
