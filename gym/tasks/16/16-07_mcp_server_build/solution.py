"""Build mcp server: Invoke a tool from the published MCP registry.. Run this file with Python. No live model or network."""

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


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
