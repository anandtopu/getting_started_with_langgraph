# 13-10 — Diagnose schema adapters from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

When parent and child schemas differ, call the child inside an adapter node. Map the input fields explicitly, then return only the public finding. Private child fields should not become parent state just because a dictionary is convenient to copy.

## Your task

Diagnose schema adapters from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "amount_cents": 600000
  },
  {
    "claim_id": "CLM-0001",
    "amount_cents": 500000
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Map the actual claim amount into the child input."
- "Preserve the exact review threshold."
- "Return the public risk finding rather than private investigation notes."
- "Preserve the parent claim identity across the adapter."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 13-10
uv run gym check 13-10
uv run gym hint 13-10
```

## Reading

[Module lesson](../../../../modules/13_subgraphs/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/use-subgraphs)
