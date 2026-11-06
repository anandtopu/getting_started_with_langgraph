# 18-03 — Predict async streams across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

ainvoke awaits one result; astream yields intermediate parts. Pass RunnableConfig into async model calls for explicit context propagation. The seven v2 modes expose different views, so count types rather than assuming one common payload. Cancellation must await cleanup; a browser disconnect is not proof that an external effect was rolled back.

## Your task

Predict async streams across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "text": "Your estimate is ready.",
    "cancel": true
  },
  {
    "text": "Documents ready.",
    "cancel": false
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 18-03
uv run gym check 18-03
uv run gym hint 18-03
```

## Reading

[Module lesson](../../../../modules/18_streaming_user_interfaces/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/streaming)
