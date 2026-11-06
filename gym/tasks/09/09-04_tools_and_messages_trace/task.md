# 09-04 — Diagnose tools and messages from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A tool's typed parameters become a schema the model can request. ToolNode runs the requested function and returns a ToolMessage with the original call ID. Expected lookup failures become error messages when error handling is enabled. A payout calculator proposes cents; it does not transfer money.

## Your task

Diagnose tools and messages from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

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

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Apply the deductible before proposing a payout."
- "Return a correlated tool error for an unknown policy."
- "Cap the proposal at the synthetic coverage limit."
- "Preserve the call identity rather than substituting the tool name."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 09-04
uv run gym check 09-04
uv run gym hint 09-04
```

## Reading

[Module lesson](../../../../modules/09_tools_and_agent_loop/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/tools)
