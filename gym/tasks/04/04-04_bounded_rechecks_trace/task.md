# 04-04 — Diagnose bounded rechecks from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A loop is an edge back to earlier work. Business state must move toward an exit. recursion_limit is a runtime backstop measured in graph steps, not a replacement for a document-recheck budget.

## Your task

Diagnose bounded rechecks from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "history": [
      false,
      false,
      true
    ],
    "budget": 3
  },
  {
    "history": [
      true
    ],
    "budget": 3
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Received evidence must terminate the recheck loop."
- "Without a changing retry counter, the graph reaches its recursion limit."
- "The business budget needs an explicit exhausted outcome."
- "Equivalent loops must preserve the exact attempt budget."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 04-04
uv run gym check 04-04
uv run gym hint 04-04
```

## Reading

[Module lesson](../../../../modules/04_loops_parallel_map_reduce/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-control-flow)
