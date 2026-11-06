# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_local_visual_debugging.py using one claim from its input cases.
2. Diagnose this broken behavior: Debug the supplied claim amount rather than a substituted value. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_structured_logs.py using one claim from its input cases.
4. Diagnose this broken behavior: Attach each log record to its actual node. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_optional_tracing.py using one claim from its input cases.
6. Diagnose this broken behavior: Fork at the intended pre-routing boundary. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. langgraph.json maps a public graph name to a Python export. The local Agent Server hosts that graph; Studio adds a visual client and may require an account. Without Studio, draw_mermaid, updates, and checkpoint snapshots still reveal the route and pause. The export leaves persistence to the server instead of constructing its own competing saver.
2. Debug the supplied claim amount rather than a substituted value. Compare the normal case with the boundary fixtures and identify the first differing update.
3. Structured logs are small machine-readable records correlated by thread and run. An allowlist excludes raw prompts, contact details, and credentials rather than hoping a redactor recognizes every secret. Random run identifiers belong in operational logs but should be normalized out of teaching snapshots.
4. Attach each log record to its actual node. Compare the normal case with the boundary fixtures and identify the first differing update.
5. LangSmith tracing is optional and independent of checkpoint persistence. A local trace can show an old route, locate the checkpoint before routing, fork with corrected data, and retain the original history. This example explicitly disables remote tracing. Enable hosted tracing only for sanitized data and an account you intend to use.
6. Fork at the intended pre-routing boundary. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
