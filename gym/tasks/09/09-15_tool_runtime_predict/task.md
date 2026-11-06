# 09-15 — Predict tool runtime across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

ToolRuntime injects trusted context, graph state, the Store, and tool_call_id without exposing them as model-selectable fields. A tool returning Command can update graph state and acknowledge its own request. Customer identity belongs in authenticated context, not in an argument the model invents.

## Your task

Predict tool runtime across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "customer_id": "CUS-0001",
    "preference": "email"
  },
  {
    "customer_id": "CUS-0020",
    "preference": "sms"
  },
  {
    "customer_id": "CUS-0001",
    "preference": "fax"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 09-15
uv run gym check 09-15
uv run gym hint 09-15
```

## Reading

[Module lesson](../../../../modules/09_tools_and_agent_loop/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/tools)
