# Practice Gym — complete task catalog

All 486 exercises are shipped: 414 core and 72 bonus tasks. Refactor starters preserve behavior and fail a structural check; Extend tasks retain old checks and add a capability. Predict and Trace use written answers. Design includes a rationale rubric.

## 00 — Setup and orientation

[Lesson](../modules/00_setup/README.md)

### 00-A: plain checklist

Features: Plain Python versus stateful orchestration; workflow versus agent; LangGraph, LangChain, and LangSmith roles.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [00-01](../gym/tasks/00/00-01_plain_checklist_build/task.md) | 00 | build | easy | Build a three-step checklist that reads a synthetic claim without needing a model. |
| [00-02](../gym/tasks/00/00-02_plain_checklist_fix/task.md) | 00 | fix | medium | Fix a checklist whose missing-data branch silently approves an incomplete claim. |
| [00-03](../gym/tasks/00/00-03_plain_checklist_predict/task.md) | 00 | predict | easy | Predict the checklist results for complete, incomplete, and duplicate submissions. |
| [00-04](../gym/tasks/00/00-04_plain_checklist_trace/task.md) | 00 | trace | medium | Trace which checklist step dropped the claim identifier. |
| [00-05](../gym/tasks/00/00-05_plain_checklist_extend/task.md) | 00 | extend | hard | Extend the checklist to return an explicit reason for every intake decision. |
| [00-06](../gym/tasks/00/00-06_plain_checklist_design/task.md) | 00 | design | hard | Choose the smallest sufficient implementation for six Larkspur requests. |

### 00-B: environment

Features: uv and pip environments; portable script entry points; optional providers; safe configuration.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [00-07](../gym/tasks/00/00-07_environment_build/task.md) | 00 | build | easy | Build environment: Required and optional packages are different contracts. |
| [00-08](../gym/tasks/00/00-08_environment_fix/task.md) | 00 | fix | medium | Fix environment: A missing provider is a problem only when live mode was requested. |
| [00-09](../gym/tasks/00/00-09_environment_predict/task.md) | 00 | predict | easy | Predict environment across the declared cases |
| [00-10](../gym/tasks/00/00-10_environment_trace/task.md) | 00 | trace | medium | Diagnose environment from execution evidence |
| [00-11](../gym/tasks/00/00-11_environment_extend/task.md) | 00 | extend | hard | Extend environment: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [00-12](../gym/tasks/00/00-12_environment_refactor/task.md) | 00 | refactor | hard | Refactor environment: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 00-C: first gym

Features: Gym workflow; pytest assertions; progress and hints; deterministic acceptance criteria.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [00-13](../gym/tasks/00/00-13_first_gym_build/task.md) | 00 | build | easy | Build first gym: Unknown claim categories need an explicit label. |
| [00-14](../gym/tasks/00/00-14_first_gym_fix/task.md) | 00 | fix | medium | Fix first gym: Labels need case normalization before comparison. |
| [00-15](../gym/tasks/00/00-15_first_gym_predict/task.md) | 00 | predict | easy | Predict first gym across the declared cases |
| [00-16](../gym/tasks/00/00-16_first_gym_trace/task.md) | 00 | trace | medium | Diagnose first gym from execution evidence |
| [00-17](../gym/tasks/00/00-17_first_gym_extend/task.md) | 00 | extend | hard | Extend first gym: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [00-18](../gym/tasks/00/00-18_first_gym_design/task.md) | 00 | design | hard | Design first gym and justify the boundary policies |

## 01 — Your first graph

[Lesson](../modules/01_your_first_graph/README.md)

### 01-A: intake nodes

Features: StateGraph; TypedDict state; nodes as functions; partial node updates.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [01-01](../gym/tasks/01/01-01_intake_nodes_build/task.md) | 01 | build | easy | Build intake nodes: Normalize the description while preserving unrelated state. |
| [01-02](../gym/tasks/01/01-02_intake_nodes_fix/task.md) | 01 | fix | medium | Fix intake nodes: A graph node must return a mapping of state updates. |
| [01-03](../gym/tasks/01/01-03_intake_nodes_predict/task.md) | 01 | predict | easy | Predict intake nodes across the declared cases |
| [01-04](../gym/tasks/01/01-04_intake_nodes_trace/task.md) | 01 | trace | medium | Diagnose intake nodes from execution evidence |
| [01-05](../gym/tasks/01/01-05_intake_nodes_extend/task.md) | 01 | extend | hard | Extend intake nodes: Add a contact-normalization node without erasing claim identity. |
| [01-06](../gym/tasks/01/01-06_intake_nodes_refactor/task.md) | 01 | refactor | hard | Refactor intake nodes: Refactor mutation into a pure partial update. |

### 01-B: wire pipeline

Features: add_node; add_edge; START and END; compile; invoke with GraphOutput.value.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [01-07](../gym/tasks/01/01-07_wire_pipeline_build/task.md) | 01 | build | easy | Build wire pipeline: The acknowledgment must be reachable. |
| [01-08](../gym/tasks/01/01-08_wire_pipeline_fix/task.md) | 01 | fix | medium | Fix wire pipeline: Validation must occur before acknowledging the claim. |
| [01-09](../gym/tasks/01/01-09_wire_pipeline_predict/task.md) | 01 | predict | easy | Predict wire pipeline across the declared cases |
| [01-10](../gym/tasks/01/01-10_wire_pipeline_trace/task.md) | 01 | trace | medium | Diagnose wire pipeline from execution evidence |
| [01-11](../gym/tasks/01/01-11_wire_pipeline_extend/task.md) | 01 | extend | hard | Extend wire pipeline: Connect the receipt-number node after acknowledgment and before termination. |
| [01-12](../gym/tasks/01/01-12_wire_pipeline_refactor/task.md) | 01 | refactor | hard | Refactor wire pipeline: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 01-C: draw and explain

Features: get_graph().draw_mermaid(); graph visualization; sequential supersteps.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [01-13](../gym/tasks/01/01-13_draw_and_explain_build/task.md) | 01 | build | easy | Build draw and explain: The diagram must include validation on the executed route. |
| [01-14](../gym/tasks/01/01-14_draw_and_explain_fix/task.md) | 01 | fix | medium | Fix draw and explain: The intended final node must be connected. |
| [01-15](../gym/tasks/01/01-15_draw_and_explain_predict/task.md) | 01 | predict | easy | Predict draw and explain across the declared cases |
| [01-16](../gym/tasks/01/01-16_draw_and_explain_trace/task.md) | 01 | trace | medium | Diagnose draw and explain from execution evidence |
| [01-17](../gym/tasks/01/01-17_draw_and_explain_extend/task.md) | 01 | extend | hard | Extend draw and explain: Add an opt-in eligibility node selected by eligibility_check=True. Preserve the original steps when absent; verify the new diagram connection and valid/invalid updates when enabled. |
| [01-18](../gym/tasks/01/01-18_draw_and_explain_design/task.md) | 01 | design | hard | Design draw and explain and justify the boundary policies |

## 02 — State and reducers

[Lesson](../modules/02_state_and_reducers/README.md)

### 02-A: schema contracts

Features: TypedDict, dataclass, and Pydantic schemas; defaults; input validation; v2 output coercion.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [02-01](../gym/tasks/02/02-01_schema_contracts_build/task.md) | 02 | build | easy | Build schema contracts: A successful validation node must record its result. |
| [02-02](../gym/tasks/02/02-02_schema_contracts_fix/task.md) | 02 | fix | medium | Fix schema contracts: Use Pydantic field access or model_dump instead of losing validated values. |
| [02-03](../gym/tasks/02/02-03_schema_contracts_predict/task.md) | 02 | predict | easy | Predict schema contracts across the declared cases |
| [02-04](../gym/tasks/02/02-04_schema_contracts_trace/task.md) | 02 | trace | medium | Diagnose schema contracts from execution evidence |
| [02-05](../gym/tasks/02/02-05_schema_contracts_extend/task.md) | 02 | extend | hard | Extend schema contracts: Preserve an optional loss date and its None default across all three schema styles. |
| [02-06](../gym/tasks/02/02-06_schema_contracts_refactor/task.md) | 02 | refactor | hard | Refactor schema contracts: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 02-B: reducer findings

Features: Overwrite channels; Annotated reducers; operator.add; custom reducers; associativity.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [02-07](../gym/tasks/02/02-07_reducer_findings_build/task.md) | 02 | build | easy | Build reducer findings: A merge must preserve evidence from earlier updates. |
| [02-08](../gym/tasks/02/02-08_reducer_findings_fix/task.md) | 02 | fix | medium | Fix reducer findings: Return new evidence only; the reducer already has previous values. |
| [02-09](../gym/tasks/02/02-09_reducer_findings_predict/task.md) | 02 | predict | easy | Predict reducer findings across the declared cases |
| [02-10](../gym/tasks/02/02-10_reducer_findings_trace/task.md) | 02 | trace | medium | Diagnose reducer findings from execution evidence |
| [02-11](../gym/tasks/02/02-11_reducer_findings_extend/task.md) | 02 | extend | hard | Extend reducer findings: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [02-12](../gym/tasks/02/02-12_reducer_findings_refactor/task.md) | 02 | refactor | hard | Refactor reducer findings: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 02-C: state boundaries

Features: Input and output schemas; private state channels; MessagesState introduction; add_messages introduction.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [02-13](../gym/tasks/02/02-13_state_boundaries_build/task.md) | 02 | build | easy | Build state boundaries: Internal channels must not become public output. |
| [02-14](../gym/tasks/02/02-14_state_boundaries_fix/task.md) | 02 | fix | medium | Fix state boundaries: Use the same message ID to replace the original message. |
| [02-15](../gym/tasks/02/02-15_state_boundaries_predict/task.md) | 02 | predict | easy | Predict state boundaries across the declared cases |
| [02-16](../gym/tasks/02/02-16_state_boundaries_trace/task.md) | 02 | trace | medium | Diagnose state boundaries from execution evidence |
| [02-17](../gym/tasks/02/02-17_state_boundaries_extend/task.md) | 02 | extend | hard | Extend state boundaries: Append a customer-safe explanation without exposing internal notes or duplicating the original message. |
| [02-18](../gym/tasks/02/02-18_state_boundaries_refactor/task.md) | 02 | refactor | hard | Refactor state boundaries: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

## 03 — Branching and routing

[Lesson](../modules/03_branching_and_routing/README.md)

### 03-A: conditional router

Features: Conditional edges; routing functions; path maps; state-based routing.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [03-01](../gym/tasks/03/03-01_conditional_router_build/task.md) | 03 | build | easy | Build conditional router: The exact fast-track threshold is inclusive. |
| [03-02](../gym/tasks/03/03-02_conditional_router_fix/task.md) | 03 | fix | medium | Fix conditional router: Path-map values must match each intended destination. |
| [03-03](../gym/tasks/03/03-03_conditional_router_predict/task.md) | 03 | predict | easy | Predict conditional router across the declared cases |
| [03-04](../gym/tasks/03/03-04_conditional_router_trace/task.md) | 03 | trace | medium | Diagnose conditional router from execution evidence |
| [03-05](../gym/tasks/03/03-05_conditional_router_extend/task.md) | 03 | extend | hard | Extend conditional router: Add an opt-in jewelry-specialist path selected by specialize_jewelry=True. Preserve legacy routing when absent, and keep invalid-amount, high-value, and missing-evidence guards ahead of specialization. |
| [03-06](../gym/tasks/03/03-06_conditional_router_refactor/task.md) | 03 | refactor | hard | Refactor conditional router: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 03-B: command routes

