# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_approve_or_reject.py using one claim from its input cases.
2. Diagnose this broken behavior: An interrupt needs persistence to resume the saved task. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_collect_and_edit.py using one claim from its input cases.
4. Diagnose this broken behavior: Each interrupt must receive the response for its own request kind. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_safe_reentry.py using one claim from its input cases.
6. Diagnose this broken behavior: Effects before interrupt repeat when the node restarts. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. interrupt pauses graph work and returns a request to the caller. A checkpointer and stable thread preserve that pause. Command(resume=...) supplies the response; the interrupted node restarts, so validate the response rather than trusting its shape.
2. An interrupt needs persistence to resume the saved task. Compare the normal case with the boundary fixtures and identify the first differing update.
3. Parallel pauses can be answered with an interrupt-ID-to-response map. IDs identify requests; list order does not. Validate each edited value against its own schema and business limit before merging it into state.
4. Each interrupt must receive the response for its own request kind. Compare the normal case with the boundary fixtures and identify the first differing update.
5. On resume, Python starts the interrupted node again. Code before interrupt can therefore repeat. Move effects after validated approval into separate checkpointed work, and use a stable idempotency key because a crash can occur after a write but before its checkpoint.
6. Effects before interrupt repeat when the node restarts. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
