# Practice Gym — complete planned task catalog

Phase 1 design, checked 2026-11-05 (America/Chicago). These are planned tasks, not implemented or validated exercises.

**486 tasks:** 414 core tasks (18 per module, 00–22) and 72 optional bonus tasks (18 per module, B1–B4). Each module has three feature groups with six tasks each; every group includes easy, medium, and hard work and at least five task types. All seven task types occur across the course.

Every task must assess each feature in its group through an explicit acceptance criterion or graded answer/rubric item. A tag alone is not evidence of coverage. If implementation review finds that a group is too broad to teach or grade clearly, split it and add tasks; never silently reduce the six-task guarantee. The [feature map](FEATURE_MAP.md) is the coverage contract.

Task IDs are stable. The folder name is `<ID>_<feature-group-slug>_<type>`, inside `gym/tasks/<module>/`. The [machine-readable catalog](planning/course_catalog.json) contains every exact path. Main-path recommendations choose one Build and one Fix task per group; the other tasks support prediction, tracing, extension, and independent design.

Code tasks have runnable, deliberately incorrect starters. Predict/Trace use JSON answer files, have no code starter, and compare answers with actual deterministic runs. Design has executable constraints plus a written rubric: passing mechanical checks does not certify design quality. Solutions and rubric examples are complete. Every task gets three hints, an explanation, and the required fixture-backed checks.

## Module 00: Setup and orientation

### 00-A: plain checklist

Features: Plain Python versus stateful orchestration; workflow versus agent; LangGraph, LangChain, and LangSmith roles.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 00-01 | 00 | build | easy | Build a three-step checklist that reads a synthetic claim without needing a model. |
| 00-02 | 00 | fix | medium | Fix a checklist whose missing-data branch silently approves an incomplete claim. |
| 00-03 | 00 | predict | easy | Predict the checklist results for complete, incomplete, and duplicate submissions. |
| 00-04 | 00 | trace | medium | Trace which checklist step dropped the claim identifier. |
| 00-05 | 00 | extend | hard | Extend the checklist to return an explicit reason for every intake decision. |
| 00-06 | 00 | design | hard | Choose the smallest sufficient implementation for six Larkspur requests. |

### 00-B: environment

Features: uv and pip environments; portable script entry points; optional providers; safe configuration.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 00-07 | 00 | build | easy | Build a diagnostic summary of Python, installed packages, and synthetic-data availability. |
| 00-08 | 00 | fix | medium | Fix a setup report that treats an absent optional model key as a Tier 1 failure. |
| 00-09 | 00 | predict | easy | Predict which environment checks are required for deterministic intake versus live extraction. |
| 00-10 | 00 | trace | medium | Trace a failed import to the wrong interpreter without exposing environment secrets. |
| 00-11 | 00 | extend | hard | Extend the setup report with a readable missing-dataset error. |
| 00-12 | 00 | refactor | hard | Refactor a shell-specific setup check into portable Python checks. |

### 00-C: first gym

Features: Gym workflow; pytest assertions; progress and hints; deterministic acceptance criteria.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 00-13 | 00 | build | easy | Build the first passing intake-label function using the guided gym task. |
| 00-14 | 00 | fix | medium | Fix a normalization mismatch revealed by an assertion diff. |
| 00-15 | 00 | predict | easy | Predict which sample attempts pass the first task and why. |
| 00-16 | 00 | trace | medium | Trace an attempt from start through hint, failed check, successful check, and saved progress. |
| 00-17 | 00 | extend | hard | Extend the first task solution to handle leading and trailing whitespace. |
| 00-18 | 00 | design | hard | Write a self-review for a claims checklist with explicit acceptance criteria. |

## Module 01: Your first graph

### 01-A: intake nodes

Features: StateGraph; TypedDict state; nodes as functions; partial node updates.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 01-01 | 01 | build | easy | Build intake nodes that preserve claim IDs while normalizing descriptions and amounts. |
| 01-02 | 01 | fix | medium | Fix a normalizer returning a string instead of a state update. |
| 01-03 | 01 | predict | easy | Predict the state after each normalization node on two incoming claims. |
| 01-04 | 01 | trace | medium | Trace a disappearing field to a full-state reconstruction in a node. |
| 01-05 | 01 | extend | hard | Extend the intake state and nodes with a normalized contact preference. |
| 01-06 | 01 | refactor | hard | Refactor a mutable checklist into independently testable partial-update nodes. |

### 01-B: wire pipeline

Features: add_node; add_edge; START and END; compile; invoke with GraphOutput.value.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 01-07 | 01 | build | easy | Build and invoke the complete normalize, validate, and acknowledge graph. |
| 01-08 | 01 | fix | medium | Fix a missing connection that prevents the acknowledgment node from running. |
| 01-09 | 01 | predict | easy | Predict the final state and execution sequence for the three-step graph. |
| 01-10 | 01 | trace | medium | Trace an unreachable intake node from the edge list and run output. |
| 01-11 | 01 | extend | hard | Extend the pipeline with a receipt-number node before termination. |
| 01-12 | 01 | refactor | hard | Refactor a plain chain of intake functions into the equivalent compiled graph. |

### 01-C: draw and explain

Features: get_graph().draw_mermaid(); graph visualization; sequential supersteps.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 01-13 | 01 | build | easy | Build an intake graph whose generated diagram has the required labeled edges. |
| 01-14 | 01 | fix | medium | Fix misleading node wiring that makes the diagram disagree with the claims specification. |
| 01-15 | 01 | predict | easy | Predict the three supersteps and visible state at each boundary. |
| 01-16 | 01 | trace | medium | Trace a displayed route back to its compiled graph connections. |
| 01-17 | 01 | extend | hard | Extend the diagram and execution contract with a deterministic eligibility check. |
| 01-18 | 01 | design | hard | Annotate an intake diagram with state visibility and termination criteria. |

## Module 02: State and reducers

### 02-A: schema contracts

Features: TypedDict, dataclass, and Pydantic schemas; defaults; input validation; v2 output coercion.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 02-01 | 02 | build | easy | Build equivalent claim schemas with explicit defaults and validated positive amounts. |
| 02-02 | 02 | fix | medium | Fix a Pydantic graph that assumes its v2 result is an untyped dictionary. |
| 02-03 | 02 | predict | easy | Predict missing-field behavior and output types for all three schema styles. |
| 02-04 | 02 | trace | medium | Trace an invalid claim through schema validation and node entry. |
| 02-05 | 02 | extend | hard | Extend each schema with an optional loss date and verify its default behavior. |
| 02-06 | 02 | refactor | hard | Refactor a TypedDict boundary into validated Pydantic input without changing valid results. |

### 02-B: reducer findings

Features: Overwrite channels; Annotated reducers; operator.add; custom reducers; associativity.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 02-07 | 02 | build | easy | Build a reducer that accumulates unique document findings in a stable order. |
| 02-08 | 02 | fix | medium | Fix a validation node that overwrites earlier findings. |
| 02-09 | 02 | predict | easy | Predict successive overwrite, append, and deduplication results for the same claims. |
| 02-10 | 02 | trace | medium | Trace a duplicated finding to a reducer that receives already-accumulated state. |
| 02-11 | 02 | extend | hard | Extend the findings reducer to merge severity without discarding evidence. |
| 02-12 | 02 | refactor | hard | Refactor an order-sensitive reducer into an associative merge with canonical presentation. |

### 02-C: state boundaries

Features: Input and output schemas; private state channels; MessagesState introduction; add_messages introduction.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 02-13 | 02 | build | easy | Build a public intake result that hides internal scoring notes and preserves message updates. |
| 02-14 | 02 | fix | medium | Fix a boundary that leaks private adjuster notes or replaces an existing message incorrectly. |
| 02-15 | 02 | predict | easy | Predict public output fields and ID-based message replacement after two updates. |
| 02-16 | 02 | trace | medium | Trace where private values and message IDs appear inside versus outside the graph. |
| 02-17 | 02 | extend | hard | Extend the intake boundary with a customer-safe explanation message. |
| 02-18 | 02 | refactor | hard | Refactor a single public schema into input, internal, and output contracts. |

