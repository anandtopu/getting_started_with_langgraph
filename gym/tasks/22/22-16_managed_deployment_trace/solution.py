"""Diagnose managed deployment from execution evidence. Run this file with Python. No live model or network."""

from common.data import load_submission
from common.pretty import print_state

DEFAULT_CASE = {
    "assistant_id": "claims",
    "thread_id": "claim-thread",
    "schedule": "0 9 * * 1-5",
    "background": True,
}


def request_plan(case: dict) -> dict:
    if not case["assistant_id"] or not case["thread_id"]:
        raise ValueError("Assistant and thread identifiers are required")
    if len(case["schedule"].split()) != 5:
        raise ValueError("This teaching plan requires a five-field cron expression")
    return {
        "assistant": {"graph_id": case["assistant_id"]},
        "thread": {"thread_id": case["thread_id"]},
        "run": {
            "assistant_id": case["assistant_id"],
            "input": {"claim": load_submission(1), "audit": [], "findings": []},
        },
        "mode": "background",
        "schedule": case["schedule"],
    }


async def submit_background(client, thread_id: str, assistant_id: str, input_state: dict):
    """Explicit live variant: the caller supplies an authenticated SDK client and full state."""
    return await client.runs.create(thread_id, assistant_id, input=input_state)


async def submit_wait(client, thread_id: str, assistant_id: str, input_state: dict):
    """Wait for completion on a persistent thread; the caller owns authentication."""
    return await client.runs.wait(thread_id, assistant_id, input=input_state)


async def submit_ephemeral(client, assistant_id: str, input_state: dict):
    """Use only for work that needs no durable human-response thread."""
    return await client.runs.wait(None, assistant_id, input=input_state)


async def schedule_run(client, thread_id: str, assistant_id: str, input_state: dict, schedule: str):
    """Explicit live action: schedule repeated input. Retain its cron_id for deletion."""
    return await client.crons.create_for_thread(
        thread_id, assistant_id, input=input_state, schedule=schedule
    )


def scenario(case: dict | None = None) -> dict:
    return request_plan(dict(DEFAULT_CASE if case is None else case))


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {
            "assistant_id": "claims",
            "background": True,
            "schedule": "0 9 * * 1-5",
            "thread_id": "claim-thread",
        },
        {
            "assistant_id": "claims",
            "background": False,
            "schedule": "0 9 * * 1-5",
            "thread_id": "claim-thread",
        },
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {
        "observations": observations,
        "cause": "Keep interactive waiting distinct from background execution.",
    }


if __name__ == "__main__":
    main()
