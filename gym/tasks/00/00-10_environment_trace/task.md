# 00-10 — Trace environment: A missing provider is a problem only when live mode was requested.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

An environment is the interpreter and packages used by one command. A package installed for another interpreter is still missing here. An optional live provider must not block a deterministic checklist.

## Your task

A missing provider is a problem only when live mode was requested. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "python": [
      3,
      12
    ],
    "packages": [
      "langgraph",
      "pytest"
    ],
    "data_present": true,
    "live": false,
    "provider_ready": false
  },
  {
    "python": [
      3,
      12
    ],
    "packages": [
      "langgraph",
      "pytest"
    ],
    "data_present": true,
    "live": true,
    "provider_ready": false
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 00-10
uv run gym check 00-10
uv run gym hint 00-10
```

## Reading

[Module lesson](../../../../modules/00_setup/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/overview)