Features: Command.update; Command.goto; destination annotations; avoiding duplicate routing.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [03-07](../gym/tasks/03/03-07_command_routes_build/task.md) | 03 | build | easy | Build command routes: Suspicious evidence must affect the selected destination. |
| [03-08](../gym/tasks/03/03-08_command_routes_fix/task.md) | 03 | fix | medium | Fix command routes: A competing static edge schedules an extra acknowledgment. |
| [03-09](../gym/tasks/03/03-09_command_routes_predict/task.md) | 03 | predict | easy | Predict command routes across the declared cases |
| [03-10](../gym/tasks/03/03-10_command_routes_trace/task.md) | 03 | trace | medium | Diagnose command routes from execution evidence |
| [03-11](../gym/tasks/03/03-11_command_routes_extend/task.md) | 03 | extend | hard | Extend command routes: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [03-12](../gym/tasks/03/03-12_command_routes_refactor/task.md) | 03 | refactor | hard | Refactor command routes: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 03-C: early exit

Features: Routing to END; total routers; threshold testing; business decisions versus model guesses.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [03-13](../gym/tasks/03/03-13_early_exit_build/task.md) | 03 | build | easy | Build early exit: Rejected claims must stop before assignment. |
| [03-14](../gym/tasks/03/03-14_early_exit_fix/task.md) | 03 | fix | medium | Fix early exit: Zero is a defined boundary, not an omitted case. |
| [03-15](../gym/tasks/03/03-15_early_exit_predict/task.md) | 03 | predict | easy | Predict early exit across the declared cases |
| [03-16](../gym/tasks/03/03-16_early_exit_trace/task.md) | 03 | trace | medium | Diagnose early exit from execution evidence |
| [03-17](../gym/tasks/03/03-17_early_exit_extend/task.md) | 03 | extend | hard | Extend early exit: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [03-18](../gym/tasks/03/03-18_early_exit_design/task.md) | 03 | design | hard | Design early exit and justify the boundary policies |

## 04 — Loops, parallel branches, and map-reduce

[Lesson](../modules/04_loops_parallel_map_reduce/README.md)

### 04-A: bounded rechecks

Features: Loops with exit conditions; recursion_limit; GraphRecursionError.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [04-01](../gym/tasks/04/04-01_bounded_rechecks_build/task.md) | 04 | build | easy | Build bounded rechecks: Received evidence must terminate the recheck loop. |
| [04-02](../gym/tasks/04/04-02_bounded_rechecks_fix/task.md) | 04 | fix | medium | Fix bounded rechecks: Without a changing retry counter, the graph reaches its recursion limit. |
| [04-03](../gym/tasks/04/04-03_bounded_rechecks_predict/task.md) | 04 | predict | easy | Predict bounded rechecks across the declared cases |
| [04-04](../gym/tasks/04/04-04_bounded_rechecks_trace/task.md) | 04 | trace | medium | Diagnose bounded rechecks from execution evidence |
| [04-05](../gym/tasks/04/04-05_bounded_rechecks_extend/task.md) | 04 | extend | hard | Extend bounded rechecks: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [04-06](../gym/tasks/04/04-06_bounded_rechecks_refactor/task.md) | 04 | refactor | hard | Refactor bounded rechecks: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 04-B: fan out fan in

Features: Fan-out and fan-in; parallel supersteps; InvalidUpdateError; Send map-reduce; deferred nodes.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [04-07](../gym/tasks/04/04-07_fan_out_fan_in_build/task.md) | 04 | build | easy | Build fan out fan in: Each worker must contribute its own document evidence. |
| [04-08](../gym/tasks/04/04-08_fan_out_fan_in_fix/task.md) | 04 | fix | medium | Fix fan out fan in: Parallel writes to an overwrite channel conflict. |
| [04-09](../gym/tasks/04/04-09_fan_out_fan_in_predict/task.md) | 04 | predict | easy | Predict fan out fan in across the declared cases |
| [04-10](../gym/tasks/04/04-10_fan_out_fan_in_trace/task.md) | 04 | trace | medium | Diagnose fan out fan in from execution evidence |
| [04-11](../gym/tasks/04/04-11_fan_out_fan_in_extend/task.md) | 04 | extend | hard | Extend fan out fan in: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [04-12](../gym/tasks/04/04-12_fan_out_fan_in_refactor/task.md) | 04 | refactor | hard | Refactor fan out fan in: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 04-C: retry and cache

Features: RetryPolicy; node caching; CachePolicy; cache keys and TTL; pure versus side-effecting nodes.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [04-13](../gym/tasks/04/04-13_retry_and_cache_build/task.md) | 04 | build | easy | Build retry and cache: A bounded retry must recover from the injected transient read failure. |
| [04-14](../gym/tasks/04/04-14_retry_and_cache_fix/task.md) | 04 | fix | medium | Fix retry and cache: Customer identity belongs in the cache key. |
| [04-15](../gym/tasks/04/04-15_retry_and_cache_predict/task.md) | 04 | predict | easy | Predict retry and cache across the declared cases |
| [04-16](../gym/tasks/04/04-16_retry_and_cache_trace/task.md) | 04 | trace | medium | Diagnose retry and cache from execution evidence |
| [04-17](../gym/tasks/04/04-17_retry_and_cache_extend/task.md) | 04 | extend | hard | Extend retry and cache: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [04-18](../gym/tasks/04/04-18_retry_and_cache_design/task.md) | 04 | design | hard | Design retry and cache and justify the boundary policies |

## 05 — Persistence and threads

[Lesson](../modules/05_persistence_and_threads/README.md)

### 05-A: thread identity

Features: InMemorySaver; checkpointer compilation; thread_id; config; continuing versus resuming.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [05-01](../gym/tasks/05/05-01_thread_identity_build/task.md) | 05 | build | easy | Build thread identity: Saved notes must survive a second invocation on the same graph. |
| [05-02](../gym/tasks/05/05-02_thread_identity_fix/task.md) | 05 | fix | medium | Fix thread identity: A persisted invocation needs an explicit thread identifier. |
| [05-03](../gym/tasks/05/05-03_thread_identity_predict/task.md) | 05 | predict | easy | Predict thread identity across the declared cases |
| [05-04](../gym/tasks/05/05-04_thread_identity_trace/task.md) | 05 | trace | medium | Diagnose thread identity from execution evidence |
| [05-05](../gym/tasks/05/05-05_thread_identity_extend/task.md) | 05 | extend | hard | Extend thread identity: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [05-06](../gym/tasks/05/05-06_thread_identity_refactor/task.md) | 05 | refactor | hard | Refactor thread identity: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 05-B: sqlite lifetime

Features: SqliteSaver; checkpoint resource lifetimes; persistence across processes; SQLite Windows locking.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [05-07](../gym/tasks/05/05-07_sqlite_lifetime_build/task.md) | 05 | build | easy | Build sqlite lifetime: A restarted process must merge the new note with stored notes. |
| [05-08](../gym/tasks/05/05-08_sqlite_lifetime_fix/task.md) | 05 | fix | medium | Fix sqlite lifetime: A compiled graph cannot use a saver whose connection has closed. |
| [05-09](../gym/tasks/05/05-09_sqlite_lifetime_predict/task.md) | 05 | predict | easy | Predict sqlite lifetime across the declared cases |
| [05-10](../gym/tasks/05/05-10_sqlite_lifetime_trace/task.md) | 05 | trace | medium | Diagnose sqlite lifetime from execution evidence |
| [05-11](../gym/tasks/05/05-11_sqlite_lifetime_extend/task.md) | 05 | extend | hard | Extend sqlite lifetime: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [05-12](../gym/tasks/05/05-12_sqlite_lifetime_refactor/task.md) | 05 | refactor | hard | Refactor sqlite lifetime: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 05-C: inspect checkpoints

Features: StateSnapshot; get_state; get_state_history; update_state; durability sync, async, and exit.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [05-13](../gym/tasks/05/05-13_inspect_checkpoints_build/task.md) | 05 | build | easy | Build inspect checkpoints: The corrected checkpoint must contain the replacement evidence. |
| [05-14](../gym/tasks/05/05-14_inspect_checkpoints_fix/task.md) | 05 | fix | medium | Fix inspect checkpoints: Continue the configuration returned by update_state, not an unrelated checkpoint. |
| [05-15](../gym/tasks/05/05-15_inspect_checkpoints_predict/task.md) | 05 | predict | easy | Predict inspect checkpoints across the declared cases |
| [05-16](../gym/tasks/05/05-16_inspect_checkpoints_trace/task.md) | 05 | trace | medium | Diagnose inspect checkpoints from execution evidence |
| [05-17](../gym/tasks/05/05-17_inspect_checkpoints_extend/task.md) | 05 | extend | hard | Extend inspect checkpoints: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [05-18](../gym/tasks/05/05-18_inspect_checkpoints_design/task.md) | 05 | design | hard | Design inspect checkpoints and justify the boundary policies |

## 06 — Human-in-the-loop with interrupts

[Lesson](../modules/06_human_in_the_loop/README.md)

### 06-A: approve or reject

Features: interrupt(); Command(resume=...); checkpointer requirement; v2 interrupt output.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [06-01](../gym/tasks/06/06-01_approve_or_reject_build/task.md) | 06 | build | easy | Build approve or reject: A rejected proposal must not become an approved result. |
| [06-02](../gym/tasks/06/06-02_approve_or_reject_fix/task.md) | 06 | fix | medium | Fix approve or reject: An interrupt needs persistence to resume the saved task. |
| [06-03](../gym/tasks/06/06-03_approve_or_reject_predict/task.md) | 06 | predict | easy | Predict approve or reject across the declared cases |
| [06-04](../gym/tasks/06/06-04_approve_or_reject_trace/task.md) | 06 | trace | medium | Diagnose approve or reject from execution evidence |
| [06-05](../gym/tasks/06/06-05_approve_or_reject_extend/task.md) | 06 | extend | hard | Extend approve or reject: Validate adjuster identity from the trusted invocation configuration, independently of the response payload. |
| [06-06](../gym/tasks/06/06-06_approve_or_reject_refactor/task.md) | 06 | refactor | hard | Refactor approve or reject: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 06-B: collect and edit

Features: Editing through resume; missing-input interrupts; multiple interrupts; ID-based resume mapping.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [06-07](../gym/tasks/06/06-07_collect_and_edit_build/task.md) | 06 | build | easy | Build collect and edit: A zero approved amount is a valid edited decision. |
| [06-08](../gym/tasks/06/06-08_collect_and_edit_fix/task.md) | 06 | fix | medium | Fix collect and edit: Each interrupt must receive the response for its own request kind. |
| [06-09](../gym/tasks/06/06-09_collect_and_edit_predict/task.md) | 06 | predict | easy | Predict collect and edit across the declared cases |
| [06-10](../gym/tasks/06/06-10_collect_and_edit_trace/task.md) | 06 | trace | medium | Diagnose collect and edit from execution evidence |
| [06-11](../gym/tasks/06/06-11_collect_and_edit_extend/task.md) | 06 | extend | hard | Extend collect and edit: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [06-12](../gym/tasks/06/06-12_collect_and_edit_design/task.md) | 06 | design | hard | Design collect and edit and justify the boundary policies |

### 06-C: safe reentry

