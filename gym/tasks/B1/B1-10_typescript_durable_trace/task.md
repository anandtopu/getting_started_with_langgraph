# B1-10 — Trace typescript durable: Accept explicit boolean decisions and reject strings at the interrupt boundary.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

JavaScript Send fans out document work, SqliteSaver retains the approval pause, and Command resumes it. The saver connection is explicitly closed. JavaScript uses camelCase options such as streamMode and returns its documented update shape; this lesson intentionally does not copy Python invocation parameters.

## Your task

Accept explicit boolean decisions and reject strings at the interrupt boundary. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "documents": [
      "estimate",
      "receipt"
    ],
    "approved": false
  },
  {
    "documents": [],
    "approved": true
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B1-10
uv run gym check B1-10
uv run gym hint B1-10
```

## Reading

[Module lesson](../../../../modules/bonus/B1_langgraph_js/README.md) · [Official guide](https://docs.langchain.com/oss/javascript/langgraph/interrupts)