## Module 03: Branching and routing

### 03-A: conditional router

Features: Conditional edges; routing functions; path maps; state-based routing.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 03-01 | 03 | build | easy | Build a pure router for claim type, amount, and missing evidence. |
| 03-02 | 03 | fix | medium | Fix a path-map label mismatch that sends theft claims to a nonexistent destination. |
| 03-03 | 03 | predict | easy | Predict routes for claims immediately below, at, and above the fast-track threshold. |
| 03-04 | 03 | trace | medium | Trace a specialist claim incorrectly routed by a truthy string amount. |
| 03-05 | 03 | extend | hard | Extend routing with a jewelry-specialist path while preserving existing decisions. |
| 03-06 | 03 | refactor | hard | Refactor nested routing conditions into a table with equivalent boundary behavior. |

### 03-B: command routes

Features: Command.update; Command.goto; destination annotations; avoiding duplicate routing.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 03-07 | 03 | build | easy | Build a triage node that records its reason and routes with one Command. |
| 03-08 | 03 | fix | medium | Fix a graph that schedules two next nodes through conflicting static and dynamic routing. |
| 03-09 | 03 | predict | easy | Predict updates and destinations produced by three triage Commands. |
| 03-10 | 03 | trace | medium | Trace a duplicate acknowledgment to competing routing mechanisms. |
| 03-11 | 03 | extend | hard | Extend Command routing to include a manual-review explanation for suspicious claims. |
| 03-12 | 03 | refactor | hard | Refactor conditional-edge triage into Command-based triage with equivalent outcomes. |

### 03-C: early exit

Features: Routing to END; total routers; threshold testing; business decisions versus model guesses.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 03-13 | 03 | build | easy | Build early termination for invalid or duplicate incoming claims. |
| 03-14 | 03 | fix | medium | Fix a router with no outcome for a boundary-value claim. |
| 03-15 | 03 | predict | easy | Predict which claims terminate immediately and which reach an adjuster. |
| 03-16 | 03 | trace | medium | Trace a terminated claim using the router decision and final graph state. |
| 03-17 | 03 | extend | hard | Extend early exits with machine-readable rejection reasons. |
| 03-18 | 03 | design | hard | Specify exhaustive routes for five claim categories and unknown input. |

## Module 04: Loops, parallel branches, and map-reduce

### 04-A: bounded rechecks

Features: Loops with exit conditions; recursion_limit; GraphRecursionError.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 04-01 | 04 | build | easy | Build a bounded document-recheck loop with a terminal missing-information outcome. |
| 04-02 | 04 | fix | medium | Fix a loop whose retry state never changes and exhausts the recursion limit. |
| 04-03 | 04 | predict | easy | Predict successful and exhausted paths for two document check histories. |
| 04-04 | 04 | trace | medium | Trace a recursion error to the actual sequence of supersteps. |
| 04-05 | 04 | extend | hard | Extend the recheck loop with an explicit exhausted-budget state. |
| 04-06 | 04 | refactor | hard | Refactor a recursive document validator into an equivalent graph loop. |

### 04-B: fan out fan in

Features: Fan-out and fan-in; parallel supersteps; InvalidUpdateError; Send map-reduce; deferred nodes.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 04-07 | 04 | build | easy | Build document fan-out with Send, a findings reducer, and one final summary. |
| 04-08 | 04 | fix | medium | Fix parallel writes and premature aggregation in a document-review graph. |
| 04-09 | 04 | predict | easy | Predict superstep batches for empty, one-document, and uneven multi-document workloads. |
| 04-10 | 04 | trace | medium | Trace an InvalidUpdateError and early summary from the branches that produced them. |
| 04-11 | 04 | extend | hard | Extend dynamic document workers with a deeper police-report branch and a deferred summary. |
| 04-12 | 04 | refactor | hard | Refactor fixed parallel document branches into equivalent dynamic map-reduce. |

### 04-C: retry and cache

Features: RetryPolicy; node caching; CachePolicy; cache keys and TTL; pure versus side-effecting nodes.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 04-13 | 04 | build | easy | Build cached policy checks with bounded retries for transient lookup failures. |
| 04-14 | 04 | fix | medium | Fix a cache key that reuses one customer's coverage result for another customer. |
| 04-15 | 04 | predict | easy | Predict node executions, retry counts, and cache hits for repeated claims. |
| 04-16 | 04 | trace | medium | Trace stale coverage to a missing policy version in the cache key. |
| 04-17 | 04 | extend | hard | Extend the policy lookup with an injectable clock for deterministic TTL tests. |
| 04-18 | 04 | design | hard | Choose retry and cache rules for read-only checks and payout writes. |

## Module 05: Persistence and threads

### 05-A: thread identity

Features: InMemorySaver; checkpointer compilation; thread_id; config; continuing versus resuming.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 05-01 | 05 | build | easy | Build independent checkpointed conversations for two claim IDs. |
| 05-02 | 05 | fix | medium | Fix a persisted invocation that omits its thread identifier. |
| 05-03 | 05 | predict | easy | Predict which fields survive repeated input on one thread versus a fresh thread. |
| 05-04 | 05 | trace | medium | Trace accidental claim mixing to a reused thread ID. |
| 05-05 | 05 | extend | hard | Extend thread handling with a stable claim-to-thread mapping. |
| 05-06 | 05 | refactor | hard | Refactor an ephemeral claim session into a checkpointed session. |

### 05-B: sqlite lifetime

Features: SqliteSaver; checkpoint resource lifetimes; persistence across processes; SQLite Windows locking.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 05-07 | 05 | build | easy | Build a two-process intake continuation using a temporary SQLite checkpoint file. |
| 05-08 | 05 | fix | medium | Fix a graph that uses its saver after the SQLite context has closed. |
| 05-09 | 05 | predict | easy | Predict what survives a process restart with memory versus SQLite persistence. |
| 05-10 | 05 | trace | medium | Trace a locked checkpoint file to an unclosed connection. |
| 05-11 | 05 | extend | hard | Extend the SQLite workflow to reopen cleanly after a completed session. |
| 05-12 | 05 | refactor | hard | Refactor global database connections into explicit saver lifetimes. |

### 05-C: inspect checkpoints

Features: StateSnapshot; get_state; get_state_history; update_state; durability sync, async, and exit.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 05-13 | 05 | build | easy | Build an audit report of checkpoint values, next nodes, and parent relationships. |
| 05-14 | 05 | fix | medium | Fix a state correction applied to the wrong checkpoint configuration. |
| 05-15 | 05 | predict | easy | Predict snapshots and persistence exposure under each durability mode. |
| 05-16 | 05 | trace | medium | Trace a continuation using checkpoint history without assuming timestamp order is execution order. |
| 05-17 | 05 | extend | hard | Extend the audit report with a corrected-state checkpoint and its lineage. |
| 05-18 | 05 | design | hard | Choose a durability mode for intake drafts and payment approval. |

## Module 06: Human-in-the-loop with interrupts

### 06-A: approve or reject

Features: interrupt(); Command(resume=...); checkpointer requirement; v2 interrupt output.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 06-01 | 06 | build | easy | Build approval and rejection branches for a proposed payout. |
| 06-02 | 06 | fix | medium | Fix an approval graph compiled without the persistence needed to resume. |
| 06-03 | 06 | predict | easy | Predict GraphOutput.value and GraphOutput.interrupts before and after approval. |
| 06-04 | 06 | trace | medium | Trace a rejected claim from its interrupt payload to the final reason. |
| 06-05 | 06 | extend | hard | Extend approval with an adjuster identity validated independently of the model. |
| 06-06 | 06 | refactor | hard | Refactor a synchronous approval callback into a resumable human interrupt. |

### 06-B: collect and edit

