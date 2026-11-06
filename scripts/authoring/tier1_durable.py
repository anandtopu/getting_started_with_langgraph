"""Authored loop, persistence, interrupt, and streaming exercise contracts."""

LABS = {
    "04-A": {
        "idea": "A loop is an edge back to earlier work. Business state must move toward an exit. recursion_limit is a runtime backstop measured in graph steps, not a replacement for a document-recheck budget.",
        "analogy": "A clerk can request missing evidence three times; the building's emergency stop is a different control.",
        "cases": [
            {},
            {"history": [True]},
            {"history": [False], "budget": 2},
            {"budget": 0},
            {"history": [False] * 8, "budget": 8, "recursion_limit": 3},
        ],
        "checks": [("value.attempts", 3), ("value.status", "ready")],
        "faults": [
            (
                'index < len(state["history"]) and state["history"][index]',
                "False",
                "Received evidence must terminate the recheck loop.",
            ),
            (
                '"attempts": index + 1',
                '"attempts": index',
                "Without a changing retry counter, the graph reaches its recursion limit.",
            ),
            (
                'exhausted = index + 1 >= state["budget"]',
                "exhausted = False",
                "The business budget needs an explicit exhausted outcome.",
            ),
            (
                'index + 1 >= state["budget"]',
                'index >= state["budget"]',
                "Equivalent loops must preserve the exact attempt budget.",
            ),
        ],
        "design": {
            "business_exit": "ready_or_budget_exhausted",
            "runtime_guard": "recursion_limit",
            "progress": "increment_attempts",
        },
    },
    "04-B": {
        "idea": "Send creates one worker invocation per item with its own input. Parallel workers need a reducer when they write the same channel. defer waits for pending work, which matters when one branch takes more steps than another.",
        "analogy": "An adjuster collects reports from several specialists and signs only after the slowest specialist finishes.",
        "cases": [
            {},
            {"documents": []},
            {"documents": [{"id": "DOC-Z", "kind": "estimate"}]},
            {
                "documents": [
                    {"id": "DOC-Z", "kind": "police"},
                    {"id": "DOC-A", "kind": "receipt"},
                    {"id": "DOC-B", "kind": "police"},
                ]
            },
        ],
        "checks": [("value.summaries", [["DOC-001", "DOC-021"]])],
        "faults": [
            (
                'return {"findings": [state["document"]["id"]]}',
                'return {"findings": []}',
                "Each worker must contribute its own document evidence.",
            ),
            (
                "findings: Annotated[list[str], operator.add]",
                "findings: list[str]",
                "Parallel writes to an overwrite channel conflict.",
            ),
            ("defer=True", "defer=False", "The deeper police branch must finish before summary."),
            (
                'sorted(state["findings"])',
                'state["findings"]',
                "Do not treat arrival order as the public result order.",
            ),
        ],
        "design": {
            "workers": "one_send_per_document",
            "findings": "reducer",
            "summary": "deferred",
        },
    },
    "04-C": {
        "idea": "Retry a transient failure only when repeating the operation is safe. A cache stores a node result under a key; the key must include every input that changes that result. TTL expires a result after a duration, and an injected clock makes that behavior testable without sleeping.",
        "analogy": "A policy lookup card belongs to a customer and policy version, not just the shelf where it was found.",
        "cases": [
            {},
            {"advance": 0},
            {"amount_cents": 300000},
            {"policy_version": 2},
            {"customer_id": "CUS-0003"},
        ],
        "checks": [("value.covered", [True, True, True, False]), ("value.lookup_calls", 4)],
        "faults": [
            (
                "max_attempts=2",
                "max_attempts=1",
                "A bounded retry must recover from the injected transient read failure.",
            ),
            (
                '[state["customer_id"], state["policy_version"], state["amount_cents"]]',
                '[state["policy_version"], state["amount_cents"]]',
                "Customer identity belongs in the cache key.",
            ),
            (
                "ClockCache(lambda: clock[0])",
                "ClockCache(lambda: 0)",
                "The cache must observe the injected clock advancing.",
            ),
            (
                "ttl=ttl",
                "ttl=None",
                "A refactor must preserve expiration, not silently make cached results permanent.",
            ),
        ],
        "design": {
            "policy_read": "retry_and_scoped_cache",
            "payout_write": "idempotency_before_retry",
            "ttl_test": "injected_clock",
        },
    },
    "05-A": {
        "idea": "A checkpointer saves graph state under a thread ID. New input on that thread starts another run against its saved state. Resuming a pending operation is different: use the saved continuation or an interrupt response rather than pretending it is a new claim.",
        "analogy": "The thread ID is the claim-folder number; reuse another customer's number and you open the wrong folder.",
        "cases": [{}, {"first_id": "CLM-A", "second_id": "CLM-B"}],
        "checks": [
            ("value.first_notes", ["received", "estimate attached"]),
            ("value.second_notes", ["other customer"]),
        ],
        "faults": [
            (
                "checkpointer=InMemorySaver()",
                "checkpointer=None",
                "Saved notes must survive a second invocation on the same graph.",
            ),
            (
                '{"thread_id": "claim:" + claim_id}',
                "{}",
                "A persisted invocation needs an explicit thread identifier.",
            ),
            (
                '"claim:" + claim_id',
                '"claim:shared"',
                "Claim identity must participate in the thread mapping.",
            ),
            (
                "notes: Annotated[list[str], operator.add]",
                "notes: list[str]",
                "Continuing a session must not discard earlier notes.",
            ),
        ],
        "design": {
            "thread": "stable_claim_id",
            "new_input": "continue_saved_state",
            "scope": "one_claim",
        },
    },
    "05-B": {
        "idea": "Memory persistence ends with its process. A SQLite saver stores checkpoints on disk and must remain open for every invocation that uses it. Explicit context managers release connections, including on Windows where open files can prevent cleanup.",
        "analogy": "A desk notebook disappears with the desk; a closed archive file can be reopened by the next shift.",
        "cases": [{}, {"claim_id": "CLM-0199"}],
        "checks": [
            ("value.second_notes", ["received", "estimate attached"]),
            ("value.closed", True),
        ],
        "faults": [
            (
                "notes: Annotated[list[str], operator.add]",
                "notes: list[str]",
                "A restarted process must merge the new note with stored notes.",
            ),
            (
                'with SqliteSaver.from_conn_string(database) as saver:\n        result = build_graph(saver).invoke(payload, config, version="v2").value',
                'with SqliteSaver.from_conn_string(database) as saver:\n        graph = build_graph(saver)\n    result = graph.invoke(payload, config, version="v2").value',
                "A compiled graph cannot use a saver whose connection has closed.",
            ),
            (
                '{"thread_id": claim_id}',
                '{"thread_id": claim_id + phase}',
                "Both processes must reopen the same logical claim thread.",
            ),
            (
                '"estimate attached"',
                '"received"',
                "Resource-lifetime refactoring must preserve continuation input.",
            ),
        ],
        "design": {
            "lifetime": "context_encloses_invoke",
            "restart": "same_database_and_thread",
            "cleanup": "close_before_rename",
        },
    },
    "05-C": {
        "idea": "A StateSnapshot contains values, pending next nodes, metadata, and a parent configuration. update_state writes a new checkpoint; it does not edit old history. Durability chooses when checkpoint writes complete, which changes failure exposure rather than business routing.",
        "analogy": "Correct an audit ledger by adding a new entry with a parent reference instead of erasing an old entry.",
        "cases": [
            {},
            {"amount_cents": 200000, "corrected_amount": 50000},
            {"durability": "async"},
            {"durability": "exit"},
        ],
        "checks": [
            ("value.original", "fast_track"),
            ("value.corrected", "standard"),
            ("value.pending_after_edit", ["decide"]),
        ],
        "faults": [
            (
                'case["corrected_amount"]',
                'case["amount_cents"]',
                "The corrected checkpoint must contain the replacement evidence.",
            ),
            (
                'graph.invoke(None, corrected, version="v2")',
                'graph.invoke(None, history[-1].config, version="v2")',
                "Continue the configuration returned by update_state, not an unrelated checkpoint.",
            ),
            (
                'as_node="normalize"',
                'as_node="decide"',
                "The edit attribution determines the pending successor nodes.",
            ),
            (
                'sorted(item.metadata["step"] for item in history)',
                '[item.metadata["step"] for item in history]',
                "Present logical step order explicitly instead of relying on history arrival order.",
            ),
        ],
        "design": {
            "draft": "async_with_documented_risk",
            "approval": "sync",
            "history": "parent_links_and_steps",
        },
    },
    "06-A": {
        "idea": "interrupt pauses graph work and returns a request to the caller. A checkpointer and stable thread preserve that pause. Command(resume=...) supplies the response; the interrupted node restarts, so validate the response rather than trusting its shape.",
        "analogy": "Put the claim in an approval tray, retaining its folder number, then continue when the adjuster returns a signed decision.",
        "cases": [
            {},
            {"decision": {"approved": False}},
            {"decision": {"approved": "yes"}},
            {"amount_cents": 1000000},
        ],
        "checks": [("value.status", "approved"), ("value.remaining", 0)],
        "faults": [
            (
                '"approved" if response["approved"] else "rejected"',
                '"approved"',
                "A rejected proposal must not become an approved result.",
            ),
            (
                "checkpointer=InMemorySaver()",
                "checkpointer=None",
                "An interrupt needs persistence to resume the saved task.",
            ),
            (
                'type(response.get("approved")) is not bool',
                "False",
                "Only a validated boolean authorizes this synthetic decision.",
            ),
            (
                'Command(resume=case["decision"])',
                'Command(resume={"approved": False})',
                "Replacing a callback must preserve the actual human response.",
            ),
        ],
        "design": {
            "pause": "persisted_interrupt",
            "response": "strict_boolean",
            "identity": "trusted_context",
        },
    },
    "06-B": {
        "idea": "Parallel pauses can be answered with an interrupt-ID-to-response map. IDs identify requests; list order does not. Validate each edited value against its own schema and business limit before merging it into state.",
        "analogy": "Return two forms using their tracking numbers instead of assuming they arrived in desk order.",
        "cases": [
            {},
            {"approved_cents": 0},
            {"approved_cents": 500001},
            {"loss_date": "invalid"},
            {"approved_cents": True},
        ],
        "checks": [
            ("value.prompts", ["approved_cents", "loss_date"]),
            ("value.result.approved_cents", 125000),
        ],
        "faults": [
            (
                "0 <= response <= 500000",
                "0 < response <= 500000",
                "A zero approved amount is a valid edited decision.",
            ),
            (
                'case[item.value["kind"]]',
                'case["loss_date"]',
                "Each interrupt must receive the response for its own request kind.",
            ),
            (
                "type(response) is not int",
                "not isinstance(response, int)",
                "Python booleans must not pass an integer money check.",
            ),
            (
                "date.fromisoformat(response).isoformat()",
                "response",
                "Date input must be validated before becoming graph state.",
            ),
        ],
        "design": {
            "response_address": "interrupt_id",
            "amount": "bounded_integer_cents",
            "date": "iso_date_validation",
        },
    },
    "06-C": {
        "idea": "On resume, Python starts the interrupted node again. Code before interrupt can therefore repeat. Move effects after validated approval into separate checkpointed work, and use a stable idempotency key because a crash can occur after a write but before its checkpoint.",
        "analogy": "A clerk rereads the form after approval; rereading must not send a second payment notice.",
        "cases": [{}, {"approved": False}, {"claim_id": "CLM-0041"}, {"approved": "yes"}],
        "checks": [("value.entries", 2), ("value.before_approval", 0), ("value.notifications", 1)],
        "faults": [
            (
                'if state["approved"]:',
                "if True:",
                "Rejection must not trigger the synthetic notification.",
            ),
            (
                'entries.append("review")',
                'entries.append("review")\n        notifications[str(len(entries))] = "Premature notification"',
                "Effects before interrupt repeat when the node restarts.",
            ),
            ("type(decision) is not bool", "False", "Truthiness is not validated approval."),
            (
                'notifications.setdefault(key, "Synthetic approval notification")',
                'notifications.setdefault(key, "Synthetic approval notification")\n            notifications[key + ":duplicate"] = "Duplicate"',
                "Separate checkpointed work still needs an idempotent effect contract.",
            ),
        ],
        "design": {
            "before_pause": "no_effect",
            "after_approval": "separate_node",
            "write": "stable_idempotency_key",
        },
    },
    "07-A": {
        "idea": "A checkpoint configuration identifies a historical state. Replaying it reruns later work; it does not merely print an old answer. update_state with as_node forks from that checkpoint and schedules its successors. Approval encountered again is requested again.",
        "analogy": "Copy the case file at a chosen revision, attach corrected evidence, and send the copy through review.",
        "cases": [{}, {"amount_cents": 200000, "corrected_amount": 50000}],
        "checks": [
            ("value.original_route", "fast_track"),
            ("value.fork_route", "specialist"),
            ("value.original_unchanged", True),
        ],
        "faults": [
            (
                'case["corrected_amount"]',
                'case["amount_cents"]',
                "A fork must contain the corrected evidence.",
            ),
            (
                'graph.invoke(None, fork_config, version="v2")',
                'graph.invoke(None, historical.config, version="v2")',
                "Replay the new fork configuration, not its uncorrected parent.",
            ),
            (
                "graph.update_state(\n        historical.config,",
                "graph.update_state(\n        config,",
                "Parentage must identify the selected historical evidence.",
            ),
            (
                'graph.invoke(None, historical.config, version="v2")',
                'graph.invoke(None, original_config, version="v2")',
                "Replaying a completed checkpoint is different from rerunning pending review.",
            ),
        ],
        "design": {
            "source": "selected_checkpoint",
            "edit": "new_checkpoint",
            "approval": "renewed_on_replay",
        },
    },
    "07-B": {
        "idea": "A v2 stream part has type, ns, and data fields. Updates contain a node's changed fields; values contain the visible whole state; custom events carry application progress. Interrupt metadata is separate from ordinary values and must survive UI serialization.",
        "analogy": "Keep the receipt log, the current folder, and the clerk's progress announcement in separate columns.",
        "cases": [{}, {"review": True}, {"claim_id": "CLM-0040"}],
        "checks": [],
        "faults": [
            (
                '"type": part["type"]',
                '"type": "updates"',
                "A consumer must preserve the event mode.",
            ),
            (
                'part["data"].get("status", "input")',
                'part.get("status", "input")',
                "The state payload is inside data, not at the envelope root.",
            ),
            (
                'len(part.get("interrupts", ()))',
                "0",
                "Values events must retain interrupt information.",
            ),
            (
                'result["phase"] = part["data"]["phase"]',
                'result["phase"] = "unknown"',
                "A unified dispatcher must preserve custom progress payloads.",
            ),
        ],
        "design": {
            "updates": "node_deltas",
            "values": "whole_state",
            "interrupts": "separate_metadata",
        },
    },
    "07-C": {
        "idea": "A subgraph namespace identifies nested work. Sibling parallel events can arrive in either order; causal requirements, such as summary after both checks, are stable. A live event trace is not itself the durable checkpoint history.",
        "analogy": "Two inspectors can report in either order, but the adjuster signs after both reports arrive.",
        "cases": [{}, {"claim_id": "CLM-0101"}],
        "checks": [("value.summary_last", True)],
        "faults": [
            ("subgraphs=True", "subgraphs=False", "Nested updates require subgraph streaming."),
            ('if not part["ns"]', 'if part["ns"]', "Keep parent and child scopes distinct."),
            (
                'segment.split(":")[0]',
                "segment",
                "Group by stable scope names while retaining raw IDs separately when needed.",
            ),
            (
                "sorted(value) for key, value in sorted(groups.items())",
                "list(reversed(sorted(value))) for key, value in sorted(groups.items())",
                "Canonical event reports need an explicit presentation order.",
            ),
        ],
        "design": {
            "siblings": "unordered_within_superstep",
            "summary": "after_both_checks",
            "history": "checkpoints_not_events",
        },
    },
}
