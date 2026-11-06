# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_durable_side_effects.py using one claim from its input cases.
2. Diagnose this broken behavior: Make the crash supervisor recognize the documented owned-worker exit. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_recovery_policies.py using one claim from its input cases.
4. Diagnose this broken behavior: Do not label an exhausted or timed-out request as successful. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_long_wait_postgres.py using one claim from its input cases.
6. Diagnose this broken behavior: Compute elapsed business time from explicit dates. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. A task result is reusable only after it is checkpointed. This example kills an owned child after the effect ledger commits but before the task returns, then starts a new process. A payload-bound idempotency key prevents duplicate effects even in that gap. sync, async, and exit durability offer different checkpoint guarantees; none makes an external system transactional with the graph.
2. Make the crash supervisor recognize the documented owned-worker exit. Compare the normal case with the boundary fixtures and identify the first differing update.
3. RetryPolicy repeats selected transient failures; TimeoutPolicy bounds asynchronous attempts. After retries are exhausted, a NodeError-aware handler routes to manual review. RunControl requests a cooperative drain after the current superstep, preserving a resumable boundary rather than killing in-flight work. Recovery must not invent a successful external effect.
4. Do not label an exhausted or timed-out request as successful. Compare the normal case with the boundary fixtures and identify the first differing update.
5. An interrupt persists a wait without holding a worker open. The simulated receipt date advances three days while the program itself finishes immediately. Reopening the SQLite saver proves connection-lifetime independence. The same graph includes synchronous and asynchronous Postgres variants; schema setup belongs in startup or migrations, not each request.
6. Compute elapsed business time from explicit dates. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
