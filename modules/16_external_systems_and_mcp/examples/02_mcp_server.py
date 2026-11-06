"""Inspect and call the official SDK's local MCP tool registry. Requires the mcp extra.

Run: uv run --extra mcp python modules/16_external_systems_and_mcp/examples/02_mcp_server.py
Expected: two read-only tools; read_claim exposes no customer contact details.
"""

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
    print_state(run())


if __name__ == "__main__":
    main()
