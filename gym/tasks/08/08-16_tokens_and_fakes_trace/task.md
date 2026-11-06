# 08-16 — Diagnose tokens and fakes from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

The messages stream emits a chunk and metadata inside each v2 part's data field. Assemble content in order and inspect langgraph_node to attribute it. A fake should agree between invoke and stream, including a structured JSON response; it tests orchestration, not model quality.

## Your task

Diagnose tokens and fakes from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "text": "Larkspur received your synthetic claim.",
    "structured": false
  },
  {
    "text": "Estimate received.",
    "structured": false
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Join chunks without inserting characters that were never emitted."
- "Read the documented node name from stream metadata."
- "Validate the fully assembled structured response."
- "Preserve emission order while collecting token chunks."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 08-16
uv run gym check 08-16
uv run gym hint 08-16
```

## Reading

[Module lesson](../../../../modules/08_llms_inside_nodes/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/streaming)
