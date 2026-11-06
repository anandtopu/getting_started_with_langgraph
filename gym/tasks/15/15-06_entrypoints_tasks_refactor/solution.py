"""Refactor entrypoints tasks: Convert the working Graph API pipeline to an entrypoint with normalize and route tasks, preserving every existing result and validation error.. Run this file with Python. No live model or network."""

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


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
