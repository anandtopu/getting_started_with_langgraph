"""Extend mcp server: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

import asyncio
import json

from common.mcp_server import create_server
from common.pretty import print_state

DEFAULT_CASE = {"claim_id": "CLM-0001", "tool_name": "read_claim"}


async def arun(case: dict) -> dict:
    server = create_server()
    tools = await server.list_tools()
    arguments = {"claim_id": case["claim_id"]} if case["tool_name"] == "read_claim" else {}
    response = await server.call_tool(case["tool_name"], arguments)
    # SDK tool calls return content plus structured output when available.
    content = response[0] if isinstance(response, tuple) else response
    text = "".join(item.text for item in content if item.type == "text")
    return {
        "tools": sorted(item.name for item in tools),
        "result": json.loads(text),
        "parameters": sorted(
            next(item.inputSchema for item in tools if item.name == "read_claim")["properties"]
        ),
    }


def run(case: dict | None = None) -> dict:
    return asyncio.run(arun(dict(DEFAULT_CASE if case is None else case)))


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
