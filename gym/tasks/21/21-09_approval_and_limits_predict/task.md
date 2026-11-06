# 21-09 — Predict approval and limits across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

Admission checks reject a planned operation that exceeds the configured call or estimated-token budget. They supplement, rather than replace, runtime model/tool limits and recursion bounds. The API separately verifies role, current interrupt identity, and confirmed coverage before recording a payload-bound synthetic effect. Token estimates are conservative planning inputs, not a guaranteed hosted bill.

## Your task

Predict approval and limits across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "approved": true,
    "planned_calls": 10,
    "call_budget": 12,
    "estimated_tokens": 1000,
    "token_budget": 2000
  },
  {
    "approved": false,
    "planned_calls": 10,
    "call_budget": 12,
    "estimated_tokens": 1000,
    "token_budget": 2000
  },
  {
    "approved": true,
    "planned_calls": 13,
    "call_budget": 12,
    "estimated_tokens": 1000,
    "token_budget": 2000
  },
  {
    "approved": true,
    "planned_calls": 10,
    "call_budget": 12,
    "estimated_tokens": 2001,
    "token_budget": 2000
  },
  {
    "approved": true,
    "planned_calls": true,
    "call_budget": 12,
    "estimated_tokens": 1000,
    "token_budget": 2000
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 21-09
uv run gym check 21-09
uv run gym hint 21-09
```

## Reading

[Module lesson](../../../../modules/21_security_and_guardrails/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/interrupts)
