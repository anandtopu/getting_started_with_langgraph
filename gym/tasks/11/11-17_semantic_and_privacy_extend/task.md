# 11-17 — Extend semantic and privacy: Delete the requested memory while preserving unrelated evidence.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

An embedding maps text into numbers so the Store can rank similarity within a namespace. These transparent word vectors make the offline ranking reproducible. Store deletion does not delete old checkpoint contents: retention must handle both systems separately. Retrieval is evidence selection, never an authorization check.

## Your task

Delete the requested memory while preserving unrelated evidence. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "query": "water leak",
    "customer_id": "CUS-0001"
  },
  {
    "query": "theft",
    "customer_id": "CUS-0001"
  },
  {
    "query": "unrelated",
    "customer_id": "CUS-0040"
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 11-17
uv run gym check 11-17
uv run gym hint 11-17
```

## Reading

[Module lesson](../../../../modules/11_memory/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/memory)