Features: Interrupted-node restart semantics; idempotent side effects; deterministic interrupt order; debugging breakpoint distinction.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [06-13](../gym/tasks/06/06-13_safe_reentry_build/task.md) | 06 | build | easy | Build safe reentry: Rejection must not trigger the synthetic notification. |
| [06-14](../gym/tasks/06/06-14_safe_reentry_fix/task.md) | 06 | fix | medium | Fix safe reentry: Effects before interrupt repeat when the node restarts. |
| [06-15](../gym/tasks/06/06-15_safe_reentry_predict/task.md) | 06 | predict | easy | Predict safe reentry across the declared cases |
| [06-16](../gym/tasks/06/06-16_safe_reentry_trace/task.md) | 06 | trace | medium | Diagnose safe reentry from execution evidence |
| [06-17](../gym/tasks/06/06-17_safe_reentry_extend/task.md) | 06 | extend | hard | Extend safe reentry: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [06-18](../gym/tasks/06/06-18_safe_reentry_refactor/task.md) | 06 | refactor | hard | Refactor safe reentry: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

## 07 — Time travel, debugging, and streaming basics

[Lesson](../modules/07_time_travel_and_streaming/README.md)

### 07-A: replay and fork

Features: Historical checkpoint replay; checkpoint_id; update_state forks; as_node; renewed interrupts.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [07-01](../gym/tasks/07/07-01_replay_and_fork_build/task.md) | 07 | build | easy | Build replay and fork: A fork must contain the corrected evidence. |
| [07-02](../gym/tasks/07/07-02_replay_and_fork_fix/task.md) | 07 | fix | medium | Fix replay and fork: Replay the new fork configuration, not its uncorrected parent. |
| [07-03](../gym/tasks/07/07-03_replay_and_fork_predict/task.md) | 07 | predict | easy | Predict replay and fork across the declared cases |
| [07-04](../gym/tasks/07/07-04_replay_and_fork_trace/task.md) | 07 | trace | medium | Diagnose replay and fork from execution evidence |
| [07-05](../gym/tasks/07/07-05_replay_and_fork_extend/task.md) | 07 | extend | hard | Extend replay and fork: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [07-06](../gym/tasks/07/07-06_replay_and_fork_refactor/task.md) | 07 | refactor | hard | Refactor replay and fork: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 07-B: v2 stream parts

Features: values, updates, debug, and custom stream modes; get_stream_writer; v2 StreamPart envelope.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [07-07](../gym/tasks/07/07-07_v2_stream_parts_build/task.md) | 07 | build | easy | Build v2 stream parts: A consumer must preserve the event mode. |
| [07-08](../gym/tasks/07/07-08_v2_stream_parts_fix/task.md) | 07 | fix | medium | Fix v2 stream parts: The state payload is inside data, not at the envelope root. |
| [07-09](../gym/tasks/07/07-09_v2_stream_parts_predict/task.md) | 07 | predict | easy | Predict v2 stream parts across the declared cases |
| [07-10](../gym/tasks/07/07-10_v2_stream_parts_trace/task.md) | 07 | trace | medium | Diagnose v2 stream parts from execution evidence |
| [07-11](../gym/tasks/07/07-11_v2_stream_parts_extend/task.md) | 07 | extend | hard | Extend v2 stream parts: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [07-12](../gym/tasks/07/07-12_v2_stream_parts_refactor/task.md) | 07 | refactor | hard | Refactor v2 stream parts: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 07-C: namespaces and errors

Features: Subgraph namespace preview; parallel event ordering; error reading; stream versus checkpoint history.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [07-13](../gym/tasks/07/07-13_namespaces_and_errors_build/task.md) | 07 | build | easy | Build namespaces and errors: Nested updates require subgraph streaming. |
| [07-14](../gym/tasks/07/07-14_namespaces_and_errors_fix/task.md) | 07 | fix | medium | Fix namespaces and errors: Keep parent and child scopes distinct. |
| [07-15](../gym/tasks/07/07-15_namespaces_and_errors_predict/task.md) | 07 | predict | easy | Predict namespaces and errors across the declared cases |
| [07-16](../gym/tasks/07/07-16_namespaces_and_errors_trace/task.md) | 07 | trace | medium | Diagnose namespaces and errors from execution evidence |
| [07-17](../gym/tasks/07/07-17_namespaces_and_errors_extend/task.md) | 07 | extend | hard | Extend namespaces and errors: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [07-18](../gym/tasks/07/07-18_namespaces_and_errors_design/task.md) | 07 | design | hard | Design namespaces and errors and justify the boundary policies |

## 08 — LLMs inside nodes

[Lesson](../modules/08_llms_inside_nodes/README.md)

### 08-A: model boundary

Features: LLM and prompt basics; init_chat_model; common model factory; provider configuration; structured output validation.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [08-01](../gym/tasks/08/08-01_model_boundary_build/task.md) | 08 | build | easy | Build model boundary: Send uncertain extractions to review. |
| [08-02](../gym/tasks/08/08-02_model_boundary_fix/task.md) | 08 | fix | medium | Fix model boundary: Include exactly 100000 cents in fast-track routing. |
| [08-03](../gym/tasks/08/08-03_model_boundary_predict/task.md) | 08 | predict | easy | Predict model boundary across the declared cases |
| [08-04](../gym/tasks/08/08-04_model_boundary_trace/task.md) | 08 | trace | medium | Diagnose model boundary from execution evidence |
| [08-05](../gym/tasks/08/08-05_model_boundary_extend/task.md) | 08 | extend | hard | Extend model boundary: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [08-06](../gym/tasks/08/08-06_model_boundary_refactor/task.md) | 08 | refactor | hard | Refactor model boundary: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 08-B: message identity

Features: MessagesState; add_messages; message IDs; RemoveMessage; human, AI, and tool messages.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [08-07](../gym/tasks/08/08-07_message_identity_build/task.md) | 08 | build | easy | Build message identity: Delete by the existing message ID. |
| [08-08](../gym/tasks/08/08-08_message_identity_fix/task.md) | 08 | fix | medium | Fix message identity: Correct an existing message without appending another customer message. |
| [08-09](../gym/tasks/08/08-09_message_identity_predict/task.md) | 08 | predict | easy | Predict message identity across the declared cases |
| [08-10](../gym/tasks/08/08-10_message_identity_trace/task.md) | 08 | trace | medium | Diagnose message identity from execution evidence |
| [08-11](../gym/tasks/08/08-11_message_identity_extend/task.md) | 08 | extend | hard | Extend message identity: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [08-12](../gym/tasks/08/08-12_message_identity_refactor/task.md) | 08 | refactor | hard | Refactor message identity: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 08-C: tokens and fakes

Features: messages stream mode; token chunks and metadata; scripted fake chat models; structured-output and streaming fake contracts.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [08-13](../gym/tasks/08/08-13_tokens_and_fakes_build/task.md) | 08 | build | easy | Build tokens and fakes: Join chunks without inserting characters that were never emitted. |
| [08-14](../gym/tasks/08/08-14_tokens_and_fakes_fix/task.md) | 08 | fix | medium | Fix tokens and fakes: Read the documented node name from stream metadata. |
| [08-15](../gym/tasks/08/08-15_tokens_and_fakes_predict/task.md) | 08 | predict | easy | Predict tokens and fakes across the declared cases |
| [08-16](../gym/tasks/08/08-16_tokens_and_fakes_trace/task.md) | 08 | trace | medium | Diagnose tokens and fakes from execution evidence |
| [08-17](../gym/tasks/08/08-17_tokens_and_fakes_extend/task.md) | 08 | extend | hard | Extend tokens and fakes: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [08-18](../gym/tasks/08/08-18_tokens_and_fakes_refactor/task.md) | 08 | refactor | hard | Refactor tokens and fakes: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

## 09 — Tools and the agent loop

[Lesson](../modules/09_tools_and_agent_loop/README.md)

### 09-A: tools and messages

Features: Tool definitions and schemas; tool calls; ToolMessage IDs; tool errors; deterministic policy lookup.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [09-01](../gym/tasks/09/09-01_tools_and_messages_build/task.md) | 09 | build | easy | Build tools and messages: Apply the deductible before proposing a payout. |
| [09-02](../gym/tasks/09/09-02_tools_and_messages_fix/task.md) | 09 | fix | medium | Fix tools and messages: Return a correlated tool error for an unknown policy. |
| [09-03](../gym/tasks/09/09-03_tools_and_messages_predict/task.md) | 09 | predict | easy | Predict tools and messages across the declared cases |
| [09-04](../gym/tasks/09/09-04_tools_and_messages_trace/task.md) | 09 | trace | medium | Diagnose tools and messages from execution evidence |
| [09-05](../gym/tasks/09/09-05_tools_and_messages_extend/task.md) | 09 | extend | hard | Extend tools and messages: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [09-06](../gym/tasks/09/09-06_tools_and_messages_refactor/task.md) | 09 | refactor | hard | Refactor tools and messages: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 09-B: manual react

Features: Manual ReAct graph; model node; ToolNode; tools_condition; bounded agent loop.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [09-07](../gym/tasks/09/09-07_manual_react_build/task.md) | 09 | build | easy | Build manual react: Return tool evidence to the model before ending. |
| [09-08](../gym/tasks/09/09-08_manual_react_fix/task.md) | 09 | fix | medium | Fix manual react: Let the agent observe a policy lookup failure. |
| [09-09](../gym/tasks/09/09-09_manual_react_predict/task.md) | 09 | predict | easy | Predict manual react across the declared cases |
| [09-10](../gym/tasks/09/09-10_manual_react_trace/task.md) | 09 | trace | medium | Diagnose manual react from execution evidence |
| [09-11](../gym/tasks/09/09-11_manual_react_extend/task.md) | 09 | extend | hard | Extend manual react: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [09-12](../gym/tasks/09/09-12_manual_react_refactor/task.md) | 09 | refactor | hard | Refactor manual react: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 09-C: tool runtime

Features: ToolRuntime; Runtime context; state and Store access; tool Command updates; trusted tool-call identity.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [09-13](../gym/tasks/09/09-13_tool_runtime_build/task.md) | 09 | build | easy | Build tool runtime: Write only in the trusted customer namespace. |
| [09-14](../gym/tasks/09/09-14_tool_runtime_fix/task.md) | 09 | fix | medium | Fix tool runtime: Keep the graph state consistent with the Store write. |
| [09-15](../gym/tasks/09/09-15_tool_runtime_predict/task.md) | 09 | predict | easy | Predict tool runtime across the declared cases |
| [09-16](../gym/tasks/09/09-16_tool_runtime_trace/task.md) | 09 | trace | medium | Diagnose tool runtime from execution evidence |
| [09-17](../gym/tasks/09/09-17_tool_runtime_extend/task.md) | 09 | extend | hard | Extend tool runtime: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [09-18](../gym/tasks/09/09-18_tool_runtime_design/task.md) | 09 | design | hard | Design tool runtime and justify the boundary policies |

## 10 — Prebuilt agents and when to drop down a level

[Lesson](../modules/10_prebuilt_agents/README.md)

### 10-A: create agent

Features: langchain.agents.create_agent; agent state; model and tools wiring; prebuilt versus custom graph.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [10-01](../gym/tasks/10/10-01_create_agent_build/task.md) | 10 | build | easy | Build create agent: Register the requested tool with the prebuilt agent. |
| [10-02](../gym/tasks/10/10-02_create_agent_fix/task.md) | 10 | fix | medium | Fix create agent: Reject unknown policy IDs, not the known fixture. |
| [10-03](../gym/tasks/10/10-03_create_agent_predict/task.md) | 10 | predict | easy | Predict create agent across the declared cases |
| [10-04](../gym/tasks/10/10-04_create_agent_trace/task.md) | 10 | trace | medium | Diagnose create agent from execution evidence |
| [10-05](../gym/tasks/10/10-05_create_agent_extend/task.md) | 10 | extend | hard | Extend create agent: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [10-06](../gym/tasks/10/10-06_create_agent_refactor/task.md) | 10 | refactor | hard | Refactor create agent: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 10-B: middleware

