"""Authored production contracts: streams, tests, observability, authorization, deployment."""

from scripts.authoring.tier2 import lab

LABS = {
    "18-A": lab(
        "ainvoke awaits one result; astream yields intermediate parts. Pass RunnableConfig into async model calls for explicit context propagation. The seven v2 modes expose different views, so count types rather than assuming one common payload. Cancellation must await cleanup; a browser disconnect is not proof that an external effect was rolled back.",
        "Watch the service desks work while retaining a final receipt, and close every open folder when stopping early.",
        [{}, {"text": "Documents ready.", "cancel": False}],
        [("value.matches_invoke", True), ("value.cancelled_cleanly", True)],
        [
            (
                'text += part["data"][0].content',
                'text = part["data"][0].content',
                "Accumulate chunks instead of replacing the previous text.",
            ),
            (
                "stream_mode=MODES",
                'stream_mode=["updates"]',
                "Request the intended seven stream projections.",
            ),
            (
                'if case["cancel"]:',
                "if False:",
                "Cancel and await the pending async graph when requested.",
            ),
            (
                'cleaned.append("closed")',
                "cleaned.clear()",
                "Record cleanup after the waiting node receives cancellation.",
            ),
        ],
        execution="awaited_operations",
        stream="v2_discriminated_parts",
        cancellation="await_cleanup",
    ),
    "18-B": lab(
        "An SSE frame ends with a blank line and carries JSON on its data line. JSON escaping keeps embedded newlines inside one frame. The real FastAPI routes authenticate callers, check thread ownership, and bind resumed decisions to the current interrupt ID. Reconnect by reading a snapshot; this demo does not promise durable replay from Last-Event-ID.",
        "A numbered progress bulletin is useful only when it goes to the right customer and references the current approval form.",
        [{}, {"approved": False}, {"note": 'Quote: "estimate"\nready'}],
        [
            ("value.customer_approval_status", 403),
            ("value.effects", 1),
            ("value.framing_roundtrip", True),
        ],
        [
            (
                'encode_event("progress", {"node": case["note"]}, 1)',
                'encode_event("progress", {"node": "changed"}, 1)',
                "Preserve the exact event payload through SSE encoding.",
            ),
            (
                'approve=case["approved"]',
                "approve=True",
                "Carry a rejection through the authenticated workflow.",
            ),
            (
                "decoded = decode_events(frame)",
                "decoded = decode_events(frame + frame)",
                "Emit each progress event once, not twice.",
            ),
            (
                'decoded[0]["data"]["node"] == case["note"]',
                'decoded[0]["event"] == case["note"]',
                "Compare the payload field after decoding, not its event category.",
            ),
        ],
        ownership="authenticated_registry",
        resume="current_interrupt_id",
        reconnect="snapshot_then_resume",
    ),
    "18-C": lab(
        "The dashboard is a projection of server events: append progress and text, replace pending approvals when a new snapshot arrives. Streamlit session state remembers the selected thread between UI reruns. Client-side controls improve usability, while the API independently rejects stale or unauthorized decisions. Beta v3 typed projections are explored in B4; this UI uses stable v2-derived SSE.",
        "Replace an outdated approval form when the desk sends a corrected one instead of keeping both forms active.",
        [{}, {"submitted_id": "current-approval"}, {"chunks": []}],
        [("value.text", "Estimate received."), ("value.can_submit", False)],
        [
            (
                'for chunk in case["chunks"]:',
                'for chunk in case["chunks"][:1]:',
                "Render every received text chunk in order.",
            ),
            (
                '"id": "current-approval", "request"',
                '"id": "old-approval", "request"',
                "Replace the stale approval identity with the current snapshot.",
            ),
            (
                'case["submitted_id"] in {item["id"] for item in state["pending"]}',
                "True",
                "Enable submission only for a currently pending interrupt.",
            ),
            (
                '"node": "review_documents"',
                '"node": "unrelated_node"',
                "Attribute displayed progress to the node that emitted it.",
            ),
        ],
        state="session_projection",
        pending="replace_on_snapshot",
        authority="server_recheck",
    ),
    "19-A": lab(
        "A pytest test is a function whose assertions express requirements. Parametrized tests run it over many inputs. Compare pure node rules and whole graphs against independently specified boundary outcomes; comparing two copies of the same implementation can preserve the same bug. Fake models make orchestration tests repeatable, not model accuracy measurable.",
        "Check a ruler against known measurements instead of checking it against a second copy of the same misprinted ruler.",
        [{}, {"amounts": [0, -1, 500000]}, {"amounts": []}],
        [("value.passed", True)],
        [
            (
                "amount <= 100000",
                "amount < 100000",
                "Specify the inclusive fast-track boundary in the test oracle.",
            ),
            (
                "type(amount) is not int",
                "not isinstance(amount, int)",
                "Include boolean cents in invalid-input coverage.",
            ),
            (
                "amount <= 500000",
                "amount < 500000",
                "Keep exactly 500000 cents in the standard route.",
            ),
            (
                'row["expected"] == row["rule"] == row["graph"]',
                'row["expected"] != row["rule"] == row["graph"]',
                "Require both implementations to match the independent expected route.",
            ),
        ],
        oracle="independent_requirements",
        levels="node_and_graph",
        inputs="boundaries_and_invalid",
    ),
    "19-B": lab(
        "Durable tests assert the state before a pause, the pending node, and the resumed result. Snapshot only stable semantic fields, not random checkpoint IDs or timestamps. Reducer algebra can be checked over many generated inputs: associativity and idempotence protect parallel and replay behavior. The process-death test in module 17 covers a failure an in-memory mock cannot reproduce.",
        "Inspect the waiting shelf before and after an approval rather than checking only the final receipt.",
        [{}, {"approved": True}, {"groups": [[], ["receipt"], ["receipt"]]}],
        [("value.paused", True), ("value.associative", True)],
        [
            (
                '"approved": case["approved"]',
                '"approved": True',
                "Test rejection as well as approval on resume.",
            ),
            (
                '"pending_before": list(before.next)',
                '"pending_before": list(graph.get_state(config).next)',
                "Capture the pre-resume pending state before it changes.",
            ),
            (
                "merge_findings(merge_findings(a, b), c)",
                "merge_findings(a, b)",
                "Include every update group when checking reducer behavior.",
            ),
            (
                '"pending_after": list(graph.get_state(config).next)',
                '"pending_after": list(before.next)',
                "Read the completed snapshot after resumption.",
            ),
        ],
        snapshot="semantic_fields",
        resume="both_decisions",
        reducer="algebraic_properties",
    ),
    "19-C": lab(
        "A trajectory is the sequence of tool requests, separate from the final answer. agentevals can compare strict order, unordered calls, subsets, or supersets. Exact argument matching catches the right tool used on the wrong policy. Choose the matching rule from the business requirement; parallel independent calls may legitimately change order.",
        "Review both the investigator's conclusion and the records they actually requested.",
        [
            {},
            {"tools": ["check_coverage", "lookup_policy"]},
            {"tools": ["check_coverage", "lookup_policy"], "mode": "unordered"},
            {"policy_id": "POL-0002"},
        ],
        [("value.score", True)],
        [
            (
                'trajectory_match_mode=case["mode"]',
                'trajectory_match_mode="unordered"',
                "Respect strict ordering when the evaluation contract requests it.",
            ),
            (
                'tool_args_match_mode="exact"',
                'tool_args_match_mode="ignore"',
                "Check the policy arguments, not only tool names.",
            ),
            (
                'messages(case["tools"], case["policy_id"])',
                'messages(case["tools"], "POL-0001")',
                "Evaluate the actual requested policy instead of replacing it with the reference.",
            ),
            (
                '"score": result["score"]',
                '"score": not result["score"]',
                "Preserve the evaluator's boolean score in the report.",
            ),
        ],
        trajectory="tool_requests",
        order="business_contract",
        arguments="exact",
    ),
    "20-A": lab(
        "langgraph.json maps a public graph name to a Python export. The local Agent Server hosts that graph; Studio adds a visual client and may require an account. Without Studio, draw_mermaid, updates, and checkpoint snapshots still reveal the route and pause. The export leaves persistence to the server instead of constructing its own competing saver.",
        "A process map and a dated case file can diagnose a wrong desk assignment even without a visual control room.",
        [
            {},
            {"amount_cents": 100000, "reported_route": "fast_track"},
            {"reported_route": "specialist"},
        ],
        [("value.export_exists", True), ("value.misrouted", True)],
        [
            (
                'config["graphs"]["claims"]',
                'config["graphs"]["missing"]',
                "Resolve the graph name declared in the server configuration.",
            ),
            (
                '"amount_cents": case["amount_cents"]',
                '"amount_cents": 0',
                "Debug the supplied claim amount rather than a substituted value.",
            ),
            (
                'result.value["route"] != case["reported_route"]',
                'result.value["route"] == case["reported_route"]',
                "Report a discrepancy only when observed and reported routes differ.",
            ),
            (
                '"approve_claim" in diagram',
                '"imaginary_node" in diagram',
                "Inspect the actual approval node in the generated graph diagram.",
            ),
        ],
        config="graph_export",
        offline="diagram_and_snapshots",
        persistence="server_owned",
    ),
    "20-B": lab(
        "Structured logs are small machine-readable records correlated by thread and run. An allowlist excludes raw prompts, contact details, and credentials rather than hoping a redactor recognizes every secret. Random run identifiers belong in operational logs but should be normalized out of teaching snapshots.",
        "A tracking slip names the case and desk, without photocopying the customer's private paperwork.",
        [{}, {"thread_id": "second-claim", "run_id": "review-2"}],
        [("value.raw_text_logged", False), ("value.credential_logged", False)],
        [
            (
                '"event": "node_finished"',
                '"event": "unknown"',
                "Use the documented event category for node completion.",
            ),
            ('"node": node', '"node": "normalize"', "Attach each log record to its actual node."),
            (
                '{**case, "event"',
                '{**case, "thread_id": "wrong-thread", "event"',
                "Retain the caller's thread correlation identifier.",
            ),
            (
                '"status": "ok"',
                '"status": "failed"',
                "Do not report a successful node as failed during logging refactors.",
            ),
        ],
        content="allowlisted_fields",
        correlation="thread_and_run",
        credentials="never_logged",
    ),
    "20-C": lab(
        "LangSmith tracing is optional and independent of checkpoint persistence. A local trace can show an old route, locate the checkpoint before routing, fork with corrected data, and retain the original history. This example explicitly disables remote tracing. Enable hosted tracing only for sanitized data and an account you intend to use.",
        "Keep the original case file and attach a corrected branch instead of erasing the disputed decision.",
        [{}, {"corrected_cents": 600000}, {"corrected_cents": 100001}],
        [("value.original_route", "specialist"), ("value.forked_route", "fast_track")],
        [
            (
                'case["corrected_cents"]',
                "600000",
                "Apply the corrected amount to the fork before resuming routing.",
            ),
            (
                '"route" in item.next',
                '"normalize" in item.next',
                "Fork at the intended pre-routing boundary.",
            ),
            (
                '"original_route": history[0].values["route"]',
                '"original_route": result.value["route"]',
                "Keep the original route distinct from the corrected branch.",
            ),
            (
                "len(list(graph.get_state_history(config))) > len(history)",
                "len(list(graph.get_state_history(config))) < len(history)",
                "Verify that branching retains and extends checkpoint history.",
            ),
        ],
        tracing="optional",
        evidence="local_checkpoints",
        correction="retained_branch",
    ),
    "21-A": lab(
        "Claim text and retrieved documents are untrusted data. A structured schema rejects extra authority fields and impossible amounts, while deterministic rules select routes. Neither a model's confidence nor a sentence saying 'approved' grants permission. Tool capabilities are independently restricted to the minimum required evidence reads.",
        "A customer's handwritten instruction cannot become an employee access badge.",
        [{}, {"extra_authority": True}, {"amount_cents": 100000}, {"amount_cents": -1}],
        [("value.payment_authorized", False), ("value.route", "specialist")],
        [
            (
                '"payment_authorized": False',
                '"payment_authorized": True',
                "Do not let extracted text authorize a payment.",
            ),
            (
                '"amount_cents": case["amount_cents"]',
                '"amount_cents": 1',
                "Preserve validated amounts before applying deterministic routing.",
            ),
            (
                'if case["extra_authority"]:',
                "if False:",
                "Expose and reject an unexpected authority field instead of silently hiding it from validation.",
            ),
            (
                '["read_synthetic_policy"]',
                '["read_synthetic_policy", "issue_payment"]',
                "Keep model-visible tool capabilities read-only.",
            ),
        ],
        text="untrusted",
        authorization="outside_model",
        schema="extra_fields_forbidden",
    ),
    "21-B": lab(
        "Admission checks reject a planned operation that exceeds the configured call or estimated-token budget. They supplement, rather than replace, runtime model/tool limits and recursion bounds. The API separately verifies role, current interrupt identity, and confirmed coverage before recording a payload-bound synthetic effect. Token estimates are conservative planning inputs, not a guaranteed hosted bill.",
        "A spending envelope limits the planned work, while an authorized signature is still required for the actual payment.",
        [
            {},
            {"approved": False},
            {"planned_calls": 13},
            {"estimated_tokens": 2001},
            {"planned_calls": True},
        ],
        [("value.effects", 1), ("value.customer_approval_status", 403)],
        [
            (
                'case["planned_calls"] > case["call_budget"]',
                "False",
                "Enforce the separate planned-call budget.",
            ),
            (
                'case["estimated_tokens"] > case["token_budget"]',
                "False",
                "Reject an operation above the token admission budget.",
            ),
            (
                'approve=case["approved"]',
                "approve=True",
                "Keep a human rejection from creating an effect.",
            ),
            (
                "type(value) is not int",
                "not isinstance(value, int)",
                "Reject boolean values masquerading as numeric budgets.",
            ),
        ],
        admission="call_and_token_limits",
        decision="authenticated_adjuster",
        effect="idempotent_ledger",
    ),
    "21-C": lab(
        "EncryptedSerializer encrypts serialized checkpoint payloads using an externally supplied key. The example creates an ephemeral key and never returns it. Minimize PII before storage; encryption does not hide every database field or replace access control, key rotation, and retention. A wrong key fails authentication, and deleting a thread is separate from deleting Store memories and backups.",
        "Lock the retained folder, keep its key outside the folder, and still follow a shredding schedule.",
        [{}, {"delete": False}, {"wrong_key": True}, {"note": "Another synthetic private note"}],
        [("value.plaintext_visible", False), ("value.checkpoint_plaintext_visible", False)],
        [
            (
                "InMemorySaver(serde=serializer)",
                "InMemorySaver()",
                "Install encryption on the actual checkpointer, not just a standalone serialization demo.",
            ),
            ('if case["delete"]:', "if False:", "Apply the requested thread-retention deletion."),
            (
                'if case["wrong_key"] else serializer',
                "if False else serializer",
                "Verify that a wrong encryption key cannot restore the payload.",
            ),
            (
                'restored["note"] == case["note"]',
                'restored["note"] != case["note"]',
                "Check exact restoration after successful authenticated decryption.",
            ),
        ],
        minimization="before_storage",
        key="external_to_state",
        retention="explicit_thread_delete",
    ),
    "22-A": lab(
        "The self-hosted stack has an API, Postgres, and a Streamlit UI. Database readiness gates API startup, and API health gates the UI. Required credentials come from the environment; published ports bind to localhost for this teaching deployment. The example validates the committed configuration, while the integration job actually starts the containers and calls the service.",
        "Open the service counter only after the archive is ready, then open the waiting room.",
        [{}, {"public_bind": True}, {"remove_healthcheck": True}],
        [("value.valid", True), ("value.services", ["api", "postgres", "ui"])],
        [
            (
                'if "healthcheck" not in services["postgres"]:',
                "if False:",
                "Reject a database without a readiness check.",
            ),
            (
                'not binding.startswith("127.0.0.1:")',
                "False",
                "Detect accidental public binding of the teaching service.",
            ),
            (
                '"valid": not errors',
                '"valid": True',
                "Do not mark a stack valid after detecting a deployment error.",
            ),
            (
                '== "service_healthy"',
                '== "service_started"',
                "Distinguish service readiness from process startup.",
            ),
        ],
        services="api_database_ui",
        startup="health_gated",
        exposure="localhost",
    ),
    "22-B": lab(
        "Stateless workers share durable checkpoints, ownership records, and effect keys. One active run may mutate a thread at a time. The local registry demonstrates lease exclusion within one process; the Postgres implementation uses a transaction-scoped advisory lock across workers. A new ledger instance proves that idempotency survives worker replacement, and conflicting payloads are rejected.",
        "Any adjuster may pick up the durable folder, but only one holds its checkout card at a time.",
        [{}, {"claim_id": "CLM-0020"}, {"changed_payload": True}],
        [("value.competing_worker_busy", True), ("value.effects", 1)],
        [
            (
                '"payment:" + case["claim_id"]',
                '"first-payment:" + case["claim_id"]',
                "Use the same business effect identity after worker replacement.",
            ),
            ("busy = True", "busy = False", "Report that a competing run was excluded."),
            (
                '+ int(case["changed_payload"])',
                "+ 0",
                "Exercise and reject idempotency-key reuse with a changed payload.",
            ),
            (
                '"effects": len(restarted.rows())',
                '"effects": 0',
                "Read the persisted effect count from the restarted worker's ledger.",
            ),
        ],
        workers="stateless",
        concurrency="one_run_per_thread",
        effects="durable_unique_keys",
    ),
    "22-C": lab(
        "An assistant selects graph configuration, a thread identifies persisted state, and a run is one execution. Agent Server supports background runs; LangSmith Deployment adds managed hosting and scheduled jobs subject to account access and current pricing. This offline request planner creates no hosted resources. The explicit SDK function requires a caller-supplied authenticated client and full graph input.",
        "A service definition, a case folder, and a work session are three different identifiers.",
        [{}, {"background": False}, {"assistant_id": ""}, {"schedule": "invalid"}],
        [("value.mode", "background")],
        [
            (
                'if not case["assistant_id"] or not case["thread_id"]:',
                "if False:",
                "Require both assistant configuration and thread identity.",
            ),
            (
                '"background" if case["background"] else "wait"',
                '"background"',
                "Keep interactive waiting distinct from background execution.",
            ),
            (
                'len(case["schedule"].split()) != 5',
                "False",
                "Reject an obviously malformed schedule before proposing a hosted job.",
            ),
            (
                '"thread_id": case["thread_id"]',
                '"thread_id": case["assistant_id"]',
                "Do not substitute assistant identity for thread identity.",
            ),
        ],
        identities="assistant_thread_run",
        hosting="explicit_account_action",
        schedule="validated_plan",
    ),
}
