# 08-17 — Extend tokens and fakes: Validate the fully assembled structured response.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

The messages stream emits a chunk and metadata inside each v2 part's data field. Assemble content in order and inspect langgraph_node to attribute it. A fake should agree between invoke and stream, including a structured JSON response; it tests orchestration, not model quality.

## Your task

Validate the fully assembled structured response. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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
  },
  {
    "text": "{\"claim_type\":\"water\",\"amount_cents\":50,\"confidence\":0.9}",
    "structured": true
  },
  {
    "text": "invalid",
    "structured": true
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 08-17
uv run gym check 08-17
uv run gym hint 08-17
```

## Reading

[Module lesson](../../../../modules/08_llms_inside_nodes/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/streaming)
