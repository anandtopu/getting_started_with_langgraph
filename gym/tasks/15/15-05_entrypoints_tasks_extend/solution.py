"""Extend entrypoints tasks: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

from langgraph.func import entrypoint, task

from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001", "description": "  Pipe burst  ", "amount_cents": 125000}


@task
def normalize(claim: dict) -> dict:
    if type(claim["amount_cents"]) is not int or claim["amount_cents"] < 0:
        raise ValueError("Amount must be nonnegative integer cents")
    return {**claim, "description": claim["description"].strip()}


@task
def route(claim: dict) -> str:
    return "fast_track" if claim["amount_cents"] <= 100000 else "standard"


@entrypoint()
def intake(claim: dict) -> dict:
    # KEY IDEA: a task call returns a future; result() obtains its completed value.
    cleaned = normalize(claim).result()
    destination = route(cleaned).result() if cleaned["description"] else "needs_information"
    return {**cleaned, "route": destination}


def run(case: dict | None = None) -> dict:
    return intake.invoke(dict(DEFAULT_CASE if case is None else case), version="v2").value


def run_batch(cases: list[dict]) -> list[dict]:
    """Preview independent claims in order; one rejected input must not lose its siblings.

    This sequential interface favors isolation over throughput. It is not a shared
    checkpoint thread or a promise of transaction atomicity.
    """
    from copy import deepcopy

    from common.pretty import safe_value

    results = []
    for case in cases:
        try:
            results.append({"value": safe_value(run(deepcopy(case)))})
        except Exception as error:
            results.append({"error": type(error).__name__})
    return results


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
