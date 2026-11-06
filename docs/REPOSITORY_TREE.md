# Final repository tree

This is the Phase 1 destination tree for `getting_started_with_langgraph`. It describes the completed course, including future deliverables. Phase 2 now provides the foundation; see [the acceptance report](ACCEPTANCE_REPORT.md) for the implemented scope. The workspace folder can retain its current name while the GitHub repository is named `getting_started_with_langgraph`.

The [complete file manifest](planning/REPOSITORY_MANIFEST.txt) enumerates every planned leaf, including all 486 task folders and their exact files. The compact tree below uses counts only for repeated data and task contents; the manifest resolves them completely. `workspace/` is created by the gym at runtime and is never committed.

```text
getting_started_with_langgraph/
├── README.md
├── LEARNING_PATH.md
├── PHASE_1_PLAN.md
├── pyproject.toml
├── uv.lock
├── .python-version
├── .env.example
├── .gitignore
├── .gitattributes
├── .pre-commit-config.yaml
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
├── .github/
│   ├── workflows/ci.yml
│   ├── ISSUE_TEMPLATE/{bug,content_error,new_task}.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── common/
│   ├── __init__.py
│   ├── models.py, fakes.py, config.py, data.py, pretty.py
│   ├── loading.py, clock.py, schemas.py, tools.py, ledger.py
│   ├── evaluation.py, retrieval.py, security.py, streaming.py
│   ├── mcp_server.py, mcp_client.py, api.py, dashboard.py
│   └── copilot/{__init__,v00,v01,v02,v03,v04,v05,v06,v07,v08,v09,v10,v11}.py
├── data/
│   ├── README.md, manifest.json, claims.db, fraud_rules.yaml
│   ├── policies/{home,renters,condo,flood_add_on,jewelry_add_on}.md
│   ├── claim_submissions/claim_001.json through claim_060.json
│   ├── documents/ (10 estimates, 10 receipts, 10 police summaries; TXT and PDF)
│   ├── emails/email_001.eml through email_020.eml
│   ├── eval/{routing,decisions,final_states,trajectories,security}.jsonl
│   └── security/injected_claim.json
├── modules/
│   ├── 00_setup/
│   │   ├── examples/01_plain_checklist.py
│   │   ├── examples/02_environment.py
│   │   ├── examples/03_first_gym.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 01_your_first_graph/
│   │   ├── examples/01_intake_nodes.py
│   │   ├── examples/02_wire_pipeline.py
│   │   ├── examples/03_draw_and_explain.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 02_state_and_reducers/
│   │   ├── examples/01_schema_contracts.py
│   │   ├── examples/02_reducer_findings.py
│   │   ├── examples/03_state_boundaries.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 03_branching_and_routing/
│   │   ├── examples/01_conditional_router.py
│   │   ├── examples/02_command_routes.py
│   │   ├── examples/03_early_exit.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 04_loops_parallel_map_reduce/
│   │   ├── examples/01_bounded_rechecks.py
│   │   ├── examples/02_fan_out_fan_in.py
│   │   ├── examples/03_retry_and_cache.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 05_persistence_and_threads/
│   │   ├── examples/01_thread_identity.py
│   │   ├── examples/02_sqlite_lifetime.py
│   │   ├── examples/03_inspect_checkpoints.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 06_human_in_the_loop/
│   │   ├── examples/01_approve_or_reject.py
│   │   ├── examples/02_collect_and_edit.py
│   │   ├── examples/03_safe_reentry.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 07_time_travel_and_streaming/
│   │   ├── examples/01_replay_and_fork.py
│   │   ├── examples/02_v2_stream_parts.py
│   │   ├── examples/03_namespaces_and_errors.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 08_llms_inside_nodes/
│   │   ├── examples/01_model_boundary.py
│   │   ├── examples/02_message_identity.py
│   │   ├── examples/03_tokens_and_fakes.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 09_tools_and_agent_loop/
│   │   ├── examples/01_tools_and_messages.py
│   │   ├── examples/02_manual_react.py
│   │   ├── examples/03_tool_runtime.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 10_prebuilt_agents/
│   │   ├── examples/01_create_agent.py
│   │   ├── examples/02_middleware.py
│   │   ├── examples/03_agent_composition.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 11_memory/
│   │   ├── examples/01_short_term_memory.py
│   │   ├── examples/02_store_namespaces.py
│   │   ├── examples/03_semantic_and_privacy.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 12_workflow_patterns/
│   │   ├── examples/01_chains_and_gates.py
│   │   ├── examples/02_orchestrator_workers.py
│   │   ├── examples/03_evaluator_optimizer.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 13_subgraphs/
│   │   ├── examples/01_shared_subgraph.py
│   │   ├── examples/02_schema_adapters.py
│   │   ├── examples/03_subgraph_persistence.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 14_multi_agent_systems/
│   │   ├── examples/01_supervisor_tools.py
│   │   ├── examples/02_handoffs.py
│   │   ├── examples/03_team_tradeoffs.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 15_functional_api/
│   │   ├── examples/01_entrypoints_tasks.py
│   │   ├── examples/02_parallel_futures.py
│   │   ├── examples/03_functional_resume.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 16_external_systems_and_mcp/
│   │   ├── examples/01_api_boundaries.py
│   │   ├── examples/02_mcp_server.py
│   │   ├── examples/03_mcp_adapter.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 17_durable_execution/
│   │   ├── examples/01_durable_side_effects.py
│   │   ├── examples/02_recovery_policies.py
│   │   ├── examples/03_long_wait_postgres.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 18_streaming_user_interfaces/
│   │   ├── examples/01_async_streams.py
│   │   ├── examples/02_sse_api.py
│   │   ├── examples/03_adjuster_dashboard.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 19_testing_and_evaluation/
│   │   ├── examples/01_test_graph_behavior.py
│   │   ├── examples/02_test_durable_execution.py
│   │   ├── examples/03_trajectory_evals.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 20_observability_and_debugging/
│   │   ├── examples/01_local_visual_debugging.py
│   │   ├── examples/02_structured_logs.py
│   │   ├── examples/03_optional_tracing.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 21_security_and_guardrails/
│   │   ├── examples/01_untrusted_input.py
│   │   ├── examples/02_approval_and_limits.py
│   │   ├── examples/03_private_checkpoints.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   ├── 22_deployment/
│   │   ├── examples/01_compose_stack.py
│   │   ├── examples/02_worker_reliability.py
│   │   ├── examples/03_managed_deployment.py
│   │   ├── use_case/claims_copilot.py
│   │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│   └── bonus/
│       ├── B1_langgraph_js/
│       │   ├── examples/01_typescript_state.ts
│       │   ├── examples/02_typescript_durable.ts
│       │   ├── examples/03_typescript_agents.ts
│       │   ├── use_case/claims_copilot.ts
│       │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│       ├── B2_deep_agents/
│       │   ├── examples/01_deep_agent_planning.py
│       │   ├── examples/02_virtual_filesystem.py
│       │   ├── examples/03_deep_subagents.py
│       │   ├── use_case/claims_copilot.py
│       │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│       ├── B3_mini_langgraph/
│       │   ├── examples/01_channels_and_steps.py
│       │   ├── examples/02_mini_reducers.py
│       │   ├── examples/03_mini_checkpoints.py
│       │   ├── use_case/claims_copilot.py
│       │   └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
│       └── B4_whats_new/
│           ├── examples/01_event_streaming_beta.py
│           ├── examples/02_delta_channels_beta.py
│           ├── examples/03_typed_approvals.py
│           ├── use_case/claims_copilot.py
│           └── README.md, notebook.ipynb, quiz.md, diagram.mmd, tests/
├── gym/
│   ├── __init__.py, cli.py, catalog.py, runner.py, progress.py, answers.py
│   ├── manifest.json, pytest_plugin.py
│   └── tasks/
│       ├── 00/
│       │   ├── 00-01_plain_checklist_build/
│       │   ├── 00-02_plain_checklist_fix/
│       │   ├── 00-03_plain_checklist_predict/
│       │   ├── 00-04_plain_checklist_trace/
│       │   ├── 00-05_plain_checklist_extend/
│       │   ├── 00-06_plain_checklist_design/
│       │   ├── 00-07_environment_build/
│       │   ├── 00-08_environment_fix/
│       │   ├── 00-09_environment_predict/
│       │   ├── 00-10_environment_trace/
│       │   ├── 00-11_environment_extend/
│       │   ├── 00-12_environment_refactor/
│       │   ├── 00-13_first_gym_build/
│       │   ├── 00-14_first_gym_fix/
│       │   ├── 00-15_first_gym_predict/
│       │   ├── 00-16_first_gym_trace/
│       │   ├── 00-17_first_gym_extend/
│       │   ├── 00-18_first_gym_design/
│       ├── 01/
│       │   ├── 01-01_intake_nodes_build/
│       │   ├── 01-02_intake_nodes_fix/
│       │   ├── 01-03_intake_nodes_predict/
│       │   ├── 01-04_intake_nodes_trace/
│       │   ├── 01-05_intake_nodes_extend/
│       │   ├── 01-06_intake_nodes_refactor/
│       │   ├── 01-07_wire_pipeline_build/
│       │   ├── 01-08_wire_pipeline_fix/
│       │   ├── 01-09_wire_pipeline_predict/
│       │   ├── 01-10_wire_pipeline_trace/
│       │   ├── 01-11_wire_pipeline_extend/
│       │   ├── 01-12_wire_pipeline_refactor/
│       │   ├── 01-13_draw_and_explain_build/
│       │   ├── 01-14_draw_and_explain_fix/
│       │   ├── 01-15_draw_and_explain_predict/
│       │   ├── 01-16_draw_and_explain_trace/
│       │   ├── 01-17_draw_and_explain_extend/
│       │   ├── 01-18_draw_and_explain_design/
│       ├── 02/
│       │   ├── 02-01_schema_contracts_build/
│       │   ├── 02-02_schema_contracts_fix/
│       │   ├── 02-03_schema_contracts_predict/
│       │   ├── 02-04_schema_contracts_trace/
│       │   ├── 02-05_schema_contracts_extend/
│       │   ├── 02-06_schema_contracts_refactor/
│       │   ├── 02-07_reducer_findings_build/
│       │   ├── 02-08_reducer_findings_fix/
│       │   ├── 02-09_reducer_findings_predict/
│       │   ├── 02-10_reducer_findings_trace/
│       │   ├── 02-11_reducer_findings_extend/
│       │   ├── 02-12_reducer_findings_refactor/
│       │   ├── 02-13_state_boundaries_build/
│       │   ├── 02-14_state_boundaries_fix/
│       │   ├── 02-15_state_boundaries_predict/
│       │   ├── 02-16_state_boundaries_trace/
│       │   ├── 02-17_state_boundaries_extend/
│       │   ├── 02-18_state_boundaries_refactor/
│       ├── 03/
│       │   ├── 03-01_conditional_router_build/
│       │   ├── 03-02_conditional_router_fix/
│       │   ├── 03-03_conditional_router_predict/
│       │   ├── 03-04_conditional_router_trace/
│       │   ├── 03-05_conditional_router_extend/
│       │   ├── 03-06_conditional_router_refactor/
│       │   ├── 03-07_command_routes_build/
│       │   ├── 03-08_command_routes_fix/
│       │   ├── 03-09_command_routes_predict/
│       │   ├── 03-10_command_routes_trace/
│       │   ├── 03-11_command_routes_extend/
│       │   ├── 03-12_command_routes_refactor/
│       │   ├── 03-13_early_exit_build/
│       │   ├── 03-14_early_exit_fix/
│       │   ├── 03-15_early_exit_predict/
│       │   ├── 03-16_early_exit_trace/
│       │   ├── 03-17_early_exit_extend/
│       │   ├── 03-18_early_exit_design/
│       ├── 04/
│       │   ├── 04-01_bounded_rechecks_build/
│       │   ├── 04-02_bounded_rechecks_fix/
│       │   ├── 04-03_bounded_rechecks_predict/
│       │   ├── 04-04_bounded_rechecks_trace/
│       │   ├── 04-05_bounded_rechecks_extend/
│       │   ├── 04-06_bounded_rechecks_refactor/
│       │   ├── 04-07_fan_out_fan_in_build/
│       │   ├── 04-08_fan_out_fan_in_fix/
│       │   ├── 04-09_fan_out_fan_in_predict/
│       │   ├── 04-10_fan_out_fan_in_trace/
│       │   ├── 04-11_fan_out_fan_in_extend/
│       │   ├── 04-12_fan_out_fan_in_refactor/
│       │   ├── 04-13_retry_and_cache_build/
│       │   ├── 04-14_retry_and_cache_fix/
│       │   ├── 04-15_retry_and_cache_predict/
│       │   ├── 04-16_retry_and_cache_trace/
│       │   ├── 04-17_retry_and_cache_extend/
│       │   ├── 04-18_retry_and_cache_design/
│       ├── 05/
│       │   ├── 05-01_thread_identity_build/
│       │   ├── 05-02_thread_identity_fix/
│       │   ├── 05-03_thread_identity_predict/
│       │   ├── 05-04_thread_identity_trace/
│       │   ├── 05-05_thread_identity_extend/
│       │   ├── 05-06_thread_identity_refactor/
│       │   ├── 05-07_sqlite_lifetime_build/
│       │   ├── 05-08_sqlite_lifetime_fix/
│       │   ├── 05-09_sqlite_lifetime_predict/
│       │   ├── 05-10_sqlite_lifetime_trace/
│       │   ├── 05-11_sqlite_lifetime_extend/
│       │   ├── 05-12_sqlite_lifetime_refactor/
│       │   ├── 05-13_inspect_checkpoints_build/
│       │   ├── 05-14_inspect_checkpoints_fix/
│       │   ├── 05-15_inspect_checkpoints_predict/
│       │   ├── 05-16_inspect_checkpoints_trace/
│       │   ├── 05-17_inspect_checkpoints_extend/
│       │   ├── 05-18_inspect_checkpoints_design/
│       ├── 06/
│       │   ├── 06-01_approve_or_reject_build/
│       │   ├── 06-02_approve_or_reject_fix/
│       │   ├── 06-03_approve_or_reject_predict/
│       │   ├── 06-04_approve_or_reject_trace/
│       │   ├── 06-05_approve_or_reject_extend/
│       │   ├── 06-06_approve_or_reject_refactor/
│       │   ├── 06-07_collect_and_edit_build/
│       │   ├── 06-08_collect_and_edit_fix/
│       │   ├── 06-09_collect_and_edit_predict/
│       │   ├── 06-10_collect_and_edit_trace/
│       │   ├── 06-11_collect_and_edit_extend/
│       │   ├── 06-12_collect_and_edit_design/
│       │   ├── 06-13_safe_reentry_build/
│       │   ├── 06-14_safe_reentry_fix/
│       │   ├── 06-15_safe_reentry_predict/
│       │   ├── 06-16_safe_reentry_trace/
│       │   ├── 06-17_safe_reentry_extend/
│       │   ├── 06-18_safe_reentry_refactor/
│       ├── 07/
│       │   ├── 07-01_replay_and_fork_build/
│       │   ├── 07-02_replay_and_fork_fix/
│       │   ├── 07-03_replay_and_fork_predict/
│       │   ├── 07-04_replay_and_fork_trace/
│       │   ├── 07-05_replay_and_fork_extend/
│       │   ├── 07-06_replay_and_fork_refactor/
│       │   ├── 07-07_v2_stream_parts_build/
│       │   ├── 07-08_v2_stream_parts_fix/
│       │   ├── 07-09_v2_stream_parts_predict/
│       │   ├── 07-10_v2_stream_parts_trace/
│       │   ├── 07-11_v2_stream_parts_extend/
│       │   ├── 07-12_v2_stream_parts_refactor/
│       │   ├── 07-13_namespaces_and_errors_build/
│       │   ├── 07-14_namespaces_and_errors_fix/
│       │   ├── 07-15_namespaces_and_errors_predict/
│       │   ├── 07-16_namespaces_and_errors_trace/
│       │   ├── 07-17_namespaces_and_errors_extend/
│       │   ├── 07-18_namespaces_and_errors_design/
│       ├── 08/
│       │   ├── 08-01_model_boundary_build/
│       │   ├── 08-02_model_boundary_fix/
│       │   ├── 08-03_model_boundary_predict/
│       │   ├── 08-04_model_boundary_trace/
│       │   ├── 08-05_model_boundary_extend/
│       │   ├── 08-06_model_boundary_refactor/
│       │   ├── 08-07_message_identity_build/
│       │   ├── 08-08_message_identity_fix/
│       │   ├── 08-09_message_identity_predict/
│       │   ├── 08-10_message_identity_trace/
│       │   ├── 08-11_message_identity_extend/
│       │   ├── 08-12_message_identity_refactor/
│       │   ├── 08-13_tokens_and_fakes_build/
│       │   ├── 08-14_tokens_and_fakes_fix/
│       │   ├── 08-15_tokens_and_fakes_predict/
│       │   ├── 08-16_tokens_and_fakes_trace/
│       │   ├── 08-17_tokens_and_fakes_extend/
│       │   ├── 08-18_tokens_and_fakes_refactor/
│       ├── 09/
│       │   ├── 09-01_tools_and_messages_build/
│       │   ├── 09-02_tools_and_messages_fix/
│       │   ├── 09-03_tools_and_messages_predict/
│       │   ├── 09-04_tools_and_messages_trace/
│       │   ├── 09-05_tools_and_messages_extend/
│       │   ├── 09-06_tools_and_messages_refactor/
│       │   ├── 09-07_manual_react_build/
│       │   ├── 09-08_manual_react_fix/
│       │   ├── 09-09_manual_react_predict/
│       │   ├── 09-10_manual_react_trace/
│       │   ├── 09-11_manual_react_extend/
│       │   ├── 09-12_manual_react_refactor/
│       │   ├── 09-13_tool_runtime_build/
│       │   ├── 09-14_tool_runtime_fix/
│       │   ├── 09-15_tool_runtime_predict/
│       │   ├── 09-16_tool_runtime_trace/
│       │   ├── 09-17_tool_runtime_extend/
│       │   ├── 09-18_tool_runtime_design/
│       ├── 10/
│       │   ├── 10-01_create_agent_build/
│       │   ├── 10-02_create_agent_fix/
│       │   ├── 10-03_create_agent_predict/
│       │   ├── 10-04_create_agent_trace/
│       │   ├── 10-05_create_agent_extend/
│       │   ├── 10-06_create_agent_refactor/
│       │   ├── 10-07_middleware_build/
│       │   ├── 10-08_middleware_fix/
│       │   ├── 10-09_middleware_predict/
│       │   ├── 10-10_middleware_trace/
│       │   ├── 10-11_middleware_extend/
│       │   ├── 10-12_middleware_design/
│       │   ├── 10-13_agent_composition_build/
│       │   ├── 10-14_agent_composition_fix/
│       │   ├── 10-15_agent_composition_predict/
│       │   ├── 10-16_agent_composition_trace/
│       │   ├── 10-17_agent_composition_extend/
│       │   ├── 10-18_agent_composition_refactor/
│       ├── 11/
│       │   ├── 11-01_short_term_memory_build/
│       │   ├── 11-02_short_term_memory_fix/
│       │   ├── 11-03_short_term_memory_predict/
│       │   ├── 11-04_short_term_memory_trace/
│       │   ├── 11-05_short_term_memory_extend/
│       │   ├── 11-06_short_term_memory_refactor/
│       │   ├── 11-07_store_namespaces_build/
│       │   ├── 11-08_store_namespaces_fix/
│       │   ├── 11-09_store_namespaces_predict/
│       │   ├── 11-10_store_namespaces_trace/
│       │   ├── 11-11_store_namespaces_extend/
│       │   ├── 11-12_store_namespaces_refactor/
│       │   ├── 11-13_semantic_and_privacy_build/
│       │   ├── 11-14_semantic_and_privacy_fix/
│       │   ├── 11-15_semantic_and_privacy_predict/
│       │   ├── 11-16_semantic_and_privacy_trace/
│       │   ├── 11-17_semantic_and_privacy_extend/
│       │   ├── 11-18_semantic_and_privacy_design/
│       ├── 12/
│       │   ├── 12-01_chains_and_gates_build/
│       │   ├── 12-02_chains_and_gates_fix/
│       │   ├── 12-03_chains_and_gates_predict/
│       │   ├── 12-04_chains_and_gates_trace/
│       │   ├── 12-05_chains_and_gates_extend/
│       │   ├── 12-06_chains_and_gates_design/
│       │   ├── 12-07_orchestrator_workers_build/
│       │   ├── 12-08_orchestrator_workers_fix/
│       │   ├── 12-09_orchestrator_workers_predict/
│       │   ├── 12-10_orchestrator_workers_trace/
│       │   ├── 12-11_orchestrator_workers_extend/
│       │   ├── 12-12_orchestrator_workers_refactor/
│       │   ├── 12-13_evaluator_optimizer_build/
│       │   ├── 12-14_evaluator_optimizer_fix/
│       │   ├── 12-15_evaluator_optimizer_predict/
│       │   ├── 12-16_evaluator_optimizer_trace/
│       │   ├── 12-17_evaluator_optimizer_extend/
│       │   ├── 12-18_evaluator_optimizer_refactor/
│       ├── 13/
│       │   ├── 13-01_shared_subgraph_build/
│       │   ├── 13-02_shared_subgraph_fix/
│       │   ├── 13-03_shared_subgraph_predict/
│       │   ├── 13-04_shared_subgraph_trace/
│       │   ├── 13-05_shared_subgraph_extend/
│       │   ├── 13-06_shared_subgraph_refactor/
│       │   ├── 13-07_schema_adapters_build/
│       │   ├── 13-08_schema_adapters_fix/
│       │   ├── 13-09_schema_adapters_predict/
│       │   ├── 13-10_schema_adapters_trace/
│       │   ├── 13-11_schema_adapters_extend/
│       │   ├── 13-12_schema_adapters_refactor/
│       │   ├── 13-13_subgraph_persistence_build/
│       │   ├── 13-14_subgraph_persistence_fix/
│       │   ├── 13-15_subgraph_persistence_predict/
│       │   ├── 13-16_subgraph_persistence_trace/
│       │   ├── 13-17_subgraph_persistence_extend/
│       │   ├── 13-18_subgraph_persistence_design/
│       ├── 14/
│       │   ├── 14-01_supervisor_tools_build/
│       │   ├── 14-02_supervisor_tools_fix/
│       │   ├── 14-03_supervisor_tools_predict/
│       │   ├── 14-04_supervisor_tools_trace/
│       │   ├── 14-05_supervisor_tools_extend/
│       │   ├── 14-06_supervisor_tools_refactor/
│       │   ├── 14-07_handoffs_build/
│       │   ├── 14-08_handoffs_fix/
│       │   ├── 14-09_handoffs_predict/
│       │   ├── 14-10_handoffs_trace/
│       │   ├── 14-11_handoffs_extend/
│       │   ├── 14-12_handoffs_refactor/
│       │   ├── 14-13_team_tradeoffs_build/
│       │   ├── 14-14_team_tradeoffs_fix/
│       │   ├── 14-15_team_tradeoffs_predict/
│       │   ├── 14-16_team_tradeoffs_trace/
│       │   ├── 14-17_team_tradeoffs_extend/
│       │   ├── 14-18_team_tradeoffs_design/
│       ├── 15/
│       │   ├── 15-01_entrypoints_tasks_build/
│       │   ├── 15-02_entrypoints_tasks_fix/
│       │   ├── 15-03_entrypoints_tasks_predict/
│       │   ├── 15-04_entrypoints_tasks_trace/
│       │   ├── 15-05_entrypoints_tasks_extend/
│       │   ├── 15-06_entrypoints_tasks_refactor/
│       │   ├── 15-07_parallel_futures_build/
│       │   ├── 15-08_parallel_futures_fix/
│       │   ├── 15-09_parallel_futures_predict/
│       │   ├── 15-10_parallel_futures_trace/
│       │   ├── 15-11_parallel_futures_extend/
│       │   ├── 15-12_parallel_futures_refactor/
│       │   ├── 15-13_functional_resume_build/
│       │   ├── 15-14_functional_resume_fix/
│       │   ├── 15-15_functional_resume_predict/
│       │   ├── 15-16_functional_resume_trace/
│       │   ├── 15-17_functional_resume_extend/
│       │   ├── 15-18_functional_resume_design/
│       ├── 16/
│       │   ├── 16-01_api_boundaries_build/
│       │   ├── 16-02_api_boundaries_fix/
│       │   ├── 16-03_api_boundaries_predict/
│       │   ├── 16-04_api_boundaries_trace/
│       │   ├── 16-05_api_boundaries_extend/
│       │   ├── 16-06_api_boundaries_refactor/
│       │   ├── 16-07_mcp_server_build/
│       │   ├── 16-08_mcp_server_fix/
│       │   ├── 16-09_mcp_server_predict/
│       │   ├── 16-10_mcp_server_trace/
│       │   ├── 16-11_mcp_server_extend/
│       │   ├── 16-12_mcp_server_refactor/
│       │   ├── 16-13_mcp_adapter_build/
│       │   ├── 16-14_mcp_adapter_fix/
│       │   ├── 16-15_mcp_adapter_predict/
│       │   ├── 16-16_mcp_adapter_trace/
│       │   ├── 16-17_mcp_adapter_extend/
│       │   ├── 16-18_mcp_adapter_design/
│       ├── 17/
│       │   ├── 17-01_durable_side_effects_build/
│       │   ├── 17-02_durable_side_effects_fix/
│       │   ├── 17-03_durable_side_effects_predict/
│       │   ├── 17-04_durable_side_effects_trace/
│       │   ├── 17-05_durable_side_effects_extend/
│       │   ├── 17-06_durable_side_effects_refactor/
│       │   ├── 17-07_recovery_policies_build/
│       │   ├── 17-08_recovery_policies_fix/
│       │   ├── 17-09_recovery_policies_predict/
│       │   ├── 17-10_recovery_policies_trace/
│       │   ├── 17-11_recovery_policies_extend/
│       │   ├── 17-12_recovery_policies_design/
│       │   ├── 17-13_long_wait_postgres_build/
│       │   ├── 17-14_long_wait_postgres_fix/
│       │   ├── 17-15_long_wait_postgres_predict/
│       │   ├── 17-16_long_wait_postgres_trace/
│       │   ├── 17-17_long_wait_postgres_extend/
│       │   ├── 17-18_long_wait_postgres_refactor/
│       ├── 18/
│       │   ├── 18-01_async_streams_build/
│       │   ├── 18-02_async_streams_fix/
│       │   ├── 18-03_async_streams_predict/
│       │   ├── 18-04_async_streams_trace/
│       │   ├── 18-05_async_streams_extend/
│       │   ├── 18-06_async_streams_refactor/
│       │   ├── 18-07_sse_api_build/
│       │   ├── 18-08_sse_api_fix/
│       │   ├── 18-09_sse_api_predict/
│       │   ├── 18-10_sse_api_trace/
│       │   ├── 18-11_sse_api_extend/
│       │   ├── 18-12_sse_api_refactor/
│       │   ├── 18-13_adjuster_dashboard_build/
│       │   ├── 18-14_adjuster_dashboard_fix/
│       │   ├── 18-15_adjuster_dashboard_predict/
│       │   ├── 18-16_adjuster_dashboard_trace/
│       │   ├── 18-17_adjuster_dashboard_extend/
│       │   ├── 18-18_adjuster_dashboard_design/
│       ├── 19/
│       │   ├── 19-01_test_graph_behavior_build/
│       │   ├── 19-02_test_graph_behavior_fix/
│       │   ├── 19-03_test_graph_behavior_predict/
│       │   ├── 19-04_test_graph_behavior_trace/
│       │   ├── 19-05_test_graph_behavior_extend/
│       │   ├── 19-06_test_graph_behavior_refactor/
│       │   ├── 19-07_test_durable_execution_build/
│       │   ├── 19-08_test_durable_execution_fix/
│       │   ├── 19-09_test_durable_execution_predict/
│       │   ├── 19-10_test_durable_execution_trace/
│       │   ├── 19-11_test_durable_execution_extend/
│       │   ├── 19-12_test_durable_execution_refactor/
│       │   ├── 19-13_trajectory_evals_build/
│       │   ├── 19-14_trajectory_evals_fix/
│       │   ├── 19-15_trajectory_evals_predict/
│       │   ├── 19-16_trajectory_evals_trace/
│       │   ├── 19-17_trajectory_evals_extend/
│       │   ├── 19-18_trajectory_evals_design/
│       ├── 20/
│       │   ├── 20-01_local_visual_debugging_build/
│       │   ├── 20-02_local_visual_debugging_fix/
│       │   ├── 20-03_local_visual_debugging_predict/
│       │   ├── 20-04_local_visual_debugging_trace/
│       │   ├── 20-05_local_visual_debugging_extend/
│       │   ├── 20-06_local_visual_debugging_refactor/
│       │   ├── 20-07_structured_logs_build/
│       │   ├── 20-08_structured_logs_fix/
│       │   ├── 20-09_structured_logs_predict/
│       │   ├── 20-10_structured_logs_trace/
│       │   ├── 20-11_structured_logs_extend/
│       │   ├── 20-12_structured_logs_refactor/
│       │   ├── 20-13_optional_tracing_build/
│       │   ├── 20-14_optional_tracing_fix/
│       │   ├── 20-15_optional_tracing_predict/
│       │   ├── 20-16_optional_tracing_trace/
│       │   ├── 20-17_optional_tracing_extend/
│       │   ├── 20-18_optional_tracing_design/
│       ├── 21/
│       │   ├── 21-01_untrusted_input_build/
│       │   ├── 21-02_untrusted_input_fix/
│       │   ├── 21-03_untrusted_input_predict/
│       │   ├── 21-04_untrusted_input_trace/
│       │   ├── 21-05_untrusted_input_extend/
│       │   ├── 21-06_untrusted_input_refactor/
│       │   ├── 21-07_approval_and_limits_build/
│       │   ├── 21-08_approval_and_limits_fix/
│       │   ├── 21-09_approval_and_limits_predict/
│       │   ├── 21-10_approval_and_limits_trace/
│       │   ├── 21-11_approval_and_limits_extend/
│       │   ├── 21-12_approval_and_limits_design/
│       │   ├── 21-13_private_checkpoints_build/
│       │   ├── 21-14_private_checkpoints_fix/
│       │   ├── 21-15_private_checkpoints_predict/
│       │   ├── 21-16_private_checkpoints_trace/
│       │   ├── 21-17_private_checkpoints_extend/
│       │   ├── 21-18_private_checkpoints_refactor/
│       ├── 22/
│       │   ├── 22-01_compose_stack_build/
│       │   ├── 22-02_compose_stack_fix/
│       │   ├── 22-03_compose_stack_predict/
│       │   ├── 22-04_compose_stack_trace/
│       │   ├── 22-05_compose_stack_extend/
│       │   ├── 22-06_compose_stack_refactor/
│       │   ├── 22-07_worker_reliability_build/
│       │   ├── 22-08_worker_reliability_fix/
│       │   ├── 22-09_worker_reliability_predict/
│       │   ├── 22-10_worker_reliability_trace/
│       │   ├── 22-11_worker_reliability_extend/
│       │   ├── 22-12_worker_reliability_design/
│       │   ├── 22-13_managed_deployment_build/
│       │   ├── 22-14_managed_deployment_fix/
│       │   ├── 22-15_managed_deployment_predict/
│       │   ├── 22-16_managed_deployment_trace/
│       │   ├── 22-17_managed_deployment_extend/
│       │   ├── 22-18_managed_deployment_design/
│       ├── B1/
│       │   ├── B1-01_typescript_state_build/
│       │   ├── B1-02_typescript_state_fix/
│       │   ├── B1-03_typescript_state_predict/
│       │   ├── B1-04_typescript_state_trace/
│       │   ├── B1-05_typescript_state_extend/
│       │   ├── B1-06_typescript_state_refactor/
│       │   ├── B1-07_typescript_durable_build/
│       │   ├── B1-08_typescript_durable_fix/
│       │   ├── B1-09_typescript_durable_predict/
│       │   ├── B1-10_typescript_durable_trace/
│       │   ├── B1-11_typescript_durable_extend/
│       │   ├── B1-12_typescript_durable_refactor/
│       │   ├── B1-13_typescript_agents_build/
│       │   ├── B1-14_typescript_agents_fix/
│       │   ├── B1-15_typescript_agents_predict/
│       │   ├── B1-16_typescript_agents_trace/
│       │   ├── B1-17_typescript_agents_extend/
│       │   ├── B1-18_typescript_agents_refactor/
│       ├── B2/
│       │   ├── B2-01_deep_agent_planning_build/
│       │   ├── B2-02_deep_agent_planning_fix/
│       │   ├── B2-03_deep_agent_planning_predict/
│       │   ├── B2-04_deep_agent_planning_trace/
│       │   ├── B2-05_deep_agent_planning_extend/
│       │   ├── B2-06_deep_agent_planning_refactor/
│       │   ├── B2-07_virtual_filesystem_build/
│       │   ├── B2-08_virtual_filesystem_fix/
│       │   ├── B2-09_virtual_filesystem_predict/
│       │   ├── B2-10_virtual_filesystem_trace/
│       │   ├── B2-11_virtual_filesystem_extend/
│       │   ├── B2-12_virtual_filesystem_refactor/
│       │   ├── B2-13_deep_subagents_build/
│       │   ├── B2-14_deep_subagents_fix/
│       │   ├── B2-15_deep_subagents_predict/
│       │   ├── B2-16_deep_subagents_trace/
│       │   ├── B2-17_deep_subagents_extend/
│       │   ├── B2-18_deep_subagents_design/
│       ├── B3/
│       │   ├── B3-01_channels_and_steps_build/
│       │   ├── B3-02_channels_and_steps_fix/
│       │   ├── B3-03_channels_and_steps_predict/
│       │   ├── B3-04_channels_and_steps_trace/
│       │   ├── B3-05_channels_and_steps_extend/
│       │   ├── B3-06_channels_and_steps_refactor/
│       │   ├── B3-07_mini_reducers_build/
│       │   ├── B3-08_mini_reducers_fix/
│       │   ├── B3-09_mini_reducers_predict/
│       │   ├── B3-10_mini_reducers_trace/
│       │   ├── B3-11_mini_reducers_extend/
│       │   ├── B3-12_mini_reducers_refactor/
│       │   ├── B3-13_mini_checkpoints_build/
│       │   ├── B3-14_mini_checkpoints_fix/
│       │   ├── B3-15_mini_checkpoints_predict/
│       │   ├── B3-16_mini_checkpoints_trace/
│       │   ├── B3-17_mini_checkpoints_extend/
│       │   ├── B3-18_mini_checkpoints_design/
│       ├── B4/
│       │   ├── B4-01_event_streaming_beta_build/
│       │   ├── B4-02_event_streaming_beta_fix/
│       │   ├── B4-03_event_streaming_beta_predict/
│       │   ├── B4-04_event_streaming_beta_trace/
│       │   ├── B4-05_event_streaming_beta_extend/
│       │   ├── B4-06_event_streaming_beta_refactor/
│       │   ├── B4-07_delta_channels_beta_build/
│       │   ├── B4-08_delta_channels_beta_fix/
│       │   ├── B4-09_delta_channels_beta_predict/
│       │   ├── B4-10_delta_channels_beta_trace/
│       │   ├── B4-11_delta_channels_beta_extend/
│       │   ├── B4-12_delta_channels_beta_design/
│       │   ├── B4-13_typed_approvals_build/
│       │   ├── B4-14_typed_approvals_fix/
│       │   ├── B4-15_typed_approvals_predict/
│       │   ├── B4-16_typed_approvals_trace/
│       │   ├── B4-17_typed_approvals_extend/
│       │   ├── B4-18_typed_approvals_design/
├── workspace/ (ignored; created at runtime)
├── capstones/
│   ├── 01_claims_intake_engine/
│   ├── 02_policy_qa_with_memory/
│   ├── 03_fraud_investigation_team/
│   ├── 04_larkspur_claims_copilot/
│   └── 05_design_your_own/
├── deploy/
│   └── langgraph.json, Dockerfile, docker-compose.yml, README.md, healthcheck.py
├── cheatsheets/
│   └── tier_1, tier_2, tier_3, tier_4, api_at_a_glance (each MD and printable PDF)
├── docs/
│   ├── FEATURE_MAP.md, GYM_TASK_CATALOG.md, MENTAL_MODEL.md
│   ├── CHOOSING_THE_RIGHT_DESIGN.md, COMMON_BUGS.md, GLOSSARY.md
│   ├── TROUBLESHOOTING.md, MIGRATING_FROM_OLDER_VERSIONS.md
│   ├── VERIFICATION_NOTES.md, REPOSITORY_TREE.md, DATA_DICTIONARY.md
│   ├── ACCEPTANCE_REPORT.md
│   ├── planning/{course_catalog.json,REPOSITORY_MANIFEST.txt,PLAN_VALIDATION.json}
│   └── verification/ (registry snapshots, dependency resolution, source checks)
├── scripts/
│   ├── __init__.py, build_data.py, check_env.py, validate_gym.py
│   ├── run_all_examples.py, check_coverage.py, check_links.py
│   ├── check_legacy_apis.py, check_notebooks.py, render_diagrams.py
│   ├── run_evaluation.py, run_stack.py, run_typescript.py, setup_typescript.py
│   └── verify_apis.py
└── tests/
    ├── conftest.py
    ├── test_models.py, test_fakes.py, test_data.py
    ├── test_gym_cli.py, test_gym_runner.py, test_gym_progress.py
    ├── test_banned_apis.py, test_content_contracts.py, test_feature_coverage.py
    ├── test_notebooks.py, test_security.py, test_offline.py
    ├── test_copilot_versions.py, test_api.py, test_optional_installs.py
    ├── integration/{test_postgres,test_compose,test_mcp_stdio}.py
    └── live/{test_providers,test_langsmith}.py
```