Features: Editing through resume; missing-input interrupts; multiple interrupts; ID-based resume mapping.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 06-07 | 06 | build | easy | Build a review flow that collects a missing loss date and an edited approved amount. |
| 06-08 | 06 | fix | medium | Fix multiple pending reviews resumed with the wrong interrupt IDs. |
| 06-09 | 06 | predict | easy | Predict pending prompts after each of two responses. |
| 06-10 | 06 | trace | medium | Trace an out-of-order response to the interrupted claim that should receive it. |
| 06-11 | 06 | extend | hard | Extend a parallel review with independent document and payout approvals. |
| 06-12 | 06 | design | hard | Specify validated approval, rejection, and edit payloads for the adjuster UI. |

### 06-C: safe reentry

Features: Interrupted-node restart semantics; idempotent side effects; deterministic interrupt order; debugging breakpoint distinction.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 06-13 | 06 | build | easy | Build a resumable approval step whose synthetic notification is recorded once. |
| 06-14 | 06 | fix | medium | Fix a notification repeated when its interrupted node restarts. |
| 06-15 | 06 | predict | easy | Predict pre-interrupt execution counts across initial run and resumption. |
| 06-16 | 06 | trace | medium | Trace duplicate notifications to work placed before the interrupt. |
| 06-17 | 06 | extend | hard | Extend approval with a stable idempotency key and a failed-write retry case. |
| 06-18 | 06 | refactor | hard | Refactor side effects into separately checkpointed work after validated approval. |

## Module 07: Time travel, debugging, and streaming basics

### 07-A: replay and fork

Features: Historical checkpoint replay; checkpoint_id; update_state forks; as_node; renewed interrupts.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 07-01 | 07 | build | easy | Build an audit replay and a corrected fork of a disputed water-damage claim. |
| 07-02 | 07 | fix | medium | Fix a correction that continues the original latest thread instead of the historical fork. |
| 07-03 | 07 | predict | easy | Predict which nodes rerun and which approval is requested again. |
| 07-04 | 07 | trace | medium | Trace original and forked checkpoint parentage. |
| 07-05 | 07 | extend | hard | Extend the audit result with separate original and corrected decision histories. |
| 07-06 | 07 | refactor | hard | Refactor a manual rerun into checkpoint-based replay with equivalent business evidence. |

### 07-B: v2 stream parts

Features: values, updates, debug, and custom stream modes; get_stream_writer; v2 StreamPart envelope.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 07-07 | 07 | build | easy | Build a stream printer that separates whole states, node updates, and document progress. |
| 07-08 | 07 | fix | medium | Fix a v2 stream consumer that unpacks events as positional tuples. |
| 07-09 | 07 | predict | easy | Predict stream-part types and payloads for a deterministic intake run. |
| 07-10 | 07 | trace | medium | Trace a stalled intake step from update and debug evidence. |
| 07-11 | 07 | extend | hard | Extend the stream consumer to preserve interrupt metadata in values events. |
| 07-12 | 07 | refactor | hard | Refactor separate mode-specific printers into one typed envelope dispatcher. |

### 07-C: namespaces and errors

Features: Subgraph namespace preview; parallel event ordering; error reading; stream versus checkpoint history.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 07-13 | 07 | build | easy | Build a trace report that groups events by namespace and superstep. |
| 07-14 | 07 | fix | medium | Fix a trace checker that assumes concurrent nodes finish in one fixed order. |
| 07-15 | 07 | predict | easy | Predict all valid sibling event orders for parallel claim checks. |
| 07-16 | 07 | trace | medium | Trace a missing field from its error back to the responsible node and checkpoint. |
| 07-17 | 07 | extend | hard | Extend the trace report with a concise diagnosis for three common graph failures. |
| 07-18 | 07 | design | hard | Specify an audit view that distinguishes updates, snapshots, and nested runs. |

## Module 08: LLMs inside nodes

### 08-A: model boundary

Features: LLM and prompt basics; init_chat_model; common model factory; provider configuration; structured output validation.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 08-01 | 08 | build | easy | Build a claim extractor that obtains its scripted structured response through the shared factory. |
| 08-02 | 08 | fix | medium | Fix unvalidated model output that accepts a negative claimed amount. |
| 08-03 | 08 | predict | easy | Predict extraction results and validation failures for three scripted responses. |
| 08-04 | 08 | trace | medium | Trace a misclassified claim through prompt, response, parsed fields, and deterministic routing. |
| 08-05 | 08 | extend | hard | Extend extraction with an explicit unknown value for missing loss dates. |
| 08-06 | 08 | refactor | hard | Refactor provider-specific extraction into the common model boundary. |

### 08-B: message identity

Features: MessagesState; add_messages; message IDs; RemoveMessage; human, AI, and tool messages.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 08-07 | 08 | build | easy | Build a claim conversation that edits a message by ID and removes an obsolete note. |
| 08-08 | 08 | fix | medium | Fix duplicate messages caused by regenerating IDs for an edited customer statement. |
| 08-09 | 08 | predict | easy | Predict message history after append, replacement, and removal operations. |
| 08-10 | 08 | trace | medium | Trace an incorrect extraction to an outdated message left in state. |
| 08-11 | 08 | extend | hard | Extend the conversation with a stable correction trail separate from model context. |
| 08-12 | 08 | refactor | hard | Refactor raw string history into typed messages with stable identities. |

### 08-C: tokens and fakes

Features: messages stream mode; token chunks and metadata; scripted fake chat models; structured-output and streaming fake contracts.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 08-13 | 08 | build | easy | Build an offline extraction stream with deterministic chunks and node metadata. |
| 08-14 | 08 | fix | medium | Fix a fake model whose stream and invoke results disagree. |
| 08-15 | 08 | predict | easy | Predict token events and final structured extraction from a scripted response. |
| 08-16 | 08 | trace | medium | Trace tokens back to the extraction node using stream metadata. |
| 08-17 | 08 | extend | hard | Extend the fake with malformed structured output to test the validation branch. |
| 08-18 | 08 | refactor | hard | Refactor direct fake construction in examples into the shared model factory. |

## Module 09: Tools and the agent loop

### 09-A: tools and messages

Features: Tool definitions and schemas; tool calls; ToolMessage IDs; tool errors; deterministic policy lookup.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 09-01 | 09 | build | easy | Build lookup_policy and check_coverage tools over committed synthetic records. |
| 09-02 | 09 | fix | medium | Fix a tool response whose call ID does not match the model's request. |
| 09-03 | 09 | predict | easy | Predict tool arguments, outputs, and error messages for a scripted policy lookup. |
| 09-04 | 09 | trace | medium | Trace a failed coverage answer to a malformed tool argument. |
| 09-05 | 09 | extend | hard | Extend the tool set with get_claim_history and calculate_payout. |
| 09-06 | 09 | refactor | hard | Refactor exception-prone tools into validated tools with safe business-error results. |

### 09-B: manual react

Features: Manual ReAct graph; model node; ToolNode; tools_condition; bounded agent loop.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 09-07 | 09 | build | easy | Build the model-tools loop by hand and stop when the model returns a final answer. |
| 09-08 | 09 | fix | medium | Fix an agent that loops into tools when the model made no tool calls. |
| 09-09 | 09 | predict | easy | Predict the exact scripted policy-lookup and payout trajectory. |
| 09-10 | 09 | trace | medium | Trace a repeated tool call to the wrong conditional route. |
| 09-11 | 09 | extend | hard | Extend the custom agent with an explicit tool-call budget. |
| 09-12 | 09 | refactor | hard | Refactor an unbounded agent loop into a graph with checked termination. |

### 09-C: tool runtime

Features: ToolRuntime; Runtime context; state and Store access; tool Command updates; trusted tool-call identity.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 09-13 | 09 | build | easy | Build a tool that reads trusted customer context and updates claim status with a Command. |
| 09-14 | 09 | fix | medium | Fix a tool that trusts a model-supplied customer ID instead of runtime context. |
| 09-15 | 09 | predict | easy | Predict state updates and tool-result messages from a Command-returning tool. |
| 09-16 | 09 | trace | medium | Trace a missing status update through ToolNode and the returned Command. |
| 09-17 | 09 | extend | hard | Extend tool execution with a scoped read-only claims repository. |
| 09-18 | 09 | design | hard | Define allowed tool capabilities and context boundaries for a claims adjuster. |

