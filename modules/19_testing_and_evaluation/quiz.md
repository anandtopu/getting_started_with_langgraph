# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_test_graph_behavior.py using one claim from its input cases.
2. Diagnose this broken behavior: Include boolean cents in invalid-input coverage. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_test_durable_execution.py using one claim from its input cases.
4. Diagnose this broken behavior: Capture the pre-resume pending state before it changes. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_trajectory_evals.py using one claim from its input cases.
6. Diagnose this broken behavior: Check the policy arguments, not only tool names. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. A pytest test is a function whose assertions express requirements. Parametrized tests run it over many inputs. Compare pure node rules and whole graphs against independently specified boundary outcomes; comparing two copies of the same implementation can preserve the same bug. Fake models make orchestration tests repeatable, not model accuracy measurable.
2. Include boolean cents in invalid-input coverage. Compare the normal case with the boundary fixtures and identify the first differing update.
3. Durable tests assert the state before a pause, the pending node, and the resumed result. Snapshot only stable semantic fields, not random checkpoint IDs or timestamps. Reducer algebra can be checked over many generated inputs: associativity and idempotence protect parallel and replay behavior. The process-death test in module 17 covers a failure an in-memory mock cannot reproduce.
4. Capture the pre-resume pending state before it changes. Compare the normal case with the boundary fixtures and identify the first differing update.
5. A trajectory is the sequence of tool requests, separate from the final answer. agentevals can compare strict order, unordered calls, subsets, or supersets. Exact argument matching catches the right tool used on the wrong policy. Choose the matching rule from the business requirement; parallel independent calls may legitimately change order.
6. Check the policy arguments, not only tool names. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
