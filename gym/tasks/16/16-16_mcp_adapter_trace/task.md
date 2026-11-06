# 16-16 — Trace mcp adapter: Send the selected claim identifier to the MCP service.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

MultiServerMCPClient loads tool definitions from a real local stdio subprocess. The adapter turns them into LangChain tools while an explicit client session owns their lifetime. The pinned adapter supports MCP SDK 1.x. The newer langchain.mcp successor is Beta and is documented separately instead of silently mixing incompatible APIs.

## Your task

Send the selected claim identifier to the MCP service. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001"
  },
  {
    "claim_id": "CLM-0002"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 16-16
uv run gym check 16-16
uv run gym hint 16-16
```

## Reading

[Module lesson](../../../../modules/16_external_systems_and_mcp/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/mcp)
