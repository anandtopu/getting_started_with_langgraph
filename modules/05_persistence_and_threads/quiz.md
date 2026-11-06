# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_thread_identity.py using one claim from its input cases.
2. Diagnose this broken behavior: A persisted invocation needs an explicit thread identifier. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_sqlite_lifetime.py using one claim from its input cases.
4. Diagnose this broken behavior: A compiled graph cannot use a saver whose connection has closed. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_inspect_checkpoints.py using one claim from its input cases.
6. Diagnose this broken behavior: Continue the configuration returned by update_state, not an unrelated checkpoint. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. A checkpointer saves graph state under a thread ID. New input on that thread starts another run against its saved state. Resuming a pending operation is different: use the saved continuation or an interrupt response rather than pretending it is a new claim.
2. A persisted invocation needs an explicit thread identifier. Compare the normal case with the boundary fixtures and identify the first differing update.
3. Memory persistence ends with its process. A SQLite saver stores checkpoints on disk and must remain open for every invocation that uses it. Explicit context managers release connections, including on Windows where open files can prevent cleanup.
4. A compiled graph cannot use a saver whose connection has closed. Compare the normal case with the boundary fixtures and identify the first differing update.
5. A StateSnapshot contains values, pending next nodes, metadata, and a parent configuration. update_state writes a new checkpoint; it does not edit old history. Durability chooses when checkpoint writes complete, which changes failure exposure rather than business routing.
6. Continue the configuration returned by update_state, not an unrelated checkpoint. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
