# 00-10 — Diagnose environment from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

An environment is the interpreter and packages used by one command. A package installed for another interpreter is still missing here. An optional live provider must not block a deterministic checklist.

## Your task

Diagnose environment from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

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

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Required and optional packages are different contracts."
- "A missing provider is a problem only when live mode was requested."
- "A setup report must identify missing committed fixtures."
- "Use the supplied interpreter version; do not assume the recommended version is installed."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 00-10
uv run gym check 00-10
uv run gym hint 00-10
```

## Reading

[Module lesson](../../../../modules/00_setup/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/overview)
