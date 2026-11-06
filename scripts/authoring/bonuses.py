"""Bonus contracts exercise real language, deep-agent, runner, and recent-release behavior."""

from scripts.authoring.tier2 import lab

LABS = {
    "B1-A": lab(
        "TypeScript adds static types to JavaScript; StateSchema uses Zod schemas for graph state and ReducedValue declares merges. Nodes return partial objects, await obtains a Promise result, and integer cents preserve Python parity. The JavaScript API returns state directly here; do not assume Python's v2 result wrapper exists in another language.",
        "The same claim folder can use different language labels while keeping its business rules unchanged.",
        [{}, {"amount_cents": 100000}, {"description": " "}, {"amount_cents": True}],
        [("value.audit", ["normalized", "routed"]), ("value.route", "standard")],
        [
            (
                "state.description.trim()",
                "state.description",
                "Trim the input description before testing completeness.",
            ),
            (
                "state.amount_cents <= 100000",
                "state.amount_cents < 100000",
                "Preserve Python's inclusive fast-track boundary.",
            ),
            (
                "!state.description ?",
                "false ?",
                "Handle an empty normalized description as missing information.",
            ),
            ("old.concat(update)", "update", "Accumulate both audit labels across node updates."),
        ],
        language="typescript",
        schema="StateSchema_and_Zod",
        parity="integer_cent_rules",
    ),
    "B1-B": lab(
        "JavaScript Send fans out document work, SqliteSaver retains the approval pause, and Command resumes it. The saver connection is explicitly closed. JavaScript uses camelCase options such as streamMode and returns its documented update shape; this lesson intentionally does not copy Python invocation parameters.",
        "The same waiting shelf works across languages, but each desk's form has its own field names.",
        [
            {},
            {"documents": [], "approved": True},
            {"documents": ["police_report"]},
            {"approved": "yes"},
        ],
        [("value.approved", False), ("value.pending_before", ["approve"])],
        [
            (
                "state.documents.map((document)",
                "state.documents.slice(0, 1).map((document)",
                "Review every document before the approval step.",
            ),
            (
                'typeof decision !== "boolean"',
                'typeof decision === "boolean"',
                "Accept explicit boolean decisions and reject strings at the interrupt boundary.",
            ),
            (
                "return { approved: decision }",
                "return { approved: true }",
                "Preserve a rejected approval through JavaScript resume.",
            ),
            (
                "old.concat(update)",
                "update",
                "Combine all parallel findings rather than retaining only the last write.",
            ),
        ],
        persistence="SQLite",
        resume="checked_boolean",
        format="JavaScript_documented_options",
    ),
    "B1-C": lab(
        "The TypeScript model factory returns a scripted LangChain fake with tool calls. A manual StateGraph loop and createAgent consume the same trajectory, making their roles and call identities directly comparable. The Python gym bridge executes the selected TypeScript file in Node; it never supplies the business answer itself.",
        "Two service-desk layouts must produce the same numbered work orders and final explanation.",
        [{}, {"recursion_limit": 1}, {"policy_id": "MISSING"}],
        [("value.roles", ["human", "ai", "tool", "ai"]), ("value.tool_ids", ["lookup-1"])],
        [
            (
                '.addEdge("tools", "model")',
                '.addEdge("tools", END)',
                "Return the tool result to the manual agent before ending.",
            ),
            (
                "recursionLimit: input.recursion_limit",
                "recursionLimit: 100",
                "Respect the configured loop budget in both JavaScript agents.",
            ),
            (
                'id: "lookup-1"',
                'id: "wrong-call"',
                "Preserve the expected tool-call identity across the language port.",
            ),
            (
                "tools: [lookup] }).invoke",
                "tools: [] }).invoke",
                "Register the same evidence tool in the prebuilt implementation.",
            ),
        ],
        models="one_fake_factory",
        grading="actual_Node_execution",
        parity="tool_trajectory",
    ),
    "B2-A": lab(
        "create_deep_agent supplies an agent harness, but current defaults should be inspected rather than remembered from older tutorials. This pinned release uses explicit TodoListMiddleware for planning. The write_todos tool updates declared task state; marking an item completed is not evidence that the underlying investigation actually happened.",
        "A visible investigation checklist helps organize work, but checked boxes still need supporting records.",
        [
            {},
            {"first_status": "completed"},
            {"include_planning": False},
            {"first_status": "invalid"},
        ],
        [("value.todos.0.status", "in_progress")],
        [
            (
                '[TodoListMiddleware()] if case["include_planning"] else []',
                "[]",
                "Install the explicit planning middleware when requested.",
            ),
            (
                '"status": case["first_status"]',
                '"status": "completed"',
                "Keep task progress consistent with the supplied status.",
            ),
            (
                '"status": "pending"',
                '"status": "completed"',
                "Do not mark unstarted document review as completed.",
            ),
            (
                '"name": "write_todos"',
                '"name": "missing_planning_tool"',
                "Call the registered planning capability.",
            ),
        ],
        planning="explicit_middleware",
        progress="declared_todos",
        evidence="separate_from_status",
    ),
    "B2-B": lab(
        "StateBackend stores a virtual filesystem in graph state instead of writing host files. Typed FilesystemPermission rules restrict writes to the claim directory, and checkpoints retain the resulting artifact. Tool success is checked separately from the final model sentence: a scripted acknowledgment cannot prove a denied write happened.",
        "A virtual filing tray is part of the case record, not unrestricted access to the building's cabinets.",
        [
            {},
            {"path": "/private/key.txt"},
            {"path": "/claims/second.txt", "content": "Another synthetic finding"},
        ],
        [("value.paths", ["/claims/review.txt"]), ("value.tool_statuses", ["success"])],
        [
            (
                'paths=["/claims/**"], mode="allow"',
                'paths=["/claims/**"], mode="deny"',
                "Allow the explicitly scoped claim artifact path.",
            ),
            (
                'paths=["/**"], mode="deny"',
                'paths=["/**"], mode="allow"',
                "Deny writes outside the permitted virtual directory.",
            ),
            (
                '"content": case["content"]',
                '"content": "replaced"',
                "Persist the supplied investigation note without substitution.",
            ),
            (
                '"file_path": case["path"]',
                '"file_path": "/claims/review.txt"',
                "Honor and validate the requested virtual artifact path.",
            ),
        ],
        backend="virtual_state",
        permissions="typed_path_rules",
        persistence="checkpointed_artifacts",
    ),
    "B2-C": lab(
        "A deep-agent specialist has an explicit name, scoped tools, and isolated context. Delegation itself is gated by human approval and the parent has a model-call budget. The specialist receives a narrow policy question rather than the whole customer file. A rejected delegation must not execute the specialist task.",
        "The lead adjuster needs approval to commission a specialist and sends only the relevant question.",
        [{}, {"decision": "reject"}, {"specialist": "missing_specialist"}],
        [("value.paused", 1)],
        [
            (
                '"subagent_type": case["specialist"]',
                '"subagent_type": "missing_specialist"',
                "Delegate to the explicitly registered specialist.",
            ),
            (
                'decision = {"type": case["decision"]}',
                'decision = {"type": "approve"}',
                "Preserve a human rejection of delegation.",
            ),
            (
                '"The synthetic deductible is 100000 cents."',
                '"The synthetic deductible is 0 cents."',
                "Keep the specialist's evidence answer tied to the policy fixture.",
            ),
            (
                "run_limit=3",
                "run_limit=0",
                "Allow the bounded model operations needed to complete an approved delegation.",
            ),
        ],
        context="isolated_specialist",
        delegation="approval_gated",
        budget="bounded_parent_calls",
    ),
    "B3-A": lab(
        "The educational runner snapshots state before a superstep, collects writes from every sibling, then applies them at a barrier. Thus both workers see zero prior findings while the next-step summary sees both. This small runner explains visibility; it deliberately omits production concurrency, async execution, pending-write recovery, and serialization.",
        "Every inspector receives a photocopy from the same morning; their notes are combined only at the afternoon collection desk.",
        [{}, {"documents": []}, {"documents": ["estimate"]}],
        [("value.worker_views", [0, 0]), ("value.count", 2)],
        [
            ("(old or []) + new", "new", "Merge all sibling findings at the barrier."),
            (
                'len(state["findings"])',
                'len(state["findings"]) + 1',
                "Report the previous-boundary view seen by each worker.",
            ),
            (
                'case["documents"] or ["summary"]',
                'case["documents"]',
                "Run the summary even when the document fan-out is empty.",
            ),
            (
                '"count": len(state["findings"])',
                '"count": 0',
                "Compute the summary from the merged findings.",
            ),
        ],
        visibility="previous_snapshot",
        writes="barrier_merge",
        scope="educational_only",
    ),
    "B3-B": lab(
        "An overwrite channel accepts one update per superstep; multiple writers need a reducer. This comparison runs the same policy and estimate findings in the mini runner and real LangGraph, normalizing their different exception classes to one conflict observation. Canonical output order is separate from the algebra used to merge writes.",
        "Two people cannot independently replace the same page without an agreed rule for combining their edits.",
        [{}, {"use_reducer": False}],
        [("value.equal", True), ("value.mini.findings", ["estimate", "policy"])],
        [
            (
                '{"findings": operator.add} if case["use_reducer"] else {}',
                "{}",
                "Install the mini-runner reducer when parallel accumulation is required.",
            ),
            (
                'StateGraph(Reduced if case["use_reducer"] else Overwrite)',
                "StateGraph(Reduced)",
                "Retain the overwrite-conflict case in the real runtime comparison.",
            ),
            (
                '["policy", "estimate"],',
                '["policy"],',
                "Schedule both independent inspections in the teaching runner.",
            ),
            (
                'observed["mini"] == observed["langgraph"]',
                'observed["mini"] != observed["langgraph"]',
                "Report conformance only when both observed contracts match.",
            ),
        ],
        overwrite="single_writer",
        reducer="explicit_merge",
        conformance="real_runtime_comparison",
    ),
    "B3-C": lab(
        "A checkpoint stores state and the next scheduled work for one thread. The mini runner copies snapshots so external mutation cannot corrupt history. Its single-node pause records a request and resumes the same pending node with a checked decision; another thread remains independent. This is a teaching representation, not LangGraph's full interrupt protocol.",
        "Each customer has a separate waiting folder, and an inspection copy cannot alter the archived original.",
        [{}, {"approved": True}, {"approved": "yes"}, {"claim_id": "CLM-0010"}],
        [("value.other_pending", ["review"]), ("value.completed", True)],
        [
            (
                'resume=case["approved"]',
                "resume=True",
                "Preserve rejection when resuming the waiting teaching thread.",
            ),
            (
                "type(resume) is not bool",
                "False",
                "Validate the resumed decision before updating approval state.",
            ),
            (
                '"original_id": graph.latest("A").values["claim_id"]',
                '"original_id": copy.values["claim_id"]',
                "Read the archived snapshot rather than an externally modified copy.",
            ),
            (
                '"other_pending": graph.latest("B").pending',
                '"other_pending": graph.latest("A").pending',
                "Inspect the other thread independently after completing the first.",
            ),
        ],
        checkpoint="copied_state_and_position",
        thread="isolated",
        pause="single_node_teaching_contract",
    ),
    "B4-A": lab(
        "Beta v3 event streaming exposes typed message, subgraph, value, and output projections. Child messages belong to the subgraph projection. The raw protocol uses method and params rather than the v2 type/ns/data shape. This example uses a fresh fake run for raw-event inspection so consuming one view does not pretend to replay already-consumed events.",
        "The main case and specialist folders have separate progress feeds, even when one screen presents them together.",
        [{}, {"text": "Estimate accepted for review."}],
        [
            ("value.nested", True),
            ("value.channels", ["lifecycle", "messages", "values"]),
            ("value.tool_arguments.policy_id", "POL-0001"),
        ],
        [
            (
                "for child in stream.subgraphs for message in child.messages",
                "for message in stream.messages",
                "Read child model messages through their subgraph projection.",
            ),
            (
                'output["messages"][-1].text',
                'output["messages"][0].text',
                "Read the final model message from the completed output projection.",
            ),
            (
                "events = list(raw)",
                "events = []",
                "Consume the raw protocol when inspecting lifecycle channels.",
            ),
            (
                'event["params"]["namespace"]',
                'event["params"]["missing_namespace"]',
                "Use the v3 protocol namespace location rather than a guessed field.",
            ),
        ],
        status="Beta",
        protocol="v3_method_params",
        child_messages="subgraph_projection",
    ),
    "B4-B": lab(
        "Beta DeltaChannel stores incremental writes and reconstructs channel state through a deterministic batch reducer. snapshot_frequency bounds how often a full snapshot is written. The reducer must be invariant to regrouping write batches, because replay may batch differently from live execution. Schema and reducer changes require migration testing before reusing old threads.",
        "Retain a ledger of additions with occasional full copies, then rebuild the current folder from those records.",
        [{}, {"snapshot_frequency": 1}, {"notes": []}, {"snapshot_frequency": 0}],
        [("value.notes", ["intake", "policy", "estimate"]), ("value.reconstructed", True)],
        [
            (
                "result.extend(write)",
                "result = list(write)",
                "Retain earlier delta writes when applying a new batch.",
            ),
            (
                "snapshot_frequency=frequency",
                "snapshot_frequency=2",
                "Honor and validate the requested snapshot cadence.",
            ),
            (
                'for note in case["notes"]:',
                'for note in case["notes"][:1]:',
                "Checkpoint every supplied note before reconstruction.",
            ),
            (
                "list(current or [])",
                "[]",
                "Start each reducer batch from the reconstructed accumulated value.",
            ),
        ],
        status="Beta",
        reducer="batch_invariant",
        migration="replay_test_old_threads",
    ),
    "B4-C": lab(
        "Per-call HumanInTheLoopMiddleware emits one approval request for each gated tool call. Its response_schema describes only permitted decisions; the runtime validates the answer before saving it. Resume by interrupt ID and keep tool editing disabled when the reviewer may approve or reject only. Typed approval validates shape, while real authorization still belongs to the application.",
        "Each numbered work order carries its own approval form with only the choices that desk is allowed to accept.",
        [{}, {"decision": "reject"}, {"decision": "edit"}, {"amount_cents": 0}],
        [("value.schema_present", True), ("value.effects", [50000])],
        [
            (
                'interrupt_mode="per_call"',
                'interrupt_mode="batched"',
                "Use per-call requests when resuming individual interrupt IDs.",
            ),
            (
                'decision = {"type": case["decision"]}',
                'decision = {"type": "approve"}',
                "Respect rejection instead of coercing every decision to approval.",
            ),
            (
                '"amount_cents": case["amount_cents"]',
                '"amount_cents": 50000',
                "Bind the proposal to its requested amount.",
            ),
            (
                "effects.append(amount_cents)",
                "effects.extend([amount_cents, amount_cents])",
                "Record one effect for one approved tool execution.",
            ),
        ],
        granularity="per_tool_call",
        validation="response_schema",
        decisions="approve_or_reject",
    ),
}
