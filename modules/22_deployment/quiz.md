# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_compose_stack.py using one claim from its input cases.
2. Diagnose this broken behavior: Detect accidental public binding of the teaching service. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_worker_reliability.py using one claim from its input cases.
4. Diagnose this broken behavior: Report that a competing run was excluded. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_managed_deployment.py using one claim from its input cases.
6. Diagnose this broken behavior: Keep interactive waiting distinct from background execution. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. The self-hosted stack has an API, Postgres, and a Streamlit UI. Database readiness gates API startup, and API health gates the UI. Required credentials come from the environment; published ports bind to localhost for this teaching deployment. The example validates the committed configuration, while the integration job actually starts the containers and calls the service.
2. Detect accidental public binding of the teaching service. Compare the normal case with the boundary fixtures and identify the first differing update.
3. Stateless workers share durable checkpoints, ownership records, and effect keys. One active run may mutate a thread at a time. The local registry demonstrates lease exclusion within one process; the Postgres implementation uses a transaction-scoped advisory lock across workers. A new ledger instance proves that idempotency survives worker replacement, and conflicting payloads are rejected.
4. Report that a competing run was excluded. Compare the normal case with the boundary fixtures and identify the first differing update.
5. An assistant selects graph configuration, a thread identifies persisted state, and a run is one execution. Agent Server supports background runs; LangSmith Deployment adds managed hosting and scheduled jobs subject to account access and current pricing. This offline request planner creates no hosted resources. The explicit SDK function requires a caller-supplied authenticated client and full graph input.
6. Keep interactive waiting distinct from background execution. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
