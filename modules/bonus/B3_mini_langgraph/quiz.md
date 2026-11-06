# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_channels_and_steps.py using one claim from its input cases.
2. Diagnose this broken behavior: Report the previous-boundary view seen by each worker. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_mini_reducers.py using one claim from its input cases.
4. Diagnose this broken behavior: Retain the overwrite-conflict case in the real runtime comparison. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_mini_checkpoints.py using one claim from its input cases.
6. Diagnose this broken behavior: Validate the resumed decision before updating approval state. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. The educational runner snapshots state before a superstep, collects writes from every sibling, then applies them at a barrier. Thus both workers see zero prior findings while the next-step summary sees both. This small runner explains visibility; it deliberately omits production concurrency, async execution, pending-write recovery, and serialization.
2. Report the previous-boundary view seen by each worker. Compare the normal case with the boundary fixtures and identify the first differing update.
3. An overwrite channel accepts one update per superstep; multiple writers need a reducer. This comparison runs the same policy and estimate findings in the mini runner and real LangGraph, normalizing their different exception classes to one conflict observation. Canonical output order is separate from the algebra used to merge writes.
4. Retain the overwrite-conflict case in the real runtime comparison. Compare the normal case with the boundary fixtures and identify the first differing update.
5. A checkpoint stores state and the next scheduled work for one thread. The mini runner copies snapshots so external mutation cannot corrupt history. Its single-node pause records a request and resumes the same pending node with a checked decision; another thread remains independent. This is a teaching representation, not LangGraph's full interrupt protocol.
6. Validate the resumed decision before updating approval state. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
