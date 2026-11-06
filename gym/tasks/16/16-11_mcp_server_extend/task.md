# 16-11 — Extend mcp server: Dispatch both registered tools rather than only read_claim.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

MCP describes tools with names and JSON schemas. The official SDK validates requests before calling the function. This local service exposes only synthetic triage reads and capability discovery; it has no payment or arbitrary filesystem operation. stdio is the protocol channel, so diagnostics belong on stderr.

## Your task

Dispatch both registered tools rather than only read_claim. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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
  },
  {
    "claim_id": "../../private",
    "tool_name": "read_claim"
  },
  {
    "claim_id": "CLM-0001",
    "tool_name": "list_capabilities"
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 16-11
uv run gym check 16-11
uv run gym hint 16-11
```

## Reading

[Module lesson](../../../../modules/16_external_systems_and_mcp/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/mcp)
