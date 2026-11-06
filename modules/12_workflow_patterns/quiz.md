# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_chains_and_gates.py using one claim from its input cases.
2. Diagnose this broken behavior: Stop the chain when the fact gate fails. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_orchestrator_workers.py using one claim from its input cases.
4. Diagnose this broken behavior: Reject a plan that delegates the same section twice. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_evaluator_optimizer.py using one claim from its input cases.
6. Diagnose this broken behavior: Require the authoritative deductible fact. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. Prompt chaining fixes the order of model operations. A deterministic gate compares extracted facts with the authoritative policy before allowing a draft. The validated category can route work, but a model cannot override the gate. A blocked extraction should not consume a drafting call.
2. Stop the chain when the fact gate fails. Compare the normal case with the boundary fixtures and identify the first differing update.
3. An orchestrator proposes a structured plan, then Send creates one worker invocation per section. Validate allowed section names, uniqueness, and size before fan-out. The reducer accumulates independent reports and a deferred assembler produces a canonical order rather than relying on worker completion timing.
4. Reject a plan that delegates the same section twice. Compare the normal case with the boundary fixtures and identify the first differing update.
5. The evaluator names concrete factual and tone defects; the optimizer receives that feedback before another draft. Stop on success or a strict attempt budget. A deterministic substring check is deliberately limited: it teaches loop control and must not be mistaken for a production factuality evaluator.
6. Require the authoritative deductible fact. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
