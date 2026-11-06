# 08-09 — Predict message identity across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

MessagesState applies add_messages: a matching message ID replaces a message instead of appending a duplicate. RemoveMessage deletes by that same ID. Tool responses still need the tool_call_id from their AI request; message identity and tool-call identity serve different purposes.

## Your task

Predict message identity across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "text": "Corrected: pipe burst",
    "remove_customer": true
  },
  {
    "text": "Corrected: pipe burst",
    "remove_customer": false
  },
  {
    "text": "Corrected: theft",
    "remove_customer": false
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 08-09
uv run gym check 08-09
uv run gym hint 08-09
```

## Reading

[Module lesson](../../../../modules/08_llms_inside_nodes/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-state)