## Module 10: Prebuilt agents and when to drop down a level

### 10-A: create agent

Features: langchain.agents.create_agent; agent state; model and tools wiring; prebuilt versus custom graph.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 10-01 | 10 | build | easy | Build the policy helper with create_agent and the same scripted tools as module 09. |
| 10-02 | 10 | fix | medium | Fix a prebuilt agent whose fake model cannot bind its tools. |
| 10-03 | 10 | predict | easy | Predict equivalence between hand-wired and prebuilt agent tool trajectories. |
| 10-04 | 10 | trace | medium | Trace a behavior difference to model setup rather than graph orchestration. |
| 10-05 | 10 | extend | hard | Extend the prebuilt agent with a new read-only policy tool. |
| 10-06 | 10 | refactor | hard | Refactor the hand-wired claims agent into create_agent without changing outcomes. |

### 10-B: middleware

Features: Middleware lifecycle; before/after hooks; wrap_model_call; tool/model budgets; middleware state.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 10-07 | 10 | build | easy | Build middleware that caps model calls and records a safe reason for stopping. |
| 10-08 | 10 | fix | medium | Fix middleware that invokes its model handler twice. |
| 10-09 | 10 | predict | easy | Predict middleware hook order across a two-tool claim investigation. |
| 10-10 | 10 | trace | medium | Trace unexpected model usage to a middleware retry branch. |
| 10-11 | 10 | extend | hard | Extend middleware with deterministic validation of a final claim explanation. |
| 10-12 | 10 | design | hard | Select middleware responsibilities versus graph responsibilities for payout safety. |

### 10-C: agent composition

Features: Agent as a graph node; shared-state agent subgraph preview; agent input/output boundaries; behavior-preserving refactoring.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 10-13 | 10 | build | easy | Build a workflow that calls the policy agent between intake and approval. |
| 10-14 | 10 | fix | medium | Fix an adapter that overwrites claim data with the agent's message-only result. |
| 10-15 | 10 | predict | easy | Predict outer workflow state and agent messages at each handoff. |
| 10-16 | 10 | trace | medium | Trace private agent notes leaking through the workflow output. |
| 10-17 | 10 | extend | hard | Extend the wrapper with deterministic checks on the agent's recommendation. |
| 10-18 | 10 | refactor | hard | Refactor an all-agent workflow into fixed intake and approval around an agent step. |

## Module 11: Memory

### 11-A: short term memory

Features: Thread checkpoints as short-term memory; context windows; trim_messages; summarization nodes.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 11-01 | 11 | build | easy | Build a conversation manager that preserves required messages while trimming old exchanges. |
| 11-02 | 11 | fix | medium | Fix trimming that leaves a tool result without its preceding tool call. |
| 11-03 | 11 | predict | easy | Predict retained messages and summary contents for a scripted claim history. |
| 11-04 | 11 | trace | medium | Trace a forgotten policy limit to an overaggressive summary. |
| 11-05 | 11 | extend | hard | Extend memory with a deterministic summary threshold. |
| 11-06 | 11 | refactor | hard | Refactor a growing message list into summary plus recent messages. |

### 11-B: store namespaces

Features: InMemoryStore; namespaces; put, get, search, and delete; runtime.store; semantic, episodic, and procedural memory.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 11-07 | 11 | build | easy | Build customer-scoped storage for contact preferences and prior-claim facts. |
| 11-08 | 11 | fix | medium | Fix a namespace collision that mixes two customers' preferences. |
| 11-09 | 11 | predict | easy | Predict stored items after updates, searches, and deletion. |
| 11-10 | 11 | trace | medium | Trace a wrong contact channel to incorrect Store scope. |
| 11-11 | 11 | extend | hard | Extend memory with separate facts, past episodes, and operating procedures. |
| 11-12 | 11 | refactor | hard | Refactor global preference dictionaries into runtime-injected Store operations. |

### 11-C: semantic and privacy

Features: Embeddings basics; semantic Store index; deterministic fake embeddings; memory deletion; checkpoint versus Store retention.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 11-13 | 11 | build | easy | Build semantic search over synthetic customer memories using fixed fake embeddings. |
| 11-14 | 11 | fix | medium | Fix search results leaked across customer namespaces. |
| 11-15 | 11 | predict | easy | Predict similarity ranking and remaining memories after a deletion request. |
| 11-16 | 11 | trace | medium | Trace a deleted preference that still exists in historical checkpoints. |
| 11-17 | 11 | extend | hard | Extend deletion handling with explicit Store and checkpoint retention reports. |
| 11-18 | 11 | design | hard | Specify a privacy-aware memory lifecycle without promising instantaneous erasure everywhere. |

## Module 12: Workflow patterns with LLMs

### 12-A: chains and gates

Features: Prompt chaining; deterministic gates; model-based routing with validated outputs; workflow versus agent choice.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 12-01 | 12 | build | easy | Build extract, validate, and draft stages with a deterministic gate between them. |
| 12-02 | 12 | fix | medium | Fix a router that accepts arbitrary model text as a graph destination. |
| 12-03 | 12 | predict | easy | Predict which claim letters are drafted or blocked by the gate. |
| 12-04 | 12 | trace | medium | Trace a false coverage statement to an unchecked upstream extraction. |
| 12-05 | 12 | extend | hard | Extend the chain with a customer-language choice constrained to supported values. |
| 12-06 | 12 | design | hard | Choose fixed workflows or agents for six claims-communication tasks. |

### 12-B: orchestrator workers

Features: Parallel LLM branches; orchestrator-worker pattern; Send with structured worker plans; result aggregation.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 12-07 | 12 | build | easy | Build a letter planner that sends policy, evidence, and tone sections to scripted workers. |
| 12-08 | 12 | fix | medium | Fix a worker reducer that loses one parallel section. |
| 12-09 | 12 | predict | easy | Predict the planned workers and canonical merged letter sections. |
| 12-10 | 12 | trace | medium | Trace an unsupported worker assignment back to the plan schema. |
| 12-11 | 12 | extend | hard | Extend the planner with a bounded number of optional evidence sections. |
| 12-12 | 12 | refactor | hard | Refactor fixed letter sections into structured dynamic worker dispatch. |

### 12-C: evaluator optimizer

Features: Evaluator-optimizer loop; factual and tone criteria; iteration budgets; termination on success or exhaustion.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 12-13 | 12 | build | easy | Build a bounded letter revision loop using scripted evaluator feedback. |
| 12-14 | 12 | fix | medium | Fix a loop that keeps rewriting after all acceptance criteria pass. |
| 12-15 | 12 | predict | easy | Predict drafts, feedback, and termination for a two-revision scenario. |
| 12-16 | 12 | trace | medium | Trace a misleading final letter to an evaluator that checked tone but ignored policy facts. |
| 12-17 | 12 | extend | hard | Extend the evaluator with explicit citation and deductible checks. |
| 12-18 | 12 | refactor | hard | Refactor an open-ended revision agent into a bounded workflow. |

## Module 13: Subgraphs

### 13-A: shared subgraph

Features: Compiled subgraph as node; shared state keys; parent reducers; reuse across workflows.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 13-01 | 13 | build | easy | Build a fraud subgraph shared by claims intake and new-policy review. |
| 13-02 | 13 | fix | medium | Fix a parent reducer that duplicates findings returned by a child graph. |
| 13-03 | 13 | predict | easy | Predict parent and child state at shared-channel boundaries. |
| 13-04 | 13 | trace | medium | Trace a missing fraud flag to a mismatched shared key. |
| 13-05 | 13 | extend | hard | Extend both workflows with one additional fraud check in the shared subgraph. |
| 13-06 | 13 | refactor | hard | Refactor duplicated fraud nodes into one reusable compiled subgraph. |

### 13-B: schema adapters