Features: Middleware lifecycle; before/after hooks; wrap_model_call; tool/model budgets; middleware state.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [10-07](../gym/tasks/10/10-07_middleware_build/task.md) | 10 | build | easy | Build middleware: Allow the configured number of model operations. |
| [10-08](../gym/tasks/10/10-08_middleware_fix/task.md) | 10 | fix | medium | Fix middleware: Enforce the independent tool budget. |
| [10-09](../gym/tasks/10/10-09_middleware_predict/task.md) | 10 | predict | easy | Predict middleware across the declared cases |
| [10-10](../gym/tasks/10/10-10_middleware_trace/task.md) | 10 | trace | medium | Diagnose middleware from execution evidence |
| [10-11](../gym/tasks/10/10-11_middleware_extend/task.md) | 10 | extend | hard | Extend middleware: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [10-12](../gym/tasks/10/10-12_middleware_design/task.md) | 10 | design | hard | Design middleware and justify the boundary policies |

### 10-C: agent composition

Features: Agent as a graph node; shared-state agent subgraph preview; agent input/output boundaries; behavior-preserving refactoring.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [10-13](../gym/tasks/10/10-13_agent_composition_build/task.md) | 10 | build | easy | Build agent composition: Map the specialist answer into the parent explanation field. |
| [10-14](../gym/tasks/10/10-14_agent_composition_fix/task.md) | 10 | fix | medium | Fix agent composition: Do not turn an explanation into payment approval. |
| [10-15](../gym/tasks/10/10-15_agent_composition_predict/task.md) | 10 | predict | easy | Predict agent composition across the declared cases |
| [10-16](../gym/tasks/10/10-16_agent_composition_trace/task.md) | 10 | trace | medium | Diagnose agent composition from execution evidence |
| [10-17](../gym/tasks/10/10-17_agent_composition_extend/task.md) | 10 | extend | hard | Extend agent composition: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [10-18](../gym/tasks/10/10-18_agent_composition_refactor/task.md) | 10 | refactor | hard | Refactor agent composition: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

## 11 — Memory

[Lesson](../modules/11_memory/README.md)

### 11-A: short term memory

Features: Thread checkpoints as short-term memory; context windows; trim_messages; summarization nodes.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [11-01](../gym/tasks/11/11-01_short_term_memory_build/task.md) | 11 | build | easy | Build short term memory: Bound the messages sent to the model. |
| [11-02](../gym/tasks/11/11-02_short_term_memory_fix/task.md) | 11 | fix | medium | Fix short term memory: Use a new message ID for a new turn instead of overwriting the previous turn. |
| [11-03](../gym/tasks/11/11-03_short_term_memory_predict/task.md) | 11 | predict | easy | Predict short term memory across the declared cases |
| [11-04](../gym/tasks/11/11-04_short_term_memory_trace/task.md) | 11 | trace | medium | Diagnose short term memory from execution evidence |
| [11-05](../gym/tasks/11/11-05_short_term_memory_extend/task.md) | 11 | extend | hard | Extend short term memory: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [11-06](../gym/tasks/11/11-06_short_term_memory_refactor/task.md) | 11 | refactor | hard | Refactor short term memory: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 11-B: store namespaces

Features: InMemoryStore; namespaces; put, get, search, and delete; runtime.store; semantic, episodic, and procedural memory.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [11-07](../gym/tasks/11/11-07_store_namespaces_build/task.md) | 11 | build | easy | Build store namespaces: Store each customer's facts in a distinct namespace. |
| [11-08](../gym/tasks/11/11-08_store_namespaces_fix/task.md) | 11 | fix | medium | Fix store namespaces: Delete the actual memory key. |
| [11-09](../gym/tasks/11/11-09_store_namespaces_predict/task.md) | 11 | predict | easy | Predict store namespaces across the declared cases |
| [11-10](../gym/tasks/11/11-10_store_namespaces_trace/task.md) | 11 | trace | medium | Diagnose store namespaces from execution evidence |
| [11-11](../gym/tasks/11/11-11_store_namespaces_extend/task.md) | 11 | extend | hard | Extend store namespaces: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [11-12](../gym/tasks/11/11-12_store_namespaces_refactor/task.md) | 11 | refactor | hard | Refactor store namespaces: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 11-C: semantic and privacy

Features: Embeddings basics; semantic Store index; deterministic fake embeddings; memory deletion; checkpoint versus Store retention.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [11-13](../gym/tasks/11/11-13_semantic_and_privacy_build/task.md) | 11 | build | easy | Build semantic and privacy: Scope semantic search to the authenticated customer. |
| [11-14](../gym/tasks/11/11-14_semantic_and_privacy_fix/task.md) | 11 | fix | medium | Fix semantic and privacy: Delete checkpoint history separately from Store records. |
| [11-15](../gym/tasks/11/11-15_semantic_and_privacy_predict/task.md) | 11 | predict | easy | Predict semantic and privacy across the declared cases |
| [11-16](../gym/tasks/11/11-16_semantic_and_privacy_trace/task.md) | 11 | trace | medium | Diagnose semantic and privacy from execution evidence |
| [11-17](../gym/tasks/11/11-17_semantic_and_privacy_extend/task.md) | 11 | extend | hard | Extend semantic and privacy: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [11-18](../gym/tasks/11/11-18_semantic_and_privacy_design/task.md) | 11 | design | hard | Design semantic and privacy and justify the boundary policies |

## 12 — Workflow patterns with LLMs

[Lesson](../modules/12_workflow_patterns/README.md)

### 12-A: chains and gates

Features: Prompt chaining; deterministic gates; model-based routing with validated outputs; workflow versus agent choice.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [12-01](../gym/tasks/12/12-01_chains_and_gates_build/task.md) | 12 | build | easy | Build chains and gates: Reject contradictory extracted facts before drafting. |
| [12-02](../gym/tasks/12/12-02_chains_and_gates_fix/task.md) | 12 | fix | medium | Fix chains and gates: Stop the chain when the fact gate fails. |
| [12-03](../gym/tasks/12/12-03_chains_and_gates_predict/task.md) | 12 | predict | easy | Predict chains and gates across the declared cases |
| [12-04](../gym/tasks/12/12-04_chains_and_gates_trace/task.md) | 12 | trace | medium | Diagnose chains and gates from execution evidence |
| [12-05](../gym/tasks/12/12-05_chains_and_gates_extend/task.md) | 12 | extend | hard | Extend chains and gates: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [12-06](../gym/tasks/12/12-06_chains_and_gates_design/task.md) | 12 | design | hard | Design chains and gates and justify the boundary policies |

### 12-B: orchestrator workers

Features: Parallel LLM branches; orchestrator-worker pattern; Send with structured worker plans; result aggregation.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [12-07](../gym/tasks/12/12-07_orchestrator_workers_build/task.md) | 12 | build | easy | Build orchestrator workers: Accumulate every worker result instead of overwriting sibling reports. |
| [12-08](../gym/tasks/12/12-08_orchestrator_workers_fix/task.md) | 12 | fix | medium | Fix orchestrator workers: Reject a plan that delegates the same section twice. |
| [12-09](../gym/tasks/12/12-09_orchestrator_workers_predict/task.md) | 12 | predict | easy | Predict orchestrator workers across the declared cases |
| [12-10](../gym/tasks/12/12-10_orchestrator_workers_trace/task.md) | 12 | trace | medium | Diagnose orchestrator workers from execution evidence |
| [12-11](../gym/tasks/12/12-11_orchestrator_workers_extend/task.md) | 12 | extend | hard | Extend orchestrator workers: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [12-12](../gym/tasks/12/12-12_orchestrator_workers_refactor/task.md) | 12 | refactor | hard | Refactor orchestrator workers: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 12-C: evaluator optimizer

Features: Evaluator-optimizer loop; factual and tone criteria; iteration budgets; termination on success or exhaustion.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [12-13](../gym/tasks/12/12-13_evaluator_optimizer_build/task.md) | 12 | build | easy | Build evaluator optimizer: Stop unsuccessful revision at the configured budget. |
| [12-14](../gym/tasks/12/12-14_evaluator_optimizer_fix/task.md) | 12 | fix | medium | Fix evaluator optimizer: Require the authoritative deductible fact. |
| [12-15](../gym/tasks/12/12-15_evaluator_optimizer_predict/task.md) | 12 | predict | easy | Predict evaluator optimizer across the declared cases |
| [12-16](../gym/tasks/12/12-16_evaluator_optimizer_trace/task.md) | 12 | trace | medium | Diagnose evaluator optimizer from execution evidence |
| [12-17](../gym/tasks/12/12-17_evaluator_optimizer_extend/task.md) | 12 | extend | hard | Extend evaluator optimizer: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [12-18](../gym/tasks/12/12-18_evaluator_optimizer_refactor/task.md) | 12 | refactor | hard | Refactor evaluator optimizer: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

## 13 — Subgraphs

[Lesson](../modules/13_subgraphs/README.md)

### 13-A: shared subgraph

Features: Compiled subgraph as node; shared state keys; parent reducers; reuse across workflows.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [13-01](../gym/tasks/13/13-01_shared_subgraph_build/task.md) | 13 | build | easy | Build shared subgraph: Keep evidence already recorded by the parent. |
| [13-02](../gym/tasks/13/13-02_shared_subgraph_fix/task.md) | 13 | fix | medium | Fix shared subgraph: Apply the high-value risk boundary inside the reusable child. |
| [13-03](../gym/tasks/13/13-03_shared_subgraph_predict/task.md) | 13 | predict | easy | Predict shared subgraph across the declared cases |
| [13-04](../gym/tasks/13/13-04_shared_subgraph_trace/task.md) | 13 | trace | medium | Diagnose shared subgraph from execution evidence |
| [13-05](../gym/tasks/13/13-05_shared_subgraph_extend/task.md) | 13 | extend | hard | Extend shared subgraph: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [13-06](../gym/tasks/13/13-06_shared_subgraph_refactor/task.md) | 13 | refactor | hard | Refactor shared subgraph: Extract parallel fraud checks into a reusable subgraph; keep both workflow outputs and rejection cases unchanged. |

### 13-B: schema adapters

Features: Calling a subgraph inside a node; input/output schema conversion; private child state; context boundaries.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [13-07](../gym/tasks/13/13-07_schema_adapters_build/task.md) | 13 | build | easy | Build schema adapters: Map the actual claim amount into the child input. |
| [13-08](../gym/tasks/13/13-08_schema_adapters_fix/task.md) | 13 | fix | medium | Fix schema adapters: Preserve the exact review threshold. |
| [13-09](../gym/tasks/13/13-09_schema_adapters_predict/task.md) | 13 | predict | easy | Predict schema adapters across the declared cases |
| [13-10](../gym/tasks/13/13-10_schema_adapters_trace/task.md) | 13 | trace | medium | Diagnose schema adapters from execution evidence |
| [13-11](../gym/tasks/13/13-11_schema_adapters_extend/task.md) | 13 | extend | hard | Extend schema adapters: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [13-12](../gym/tasks/13/13-12_schema_adapters_refactor/task.md) | 13 | refactor | hard | Refactor schema adapters: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 13-C: subgraph persistence

