# Run the Larkspur application

This is a synthetic teaching application. It uses scripted models, fixed demo identities, local policy fixtures, and a synthetic effect ledger. The deployed graph includes extraction, scoped agents, customer memory, durable estimates and approvals, and a restricted public summary. It does not connect to a payment provider.

## Local application

Install `uv sync --extra apps`. Set distinct random tokens of at least 16 characters in your shell, then start the server:

```powershell
$env:LARKSPUR_CUSTOMER_TOKEN = [guid]::NewGuid().ToString('N')
$env:LARKSPUR_ADJUSTER_TOKEN = [guid]::NewGuid().ToString('N')
uv run --no-sync uvicorn apps.server:build_app --factory --host 127.0.0.1 --port 8000
```

```bash
export LARKSPUR_CUSTOMER_TOKEN="$(python -c 'import secrets; print(secrets.token_hex(24))')"
export LARKSPUR_ADJUSTER_TOKEN="$(python -c 'import secrets; print(secrets.token_hex(24))')"
uv run --no-sync uvicorn apps.server:build_app --factory --host 127.0.0.1 --port 8000
```

In a second terminal run `uv run --no-sync streamlit run apps/dashboard.py`. Open the address printed by Streamlit and enter a demo token in its password field. Create a claim from submission 1, run it, supply the requested estimate, then use the adjuster token to decide each approval. A rejection records no payment effect. Refreshing obtains current interrupt IDs; old decisions receive a conflict response.

The local mode stores SQLite checkpoints and the ownership/effect ledger under `workspace/server`. It supports a single server process. Its long-term Store is in memory and resets on restart; use the Postgres mode for durable cross-thread memory. Checkpoint state and synthetic effects survive a local server restart. Stop with Ctrl+C so saver connections close.

## Docker Compose with Postgres

Copy `.env.example` to ignored `.env` and set `LARKSPUR_DB_PASSWORD`, `LARKSPUR_CUSTOMER_TOKEN`, and `LARKSPUR_ADJUSTER_TOKEN` to distinct generated values. Use a hexadecimal database password so URL construction needs no escaping. Keep the tracing variables false.

```text
docker compose config --quiet
docker compose up --build --wait
```

Open [the dashboard](http://localhost:8501) and [API documentation](http://localhost:8000/docs). Postgres is available only to the Compose network. API and UI ports bind to loopback. The API uses a durable Postgres checkpointer, Store, ownership registry, effect ledger, and transaction-scoped advisory lease. One thread cannot execute in two workers at once.

Pause a claim, run `docker compose restart api`, refresh the dashboard, and resume the saved interrupt. Run `docker compose logs api` to inspect startup failures. `docker compose down` stops the services while preserving the named database volume. Removing that volume destroys course progress and should be a deliberate reset.

## Operational boundaries

- Replace the fixed-token demo authentication with an identity provider and server-side customer/role mapping before exposing an application to real users. TLS belongs at the ingress.
- The request token budget is an admission bound, not a provider billing meter. Live use needs measured token accounting, per-user limits, and bounded tool/model calls.
- SSE reports progress and public letter text. Refresh recovers the saved snapshot; `Last-Event-ID` replay is not implemented. A reconnect must not automatically resubmit the initial input.
- Checkpoint storage, customer memory, application ownership, and effects have distinct retention responsibilities. Delete by verified customer/thread scope and test that another customer's records remain.
- External payment integrations must accept an idempotency key and bind it to a canonical payload. The database ledger demonstrates that contract; it is not a distributed transaction with a bank.
- Collect allowlisted identifiers and durations. Avoid raw customer text, tokens, or full checkpoints in logs. Back up Postgres and test restoring a paused thread before relying on it.
- Run migrations as a controlled startup/deployment step in a real multi-worker service; this demo performs idempotent setup in its application lifecycle.

## Agent Server alternative

Install `uv sync --extra deploy`, then run `uv run --no-sync langgraph dev` from the root. The [export](../apps/studio.py) intentionally leaves checkpoint ownership to Agent Server. The core course uses the direct library API; Agent Server run requests and deployment configuration are introduced in module 22. Managed service credentials, production schedulers, and hosted deployment are optional live operations, not part of offline grading.

[Flagship capstone](../capstones/04_larkspur_claims_copilot/README.md) · [Official deployment guide](https://docs.langchain.com/oss/python/langgraph/deploy)
