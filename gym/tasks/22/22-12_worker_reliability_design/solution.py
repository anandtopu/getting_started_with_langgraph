"""Executable design constraints; the written rubric remains essential."""

from common.pretty import print_state


def run(case: dict | None = None) -> dict:
    return {
        "concurrency": "one_run_per_thread",
        "effects": "durable_unique_keys",
        "workers": "stateless",
    }


def main() -> None:
    print_state(run())


if __name__ == "__main__":
    main()
