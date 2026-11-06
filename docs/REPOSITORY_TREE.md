# Repository tree

This is the shipped structure. The [complete manifest](planning/REPOSITORY_MANIFEST.txt) enumerates every file; runtime workspaces, environments, caches, and Node dependencies are excluded.

```text
getting_started_with_langgraph/
├── README.md / LEARNING_PATH.md / CONTRIBUTING.md / LICENSE
├── pyproject.toml / uv.lock / .python-version / .env.example
├── package.json / package-lock.json / tsconfig.json
├── Dockerfile / compose.yaml / langgraph.json
├── .github/workflows/ci.yml
├── apps/                       # API, dashboard, server lifecycle, Studio export
├── common/                     # Models, fakes, data, persistence, security, stream helpers
│   └── copilot/v00.py … v11.py
├── data/                       # Synthetic database, 60 submissions, 30 PDF/TXT pairs, 20 emails
├── gym/
│   └── tasks/                  # 486 task packages across 27 modules
├── modules/
│   ├── 00_setup/
│   ├── 01_your_first_graph/
│   ├── 02_state_and_reducers/
│   ├── 03_branching_and_routing/
│   ├── 04_loops_parallel_map_reduce/
│   ├── 05_persistence_and_threads/
│   ├── 06_human_in_the_loop/
│   ├── 07_time_travel_and_streaming/
│   ├── 08_llms_inside_nodes/
│   ├── 09_tools_and_agent_loop/
│   ├── 10_prebuilt_agents/
│   ├── 11_memory/
│   ├── 12_workflow_patterns/
│   ├── 13_subgraphs/
│   ├── 14_multi_agent_systems/
│   ├── 15_functional_api/
│   ├── 16_external_systems_and_mcp/
│   ├── 17_durable_execution/
│   ├── 18_streaming_user_interfaces/
│   ├── 19_testing_and_evaluation/
│   ├── 20_observability_and_debugging/
│   ├── 21_security_and_guardrails/
│   ├── 22_deployment/
│   ├── bonus/B1_langgraph_js/
│   ├── bonus/B2_deep_agents/
│   ├── bonus/B3_mini_langgraph/
│   ├── bonus/B4_whats_new/
│   └── Each lesson: README, diagram, examples, use_case, tests, quiz, notebook
├── capstones/
│   ├── 01_claims_intake_engine/
│   ├── 02_policy_qa_with_memory/
│   ├── 03_fraud_investigation_team/
│   ├── 04_larkspur_claims_copilot/
│   └── 05_design_your_own/
├── cheatsheets/                # Five Markdown guides and five single-page PDFs
├── docs/                       # Coverage, mental model, design, bugs, glossary, operations
│   ├── planning/               # Machine-readable catalog and shipped manifest
│   └── verification/           # Package checks and actual CI evidence
├── scripts/                    # Setup, generation, evaluation, and acceptance commands
│   └── authoring/              # Exercise contracts and source templates
└── tests/                      # Core, data, models, gym, and application regression tests
```

The original planning document remains in [PHASE_1_PLAN.md](../PHASE_1_PLAN.md). Paths that changed during implementation are represented by the shipped manifest and linked feature map, rather than empty compatibility files.
