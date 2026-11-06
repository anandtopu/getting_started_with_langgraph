# 08-11 — Extend message identity: Make retention conditional on the requested minimization policy.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

MessagesState applies add_messages: a matching message ID replaces a message instead of appending a duplicate. RemoveMessage deletes by that same ID. Tool responses still need the tool_call_id from their AI request; message identity and tool-call identity serve different purposes.

## Your task

Make retention conditional on the requested minimization policy. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 08-11
uv run gym check 08-11
uv run gym hint 08-11
```

## Reading

[Module lesson](../../../../modules/08_llms_inside_nodes/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-state)
