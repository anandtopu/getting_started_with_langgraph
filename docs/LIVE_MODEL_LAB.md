# From a scripted model to real inference

The graded course uses scripted models. Their responses are fixtures, so a passing test demonstrates orchestration and validation, not extraction accuracy or resistance to every prompt injection. This optional lab uses the same provider factory for real structured extraction, a scoped tool agent, and a two-turn conversation with checkpointed memory.

First run the free, deterministic version:

```text
uv run --no-sync python scripts/live_claim_lab.py
```

For local inference, install the Ollama extra, start Ollama, download a model that supports tools and structured output, and set `LLM_PROVIDER=ollama` and `LLM_MODEL` in your local `.env`. For a hosted provider, use its extra and credentials from [.env.example](../.env.example). Follow [optional dependencies](OPTIONAL_DEPENDENCIES.md), then:

```text
uv run --no-sync python scripts/check_env.py --live
uv run --no-sync python scripts/live_claim_lab.py --live --scenario extract
uv run --no-sync python scripts/live_claim_lab.py --live --scenario tools
uv run --no-sync python scripts/live_claim_lab.py --live --scenario memory
```

Predict the amount in integer cents, the authorized tool, and the number of messages before running. Compare live and fake results. A valid schema does not prove a fact is correct. Inspect the policy tool result before accepting the answer; an agent can choose not to call a tool. Conversation memory belongs to the configured thread and is lost when this in-memory lab exits.

The extraction experiment makes one model call; memory makes two. Tool selection is variable and bounded by a recursion limit of eight. Response lengths and request timeouts come from the provider settings. Hosted calls can cost money; check your provider's prices and usage limits. This is a small experiment, not a total-spend enforcement system. No action sends a message or records a payment.

Provider capabilities differ. A tool/schema error is evidence to inspect, not a reason to silently substitute a fake model. The optional live test is skipped unless explicitly enabled:

```text
uv run --no-sync pytest tests/test_live_claim_lab.py -m live --live
```

Use extraction after module 08, tool use after modules 09–10, and memory after module 11. The remaining graded workflow lessons stay deterministic so outcomes can be compared exactly.
