# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_entrypoints_tasks.py using one claim from its input cases.
2. Diagnose this broken behavior: Match the Graph API fast-track boundary. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_parallel_futures.py using one claim from its input cases.
4. Diagnose this broken behavior: Preserve every parallel graph result. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_functional_resume.py using one claim from its input cases.
6. Diagnose this broken behavior: Validate the resumed approval before returning a business result. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. An entrypoint accepts one serializable input and uses ordinary Python branches. A task call schedules durable work and returns a future; result() obtains its value. This supports familiar control flow without removing the need for validated inputs and deterministic replay order.
2. Match the Graph API fast-track boundary. Compare the normal case with the boundary fixtures and identify the first differing update.
3. Create all task futures before resolving them to allow concurrent work. Collect results in a canonical order so scheduling differences do not change the business answer. The equivalent Send graph lets you compare the same finding function across the Graph and Functional APIs, including an empty document list.
4. Preserve every parallel graph result. Compare the normal case with the boundary fixtures and identify the first differing update.
5. Resuming a Functional API interrupt restarts the entrypoint from its beginning. Completed task results are retrieved from checkpoints, so the task body need not run again. Keep task ordering deterministic and validate the resume payload. External effects still require their own idempotency at the crash window.
6. Validate the resumed approval before returning a business result. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
