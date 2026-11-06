# 22-04 — Diagnose compose stack from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

The self-hosted stack has an API, Postgres, and a Streamlit UI. Database readiness gates API startup, and API health gates the UI. Required credentials come from the environment; published ports bind to localhost for this teaching deployment. The example validates the committed configuration, while the integration job actually starts the containers and calls the service.

## Your task

Diagnose compose stack from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "public_bind": false,
    "remove_healthcheck": false
  },
  {
    "public_bind": true,
    "remove_healthcheck": false
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Reject a database without a readiness check."
- "Detect accidental public binding of the teaching service."
- "Do not mark a stack valid after detecting a deployment error."
- "Distinguish service readiness from process startup."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 22-04
uv run gym check 22-04
uv run gym hint 22-04
```

## Reading

[Module lesson](../../../../modules/22_deployment/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/deploy)