Features: Calling a subgraph inside a node; input/output schema conversion; private child state; context boundaries.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 13-07 | 13 | build | easy | Build an adapter from claim intake fields to an independently named fraud schema. |
| 13-08 | 13 | fix | medium | Fix an adapter that drops the child's risk explanation. |
| 13-09 | 13 | predict | easy | Predict which fields are visible to the parent, child, and caller. |
| 13-10 | 13 | trace | medium | Trace private fraud notes leaking through the adapter. |
| 13-11 | 13 | extend | hard | Extend the adapter to support a new-policy input without changing the child schema. |
| 13-12 | 13 | refactor | hard | Refactor a tightly coupled child graph into an explicitly adapted component. |

### 13-C: subgraph persistence

Features: Inherited checkpointers; per-invocation versus persistent subgraphs; nested interrupts; get_state subgraphs; stream namespaces.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 13-13 | 13 | build | easy | Build a nested fraud review that pauses and resumes through the parent workflow. |
| 13-14 | 13 | fix | medium | Fix a nested review whose persisted state is unintentionally shared between calls. |
| 13-15 | 13 | predict | easy | Predict parent and nested interrupt state before and after resumption. |
| 13-16 | 13 | trace | medium | Trace one nested event using its full namespace and checkpoint path. |
| 13-17 | 13 | extend | hard | Extend nested review with inspection of pending child state. |
| 13-18 | 13 | design | hard | Choose per-invocation or persistent subgraph state for three fraud-review scenarios. |

## Module 14: Multi-agent systems

### 14-A: supervisor tools

Features: Supervisor pattern; agents as tools; private histories; context engineering; direct patterns versus helper packages.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 14-01 | 14 | build | easy | Build a supervisor that asks policy and fraud specialists through scoped tools. |
| 14-02 | 14 | fix | medium | Fix a supervisor that forwards unrelated customer history to every specialist. |
| 14-03 | 14 | predict | easy | Predict specialist calls and final recommendations from a scripted supervisor. |
| 14-04 | 14 | trace | medium | Trace conflicting recommendations to missing role-specific context. |
| 14-05 | 14 | extend | hard | Extend the team with a customer-communication specialist. |
| 14-06 | 14 | refactor | hard | Refactor a helper-style supervisor into directly composed agents and tools. |

### 14-B: handoffs

Features: Command.PARENT; handoffs; shared message history; parent reducers; tool-call pairing at handoff.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 14-07 | 14 | build | easy | Build an intake-to-policy handoff that updates shared claim state. |
| 14-08 | 14 | fix | medium | Fix a handoff that targets a parent node from the wrong graph level. |
| 14-09 | 14 | predict | easy | Predict active agents and message histories after two handoffs. |
| 14-10 | 14 | trace | medium | Trace an orphaned tool call across the parent-child handoff. |
| 14-11 | 14 | extend | hard | Extend the team with a fraud-to-adjuster escalation path. |
| 14-12 | 14 | refactor | hard | Refactor a shared-history team to isolate specialist notes behind explicit handoff payloads. |

### 14-C: team tradeoffs

Features: Swarm-style routing; active-agent state; bounded delegation; single versus multi-agent evaluation.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 14-13 | 14 | build | easy | Build a bounded peer-handoff team with one explicit active specialist. |
| 14-14 | 14 | fix | medium | Fix a policy-fraud handoff cycle that never reaches a decision. |
| 14-15 | 14 | predict | easy | Predict delegation counts and termination for three scripted investigations. |
| 14-16 | 14 | trace | medium | Trace repeated model work caused by overlapping specialist responsibilities. |
| 14-17 | 14 | extend | hard | Extend the team with a deterministic fallback when its delegation budget is exhausted. |
| 14-18 | 14 | design | hard | Compare one-agent and multi-agent designs using accuracy, latency, and cost budgets. |

## Module 15: The Functional API

### 15-A: entrypoints tasks

Features: entrypoint; task; single-input contract; task futures; result(); normal Python control flow.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 15-01 | 15 | build | easy | Build functional intake from decorated normalization and validation tasks. |
| 15-02 | 15 | fix | medium | Fix an entrypoint that returns unresolved task futures as claim fields. |
| 15-03 | 15 | predict | easy | Predict task outputs and final workflow value for two claims. |
| 15-04 | 15 | trace | medium | Trace a lost value to an incorrectly resolved task result. |
| 15-05 | 15 | extend | hard | Extend functional intake with a conditional specialist lookup. |
| 15-06 | 15 | refactor | hard | Refactor the Graph API intake pipeline into behaviorally equivalent Functional API code. |

### 15-B: parallel futures

Features: Starting tasks before resolving futures; parallel Functional API tasks; deterministic aggregation; graph versus functional comparison.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 15-07 | 15 | build | easy | Build functional document checks that start all tasks before collecting results. |
| 15-08 | 15 | fix | medium | Fix code that accidentally serializes independent tasks by resolving each immediately. |
| 15-09 | 15 | predict | easy | Predict task-start groups and allowed completion orders. |
| 15-10 | 15 | trace | medium | Trace a timing diagram to distinguish concurrent task submission from sequential work. |
| 15-11 | 15 | extend | hard | Extend functional checks with stable result ordering by document ID. |
| 15-12 | 15 | refactor | hard | Refactor a Send-based graph into an equivalent functional worker fan-out. |

### 15-C: functional resume

Features: Functional persistence; interrupts; saved task results; entrypoint replay; deterministic task ordering.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 15-13 | 15 | build | easy | Build a persistent functional intake that waits for missing documents. |
| 15-14 | 15 | fix | medium | Fix a resumed workflow whose task order depends on an unsaved random value. |
| 15-15 | 15 | predict | easy | Predict cached task reuse and repeated entrypoint code after resumption. |
| 15-16 | 15 | trace | medium | Trace a repeated synthetic side effect to work outside a task. |
| 15-17 | 15 | extend | hard | Extend functional intake with a validated edited document reference on resume. |
| 15-18 | 15 | design | hard | Choose Graph or Functional API for three long-running claims processes. |

## Module 16: External systems and MCP

### 16-A: api boundaries

Features: Async and await primer; HTTP timeouts; transient retries; idempotency keys; injectable transports.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 16-01 | 16 | build | easy | Build a claims-service client over an in-process fake transport. |
| 16-02 | 16 | fix | medium | Fix a retry that creates duplicate synthetic payment requests. |
| 16-03 | 16 | predict | easy | Predict request attempts and stored responses for a timeout followed by success. |
| 16-04 | 16 | trace | medium | Trace an exhausted retry to the correct user-facing business outcome. |
| 16-05 | 16 | extend | hard | Extend the client with per-request timeouts and a stable idempotency key. |
| 16-06 | 16 | refactor | hard | Refactor direct network calls into an injected, offline-testable transport. |

### 16-B: mcp server

Features: Official MCP SDK; local stdio server; tool schemas; server lifecycle; synthetic claims data permissions.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 16-07 | 16 | build | easy | Build a local stdio server exposing read-only claim and policy lookups. |
| 16-08 | 16 | fix | medium | Fix a server that prints diagnostic text into its JSON-RPC protocol stream. |
| 16-09 | 16 | predict | easy | Predict tool discovery and call responses for a synthetic claim. |
| 16-10 | 16 | trace | medium | Trace a malformed tool response to a server schema mismatch. |
| 16-11 | 16 | extend | hard | Extend the local server with a scoped document-summary tool. |
| 16-12 | 16 | refactor | hard | Refactor direct repository access into an MCP server with the same read-only behavior. |

### 16-C: mcp adapter

Features: langchain-mcp-adapters; MultiServerMCPClient; loading tools; async client lifetime; adapter-SDK compatibility; Beta successor awareness.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 16-13 | 16 | build | easy | Build a fake-model agent that loads and calls tools from the local stdio server. |
| 16-14 | 16 | fix | medium | Fix an agent that uses a stateful MCP session after it has closed. |
| 16-15 | 16 | predict | easy | Predict discovery, tool calls, and final claim state across the adapter boundary. |
| 16-16 | 16 | trace | medium | Trace an adapter installation failure to incompatible MCP major versions. |
| 16-17 | 16 | extend | hard | Extend adapter configuration with allowlisted server commands and tool names. |
| 16-18 | 16 | design | hard | Plan migration to the Beta integrated adapter without mixing incompatible dependency sets. |

