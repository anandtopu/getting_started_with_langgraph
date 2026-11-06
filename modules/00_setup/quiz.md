# Quiz

Predict first; explain in your own words.

1. Explain the contract in 02_environment.py using one claim from its input cases.
2. Diagnose this broken behavior: A missing provider is a problem only when live mode was requested. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 03_first_gym.py using one claim from its input cases.
4. Diagnose this broken behavior: Labels need case normalization before comparison. Which observation distinguishes the repair from a default-case-only fix?
5. When is plain Python sufficient for intake?
6. What is the difference between a workflow and an agent?

<details>
<summary>Answers</summary>

1. An environment is the interpreter and packages used by one command. A package installed for another interpreter is still missing here. An optional live provider must not block a deterministic checklist.
2. A missing provider is a problem only when live mode was requested. Compare the normal case with the boundary fixtures and identify the first differing update.
3. An assertion compares an observed result with an explicit requirement. A failing starter is useful when it runs and shows a wrong business result. Hints guide a repair; viewing a solution is recorded separately from independent work.
4. Labels need case normalization before comparison. Compare the normal case with the boundary fixtures and identify the first differing update.
5. Use a plain function for a small fixed calculation without orchestration needs.
6. A workflow follows chosen control flow; an agent selects actions dynamically within explicit limits.

</details>