Features: Inherited checkpointers; per-invocation versus persistent subgraphs; nested interrupts; get_state subgraphs; stream namespaces.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [13-13](../gym/tasks/13/13-13_subgraph_persistence_build/task.md) | 13 | build | easy | Build subgraph persistence: Request nested snapshots when inspecting child state. |
| [13-14](../gym/tasks/13/13-14_subgraph_persistence_fix/task.md) | 13 | fix | medium | Fix subgraph persistence: Reject a string masquerading as a human decision. |
| [13-15](../gym/tasks/13/13-15_subgraph_persistence_predict/task.md) | 13 | predict | easy | Predict subgraph persistence across the declared cases |
| [13-16](../gym/tasks/13/13-16_subgraph_persistence_trace/task.md) | 13 | trace | medium | Diagnose subgraph persistence from execution evidence |
| [13-17](../gym/tasks/13/13-17_subgraph_persistence_extend/task.md) | 13 | extend | hard | Extend subgraph persistence: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [13-18](../gym/tasks/13/13-18_subgraph_persistence_design/task.md) | 13 | design | hard | Design subgraph persistence and justify the boundary policies |

## 14 — Multi-agent systems

[Lesson](../modules/14_multi_agent_systems/README.md)

### 14-A: supervisor tools

Features: Supervisor pattern; agents as tools; private histories; context engineering; direct patterns versus helper packages.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [14-01](../gym/tasks/14/14-01_supervisor_tools_build/task.md) | 14 | build | easy | Build supervisor tools: Register both specialist capabilities with the supervisor. |
| [14-02](../gym/tasks/14/14-02_supervisor_tools_fix/task.md) | 14 | fix | medium | Fix supervisor tools: Keep specialist roles attached to the evidence they reviewed. |
| [14-03](../gym/tasks/14/14-03_supervisor_tools_predict/task.md) | 14 | predict | easy | Predict supervisor tools across the declared cases |
| [14-04](../gym/tasks/14/14-04_supervisor_tools_trace/task.md) | 14 | trace | medium | Diagnose supervisor tools from execution evidence |
| [14-05](../gym/tasks/14/14-05_supervisor_tools_extend/task.md) | 14 | extend | hard | Extend supervisor tools: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [14-06](../gym/tasks/14/14-06_supervisor_tools_refactor/task.md) | 14 | refactor | hard | Refactor supervisor tools: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 14-B: handoffs

Features: Command.PARENT; handoffs; shared message history; parent reducers; tool-call pairing at handoff.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [14-07](../gym/tasks/14/14-07_handoffs_build/task.md) | 14 | build | easy | Build handoffs: Address the parent graph when handing off to its specialist. |
| [14-08](../gym/tasks/14/14-08_handoffs_fix/task.md) | 14 | fix | medium | Fix handoffs: Pair the handoff acknowledgment with its AI request. |
| [14-09](../gym/tasks/14/14-09_handoffs_predict/task.md) | 14 | predict | easy | Predict handoffs across the declared cases |
| [14-10](../gym/tasks/14/14-10_handoffs_trace/task.md) | 14 | trace | medium | Diagnose handoffs from execution evidence |
| [14-11](../gym/tasks/14/14-11_handoffs_extend/task.md) | 14 | extend | hard | Extend handoffs: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [14-12](../gym/tasks/14/14-12_handoffs_refactor/task.md) | 14 | refactor | hard | Refactor handoffs: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 14-C: team tradeoffs

Features: Swarm-style routing; active-agent state; bounded delegation; single versus multi-agent evaluation.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [14-13](../gym/tasks/14/14-13_team_tradeoffs_build/task.md) | 14 | build | easy | Build team tradeoffs: Stop delegation when the business call budget is exhausted. |
| [14-14](../gym/tasks/14/14-14_team_tradeoffs_fix/task.md) | 14 | fix | medium | Fix team tradeoffs: Advance to the next specialist instead of handing work back to itself. |
| [14-15](../gym/tasks/14/14-15_team_tradeoffs_predict/task.md) | 14 | predict | easy | Predict team tradeoffs across the declared cases |
| [14-16](../gym/tasks/14/14-16_team_tradeoffs_trace/task.md) | 14 | trace | medium | Diagnose team tradeoffs from execution evidence |
| [14-17](../gym/tasks/14/14-17_team_tradeoffs_extend/task.md) | 14 | extend | hard | Extend team tradeoffs: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [14-18](../gym/tasks/14/14-18_team_tradeoffs_design/task.md) | 14 | design | hard | Design team tradeoffs and justify the boundary policies |

## 15 — The Functional API

[Lesson](../modules/15_functional_api/README.md)

### 15-A: entrypoints tasks

Features: entrypoint; task; single-input contract; task futures; result(); normal Python control flow.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [15-01](../gym/tasks/15/15-01_entrypoints_tasks_build/task.md) | 15 | build | easy | Build entrypoints tasks: Resolve the normalization future before reading its fields. |
| [15-02](../gym/tasks/15/15-02_entrypoints_tasks_fix/task.md) | 15 | fix | medium | Fix entrypoints tasks: Match the Graph API fast-track boundary. |
| [15-03](../gym/tasks/15/15-03_entrypoints_tasks_predict/task.md) | 15 | predict | easy | Predict entrypoints tasks across the declared cases |
| [15-04](../gym/tasks/15/15-04_entrypoints_tasks_trace/task.md) | 15 | trace | medium | Diagnose entrypoints tasks from execution evidence |
| [15-05](../gym/tasks/15/15-05_entrypoints_tasks_extend/task.md) | 15 | extend | hard | Extend entrypoints tasks: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [15-06](../gym/tasks/15/15-06_entrypoints_tasks_refactor/task.md) | 15 | refactor | hard | Refactor entrypoints tasks: Convert the working Graph API pipeline to an entrypoint with normalize and route tasks, preserving every existing result and validation error. |

### 15-B: parallel futures

Features: Starting tasks before resolving futures; parallel Functional API tasks; deterministic aggregation; graph versus functional comparison.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [15-07](../gym/tasks/15/15-07_parallel_futures_build/task.md) | 15 | build | easy | Build parallel futures: Canonicalize Functional API results independently of input order. |
| [15-08](../gym/tasks/15/15-08_parallel_futures_fix/task.md) | 15 | fix | medium | Fix parallel futures: Preserve every parallel graph result. |
| [15-09](../gym/tasks/15/15-09_parallel_futures_predict/task.md) | 15 | predict | easy | Predict parallel futures across the declared cases |
| [15-10](../gym/tasks/15/15-10_parallel_futures_trace/task.md) | 15 | trace | medium | Diagnose parallel futures from execution evidence |
| [15-11](../gym/tasks/15/15-11_parallel_futures_extend/task.md) | 15 | extend | hard | Extend parallel futures: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [15-12](../gym/tasks/15/15-12_parallel_futures_refactor/task.md) | 15 | refactor | hard | Refactor parallel futures: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 15-C: functional resume

Features: Functional persistence; interrupts; saved task results; entrypoint replay; deterministic task ordering.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [15-13](../gym/tasks/15/15-13_functional_resume_build/task.md) | 15 | build | easy | Build functional resume: Use a task boundary so completed evidence can be reused during replay. |
| [15-14](../gym/tasks/15/15-14_functional_resume_fix/task.md) | 15 | fix | medium | Fix functional resume: Validate the resumed approval before returning a business result. |
| [15-15](../gym/tasks/15/15-15_functional_resume_predict/task.md) | 15 | predict | easy | Predict functional resume across the declared cases |
| [15-16](../gym/tasks/15/15-16_functional_resume_trace/task.md) | 15 | trace | medium | Diagnose functional resume from execution evidence |
| [15-17](../gym/tasks/15/15-17_functional_resume_extend/task.md) | 15 | extend | hard | Extend functional resume: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [15-18](../gym/tasks/15/15-18_functional_resume_design/task.md) | 15 | design | hard | Design functional resume and justify the boundary policies |

## 16 — External systems and MCP

[Lesson](../modules/16_external_systems_and_mcp/README.md)

### 16-A: api boundaries

Features: Async and await primer; HTTP timeouts; transient retries; idempotency keys; injectable transports.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [16-01](../gym/tasks/16/16-01_api_boundaries_build/task.md) | 16 | build | easy | Build api boundaries: Reuse the same idempotency key across a retry. |
| [16-02](../gym/tasks/16/16-02_api_boundaries_fix/task.md) | 16 | fix | medium | Fix api boundaries: Honor the bounded retry allowance after a lost acknowledgment. |
| [16-03](../gym/tasks/16/16-03_api_boundaries_predict/task.md) | 16 | predict | easy | Predict api boundaries across the declared cases |
| [16-04](../gym/tasks/16/16-04_api_boundaries_trace/task.md) | 16 | trace | medium | Diagnose api boundaries from execution evidence |
| [16-05](../gym/tasks/16/16-05_api_boundaries_extend/task.md) | 16 | extend | hard | Extend api boundaries: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [16-06](../gym/tasks/16/16-06_api_boundaries_refactor/task.md) | 16 | refactor | hard | Refactor api boundaries: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 16-B: mcp server

Features: Official MCP SDK; local stdio server; tool schemas; server lifecycle; synthetic claims data permissions.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [16-07](../gym/tasks/16/16-07_mcp_server_build/task.md) | 16 | build | easy | Build mcp server: Invoke a tool from the published MCP registry. |
| [16-08](../gym/tasks/16/16-08_mcp_server_fix/task.md) | 16 | fix | medium | Fix mcp server: Pass the requested synthetic claim through schema validation. |
| [16-09](../gym/tasks/16/16-09_mcp_server_predict/task.md) | 16 | predict | easy | Predict mcp server across the declared cases |
| [16-10](../gym/tasks/16/16-10_mcp_server_trace/task.md) | 16 | trace | medium | Diagnose mcp server from execution evidence |
| [16-11](../gym/tasks/16/16-11_mcp_server_extend/task.md) | 16 | extend | hard | Extend mcp server: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [16-12](../gym/tasks/16/16-12_mcp_server_refactor/task.md) | 16 | refactor | hard | Refactor mcp server: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 16-C: mcp adapter

Features: langchain-mcp-adapters; MultiServerMCPClient; loading tools; async client lifetime; adapter-SDK compatibility; Beta successor awareness.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [16-13](../gym/tasks/16/16-13_mcp_adapter_build/task.md) | 16 | build | easy | Build mcp adapter: Load MCP tools before constructing the agent. |
| [16-14](../gym/tasks/16/16-14_mcp_adapter_fix/task.md) | 16 | fix | medium | Fix mcp adapter: Send the selected claim identifier to the MCP service. |
| [16-15](../gym/tasks/16/16-15_mcp_adapter_predict/task.md) | 16 | predict | easy | Predict mcp adapter across the declared cases |
| [16-16](../gym/tasks/16/16-16_mcp_adapter_trace/task.md) | 16 | trace | medium | Diagnose mcp adapter from execution evidence |
| [16-17](../gym/tasks/16/16-17_mcp_adapter_extend/task.md) | 16 | extend | hard | Extend mcp adapter: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [16-18](../gym/tasks/16/16-18_mcp_adapter_design/task.md) | 16 | design | hard | Design mcp adapter and justify the boundary policies |

## 17 — Durable execution and long-running workflows

[Lesson](../modules/17_durable_execution/README.md)