## Module 17: Durable execution and long-running workflows

### 17-A: durable side effects

Features: Durability modes in failures; task-wrapped side effects; checkpointed nondeterminism; idempotency; crash windows.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 17-01 | 17 | build | easy | Build a synthetic payment ledger that survives replay without duplicate payments. |
| 17-02 | 17 | fix | medium | Fix a task-wrapped side effect that still duplicates during the commit-before-checkpoint crash window. |
| 17-03 | 17 | predict | easy | Predict ledger rows and persisted state for injected failures at three boundaries. |
| 17-04 | 17 | trace | medium | Trace a replay to distinguish a cached result from an idempotent external retry. |
| 17-05 | 17 | extend | hard | Extend the workflow with a subprocess crash-and-resume acceptance test. |
| 17-06 | 17 | refactor | hard | Refactor nondeterministic timestamps and side effects into persisted task boundaries. |

### 17-B: recovery policies

Features: RetryPolicy after transient failures; async node timeouts; TimeoutPolicy; NodeError and error_handler; compensation; RunControl graceful drain.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 17-07 | 17 | build | easy | Build async estimate retrieval with a timeout, bounded retries, and a recovery route. |
| 17-08 | 17 | fix | medium | Fix retry handling that retries a permanent validation failure or loses compensating state. |
| 17-09 | 17 | predict | easy | Predict attempts, handler execution, and saved state under timeout and graceful drain. |
| 17-10 | 17 | trace | medium | Trace an interrupted shutdown to the checkpoint from which work can safely resume. |
| 17-11 | 17 | extend | hard | Extend recovery with a synthetic compensation action for a reserved payout. |
| 17-12 | 17 | design | hard | Specify retry, timeout, compensation, and graceful-shutdown rules for a claims worker. |

### 17-C: long wait postgres

Features: Durable interrupt waits; simulated time; PostgresSaver and AsyncPostgresSaver; setup lifecycle; shared database persistence.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 17-13 | 17 | build | easy | Build a missing-estimate wait resumed with a clock advanced by three days. |
| 17-14 | 17 | fix | medium | Fix a restart that resumes a fresh thread instead of the waiting claim. |
| 17-15 | 17 | predict | easy | Predict pending and completed states across the simulated three-day gap. |
| 17-16 | 17 | trace | medium | Trace a Postgres setup failure using a fake saver contract and recorded diagnostics. |
| 17-17 | 17 | extend | hard | Extend saver configuration with an optional Docker-backed Postgres integration path. |
| 17-18 | 17 | refactor | hard | Refactor the same waiting workflow from SQLite to an injected Postgres saver factory. |

## Module 18: Streaming to user interfaces

### 18-A: async streams

Features: ainvoke; astream; async context propagation; all seven stream modes; v2 serialization; cancellation.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 18-01 | 18 | build | easy | Build an async claim runner exposing values, updates, messages, custom, checkpoints, tasks, and debug. |
| 18-02 | 18 | fix | medium | Fix an async consumer that blocks the event loop or discards interrupt metadata. |
| 18-03 | 18 | predict | easy | Predict normalized async stream events and final output for a scripted claim. |
| 18-04 | 18 | trace | medium | Trace a missing token stream to its node filter or callback context. |
| 18-05 | 18 | extend | hard | Extend the runner with cancellation that closes resources and preserves resumable state. |
| 18-06 | 18 | refactor | hard | Refactor a synchronous stream consumer into its async equivalent. |

### 18-B: sse api

Features: FastAPI streaming responses; server-sent event framing; JSON-safe serialization; reconnect semantics; authenticated thread ownership.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 18-07 | 18 | build | easy | Build an SSE response generator for safe claim-progress events. |
| 18-08 | 18 | fix | medium | Fix event framing that joins two updates into one unreadable SSE message. |
| 18-09 | 18 | predict | easy | Predict event names and JSON payloads for progress, interrupt, error, and completion. |
| 18-10 | 18 | trace | medium | Trace a disconnected client without starting an unintended second claim run. |
| 18-11 | 18 | extend | hard | Extend the API with a resume endpoint that validates ownership and interrupt IDs. |
| 18-12 | 18 | refactor | hard | Refactor transport-specific graph output into a reusable SSE serialization boundary. |

### 18-C: adjuster dashboard

Features: Streamlit state; progress and token rendering; approve/reject controls; stale interrupt detection; Beta v3 stream projections.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 18-13 | 18 | build | easy | Build dashboard state transitions for loading, streaming, awaiting review, and completion. |
| 18-14 | 18 | fix | medium | Fix an approval button that submits twice after a Streamlit rerun. |
| 18-15 | 18 | predict | easy | Predict the visible dashboard state after each stored stream event. |
| 18-16 | 18 | trace | medium | Trace a stale approval response to an already-resumed interrupt. |
| 18-17 | 18 | extend | hard | Extend the dashboard adapter with an optional Beta v3 projection source and equivalent UI results. |
| 18-18 | 18 | design | hard | Specify a clear approval screen with amount, evidence, decision, and error recovery. |

## Module 19: Testing and evaluation

### 19-A: test graph behavior

Features: pytest primer in depth; node unit tests; graph tests; fake models; routing and final-state assertions.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 19-01 | 19 | build | easy | Build meaningful tests for intake nodes, routing boundaries, and final claim decisions. |
| 19-02 | 19 | fix | medium | Fix a test that passes even when the learner's graph is never imported. |
| 19-03 | 19 | predict | easy | Predict which deliberately mutated claims implementations the test suite rejects. |
| 19-04 | 19 | trace | medium | Trace a failing graph test to its smallest incorrect node behavior. |
| 19-05 | 19 | extend | hard | Extend tests with missing data, duplicate claims, and tool errors. |
| 19-06 | 19 | refactor | hard | Refactor brittle implementation assertions into observable behavior tests. |

### 19-B: test durable execution

Features: Interrupt/resume tests; checkpoint assertions; superstep-aware snapshots; reducer properties; subprocess isolation.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 19-07 | 19 | build | easy | Build tests proving approval is required and state survives resumption. |
| 19-08 | 19 | fix | medium | Fix a snapshot that assumes a fixed completion order for parallel checks. |
| 19-09 | 19 | predict | easy | Predict which checkpoint and idempotency assertions fail after a supplied mutation. |
| 19-10 | 19 | trace | medium | Trace a flaky test to shared checkpointer or fake-model state. |
| 19-11 | 19 | extend | hard | Extend coverage with reducer associativity and isolated crash recovery cases. |
| 19-12 | 19 | refactor | hard | Refactor sleep-based tests into event-driven deterministic tests. |

### 19-C: trajectory evals

Features: Local evaluation harness; golden JSONL cases; trajectory matching; agentevals; optional LangSmith evaluation.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 19-13 | 19 | build | easy | Build a local evaluation report for expected routes, decisions, and tool-call sequences. |
| 19-14 | 19 | fix | medium | Fix a trajectory matcher that treats wrong tool arguments as correct. |
| 19-15 | 19 | predict | easy | Predict exact, subset, and unordered trajectory scores on supplied investigations. |
| 19-16 | 19 | trace | medium | Trace a score regression to a changed claim scenario and mismatched tool call. |
| 19-17 | 19 | extend | hard | Extend evaluation with an explicit quality threshold that produces a failing exit code. |
| 19-18 | 19 | design | hard | Define a claims evaluation set with failure categories and no model judge requirement. |

## Module 20: Observability and visual debugging

### 20-A: local visual debugging

