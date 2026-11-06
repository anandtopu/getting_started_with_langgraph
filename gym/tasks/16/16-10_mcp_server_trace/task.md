# 16-10 — Diagnose mcp server from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

MCP describes tools with names and JSON schemas. The official SDK validates requests before calling the function. This local service exposes only synthetic triage reads and capability discovery; it has no payment or arbitrary filesystem operation. stdio is the protocol channel, so diagnostics belong on stderr.

## Your task

Diagnose mcp server from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

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

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Invoke a tool from the published MCP registry."
- "Pass the requested synthetic claim through schema validation."
- "Dispatch both registered tools rather than only read_claim."
- "Publish the complete permitted capability list."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 16-10
uv run gym check 16-10
uv run gym hint 16-10
```

## Reading

[Module lesson](../../../../modules/16_external_systems_and_mcp/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/mcp)
