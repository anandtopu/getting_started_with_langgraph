"""Build managed deployment: Require both assistant configuration and thread identity.. Run this file with Python. No live model or network."""

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
        "run": {"assistant_id": case["assistant_id"], "input": {"claim_id": "CLM-0001"}},
        "mode": "background" if case["background"] else "wait",
        "schedule": case["schedule"],
    }


async def submit_background(client, thread_id: str, assistant_id: str, input_state: dict):
    """Explicit live variant: the caller supplies an authenticated SDK client and full state."""
    return await client.runs.create(thread_id, assistant_id, input=input_state)


def run(case: dict | None = None) -> dict:
    return request_plan(dict(DEFAULT_CASE if case is None else case))


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