Features: langgraph.json; langgraph dev; graph export; Studio; local/offline alternative; static debugging breakpoints.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 20-01 | 20 | build | easy | Build a valid graph-export configuration and an offline checkpoint walkthrough. |
| 20-02 | 20 | fix | medium | Fix a graph import path that prevents the local server from loading. |
| 20-03 | 20 | predict | easy | Predict nodes and pending state shown while stepping a supplied claim. |
| 20-04 | 20 | trace | medium | Trace a misroute using recorded Studio-shaped state and checkpoint evidence. |
| 20-05 | 20 | extend | hard | Extend the export contract with safe environment-variable references. |
| 20-06 | 20 | refactor | hard | Refactor an import-time graph run into a server-loadable graph factory. |

### 20-B: structured logs

Features: Structured logging; correlation IDs; thread and run identifiers; redaction; observability without accounts.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 20-07 | 20 | build | easy | Build structured audit events that correlate one claim without logging secrets. |
| 20-08 | 20 | fix | medium | Fix a logger that serializes full customer messages and environment variables. |
| 20-09 | 20 | predict | easy | Predict allowed log fields for intake, tool, interrupt, and resume events. |
| 20-10 | 20 | trace | medium | Trace a stalled claim by joining events using stable identifiers. |
| 20-11 | 20 | extend | hard | Extend logging with duration and outcome fields while preserving redaction. |
| 20-12 | 20 | refactor | hard | Refactor print-based debugging into an injectable structured event sink. |

### 20-C: optional tracing

Features: Optional LangSmith tracing; account requirements; local trace replay; trace metadata; time-travel debugging.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 20-13 | 20 | build | easy | Build tracing configuration that leaves all offline exercises independent of an account. |
| 20-14 | 20 | fix | medium | Fix a test environment that accidentally enables remote tracing. |
| 20-15 | 20 | predict | easy | Predict which local events remain available with tracing disabled. |
| 20-16 | 20 | trace | medium | Trace a wrong routing decision and reproduce it from saved checkpoints. |
| 20-17 | 20 | extend | hard | Extend trace metadata with a safe course-version identifier. |
| 20-18 | 20 | design | hard | Define a debugging procedure that works locally and optionally uses Studio. |

## Module 21: Security and guardrails

### 21-A: untrusted input

Features: Prompt injection; deterministic authorization; validated structured output; allowlisted routes; least-privilege tools.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 21-01 | 21 | build | easy | Build a claim boundary that treats injected description text as untrusted evidence. |
| 21-02 | 21 | fix | medium | Fix a payout route that treats a model-generated approval statement as authorization. |
| 21-03 | 21 | predict | easy | Predict outcomes for clean, malformed, and prompt-injected claim descriptions. |
| 21-04 | 21 | trace | medium | Trace an attempted policy lookup outside the current customer's scope. |
| 21-05 | 21 | extend | hard | Extend validation with explicit allowed claim types and amount limits. |
| 21-06 | 21 | refactor | hard | Refactor a prompt-only defense into deterministic validation and scoped tools. |

### 21-B: approval and limits

Features: Approval before side effects; authorization outside the model; recursion and tool-call budgets; token/cost budgets; audit events.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 21-07 | 21 | build | easy | Build an approved-write gate around a synthetic payment tool. |
| 21-08 | 21 | fix | medium | Fix a tool that can execute a payment before the approval decision is checked. |
| 21-09 | 21 | predict | easy | Predict allowed writes and stop reasons when budgets or approvals fail. |
| 21-10 | 21 | trace | medium | Trace an unauthorized side effect through the checkpoint and ledger records. |
| 21-11 | 21 | extend | hard | Extend budget handling with conservative cost accounting and a safe stop result. |
| 21-12 | 21 | design | hard | Define a threat model and enforceable controls for the claims copilot. |

### 21-C: private checkpoints

Features: PII minimization; EncryptedSerializer; encryption key handling; retention and deletion; audit-trail limitations.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 21-13 | 21 | build | easy | Build encrypted local checkpoints using an injected test key and synthetic customer fields. |
| 21-14 | 21 | fix | medium | Fix logs that reveal an encryption key or decrypted checkpoint payload. |
| 21-15 | 21 | predict | easy | Predict which data remain in state, checkpoints, Store, and logs after a retention operation. |
| 21-16 | 21 | trace | medium | Trace a decryption failure to a key/configuration mismatch without printing the key. |
| 21-17 | 21 | extend | hard | Extend retention tests to distinguish deleted active data from retained audit records. |
| 21-18 | 21 | refactor | hard | Refactor unnecessary personal details out of persistent graph state. |

## Module 22: Deployment

### 22-A: compose stack

Features: FastAPI self-hosting; Docker Compose API/Postgres/UI; healthchecks; schema setup; configuration and secrets.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 22-01 | 22 | build | easy | Build a validated deployment configuration for the synthetic claims API, database, and UI. |
| 22-02 | 22 | fix | medium | Fix a service configuration that points the API at localhost instead of the database service. |
| 22-03 | 22 | predict | easy | Predict service readiness and failure states from supplied health responses. |
| 22-04 | 22 | trace | medium | Trace an API startup failure to a missing schema setup or invalid connection setting. |
| 22-05 | 22 | extend | hard | Extend deployment configuration with persistent volumes and safe secret injection. |
| 22-06 | 22 | refactor | hard | Refactor environment-specific constants into typed deployment settings. |

### 22-B: worker reliability

Features: Stateless workers; shared Postgres checkpoints; per-thread concurrency policy; idempotency; graceful shutdown; recovery.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 22-07 | 22 | build | easy | Build a worker contract that resumes persisted claims without process-local state. |
| 22-08 | 22 | fix | medium | Fix two concurrent submissions that create duplicate payments for one claim. |
| 22-09 | 22 | predict | easy | Predict worker handoff and ledger behavior during a simulated restart. |
| 22-10 | 22 | trace | medium | Trace a lost update to concurrent runs on the same claim thread. |
| 22-11 | 22 | extend | hard | Extend the worker contract with admission control and graceful draining. |
| 22-12 | 22 | design | hard | Specify scaling and failure-recovery rules for a small claims deployment. |

### 22-C: managed deployment

Features: Agent Server; LangSmith Deployment; assistants, threads, and runs; background runs; scheduled jobs; costs and access requirements.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| 22-13 | 22 | build | easy | Build a request planner for assistant configuration, threads, and background claim runs using a fake client. |
| 22-14 | 22 | fix | medium | Fix a scheduled-job specification that starts an unintended new claim thread each time. |
| 22-15 | 22 | predict | easy | Predict lifecycle transitions for background and scheduled synthetic claims. |
| 22-16 | 22 | trace | medium | Trace a deployment failure to configuration, authentication, or run-state evidence. |
| 22-17 | 22 | extend | hard | Extend the planner with cancellation and safe resumption of a background run. |
| 22-18 | 22 | design | hard | Compare self-hosted and managed deployment with measured workload and cost assumptions. |

## Module B1: LangGraph.js

### B1-A: typescript state

Features: TypeScript primer; LangGraph.js state schema; nodes and reducers; graph compilation; Python behavior parity.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| B1-01 | B1 | build | easy | Build a TypeScript intake graph that matches the Python golden claim outputs. |
| B1-02 | B1 | fix | medium | Fix a JavaScript reducer that drops previous document findings. |
| B1-03 | B1 | predict | easy | Predict TypeScript state updates and compare them with the Python fixture. |
| B1-04 | B1 | trace | medium | Trace a field-name mismatch across the Python and TypeScript boundary. |
| B1-05 | B1 | extend | hard | Extend the TypeScript graph with a specialist route and unchanged legacy outcomes. |
| B1-06 | B1 | refactor | hard | Refactor a Python intake specification into a typed TypeScript implementation. |

### B1-B: typescript durable

Features: JavaScript conditional routing and Send; persistence; interrupts; stream formats; language API differences.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| B1-07 | B1 | build | easy | Build a TypeScript document workflow with a saved approval interruption. |
| B1-08 | B1 | fix | medium | Fix resumption on a different JavaScript thread than the one that paused. |
| B1-09 | B1 | predict | easy | Predict JavaScript stream and interrupt output without assuming Python v2 shapes. |
| B1-10 | B1 | trace | medium | Trace parallel findings through the JavaScript graph and checkpoint history. |
| B1-11 | B1 | extend | hard | Extend the workflow with a corrected claim replay. |
| B1-12 | B1 | refactor | hard | Refactor the JavaScript runner to normalize output into the shared golden-case format. |

