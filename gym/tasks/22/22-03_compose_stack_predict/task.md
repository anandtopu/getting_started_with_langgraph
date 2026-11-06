# 22-03 — Predict compose stack across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

The self-hosted stack has an API, Postgres, and a Streamlit UI. Database readiness gates API startup, and API health gates the UI. Required credentials come from the environment; published ports bind to localhost for this teaching deployment. The example validates the committed configuration, while the integration job actually starts the containers and calls the service.

## Your task

Predict compose stack across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 22-03
uv run gym check 22-03
uv run gym hint 22-03
```

## Reading

[Module lesson](../../../../modules/22_deployment/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/deploy)
