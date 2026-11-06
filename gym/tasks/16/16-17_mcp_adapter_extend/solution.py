"""Extend mcp adapter: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.. Run this file with Python. No live model or network."""

import asyncio
import json
import sys

from langchain.agents import create_agent
from langchain_core.messages import AIMessage, HumanMessage

from common.config import ROOT
from common.models import get_chat_model
from common.pretty import print_state
from common.process import offline_environment

DEFAULT_CASE = {"claim_id": "CLM-0001"}


async def arun(case: dict) -> dict:
    from langchain_mcp_adapters.client import MultiServerMCPClient
    from langchain_mcp_adapters.tools import load_mcp_tools

    client = MultiServerMCPClient(
        {
            "claims": {
                "transport": "stdio",
                "command": sys.executable,
                "args": ["-m", "common.offline", str(ROOT / "common/mcp_server.py")],
                "env": offline_environment(),
                "cwd": str(ROOT),
            }
        }
    )
    # KEY IDEA: adapted tools live inside the explicitly owned session lifetime.
    async with client.session("claims") as session:
        tools = await load_mcp_tools(session)
        model = get_chat_model(
            responses=[
                AIMessage(
                    content="",
                    tool_calls=[
                        {
                            "name": "read_claim",
                            "args": {"claim_id": case["claim_id"]},
                            "id": "mcp-1",
                        }
                    ],
                ),
                AIMessage(content="Synthetic evidence read; no payment capability was exposed."),
            ]
        )
        agent = create_agent(model=model, tools=tools)
        result = await agent.ainvoke(
            {"messages": [HumanMessage(content="Read this synthetic claim.")]}, version="v2"
        )
    messages = result.value["messages"]
    tool_message = next(item for item in messages if item.type == "tool")
    content = tool_message.content
    text = (
        content if isinstance(content, str) else "".join(block.get("text", "") for block in content)
    )
    return {
        "tools": sorted(item.name for item in tools),
        "roles": [item.type for item in messages],
        "tool_call_ids": [item.tool_call_id for item in messages if item.type == "tool"],
        "claim": json.loads(text),
        "final": messages[-1].content,
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
