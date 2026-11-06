# 04-04 — Trace bounded rechecks: Without a changing retry counter, the graph reaches its recursion limit.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A loop is an edge back to earlier work. Business state must move toward an exit. recursion_limit is a runtime backstop measured in graph steps, not a replacement for a document-recheck budget.

## Your task

Without a changing retry counter, the graph reaches its recursion limit. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 04-04
uv run gym check 04-04
uv run gym hint 04-04
```

## Reading

[Module lesson](../../../../modules/04_loops_parallel_map_reduce/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-control-flow)
