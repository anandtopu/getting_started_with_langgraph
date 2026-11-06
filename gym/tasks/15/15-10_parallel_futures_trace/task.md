# 15-10 — Diagnose parallel futures from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Create all task futures before resolving them to allow concurrent work. Collect results in a canonical order so scheduling differences do not change the business answer. The equivalent Send graph lets you compare the same finding function across the Graph and Functional APIs, including an empty document list.

## Your task

Diagnose parallel futures from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "documents": [
      "estimate",
      "receipt",
      "police_report"
    ]
  },
  {
    "documents": []
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Canonicalize Functional API results independently of input order."
- "Preserve every parallel graph result."
- "Keep police-report review semantics shared by both APIs."
- "Schedule every document before resolving task futures."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 15-10
uv run gym check 15-10
uv run gym hint 15-10
```

## Reading

[Module lesson](../../../../modules/15_functional_api/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/functional-api)