### 17-A: durable side effects

Features: Durability modes in failures; task-wrapped side effects; checkpointed nondeterminism; idempotency; crash windows.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [17-01](../gym/tasks/17/17-01_durable_side_effects_build/task.md) | 17 | build | easy | Build durable side effects: Keep the effect identity stable across process death. |
| [17-02](../gym/tasks/17/17-02_durable_side_effects_fix/task.md) | 17 | fix | medium | Fix durable side effects: Make the crash supervisor recognize the documented owned-worker exit. |
| [17-03](../gym/tasks/17/17-03_durable_side_effects_predict/task.md) | 17 | predict | easy | Predict durable side effects across the declared cases |
| [17-04](../gym/tasks/17/17-04_durable_side_effects_trace/task.md) | 17 | trace | medium | Diagnose durable side effects from execution evidence |
| [17-05](../gym/tasks/17/17-05_durable_side_effects_extend/task.md) | 17 | extend | hard | Extend durable side effects: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [17-06](../gym/tasks/17/17-06_durable_side_effects_refactor/task.md) | 17 | refactor | hard | Refactor durable side effects: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 17-B: recovery policies

Features: RetryPolicy after transient failures; async node timeouts; TimeoutPolicy; NodeError and error_handler; compensation; RunControl graceful drain.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [17-07](../gym/tasks/17/17-07_recovery_policies_build/task.md) | 17 | build | easy | Build recovery policies: Retry the recoverable first failure before routing to manual review. |
| [17-08](../gym/tasks/17/17-08_recovery_policies_fix/task.md) | 17 | fix | medium | Fix recovery policies: Do not label an exhausted or timed-out request as successful. |
| [17-09](../gym/tasks/17/17-09_recovery_policies_predict/task.md) | 17 | predict | easy | Predict recovery policies across the declared cases |
| [17-10](../gym/tasks/17/17-10_recovery_policies_trace/task.md) | 17 | trace | medium | Diagnose recovery policies from execution evidence |
| [17-11](../gym/tasks/17/17-11_recovery_policies_extend/task.md) | 17 | extend | hard | Extend recovery policies: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [17-12](../gym/tasks/17/17-12_recovery_policies_design/task.md) | 17 | design | hard | Design recovery policies and justify the boundary policies |

### 17-C: long wait postgres

Features: Durable interrupt waits; simulated time; PostgresSaver and AsyncPostgresSaver; setup lifecycle; shared database persistence.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [17-13](../gym/tasks/17/17-13_long_wait_postgres_build/task.md) | 17 | build | easy | Build long wait postgres: Reject a receipt date earlier than the request date. |
| [17-14](../gym/tasks/17/17-14_long_wait_postgres_fix/task.md) | 17 | fix | medium | Fix long wait postgres: Compute elapsed business time from explicit dates. |
| [17-15](../gym/tasks/17/17-15_long_wait_postgres_predict/task.md) | 17 | predict | easy | Predict long wait postgres across the declared cases |
| [17-16](../gym/tasks/17/17-16_long_wait_postgres_trace/task.md) | 17 | trace | medium | Diagnose long wait postgres from execution evidence |
| [17-17](../gym/tasks/17/17-17_long_wait_postgres_extend/task.md) | 17 | extend | hard | Extend long wait postgres: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [17-18](../gym/tasks/17/17-18_long_wait_postgres_refactor/task.md) | 17 | refactor | hard | Refactor long wait postgres: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

## 18 — Streaming to user interfaces

[Lesson](../modules/18_streaming_user_interfaces/README.md)

### 18-A: async streams

Features: ainvoke; astream; async context propagation; all seven stream modes; v2 serialization; cancellation.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [18-01](../gym/tasks/18/18-01_async_streams_build/task.md) | 18 | build | easy | Build async streams: Accumulate chunks instead of replacing the previous text. |
| [18-02](../gym/tasks/18/18-02_async_streams_fix/task.md) | 18 | fix | medium | Fix async streams: Request the intended seven stream projections. |
| [18-03](../gym/tasks/18/18-03_async_streams_predict/task.md) | 18 | predict | easy | Predict async streams across the declared cases |
| [18-04](../gym/tasks/18/18-04_async_streams_trace/task.md) | 18 | trace | medium | Diagnose async streams from execution evidence |
| [18-05](../gym/tasks/18/18-05_async_streams_extend/task.md) | 18 | extend | hard | Extend async streams: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [18-06](../gym/tasks/18/18-06_async_streams_refactor/task.md) | 18 | refactor | hard | Refactor async streams: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 18-B: sse api

Features: FastAPI streaming responses; server-sent event framing; JSON-safe serialization; reconnect semantics; authenticated thread ownership.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [18-07](../gym/tasks/18/18-07_sse_api_build/task.md) | 18 | build | easy | Build sse api: Preserve the exact event payload through SSE encoding. |
| [18-08](../gym/tasks/18/18-08_sse_api_fix/task.md) | 18 | fix | medium | Fix sse api: Carry a rejection through the authenticated workflow. |
| [18-09](../gym/tasks/18/18-09_sse_api_predict/task.md) | 18 | predict | easy | Predict sse api across the declared cases |
| [18-10](../gym/tasks/18/18-10_sse_api_trace/task.md) | 18 | trace | medium | Diagnose sse api from execution evidence |
| [18-11](../gym/tasks/18/18-11_sse_api_extend/task.md) | 18 | extend | hard | Extend sse api: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [18-12](../gym/tasks/18/18-12_sse_api_refactor/task.md) | 18 | refactor | hard | Refactor sse api: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 18-C: adjuster dashboard

Features: Streamlit state; progress and token rendering; approve/reject controls; stale interrupt detection; Beta v3 stream projections.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [18-13](../gym/tasks/18/18-13_adjuster_dashboard_build/task.md) | 18 | build | easy | Build adjuster dashboard: Render every received text chunk in order. |
| [18-14](../gym/tasks/18/18-14_adjuster_dashboard_fix/task.md) | 18 | fix | medium | Fix adjuster dashboard: Replace the stale approval identity with the current snapshot. |
| [18-15](../gym/tasks/18/18-15_adjuster_dashboard_predict/task.md) | 18 | predict | easy | Predict adjuster dashboard across the declared cases |
| [18-16](../gym/tasks/18/18-16_adjuster_dashboard_trace/task.md) | 18 | trace | medium | Diagnose adjuster dashboard from execution evidence |
| [18-17](../gym/tasks/18/18-17_adjuster_dashboard_extend/task.md) | 18 | extend | hard | Extend adjuster dashboard: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [18-18](../gym/tasks/18/18-18_adjuster_dashboard_design/task.md) | 18 | design | hard | Design adjuster dashboard and justify the boundary policies |

## 19 — Testing and evaluation

[Lesson](../modules/19_testing_and_evaluation/README.md)

### 19-A: test graph behavior

Features: pytest primer in depth; node unit tests; graph tests; fake models; routing and final-state assertions.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [19-01](../gym/tasks/19/19-01_test_graph_behavior_build/task.md) | 19 | build | easy | Build test graph behavior: Specify the inclusive fast-track boundary in the test oracle. |
| [19-02](../gym/tasks/19/19-02_test_graph_behavior_fix/task.md) | 19 | fix | medium | Fix test graph behavior: Include boolean cents in invalid-input coverage. |
| [19-03](../gym/tasks/19/19-03_test_graph_behavior_predict/task.md) | 19 | predict | easy | Predict test graph behavior across the declared cases |
| [19-04](../gym/tasks/19/19-04_test_graph_behavior_trace/task.md) | 19 | trace | medium | Diagnose test graph behavior from execution evidence |
| [19-05](../gym/tasks/19/19-05_test_graph_behavior_extend/task.md) | 19 | extend | hard | Extend test graph behavior: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [19-06](../gym/tasks/19/19-06_test_graph_behavior_refactor/task.md) | 19 | refactor | hard | Refactor test graph behavior: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 19-B: test durable execution

Features: Interrupt/resume tests; checkpoint assertions; superstep-aware snapshots; reducer properties; subprocess isolation.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [19-07](../gym/tasks/19/19-07_test_durable_execution_build/task.md) | 19 | build | easy | Build test durable execution: Test rejection as well as approval on resume. |
| [19-08](../gym/tasks/19/19-08_test_durable_execution_fix/task.md) | 19 | fix | medium | Fix test durable execution: Capture the pre-resume pending state before it changes. |
| [19-09](../gym/tasks/19/19-09_test_durable_execution_predict/task.md) | 19 | predict | easy | Predict test durable execution across the declared cases |
| [19-10](../gym/tasks/19/19-10_test_durable_execution_trace/task.md) | 19 | trace | medium | Diagnose test durable execution from execution evidence |
| [19-11](../gym/tasks/19/19-11_test_durable_execution_extend/task.md) | 19 | extend | hard | Extend test durable execution: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [19-12](../gym/tasks/19/19-12_test_durable_execution_refactor/task.md) | 19 | refactor | hard | Refactor test durable execution: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 19-C: trajectory evals

Features: Local evaluation harness; golden JSONL cases; trajectory matching; agentevals; optional LangSmith evaluation.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [19-13](../gym/tasks/19/19-13_trajectory_evals_build/task.md) | 19 | build | easy | Build trajectory evals: Respect strict ordering when the evaluation contract requests it. |
| [19-14](../gym/tasks/19/19-14_trajectory_evals_fix/task.md) | 19 | fix | medium | Fix trajectory evals: Check the policy arguments, not only tool names. |
| [19-15](../gym/tasks/19/19-15_trajectory_evals_predict/task.md) | 19 | predict | easy | Predict trajectory evals across the declared cases |
| [19-16](../gym/tasks/19/19-16_trajectory_evals_trace/task.md) | 19 | trace | medium | Diagnose trajectory evals from execution evidence |
| [19-17](../gym/tasks/19/19-17_trajectory_evals_extend/task.md) | 19 | extend | hard | Extend trajectory evals: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [19-18](../gym/tasks/19/19-18_trajectory_evals_design/task.md) | 19 | design | hard | Design trajectory evals and justify the boundary policies |

## 20 — Observability and visual debugging

[Lesson](../modules/20_observability_and_debugging/README.md)

### 20-A: local visual debugging

Features: langgraph.json; langgraph dev; graph export; Studio; local/offline alternative; static debugging breakpoints.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [20-01](../gym/tasks/20/20-01_local_visual_debugging_build/task.md) | 20 | build | easy | Build local visual debugging: Resolve the graph name declared in the server configuration. |
| [20-02](../gym/tasks/20/20-02_local_visual_debugging_fix/task.md) | 20 | fix | medium | Fix local visual debugging: Debug the supplied claim amount rather than a substituted value. |
| [20-03](../gym/tasks/20/20-03_local_visual_debugging_predict/task.md) | 20 | predict | easy | Predict local visual debugging across the declared cases |
| [20-04](../gym/tasks/20/20-04_local_visual_debugging_trace/task.md) | 20 | trace | medium | Diagnose local visual debugging from execution evidence |
| [20-05](../gym/tasks/20/20-05_local_visual_debugging_extend/task.md) | 20 | extend | hard | Extend local visual debugging: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [20-06](../gym/tasks/20/20-06_local_visual_debugging_refactor/task.md) | 20 | refactor | hard | Refactor local visual debugging: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 20-B: structured logs