## Repeated leaf contracts

Every Python module has at least three numbered examples, its use case, a cleared notebook, a standalone quiz, a generated graph diagram where supported, and example/use-case tests. Extra examples are allowed when one concept needs its own file. Shared application code lives under `common/`; numbered module directories are executed by path and are not imported as Python packages.

Every code task has `task.md`, `starter.py`, `test_task.py`, `hints.md`, `solution.py`, and `explanation.md`. Predict/Trace omit `starter.py` and add `answer.json` plus `expected_answer.json`; their solution script is an actual deterministic oracle. Design also has `rubric.md`, `design.md`, and `solution_design.md`. B1 code tasks include real `.ts` starter/solution files and a small Python launcher; the gym copies both and grades the TypeScript file.

Each capstone contains `README.md`, `starter.py`, `solution.py`, `tests/test_solution.py`, `eval/cases.jsonl`, `rubric.md`, `extend_it.md`, and `diagram.mmd`. Capstone 05 includes a complete sample solution for a clearly marked chosen process as well as a rubric for the learner's independent design.

B1 also contains `package.json`, `package-lock.json`, `tsconfig.json`, three shared TypeScript helpers, and a parity test. Its model helper supplies scripted models only; live provider creation remains centralized in Python. Functional API and non-graph diagrams are explicitly labeled conceptual, because runtime-discovered control flow cannot be honestly presented as a generated static graph.
