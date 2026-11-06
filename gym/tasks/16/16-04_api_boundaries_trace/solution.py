"""Trace api boundaries: Honor the bounded retry allowance after a lost acknowledgment.. Run this file with Python. No live model or network."""

import asyncio
import json

import httpx

from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001", "transient_failures": 1, "attempts": 3}


async def submit(client: httpx.AsyncClient, claim_id: str, attempts: int) -> dict:
    if type(attempts) is not int or not 1 <= attempts <= 5:
        raise ValueError("Attempts must be one through five")
    for attempt in range(1):
        try:
            response = await client.post(
                "/notifications",
                json={"claim_id": claim_id},
                headers={"Idempotency-Key": "estimate-request:" + claim_id},
                timeout=1,
            )
            response.raise_for_status()
            return response.json()
        except (httpx.TimeoutException, httpx.TransportError):
            if attempt + 1 == attempts:
                raise
            await asyncio.sleep(0)
    raise AssertionError("Retry loop must return or raise")


async def arun(case: dict) -> dict:
    calls, ledger = [], {}

    def transport(request: httpx.Request) -> httpx.Response:
        key = request.headers["Idempotency-Key"]
        payload = json.loads(request.content)
        calls.append(key)
        if key in ledger and ledger[key] != payload:
            return httpx.Response(409, json={"error": "conflicting_payload"})
        ledger[key] = payload
        if len(calls) <= case["transient_failures"]:
            raise httpx.ReadTimeout(
                "Acknowledgment lost after the synthetic write", request=request
            )
        return httpx.Response(200, json={"accepted": True})

    async with httpx.AsyncClient(
        transport=httpx.MockTransport(transport), base_url="https://synthetic.invalid"
    ) as client:
        result = await submit(client, case["claim_id"], case["attempts"])
    return {
        "accepted": result["accepted"],
        "calls": len(calls),
        "effects": len(ledger),
        "keys": calls,
    }


def scenario(case: dict | None = None) -> dict:
    return asyncio.run(arun(dict(DEFAULT_CASE if case is None else case)))


def main() -> None:
    print_state(run())


def run() -> dict:
    observations = []
    for case in [
        {"attempts": 3, "claim_id": "CLM-0001", "transient_failures": 1},
        {"attempts": 3, "claim_id": "CLM-0001", "transient_failures": 0},
    ]:
        try:
            observations.append({"value": scenario(case)})
        except Exception as error:
            observations.append({"error": type(error).__name__})
    return {
        "observations": observations,
        "cause": "Honor the bounded retry allowance after a lost acknowledgment.",
    }


if __name__ == "__main__":
    main()