### B1-C: typescript agents

Features: JavaScript fake chat models; tool calls; manual agent loop; createAgent; cross-language trajectory parity.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| B1-13 | B1 | build | easy | Build a TypeScript policy agent using only scripted local model responses. |
| B1-14 | B1 | fix | medium | Fix mismatched tool-call IDs in the TypeScript agent history. |
| B1-15 | B1 | predict | easy | Predict tool trajectories for equivalent Python and TypeScript claim agents. |
| B1-16 | B1 | trace | medium | Trace a parity failure to tool argument serialization. |
| B1-17 | B1 | extend | hard | Extend the TypeScript agent with a bounded tool-call budget. |
| B1-18 | B1 | refactor | hard | Refactor the hand-built TypeScript agent into createAgent with the same golden behavior. |

## Module B2: Deep agents on LangGraph

### B2-A: deep agent planning

Features: create_deep_agent; explicit TodoListMiddleware; planning tools; task progress; current defaults.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| B2-01 | B2 | build | easy | Build a scripted deep agent with explicitly enabled investigation planning. |
| B2-02 | B2 | fix | medium | Fix an agent that assumes planning middleware is enabled by default. |
| B2-03 | B2 | predict | easy | Predict the investigation plan and task-status updates. |
| B2-04 | B2 | trace | medium | Trace an unfinished plan item to a missing tool result. |
| B2-05 | B2 | extend | hard | Extend the plan with an explicit human-review milestone. |
| B2-06 | B2 | refactor | hard | Refactor implicit planner assumptions into explicit middleware configuration. |

### B2-B: virtual filesystem

Features: Virtual filesystem; StateBackend; file tools; bounded paths; persisted artifacts; no host-shell tools.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| B2-07 | B2 | build | easy | Build a virtual case folder for synthetic estimates and investigation notes. |
| B2-08 | B2 | fix | medium | Fix a backend configuration that exposes unrelated host files. |
| B2-09 | B2 | predict | easy | Predict virtual files after a sequence of scripted reads and writes. |
| B2-10 | B2 | trace | medium | Trace an overwritten investigation note to current file-write semantics. |
| B2-11 | B2 | extend | hard | Extend the backend boundary with an allowlist of claim-specific paths. |
| B2-12 | B2 | refactor | hard | Refactor host-file access into an isolated virtual filesystem. |

### B2-C: deep subagents

Features: Subagent definitions; private context; bounded delegation; explicit tools; checkpoints and approval.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| B2-13 | B2 | build | easy | Build a deep-agent investigation with scoped policy and fraud subagents. |
| B2-14 | B2 | fix | medium | Fix a subagent that inherits a payment tool it should not have. |
| B2-15 | B2 | predict | easy | Predict delegation and approval events from a scripted investigation. |
| B2-16 | B2 | trace | medium | Trace duplicated work to overlapping parent and subagent responsibilities. |
| B2-17 | B2 | extend | hard | Extend the investigation with a bounded communication subagent. |
| B2-18 | B2 | design | hard | Compare the deep-agent harness with the explicit module 14 team. |

## Module B3: Build a mini-LangGraph

### B3-A: channels and steps

Features: Educational superstep runner; channel snapshots; pending writes; barrier synchronization; deterministic scheduling.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| B3-01 | B3 | build | easy | Build a small claims runner that gives every active node the same step-start snapshot. |
| B3-02 | B3 | fix | medium | Fix a runner that exposes one parallel node's writes before the barrier. |
| B3-03 | B3 | predict | easy | Predict active nodes and visible state at each superstep. |
| B3-04 | B3 | trace | medium | Trace a race caused by mutating the shared input snapshot. |
| B3-05 | B3 | extend | hard | Extend the runner with conditional scheduling and an explicit terminal state. |
| B3-06 | B3 | refactor | hard | Refactor a sequential loop into separate plan, execute, and update phases. |

### B3-B: mini reducers

Features: Reducer application; overwrite conflict detection; associative merge; parallel result ordering; runtime conformance.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| B3-07 | B3 | build | easy | Build overwrite and append channels for the mini claims runner. |
| B3-08 | B3 | fix | medium | Fix a mini reducer that applies accumulated history twice. |
| B3-09 | B3 | predict | easy | Predict conflicts and merged values for supplied parallel writes. |
| B3-10 | B3 | trace | medium | Trace a mismatch between the mini runner and LangGraph golden fixtures. |
| B3-11 | B3 | extend | hard | Extend the mini runner with stable deduplicated findings. |
| B3-12 | B3 | refactor | hard | Refactor hard-coded channel behavior into a small reducer registry. |

### B3-C: mini checkpoints

Features: Checkpoint snapshots; thread identities; resume positions; educational interrupt representation; implementation limits.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| B3-13 | B3 | build | easy | Build minimal checkpoint storage for pausing and continuing synthetic claims. |
| B3-14 | B3 | fix | medium | Fix a checkpoint that retains mutable references to later state. |
| B3-15 | B3 | predict | easy | Predict replay state for two threads with distinct checkpoints. |
| B3-16 | B3 | trace | medium | Trace cross-thread state leakage in the mini runner. |
| B3-17 | B3 | extend | hard | Extend the runner with a human-review pause and explicit resume input. |
| B3-18 | B3 | design | hard | Document where the mini runner falls short of production durability guarantees. |

## Module B4: What's new

### B4-A: event streaming beta

Features: Beta v3 event streaming; typed projections; lifecycle and subgraphs; tool-call deltas; version distinctions.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| B4-01 | B4 | build | easy | Build a Beta v3 claims stream consumer with message, value, and interrupt projections. |
| B4-02 | B4 | fix | medium | Fix a consumer that treats tool-call deltas as complete argument objects. |
| B4-03 | B4 | predict | easy | Predict projected events and assembled tool arguments for scripted chunks. |
| B4-04 | B4 | trace | medium | Trace duplicate text to a consumer that re-appends accumulated content. |
| B4-05 | B4 | extend | hard | Extend the consumer with nested-run projection handling. |
| B4-06 | B4 | refactor | hard | Refactor a v2 UI adapter into an optional Beta v3 adapter with the same user-visible result. |

### B4-B: delta channels beta

Features: Beta DeltaChannel; incremental checkpoint storage; snapshot_frequency; replay reconstruction; schema migration hazards.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| B4-07 | B4 | build | easy | Build a Beta delta-backed synthetic investigation history with explicit snapshot frequency. |
| B4-08 | B4 | fix | medium | Fix replay logic that treats stored deltas as complete state. |
| B4-09 | B4 | predict | easy | Predict reconstructed history from snapshots and subsequent deltas. |
| B4-10 | B4 | trace | medium | Trace a rollback failure to incompatible persisted channel representation. |
| B4-11 | B4 | extend | hard | Extend reconstruction tests with empty deltas and periodic full snapshots. |
| B4-12 | B4 | design | hard | Plan a reversible migration experiment using disposable synthetic checkpoints. |

### B4-C: typed approvals

Features: Per-call HumanInTheLoopMiddleware; response_schema; checked resume payloads; tool edit constraints; current changelog literacy.

| ID | Module | Type | Level | Task |
| --- | --- | --- | --- | --- |
| B4-13 | B4 | build | easy | Build per-call approval middleware for two synthetic payout-related tools. |
| B4-14 | B4 | fix | medium | Fix an approval edit that attempts to change the selected tool. |
| B4-15 | B4 | predict | easy | Predict pending interrupt schemas and accepted responses for each call. |
| B4-16 | B4 | trace | medium | Trace an invalid resume answer rejected before persistence. |
| B4-17 | B4 | extend | hard | Extend review with independent decisions for each gated call. |
| B4-18 | B4 | design | hard | Write an upgrade checklist connecting release notes to behavior tests. |
