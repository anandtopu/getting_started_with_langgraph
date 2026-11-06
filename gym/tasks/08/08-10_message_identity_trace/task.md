# 08-10 — Diagnose message identity from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

MessagesState applies add_messages: a matching message ID replaces a message instead of appending a duplicate. RemoveMessage deletes by that same ID. Tool responses still need the tool_call_id from their AI request; message identity and tool-call identity serve different purposes.

## Your task

Diagnose message identity from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

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

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Delete by the existing message ID."
- "Correct an existing message without appending another customer message."
- "Make retention conditional on the requested minimization policy."
- "Keep the corrected text when replacing a message."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 08-10
uv run gym check 08-10
uv run gym hint 08-10
```

## Reading

[Module lesson](../../../../modules/08_llms_inside_nodes/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-state)
