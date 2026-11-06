# 08-16 — Trace tokens and fakes: Read the documented node name from stream metadata.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

The messages stream emits a chunk and metadata inside each v2 part's data field. Assemble content in order and inspect langgraph_node to attribute it. A fake should agree between invoke and stream, including a structured JSON response; it tests orchestration, not model quality.

## Your task

Read the documented node name from stream metadata. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 08-16
uv run gym check 08-16
uv run gym hint 08-16
```

## Reading

[Module lesson](../../../../modules/08_llms_inside_nodes/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/streaming)
