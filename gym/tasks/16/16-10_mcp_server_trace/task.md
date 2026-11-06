# 16-10 — Trace mcp server: Pass the requested synthetic claim through schema validation.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

MCP describes tools with names and JSON schemas. The official SDK validates requests before calling the function. This local service exposes only synthetic triage reads and capability discovery; it has no payment or arbitrary filesystem operation. stdio is the protocol channel, so diagnostics belong on stderr.

## Your task

Pass the requested synthetic claim through schema validation. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "tool_name": "read_claim"
  },
  {
    "claim_id": "CLM-0002",
    "tool_name": "read_claim"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 16-10
uv run gym check 16-10
uv run gym hint 16-10
```

## Reading

[Module lesson](../../../../modules/16_external_systems_and_mcp/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/mcp)