Features: Structured logging; correlation IDs; thread and run identifiers; redaction; observability without accounts.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [20-07](../gym/tasks/20/20-07_structured_logs_build/task.md) | 20 | build | easy | Build structured logs: Use the documented event category for node completion. |
| [20-08](../gym/tasks/20/20-08_structured_logs_fix/task.md) | 20 | fix | medium | Fix structured logs: Attach each log record to its actual node. |
| [20-09](../gym/tasks/20/20-09_structured_logs_predict/task.md) | 20 | predict | easy | Predict structured logs across the declared cases |
| [20-10](../gym/tasks/20/20-10_structured_logs_trace/task.md) | 20 | trace | medium | Diagnose structured logs from execution evidence |
| [20-11](../gym/tasks/20/20-11_structured_logs_extend/task.md) | 20 | extend | hard | Extend structured logs: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [20-12](../gym/tasks/20/20-12_structured_logs_refactor/task.md) | 20 | refactor | hard | Refactor structured logs: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 20-C: optional tracing

Features: Optional LangSmith tracing; account requirements; local trace replay; trace metadata; time-travel debugging.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [20-13](../gym/tasks/20/20-13_optional_tracing_build/task.md) | 20 | build | easy | Build optional tracing: Apply the corrected amount to the fork before resuming routing. |
| [20-14](../gym/tasks/20/20-14_optional_tracing_fix/task.md) | 20 | fix | medium | Fix optional tracing: Fork at the intended pre-routing boundary. |
| [20-15](../gym/tasks/20/20-15_optional_tracing_predict/task.md) | 20 | predict | easy | Predict optional tracing across the declared cases |
| [20-16](../gym/tasks/20/20-16_optional_tracing_trace/task.md) | 20 | trace | medium | Diagnose optional tracing from execution evidence |
| [20-17](../gym/tasks/20/20-17_optional_tracing_extend/task.md) | 20 | extend | hard | Extend optional tracing: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [20-18](../gym/tasks/20/20-18_optional_tracing_design/task.md) | 20 | design | hard | Design optional tracing and justify the boundary policies |

## 21 — Security and guardrails

[Lesson](../modules/21_security_and_guardrails/README.md)

### 21-A: untrusted input

Features: Prompt injection; deterministic authorization; validated structured output; allowlisted routes; least-privilege tools.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [21-01](../gym/tasks/21/21-01_untrusted_input_build/task.md) | 21 | build | easy | Build untrusted input: Do not let extracted text authorize a payment. |
| [21-02](../gym/tasks/21/21-02_untrusted_input_fix/task.md) | 21 | fix | medium | Fix untrusted input: Preserve validated amounts before applying deterministic routing. |
| [21-03](../gym/tasks/21/21-03_untrusted_input_predict/task.md) | 21 | predict | easy | Predict untrusted input across the declared cases |
| [21-04](../gym/tasks/21/21-04_untrusted_input_trace/task.md) | 21 | trace | medium | Diagnose untrusted input from execution evidence |
| [21-05](../gym/tasks/21/21-05_untrusted_input_extend/task.md) | 21 | extend | hard | Extend untrusted input: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [21-06](../gym/tasks/21/21-06_untrusted_input_refactor/task.md) | 21 | refactor | hard | Refactor untrusted input: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 21-B: approval and limits

Features: Approval before side effects; authorization outside the model; recursion and tool-call budgets; token/cost budgets; audit events.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [21-07](../gym/tasks/21/21-07_approval_and_limits_build/task.md) | 21 | build | easy | Build approval and limits: Enforce the separate planned-call budget. |
| [21-08](../gym/tasks/21/21-08_approval_and_limits_fix/task.md) | 21 | fix | medium | Fix approval and limits: Reject an operation above the token admission budget. |
| [21-09](../gym/tasks/21/21-09_approval_and_limits_predict/task.md) | 21 | predict | easy | Predict approval and limits across the declared cases |
| [21-10](../gym/tasks/21/21-10_approval_and_limits_trace/task.md) | 21 | trace | medium | Diagnose approval and limits from execution evidence |
| [21-11](../gym/tasks/21/21-11_approval_and_limits_extend/task.md) | 21 | extend | hard | Extend approval and limits: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [21-12](../gym/tasks/21/21-12_approval_and_limits_design/task.md) | 21 | design | hard | Design approval and limits and justify the boundary policies |

### 21-C: private checkpoints

Features: PII minimization; EncryptedSerializer; encryption key handling; retention and deletion; audit-trail limitations.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [21-13](../gym/tasks/21/21-13_private_checkpoints_build/task.md) | 21 | build | easy | Build private checkpoints: Install encryption on the actual checkpointer, not just a standalone serialization demo. |
| [21-14](../gym/tasks/21/21-14_private_checkpoints_fix/task.md) | 21 | fix | medium | Fix private checkpoints: Apply the requested thread-retention deletion. |
| [21-15](../gym/tasks/21/21-15_private_checkpoints_predict/task.md) | 21 | predict | easy | Predict private checkpoints across the declared cases |
| [21-16](../gym/tasks/21/21-16_private_checkpoints_trace/task.md) | 21 | trace | medium | Diagnose private checkpoints from execution evidence |
| [21-17](../gym/tasks/21/21-17_private_checkpoints_extend/task.md) | 21 | extend | hard | Extend private checkpoints: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [21-18](../gym/tasks/21/21-18_private_checkpoints_refactor/task.md) | 21 | refactor | hard | Refactor private checkpoints: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

## 22 — Deployment

[Lesson](../modules/22_deployment/README.md)

### 22-A: compose stack

Features: FastAPI self-hosting; Docker Compose API/Postgres/UI; healthchecks; schema setup; configuration and secrets.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [22-01](../gym/tasks/22/22-01_compose_stack_build/task.md) | 22 | build | easy | Build compose stack: Reject a database without a readiness check. |
| [22-02](../gym/tasks/22/22-02_compose_stack_fix/task.md) | 22 | fix | medium | Fix compose stack: Detect accidental public binding of the teaching service. |
| [22-03](../gym/tasks/22/22-03_compose_stack_predict/task.md) | 22 | predict | easy | Predict compose stack across the declared cases |
| [22-04](../gym/tasks/22/22-04_compose_stack_trace/task.md) | 22 | trace | medium | Diagnose compose stack from execution evidence |
| [22-05](../gym/tasks/22/22-05_compose_stack_extend/task.md) | 22 | extend | hard | Extend compose stack: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [22-06](../gym/tasks/22/22-06_compose_stack_refactor/task.md) | 22 | refactor | hard | Refactor compose stack: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### 22-B: worker reliability

Features: Stateless workers; shared Postgres checkpoints; per-thread concurrency policy; idempotency; graceful shutdown; recovery.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [22-07](../gym/tasks/22/22-07_worker_reliability_build/task.md) | 22 | build | easy | Build worker reliability: Use the same business effect identity after worker replacement. |
| [22-08](../gym/tasks/22/22-08_worker_reliability_fix/task.md) | 22 | fix | medium | Fix worker reliability: Report that a competing run was excluded. |
| [22-09](../gym/tasks/22/22-09_worker_reliability_predict/task.md) | 22 | predict | easy | Predict worker reliability across the declared cases |
| [22-10](../gym/tasks/22/22-10_worker_reliability_trace/task.md) | 22 | trace | medium | Diagnose worker reliability from execution evidence |
| [22-11](../gym/tasks/22/22-11_worker_reliability_extend/task.md) | 22 | extend | hard | Extend worker reliability: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [22-12](../gym/tasks/22/22-12_worker_reliability_design/task.md) | 22 | design | hard | Design worker reliability and justify the boundary policies |

### 22-C: managed deployment

Features: Agent Server; LangSmith Deployment; assistants, threads, and runs; background runs; scheduled jobs; costs and access requirements.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [22-13](../gym/tasks/22/22-13_managed_deployment_build/task.md) | 22 | build | easy | Build managed deployment: Require both assistant configuration and thread identity. |
| [22-14](../gym/tasks/22/22-14_managed_deployment_fix/task.md) | 22 | fix | medium | Fix managed deployment: Keep interactive waiting distinct from background execution. |
| [22-15](../gym/tasks/22/22-15_managed_deployment_predict/task.md) | 22 | predict | easy | Predict managed deployment across the declared cases |
| [22-16](../gym/tasks/22/22-16_managed_deployment_trace/task.md) | 22 | trace | medium | Diagnose managed deployment from execution evidence |
| [22-17](../gym/tasks/22/22-17_managed_deployment_extend/task.md) | 22 | extend | hard | Extend managed deployment: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [22-18](../gym/tasks/22/22-18_managed_deployment_design/task.md) | 22 | design | hard | Design managed deployment and justify the boundary policies |

## B1 — LangGraph.js

[Lesson](../modules/bonus/B1_langgraph_js/README.md)

### B1-A: typescript state

Features: TypeScript primer; LangGraph.js state schema; nodes and reducers; graph compilation; Python behavior parity.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [B1-01](../gym/tasks/B1/B1-01_typescript_state_build/task.md) | B1 | build | easy | Build typescript state: Trim the input description before testing completeness. |
| [B1-02](../gym/tasks/B1/B1-02_typescript_state_fix/task.md) | B1 | fix | medium | Fix typescript state: Preserve Python's inclusive fast-track boundary. |
| [B1-03](../gym/tasks/B1/B1-03_typescript_state_predict/task.md) | B1 | predict | easy | Predict typescript state across the declared cases |
| [B1-04](../gym/tasks/B1/B1-04_typescript_state_trace/task.md) | B1 | trace | medium | Diagnose typescript state from execution evidence |
| [B1-05](../gym/tasks/B1/B1-05_typescript_state_extend/task.md) | B1 | extend | hard | Extend typescript state: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [B1-06](../gym/tasks/B1/B1-06_typescript_state_refactor/task.md) | B1 | refactor | hard | Refactor typescript state: Extract reusable graph construction into buildGraph; keep invocation, saver lifetime, stream counts, and all old behavior unchanged. |

### B1-B: typescript durable

Features: JavaScript conditional routing and Send; persistence; interrupts; stream formats; language API differences.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [B1-07](../gym/tasks/B1/B1-07_typescript_durable_build/task.md) | B1 | build | easy | Build typescript durable: Review every document before the approval step. |
| [B1-08](../gym/tasks/B1/B1-08_typescript_durable_fix/task.md) | B1 | fix | medium | Fix typescript durable: Accept explicit boolean decisions and reject strings at the interrupt boundary. |
| [B1-09](../gym/tasks/B1/B1-09_typescript_durable_predict/task.md) | B1 | predict | easy | Predict typescript durable across the declared cases |
| [B1-10](../gym/tasks/B1/B1-10_typescript_durable_trace/task.md) | B1 | trace | medium | Diagnose typescript durable from execution evidence |
| [B1-11](../gym/tasks/B1/B1-11_typescript_durable_extend/task.md) | B1 | extend | hard | Extend typescript durable: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [B1-12](../gym/tasks/B1/B1-12_typescript_durable_refactor/task.md) | B1 | refactor | hard | Refactor typescript durable: Extract reusable graph construction into buildGraph; keep invocation, saver lifetime, stream counts, and all old behavior unchanged. |

### B1-C: typescript agents

