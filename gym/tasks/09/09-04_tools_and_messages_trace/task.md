# 09-04 — Trace tools and messages: Return a correlated tool error for an unknown policy.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A tool's typed parameters become a schema the model can request. ToolNode runs the requested function and returns a ToolMessage with the original call ID. Expected lookup failures become error messages when error handling is enabled. A payout calculator proposes cents; it does not transfer money.

## Your task

Return a correlated tool error for an unknown policy. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "policy_id": "POL-0001",
    "amount_cents": 125000
  },
  {
    "policy_id": "MISSING",
    "amount_cents": 125000
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 09-04
uv run gym check 09-04
uv run gym hint 09-04
```

## Reading

[Module lesson](../../../../modules/09_tools_and_agent_loop/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/tools)
