# 16-15 — Predict mcp adapter across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

MultiServerMCPClient loads tool definitions from a real local stdio subprocess. The adapter turns them into LangChain tools while an explicit client session owns their lifetime. The pinned adapter supports MCP SDK 1.x. The newer langchain.mcp successor is Beta and is documented separately instead of silently mixing incompatible APIs.

## Your task

Predict mcp adapter across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

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
uv run gym start 16-15
uv run gym check 16-15
uv run gym hint 16-15
```

## Reading

[Module lesson](../../../../modules/16_external_systems_and_mcp/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/mcp)
