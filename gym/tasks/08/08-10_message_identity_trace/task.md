# 08-10 — Trace message identity: Correct an existing message without appending another customer message.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

MessagesState applies add_messages: a matching message ID replaces a message instead of appending a duplicate. RemoveMessage deletes by that same ID. Tool responses still need the tool_call_id from their AI request; message identity and tool-call identity serve different purposes.

## Your task

Correct an existing message without appending another customer message. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 08-10
uv run gym check 08-10
uv run gym hint 08-10
```

## Reading

[Module lesson](../../../../modules/08_llms_inside_nodes/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-state)
