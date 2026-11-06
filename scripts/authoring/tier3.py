"""Authored contracts for composition, external boundaries, and recovery."""

from scripts.authoring.tier2 import lab

LABS = {
    "13-A": lab(
        "A compiled subgraph can be a parent node when their state keys agree. Its updates still meet the parent's reducers. This fraud checker is reused for claims and new policies; its idempotent flag reducer avoids duplicating shared evidence when the child returns accumulated state.",
        "Two departments reuse the same inspection desk and agree on the labels in its folder.",
        [
            {},
            {"amount_cents": 100000, "documents": ["estimate"]},
            {"workflow": "new_policy"},
            {"workflow": "unknown"},
        ],
        [("value.flags", ["high_value", "intake_checked", "missing_evidence"])],
        [
            (
                "sorted(set(old) | set(new))",
                "sorted(new)",
                "Keep evidence already recorded by the parent.",
            ),
            (
                'state["amount_cents"] > 500000',
                'state["amount_cents"] > 900000',
                "Apply the high-value risk boundary inside the reusable child.",
            ),
            ('["missing_evidence"]', "[]", "Flag missing supporting documents."),
            (
                'set(state["flags"]) - {"intake_checked"}',
                'set(state["flags"])',
                "Do not confuse an intake milestone with a risk flag.",
            ),
        ],
        interface="shared_keys",
        reducer="idempotent_flags",
        reuse="claim_and_policy",
    ),
    "13-B": lab(
        "When parent and child schemas differ, call the child inside an adapter node. Map the input fields explicitly, then return only the public finding. Private child fields should not become parent state just because a dictionary is convenient to copy.",
        "Send a specialist a scoped work order and receive a conclusion without copying the private notebook.",
        [{}, {"amount_cents": 500000}, {"claim_id": "CLM-0200", "amount_cents": 10000}],
        [("value.fields", ["amount_cents", "claim_id", "risk"])],
        [
            (
                '"value": state["amount_cents"]',
                '"value": 0',
                "Map the actual claim amount into the child input.",
            ),
            (
                'state["value"] > 500000',
                'state["value"] >= 500000',
                "Preserve the exact review threshold.",
            ),
            (
                'result.value["finding"]',
                'result.value["private_notes"]',
                "Return the public risk finding rather than private investigation notes.",
            ),
            (
                'return {"risk": result.value["finding"]}',
                'return {"risk": result.value["finding"], "claim_id": "lost"}',
                "Preserve the parent claim identity across the adapter.",
            ),
        ],
        input="explicit_mapping",
        output="finding_only",
        privacy="child_notes_private",
    ),
    "13-C": lab(
        "A parent checkpointer propagates into its child. A child compiled with the default per-invocation behavior starts fresh for each invocation; checkpointer=True gives the child persistent state across calls. While paused, get_state(subgraphs=True) exposes the nested task snapshot. Streaming namespaces identify which graph emitted an update.",
        "The main case file indexes a paused specialist's folder so the adjuster can resume the right desk.",
        [{}, {"approved": True}, {"persistent_child": True}, {"approved": "yes"}],
        [("value.child_pending", ["review"]), ("value.checks", 1)],
        [
            (
                "subgraphs=True)",
                "subgraphs=False)",
                "Request nested snapshots when inspecting child state.",
            ),
            (
                "type(decision) is not bool",
                "False",
                "Reject a string masquerading as a human decision.",
            ),
            (
                'subgraphs=True, version="v2"',
                'subgraphs=False, version="v2"',
                "Include nested updates when streaming subgraphs.",
            ),
            (
                '"approved": decision',
                '"approved": True',
                "Carry the actual human approval through the child boundary.",
            ),
        ],
        persistence="inherited",
        inspection="nested_snapshot",
        resume="checked_boolean",
    ),
    "14-A": lab(
        "A supervisor may call specialists as tools. Each specialist gets a narrow evidence prompt and a private message history; the supervisor receives only the returned conclusion. This direct create_agent pattern avoids an extra helper package. More agents add calls and failure boundaries, so compare them against a single-agent baseline.",
        "The lead adjuster asks two specialists specific questions instead of forwarding the entire customer file.",
        [
            {},
            {
                "question": "Which document is missing?",
                "private_note": "Synthetic address withheld",
            },
        ],
        [
            ("value.tool_names", ["fraud_analyst", "policy_expert"]),
            ("value.private_note_leaked", False),
        ],
        [
            (
                "tools=[policy_expert, fraud_analyst]",
                "tools=[policy_expert]",
                "Register both specialist capabilities with the supervisor.",
            ),
            (
                'return specialist("fraud", "Contractor estimate is missing")',
                'return specialist("policy", "Contractor estimate is missing")',
                "Keep specialist roles attached to the evidence they reviewed.",
            ),
            (
                '"Deductible: 100000 cents"',
                '"Deductible: 0 cents"',
                "Give the policy specialist authoritative scoped evidence.",
            ),
            (
                'messages"][-1].content',
                'messages"][0].content',
                "Return the specialist conclusion instead of its input prompt.",
            ),
        ],
        orchestration="supervisor_tools",
        context="minimum_evidence",
        histories="private",
    ),
    "14-B": lab(
        "Command.PARENT transfers control from a child graph to a node in its parent. The shared messages channel uses add_messages. A tool-based handoff includes both the AI request and its ToolMessage acknowledgment so the next specialist receives a valid conversation. Parent destinations must not be declared as local child nodes.",
        "A referral changes the responsible desk and includes both the referral form and its receipt.",
        [{}, {"claim_id": "CLM-0400", "question": "What is the water deductible?"}],
        [("value.paired", True), ("value.active_agent", "policy")],
        [
            (
                "graph=Command.PARENT",
                "graph=None",
                "Address the parent graph when handing off to its specialist.",
            ),
            (
                'tool_call_id="handoff-1"',
                'tool_call_id="wrong-handoff"',
                "Pair the handoff acknowledgment with its AI request.",
            ),
            (
                '"active_agent": "policy"',
                '"active_agent": "intake"',
                "Update ownership together with the handoff.",
            ),
            (
                '"messages": [request, response]',
                '"messages": [request]',
                "Forward the complete handoff pair.",
            ),
        ],
        destination="parent",
        history="paired_messages",
        ownership="active_agent",
    ),
    "14-C": lab(
        "A swarm-style team routes according to the active specialist, without requiring a central supervisor on every transition. Its business budget is distinct from the graph recursion limit. This controlled four-role comparison measures calls and completion; scripted answers do not establish that the team is smarter than the one-call baseline.",
        "A claim folder moves between specialists, but a supervisor's budget limits how many desks it may visit.",
        [{}, {"budget": 2}, {"budget": 0}, {"start_agent": "fraud"}, {"budget": -1}],
        [("value.team_calls", 4), ("value.team_complete", True)],
        [
            (
                'state["calls"] >= state["budget"]',
                "False",
                "Stop delegation when the business call budget is exhausted.",
            ),
            (
                "ROLES[index + 1]",
                "ROLES[index]",
                "Advance to the next specialist instead of handing work back to itself.",
            ),
            (
                '"calls": state["calls"] + 1',
                '"calls": state["calls"]',
                "Count every specialist operation against the budget.",
            ),
            (
                '"complete": next_role == END',
                '"complete": False',
                "Mark successful completion when the final specialist finishes.",
            ),
        ],
        routing="active_role",
        budget="explicit_call_count",
        comparison="single_agent_baseline",
    ),
    "15-A": lab(
        "An entrypoint accepts one serializable input and uses ordinary Python branches. A task call schedules durable work and returns a future; result() obtains its value. This supports familiar control flow without removing the need for validated inputs and deterministic replay order.",
        "A familiar checklist can still assign tracked work orders and wait for their results.",
        [{}, {"amount_cents": 100000}, {"description": " "}, {"amount_cents": True}],
        [("value.description", "Pipe burst"), ("value.route", "standard")],
        [
            (
                "normalize(claim).result()",
                "normalize(claim)",
                "Resolve the normalization future before reading its fields.",
            ),
            (
                'claim["amount_cents"] <= 100000',
                'claim["amount_cents"] < 100000',
                "Match the Graph API fast-track boundary.",
            ),
            (
                'claim["description"].strip()',
                'claim["description"]',
                "Normalize whitespace before choosing the missing-information branch.",
            ),
            (
                'type(claim["amount_cents"]) is not int',
                'not isinstance(claim["amount_cents"], int)',
                "Reject booleans even though Python considers them integer instances.",
            ),
        ],
        api="functional",
        futures="resolve_before_read",
        branches="ordinary_python",
    ),
    "15-B": lab(
        "Create all task futures before resolving them to allow concurrent work. Collect results in a canonical order so scheduling differences do not change the business answer. The equivalent Send graph lets you compare the same finding function across the Graph and Functional APIs, including an empty document list.",
        "Hand out every inspection assignment before waiting at the collection desk.",
        [
            {},
            {"documents": []},
            {"documents": ["receipt", "estimate"]},
            {"documents": ["police_report"]},
        ],
        [("value.equal", True)],
        [
            (
                "sorted(future.result() for future in futures)",
                "[future.result() for future in futures]",
                "Canonicalize Functional API results independently of input order.",
            ),
            ("operator.add]", "lambda old, new: new]", "Preserve every parallel graph result."),
            (
                'if document == "police_report"',
                "if False",
                "Keep police-report review semantics shared by both APIs.",
            ),
            (
                "for document in documents]",
                "for document in documents[:1]]",
                "Schedule every document before resolving task futures.",
            ),
        ],
        scheduling="start_all_then_resolve",
        comparison="same_business_function",
        aggregation="sorted_findings",
    ),
    "15-C": lab(
        "Resuming a Functional API interrupt restarts the entrypoint from its beginning. Completed task results are retrieved from checkpoints, so the task body need not run again. Keep task ordering deterministic and validate the resume payload. External effects still require their own idempotency at the crash window.",
        "Reread the checklist after a pause while reusing stamped, completed work orders.",
        [{}, {"approved": False}, {"approved": "yes"}, {"claim_id": "CLM-0077"}],
        [("value.counts.entrypoint", 2), ("value.counts.task", 1)],
        [
            (
                "@task\n    def collect_evidence",
                "def collect_evidence",
                "Use a task boundary so completed evidence can be reused during replay.",
            ),
            (
                "type(decision) is not bool",
                "False",
                "Validate the resumed approval before returning a business result.",
            ),
            (
                '"approved": decision',
                '"approved": True',
                "Preserve a human rejection through entrypoint replay.",
            ),
            (
                'evidence["claim_id"]',
                '"CLM-0001"',
                "Preserve the claim identity from the completed task result.",
            ),
        ],
        replay="entrypoint_restarts",
        task_results="checkpoint_reuse",
        effects="idempotent_boundary",
    ),
    "16-A": lab(
        "async def creates a coroutine; await lets other work proceed while a request waits. An injected HTTP transport makes failures testable without a server. Retry only transient transport failures, bound attempts and timeouts, and reuse a stable idempotency key because a missing acknowledgment may follow a successful write.",
        "If a receipt is lost, resend the same numbered order rather than creating a second order.",
        [{}, {"transient_failures": 0}, {"transient_failures": 4}, {"attempts": 0}],
        [("value.effects", 1), ("value.calls", 2)],
        [
            (
                '"estimate-request:" + claim_id',
                '"estimate-request:" + claim_id + str(attempt)',
                "Reuse the same idempotency key across a retry.",
            ),
            (
                "range(attempts)",
                "range(1)",
                "Honor the bounded retry allowance after a lost acknowledgment.",
            ),
            (
                "if attempt + 1 == attempts:",
                "if True:",
                "Raise only when the transient retry budget is exhausted.",
            ),
            (
                "response.json()",
                '{"accepted": False}',
                "Return the actual service acknowledgment after a successful attempt.",
            ),
        ],
        transport="injected",
        timeout="bounded",
        retry_key="stable",
    ),
    "16-B": lab(
        "MCP describes tools with names and JSON schemas. The official SDK validates requests before calling the function. This local service exposes only synthetic triage reads and capability discovery; it has no payment or arbitrary filesystem operation. stdio is the protocol channel, so diagnostics belong on stderr.",
        "A service counter publishes a small menu of permitted requests, not keys to every office.",
        [
            {},
            {"claim_id": "CLM-0002"},
            {"claim_id": "../../private"},
            {"tool_name": "list_capabilities"},
        ],
        [("value.tools", ["list_capabilities", "read_claim"]), ("value.parameters", ["claim_id"])],
        [
            (
                'server.call_tool(case["tool_name"], arguments)',
                'server.call_tool("unknown_tool", arguments)',
                "Invoke a tool from the published MCP registry.",
            ),
            (
                '{"claim_id": case["claim_id"]}',
                '{"claim_id": "CLM-0001"}',
                "Pass the requested synthetic claim through schema validation.",
            ),
            (
                'server.call_tool(case["tool_name"], arguments)',
                'server.call_tool("read_claim", arguments)',
                "Dispatch both registered tools rather than only read_claim.",
            ),
            (
                "sorted(item.name for item in tools)",
                'sorted(item.name for item in tools if item.name == "read_claim")',
                "Publish the complete permitted capability list.",
            ),
        ],
        transport="stdio",
        permissions="synthetic_read_only",
        schema="sdk_validated",
    ),
    "16-C": lab(
        "MultiServerMCPClient loads tool definitions from a real local stdio subprocess. The adapter turns them into LangChain tools while an explicit client session owns their lifetime. The pinned adapter supports MCP SDK 1.x. The newer langchain.mcp successor is Beta and is documented separately instead of silently mixing incompatible APIs.",
        "A translator stays connected to the service desk for the entire conversation.",
        [{}, {"claim_id": "CLM-0002"}],
        [("value.tool_call_ids", ["mcp-1"]), ("value.claim.claim_id", "CLM-0001")],
        [
            (
                "tools = await load_mcp_tools(session)",
                "tools = []",
                "Load MCP tools before constructing the agent.",
            ),
            (
                '"claim_id": case["claim_id"]',
                '"claim_id": "CLM-0001"',
                "Send the selected claim identifier to the MCP service.",
            ),
            (
                '"id": "mcp-1"',
                '"id": "changed-call"',
                "Preserve the declared request identity through the adapter.",
            ),
            (
                '"name": "read_claim"',
                '"name": "list_capabilities"',
                "Invoke the evidence-reading capability rather than a different tool.",
            ),
        ],
        lifetime="explicit_session",
        adapter="pinned_compatible",
        network="local_stdio_only",
    ),
    "17-A": lab(
        "A task result is reusable only after it is checkpointed. This example kills an owned child after the effect ledger commits but before the task returns, then starts a new process. A payload-bound idempotency key prevents duplicate effects even in that gap. sync, async, and exit durability offer different checkpoint guarantees; none makes an external system transactional with the graph.",
        "A stamped payment register prevents a duplicate even when the worker disappears before filing the receipt.",
        [{}, {"durability": "async"}, {"durability": "exit"}, {"claim_id": "CLM-0050"}],
        [("value.crash_exit", 42), ("value.effect_count", 1)],
        [
            (
                'key = "estimate:" + claim_id',
                'key = "estimate:" + claim_id + (":first" if crash else ":second")',
                "Keep the effect identity stable across process death.",
            ),
            (
                "os._exit(42)",
                "os._exit(43)",
                "Make the crash supervisor recognize the documented owned-worker exit.",
            ),
            (
                '"claim_id": result["value"]["claim_id"]',
                '"claim_id": "CLM-0001"',
                "Recover the original claim identity after restart.",
            ),
            (
                '"effect_count": len(result["effects"])',
                '"effect_count": len(result["effects"]) + 1',
                "Report the durable ledger count, not an inferred execution count.",
            ),
        ],
        effect="payload_bound_idempotency",
        failure="real_child_exit",
        recovery="checkpoint_or_same_operation",
    ),
    "17-B": lab(
        "RetryPolicy repeats selected transient failures; TimeoutPolicy bounds asynchronous attempts. After retries are exhausted, a NodeError-aware handler routes to manual review. RunControl requests a cooperative drain after the current superstep, preserving a resumable boundary rather than killing in-flight work. Recovery must not invent a successful external effect.",
        "Try a temporarily closed service desk twice, then send the claim to review; at closing time finish the current stamped page before shelving it.",
        [{}, {"failures": 3}, {"timeout": True}, {"drain": False, "failures": 0}],
        [("value.attempts", 2), ("value.drained", True)],
        [
            (
                "max_attempts=2",
                "max_attempts=1",
                "Retry the recoverable first failure before routing to manual review.",
            ),
            (
                '"status": "manual_review"',
                '"status": "estimate_received"',
                "Do not label an exhausted or timed-out request as successful.",
            ),
            (
                'if case["drain"]:',
                "if False:",
                "Honor the cooperative shutdown request at the next boundary.",
            ),
            (
                'lambda state: {"finished": True}',
                'lambda state: {"finished": False}',
                "Finish the recovery path after success or error handling.",
            ),
        ],
        retries="transient_only",
        timeout="async_attempt",
        shutdown="cooperative_drain",
    ),
    "17-C": lab(
        "An interrupt persists a wait without holding a worker open. The simulated receipt date advances three days while the program itself finishes immediately. Reopening the SQLite saver proves connection-lifetime independence. The same graph includes synchronous and asynchronous Postgres variants; schema setup belongs in startup or migrations, not each request.",
        "Put the claim on a dated waiting shelf and let another shift resume it when the estimate arrives.",
        [{}, {"received_on": "2026-01-01"}, {"received_on": "2025-12-31"}, {"document_id": ""}],
        [("value.waited_days", 3), ("value.interrupts", 1)],
        [
            (
                "if elapsed < 0:",
                "if False:",
                "Reject a receipt date earlier than the request date.",
            ),
            (
                '"waited_days": elapsed',
                '"waited_days": 0',
                "Compute elapsed business time from explicit dates.",
            ),
            (
                'or not response.get("document_id")',
                "",
                "Require the missing document before ending the durable wait.",
            ),
            (
                '"document_id": response["document_id"]',
                '"document_id": "unverified"',
                "Preserve the received evidence identifier on resume.",
            ),
        ],
        wait="interrupt",
        clock="explicit_dates",
        persistence="reopened_saver",
    ),
}