Features: JavaScript fake chat models; tool calls; manual agent loop; createAgent; cross-language trajectory parity.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [B1-13](../gym/tasks/B1/B1-13_typescript_agents_build/task.md) | B1 | build | easy | Build typescript agents: Return the tool result to the manual agent before ending. |
| [B1-14](../gym/tasks/B1/B1-14_typescript_agents_fix/task.md) | B1 | fix | medium | Fix typescript agents: Respect the configured loop budget in both JavaScript agents. |
| [B1-15](../gym/tasks/B1/B1-15_typescript_agents_predict/task.md) | B1 | predict | easy | Predict typescript agents across the declared cases |
| [B1-16](../gym/tasks/B1/B1-16_typescript_agents_trace/task.md) | B1 | trace | medium | Diagnose typescript agents from execution evidence |
| [B1-17](../gym/tasks/B1/B1-17_typescript_agents_extend/task.md) | B1 | extend | hard | Extend typescript agents: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [B1-18](../gym/tasks/B1/B1-18_typescript_agents_refactor/task.md) | B1 | refactor | hard | Refactor typescript agents: Replace the manual model/tool loop with createAgent, keeping message roles, call IDs, errors, and final text unchanged. |

## B2 — Deep agents on LangGraph

[Lesson](../modules/bonus/B2_deep_agents/README.md)

### B2-A: deep agent planning

Features: create_deep_agent; explicit TodoListMiddleware; planning tools; task progress; current defaults.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [B2-01](../gym/tasks/B2/B2-01_deep_agent_planning_build/task.md) | B2 | build | easy | Build deep agent planning: Install the explicit planning middleware when requested. |
| [B2-02](../gym/tasks/B2/B2-02_deep_agent_planning_fix/task.md) | B2 | fix | medium | Fix deep agent planning: Keep task progress consistent with the supplied status. |
| [B2-03](../gym/tasks/B2/B2-03_deep_agent_planning_predict/task.md) | B2 | predict | easy | Predict deep agent planning across the declared cases |
| [B2-04](../gym/tasks/B2/B2-04_deep_agent_planning_trace/task.md) | B2 | trace | medium | Diagnose deep agent planning from execution evidence |
| [B2-05](../gym/tasks/B2/B2-05_deep_agent_planning_extend/task.md) | B2 | extend | hard | Extend deep agent planning: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [B2-06](../gym/tasks/B2/B2-06_deep_agent_planning_refactor/task.md) | B2 | refactor | hard | Refactor deep agent planning: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### B2-B: virtual filesystem

Features: Virtual filesystem; StateBackend; file tools; bounded paths; persisted artifacts; no host-shell tools.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [B2-07](../gym/tasks/B2/B2-07_virtual_filesystem_build/task.md) | B2 | build | easy | Build virtual filesystem: Allow the explicitly scoped claim artifact path. |
| [B2-08](../gym/tasks/B2/B2-08_virtual_filesystem_fix/task.md) | B2 | fix | medium | Fix virtual filesystem: Deny writes outside the permitted virtual directory. |
| [B2-09](../gym/tasks/B2/B2-09_virtual_filesystem_predict/task.md) | B2 | predict | easy | Predict virtual filesystem across the declared cases |
| [B2-10](../gym/tasks/B2/B2-10_virtual_filesystem_trace/task.md) | B2 | trace | medium | Diagnose virtual filesystem from execution evidence |
| [B2-11](../gym/tasks/B2/B2-11_virtual_filesystem_extend/task.md) | B2 | extend | hard | Extend virtual filesystem: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [B2-12](../gym/tasks/B2/B2-12_virtual_filesystem_refactor/task.md) | B2 | refactor | hard | Refactor virtual filesystem: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### B2-C: deep subagents

Features: Subagent definitions; private context; bounded delegation; explicit tools; checkpoints and approval.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [B2-13](../gym/tasks/B2/B2-13_deep_subagents_build/task.md) | B2 | build | easy | Build deep subagents: Delegate to the explicitly registered specialist. |
| [B2-14](../gym/tasks/B2/B2-14_deep_subagents_fix/task.md) | B2 | fix | medium | Fix deep subagents: Preserve a human rejection of delegation. |
| [B2-15](../gym/tasks/B2/B2-15_deep_subagents_predict/task.md) | B2 | predict | easy | Predict deep subagents across the declared cases |
| [B2-16](../gym/tasks/B2/B2-16_deep_subagents_trace/task.md) | B2 | trace | medium | Diagnose deep subagents from execution evidence |
| [B2-17](../gym/tasks/B2/B2-17_deep_subagents_extend/task.md) | B2 | extend | hard | Extend deep subagents: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [B2-18](../gym/tasks/B2/B2-18_deep_subagents_design/task.md) | B2 | design | hard | Design deep subagents and justify the boundary policies |

## B3 — Build a mini-LangGraph

[Lesson](../modules/bonus/B3_mini_langgraph/README.md)

### B3-A: channels and steps

Features: Educational superstep runner; channel snapshots; pending writes; barrier synchronization; deterministic scheduling.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [B3-01](../gym/tasks/B3/B3-01_channels_and_steps_build/task.md) | B3 | build | easy | Build channels and steps: Merge all sibling findings at the barrier. |
| [B3-02](../gym/tasks/B3/B3-02_channels_and_steps_fix/task.md) | B3 | fix | medium | Fix channels and steps: Report the previous-boundary view seen by each worker. |
| [B3-03](../gym/tasks/B3/B3-03_channels_and_steps_predict/task.md) | B3 | predict | easy | Predict channels and steps across the declared cases |
| [B3-04](../gym/tasks/B3/B3-04_channels_and_steps_trace/task.md) | B3 | trace | medium | Diagnose channels and steps from execution evidence |
| [B3-05](../gym/tasks/B3/B3-05_channels_and_steps_extend/task.md) | B3 | extend | hard | Extend channels and steps: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [B3-06](../gym/tasks/B3/B3-06_channels_and_steps_refactor/task.md) | B3 | refactor | hard | Refactor channels and steps: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### B3-B: mini reducers

Features: Reducer application; overwrite conflict detection; associative merge; parallel result ordering; runtime conformance.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [B3-07](../gym/tasks/B3/B3-07_mini_reducers_build/task.md) | B3 | build | easy | Build mini reducers: Install the mini-runner reducer when parallel accumulation is required. |
| [B3-08](../gym/tasks/B3/B3-08_mini_reducers_fix/task.md) | B3 | fix | medium | Fix mini reducers: Retain the overwrite-conflict case in the real runtime comparison. |
| [B3-09](../gym/tasks/B3/B3-09_mini_reducers_predict/task.md) | B3 | predict | easy | Predict mini reducers across the declared cases |
| [B3-10](../gym/tasks/B3/B3-10_mini_reducers_trace/task.md) | B3 | trace | medium | Diagnose mini reducers from execution evidence |
| [B3-11](../gym/tasks/B3/B3-11_mini_reducers_extend/task.md) | B3 | extend | hard | Extend mini reducers: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [B3-12](../gym/tasks/B3/B3-12_mini_reducers_refactor/task.md) | B3 | refactor | hard | Refactor mini reducers: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### B3-C: mini checkpoints

Features: Checkpoint snapshots; thread identities; resume positions; educational interrupt representation; implementation limits.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [B3-13](../gym/tasks/B3/B3-13_mini_checkpoints_build/task.md) | B3 | build | easy | Build mini checkpoints: Preserve rejection when resuming the waiting teaching thread. |
| [B3-14](../gym/tasks/B3/B3-14_mini_checkpoints_fix/task.md) | B3 | fix | medium | Fix mini checkpoints: Validate the resumed decision before updating approval state. |
| [B3-15](../gym/tasks/B3/B3-15_mini_checkpoints_predict/task.md) | B3 | predict | easy | Predict mini checkpoints across the declared cases |
| [B3-16](../gym/tasks/B3/B3-16_mini_checkpoints_trace/task.md) | B3 | trace | medium | Diagnose mini checkpoints from execution evidence |
| [B3-17](../gym/tasks/B3/B3-17_mini_checkpoints_extend/task.md) | B3 | extend | hard | Extend mini checkpoints: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [B3-18](../gym/tasks/B3/B3-18_mini_checkpoints_design/task.md) | B3 | design | hard | Design mini checkpoints and justify the boundary policies |

## B4 — What's new

[Lesson](../modules/bonus/B4_whats_new/README.md)

### B4-A: event streaming beta

Features: Beta v3 event streaming; typed projections; lifecycle and subgraphs; tool-call deltas; version distinctions.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [B4-01](../gym/tasks/B4/B4-01_event_streaming_beta_build/task.md) | B4 | build | easy | Build event streaming beta: Read child model messages through their subgraph projection. |
| [B4-02](../gym/tasks/B4/B4-02_event_streaming_beta_fix/task.md) | B4 | fix | medium | Fix event streaming beta: Read the final model message from the completed output projection. |
| [B4-03](../gym/tasks/B4/B4-03_event_streaming_beta_predict/task.md) | B4 | predict | easy | Predict event streaming beta across the declared cases |
| [B4-04](../gym/tasks/B4/B4-04_event_streaming_beta_trace/task.md) | B4 | trace | medium | Diagnose event streaming beta from execution evidence |
| [B4-05](../gym/tasks/B4/B4-05_event_streaming_beta_extend/task.md) | B4 | extend | hard | Extend event streaming beta: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [B4-06](../gym/tasks/B4/B4-06_event_streaming_beta_refactor/task.md) | B4 | refactor | hard | Refactor event streaming beta: Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent. |

### B4-B: delta channels beta

Features: Beta DeltaChannel; incremental checkpoint storage; snapshot_frequency; replay reconstruction; schema migration hazards.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [B4-07](../gym/tasks/B4/B4-07_delta_channels_beta_build/task.md) | B4 | build | easy | Build delta channels beta: Retain earlier delta writes when applying a new batch. |
| [B4-08](../gym/tasks/B4/B4-08_delta_channels_beta_fix/task.md) | B4 | fix | medium | Fix delta channels beta: Honor and validate the requested snapshot cadence. |
| [B4-09](../gym/tasks/B4/B4-09_delta_channels_beta_predict/task.md) | B4 | predict | easy | Predict delta channels beta across the declared cases |
| [B4-10](../gym/tasks/B4/B4-10_delta_channels_beta_trace/task.md) | B4 | trace | medium | Diagnose delta channels beta from execution evidence |
| [B4-11](../gym/tasks/B4/B4-11_delta_channels_beta_extend/task.md) | B4 | extend | hard | Extend delta channels beta: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [B4-12](../gym/tasks/B4/B4-12_delta_channels_beta_design/task.md) | B4 | design | hard | Design delta channels beta and justify the boundary policies |

### B4-C: typed approvals

Features: Per-call HumanInTheLoopMiddleware; response_schema; checked resume payloads; tool edit constraints; current changelog literacy.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| [B4-13](../gym/tasks/B4/B4-13_typed_approvals_build/task.md) | B4 | build | easy | Build typed approvals: Use per-call requests when resuming individual interrupt IDs. |
| [B4-14](../gym/tasks/B4/B4-14_typed_approvals_fix/task.md) | B4 | fix | medium | Fix typed approvals: Respect rejection instead of coercing every decision to approval. |
| [B4-15](../gym/tasks/B4/B4-15_typed_approvals_predict/task.md) | B4 | predict | easy | Predict typed approvals across the declared cases |
| [B4-16](../gym/tasks/B4/B4-16_typed_approvals_trace/task.md) | B4 | trace | medium | Diagnose typed approvals from execution evidence |
| [B4-17](../gym/tasks/B4/B4-17_typed_approvals_extend/task.md) | B4 | extend | hard | Extend typed approvals: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. |
| [B4-18](../gym/tasks/B4/B4-18_typed_approvals_design/task.md) | B4 | design | hard | Design typed approvals and justify the boundary policies |
