# 21-08 — Fix approval and limits: Reject an operation above the token admission budget.

Type: fix. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Admission checks reject a planned operation that exceeds the configured call or estimated-token budget. They supplement, rather than replace, runtime model/tool limits and recursion bounds. The API separately verifies role, current interrupt identity, and confirmed coverage before recording a payload-bound synthetic effect. Token estimates are conservative planning inputs, not a guaranteed hosted bill.

## Your task

Reject an operation above the token admission budget. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 21-08
uv run gym check 21-08
uv run gym hint 21-08
```

## Reading

[Module lesson](../../../../modules/21_security_and_guardrails/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/interrupts)
