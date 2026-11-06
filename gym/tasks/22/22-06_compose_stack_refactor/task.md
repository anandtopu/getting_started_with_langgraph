# 22-06 — Refactor compose stack: Distinguish service readiness from process startup.

Type: refactor. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

The self-hosted stack has an API, Postgres, and a Streamlit UI. Database readiness gates API startup, and API health gates the UI. Required credentials come from the environment; published ports bind to localhost for this teaching deployment. The example validates the committed configuration, while the integration job actually starts the containers and calls the service.

## Your task

Distinguish service readiness from process startup. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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
  },
  {
    "public_bind": false,
    "remove_healthcheck": true
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 22-06
uv run gym check 22-06
uv run gym hint 22-06
```

## Reading

[Module lesson](../../../../modules/22_deployment/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/deploy)
