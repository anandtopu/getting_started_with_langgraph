# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_bounded_rechecks.py using one claim from its input cases.
2. Diagnose this broken behavior: Without a changing retry counter, the graph reaches its recursion limit. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_fan_out_fan_in.py using one claim from its input cases.
4. Diagnose this broken behavior: Parallel writes to an overwrite channel conflict. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_retry_and_cache.py using one claim from its input cases.
6. Diagnose this broken behavior: Customer identity belongs in the cache key. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. A loop is an edge back to earlier work. Business state must move toward an exit. recursion_limit is a runtime backstop measured in graph steps, not a replacement for a document-recheck budget.
2. Without a changing retry counter, the graph reaches its recursion limit. Compare the normal case with the boundary fixtures and identify the first differing update.
3. Send creates one worker invocation per item with its own input. Parallel workers need a reducer when they write the same channel. defer waits for pending work, which matters when one branch takes more steps than another.
4. Parallel writes to an overwrite channel conflict. Compare the normal case with the boundary fixtures and identify the first differing update.
5. Retry a transient failure only when repeating the operation is safe. A cache stores a node result under a key; the key must include every input that changes that result. TTL expires a result after a duration, and an injected clock makes that behavior testable without sleeping.
6. Customer identity belongs in the cache key. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
