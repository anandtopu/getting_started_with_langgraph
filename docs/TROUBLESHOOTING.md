# Troubleshooting

Start with `uv run python scripts/check_env.py`. Run commands from the repository root and retain the failing task ID, selected input, and first error. An installation failure is different from an intentionally wrong starter.

| Symptom | Cause | Repair |
| --- | --- | --- |
| Import from an old tutorial fails or emits a deprecation warning | The tutorial targets a different API family | Compare its spelling and output shape with [the migration guide](MIGRATING_FROM_OLDER_VERSIONS.md); use the lockfile. |
| `No module named ...` in an advanced lesson | Its optional extra is absent, or a plain sync removed it | Follow [optional dependencies](OPTIONAL_DEPENDENCIES.md), then use `uv run --no-sync`. |
| Cannot reach Ollama | The local server is stopped or the configured URL is wrong | Start Ollama; check the URL in `.env`; run `scripts/check_env.py --live`. |
| Model is not downloaded | `.env` selects a model absent from the server | Pull the exact model named in `.env.example`, or choose an installed tool-capable model. |
| Tool-call example produces ordinary text | The selected model does not support the required tool schema | Use a documented tool-capable model and test one tool first. The scripted offline examples remain usable. |
| SQLite reports `database is locked` on Windows | Another process holds a writer or a saver was not closed | Stop that run; use context-managed savers; keep one writer per local thread. Never delete an active database to clear a lock. Use Postgres for multiple workers. |
| SQLite cannot open a database | Parent directory is missing or unwritable | Create a writable workspace directory; keep checkpoints out of the installed package and committed fixtures. |
| `asyncio.run()` cannot run inside Jupyter | Jupyter already owns an event loop | Use top-level `await` for async experiments. Shipped notebooks run canonical scripts in bounded child processes, avoiding a nested event loop and MCP stderr incompatibilities. |
| MCP stdio fails with `fileno` | A notebook's display stream is not an OS file descriptor | Use the supplied child-process notebook cell or run the script in a terminal. Do not print diagnostics to the protocol's stdout. |
| A resume starts a fresh claim | The thread ID changed, or a fresh in-memory saver replaced the original | Reopen the same durable database and resume the same thread. |
| Approval appears twice | The interrupted node restarts from its beginning | Keep pre-interrupt operations repeatable; record external effects with stable payload-bound keys. |
| A customer gets HTTP 403 when approving | Customer access is not adjuster authority | Use the separately configured synthetic adjuster token for the demo; do not weaken the role check. |
| HTTP 409 on resume | The interrupt ID is stale or another run owns the thread | Refresh the snapshot, inspect the new request, and submit its current ID. |
| Dev server cannot import the graph | Wrong working directory, export path, or missing deploy extra | Run from the root, install `deploy`, and inspect `langgraph.json` plus `apps/studio.py`. |
| Port 8000 or 8501 already in use | Another service owns the port | Stop your earlier instance or change the local mapping and dashboard API URL together. |
| Docker cannot connect to its daemon | The engine is stopped or the selected context is unavailable | Start your installed engine and verify `docker version` shows both client and server. |
| Compose reports an unset variable | Required synthetic tokens or database password are absent | Follow [deployment](DEPLOYMENT.md), keeping the two tokens distinct. |
| Postgres rejects a password after editing `.env` | An existing database volume retains the original user password | Restore the matching credential or deliberately rotate it in Postgres. Changing an environment variable does not rewrite an existing database. |
| Postgres connection refused | Wrong hostname, port, or readiness | Inside Compose use `postgres:5432`; outside use an explicitly published address. Wait for health checks. |
| TypeScript says an import cannot be resolved | Node dependencies are absent or Node is too old | Use Node 24, run `npm ci`, then `npm run typecheck`. |
| A Predict task passes only after revealing the answer | The gym distinguishes assistance from independent work | Use the progress report honestly; revisit the concept and make a fresh prediction. |

If a starter exits successfully but its tests fail, that can be expected: starters are runnable faulty programs. Compare the task's declared behavior with its observed output. Do not replace all inputs with a hard-coded sample answer.
