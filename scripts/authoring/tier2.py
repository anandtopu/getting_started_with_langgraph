"""Authored model, tool, memory, and workflow contracts; all use local fakes."""


def lab(idea, analogy, cases, checks, faults, **design):
    return dict(
        idea=idea, analogy=analogy, cases=cases, checks=checks, faults=faults, design=design
    )


LABS = {
    "08-A": lab(
        "A model predicts text from messages; a prompt is its instruction and evidence. Structured output parses that text into a validated schema. Validation can reject an impossible amount, but cannot prove a claim is true. The deterministic router owns the decision after extraction.",
        "An intake clerk transcribes a form; a separate rulebook decides which desk receives it.",
        [
            {},
            {"amount_cents": 100000},
            {"confidence": 0.7},
            {"claim_type": "unknown"},
            {"amount_cents": True},
            {"confidence": 2},
        ],
        [("value.route", "standard")],
        [
            (
                "facts.confidence < 0.8",
                "facts.confidence < 0.0",
                "Send uncertain extractions to review.",
            ),
            (
                "facts.amount_cents <= 100000",
                "facts.amount_cents < 100000",
                "Include exactly 100000 cents in fast-track routing.",
            ),
            (
                'or facts.claim_type == "unknown"',
                "",
                "Route an unknown category to review even with high confidence.",
            ),
            (
                'return {"facts": facts.model_dump()}',
                'return {"facts": {**facts.model_dump(), "amount_cents": 1}}',
                "Preserve the validated amount across the model boundary.",
            ),
        ],
        authority="deterministic_router",
        input="untrusted_text",
        validation="strict_schema",
    ),
    "08-B": lab(
        "MessagesState applies add_messages: a matching message ID replaces a message instead of appending a duplicate. RemoveMessage deletes by that same ID. Tool responses still need the tool_call_id from their AI request; message identity and tool-call identity serve different purposes.",
        "Correct a numbered page in a folder without discarding the receipt stapled to another page.",
        [{}, {"remove_customer": False}, {"text": "Corrected: theft", "remove_customer": False}],
        [("value.paired", True), ("value.messages.0.role", "ai")],
        [
            (
                'RemoveMessage(id="customer-1")',
                'RemoveMessage(id="missing-customer")',
                "Delete by the existing message ID.",
            ),
            (
                'HumanMessage(content=case["text"], id="customer-1")',
                'HumanMessage(content=case["text"], id="customer-2")',
                "Correct an existing message without appending another customer message.",
            ),
            (
                'if case["remove_customer"] else {}',
                "if True else {}",
                "Make retention conditional on the requested minimization policy.",
            ),
            (
                'content=case["text"]',
                'content="Original claim"',
                "Keep the corrected text when replacing a message.",
            ),
        ],
        identity="stable_message_id",
        pairing="tool_call_id",
        retention="explicit_removal",
    ),
    "08-C": lab(
        "The messages stream emits a chunk and metadata inside each v2 part's data field. Assemble content in order and inspect langgraph_node to attribute it. A fake should agree between invoke and stream, including a structured JSON response; it tests orchestration, not model quality.",
        "Reassemble numbered delivery envelopes before reading the complete letter.",
        [
            {},
            {"text": "Estimate received."},
            {
                "text": '{"claim_type":"water","amount_cents":50,"confidence":0.9}',
                "structured": True,
            },
            {"text": "invalid", "structured": True},
        ],
        [("value.matches_invoke", True), ("value.nodes", ["acknowledge"])],
        [
            (
                'text = "".join(chunks)',
                'text = " ".join(chunks)',
                "Join chunks without inserting characters that were never emitted.",
            ),
            (
                'metadata["langgraph_node"]',
                'metadata["missing_node"]',
                "Read the documented node name from stream metadata.",
            ),
            (
                'if case["structured"] else None',
                "if False else None",
                "Validate the fully assembled structured response.",
            ),
            (
                "chunks.append(chunk.content)",
                "chunks.insert(0, chunk.content)",
                "Preserve emission order while collecting token chunks.",
            ),
        ],
        format="v2_parts",
        validation="after_assembly",
        cost="fake_zero",
    ),
    "09-A": lab(
        "A tool's typed parameters become a schema the model can request. ToolNode runs the requested function and returns a ToolMessage with the original call ID. Expected lookup failures become error messages when error handling is enabled. A payout calculator proposes cents; it does not transfer money.",
        "A requisition number must remain attached to its completed work order.",
        [{}, {"policy_id": "MISSING"}, {"amount_cents": 0}, {"amount_cents": 500000}],
        [("value.results.0.content", "25000")],
        [
            (
                "calculate_payout(amount_cents, 200000, 100000)",
                "calculate_payout(amount_cents, 200000, 0)",
                "Apply the deductible before proposing a payout.",
            ),
            (
                "handle_tool_errors=True",
                "handle_tool_errors=False",
                "Return a correlated tool error for an unknown policy.",
            ),
            (
                "calculate_payout(amount_cents, 200000, 100000)",
                "calculate_payout(amount_cents, 900000, 100000)",
                "Cap the proposal at the synthetic coverage limit.",
            ),
            (
                '"call_id": message.tool_call_id',
                '"call_id": message.name',
                "Preserve the call identity rather than substituting the tool name.",
            ),
        ],
        tool_access="read_only",
        money="integer_cents",
        errors="correlated_results",
    ),
    "09-B": lab(
        "A manual agent loop alternates a model node and ToolNode. tools_condition checks the newest AI message: tool calls continue the loop, a final answer ends it. A recursion budget catches nontermination, but does not authorize tool effects or guarantee a useful answer.",
        "The investigator requests one record, reads the result, and then writes a conclusion.",
        [{}, {"policy_id": "MISSING"}, {"recursion_limit": 1}],
        [("value.roles", ["human", "ai", "tool", "ai"])],
        [
            (
                'graph.add_edge("tools", "call_model")',
                'graph.add_edge("tools", END)',
                "Return tool evidence to the model before ending.",
            ),
            (
                "handle_tool_errors=True",
                "handle_tool_errors=False",
                "Let the agent observe a policy lookup failure.",
            ),
            ('case["recursion_limit"]', "100", "Respect the caller's execution budget."),
            (
                '"args": {"policy_id": policy_id}',
                '"args": {"policy_id": "MISSING"}',
                "Preserve the requested policy when constructing tool arguments.",
            ),
        ],
        loop="model_tools_model",
        stop="no_tool_calls",
        authority="outside_model",
    ),
    "09-C": lab(
        "ToolRuntime injects trusted context, graph state, the Store, and tool_call_id without exposing them as model-selectable fields. A tool returning Command can update graph state and acknowledge its own request. Customer identity belongs in authenticated context, not in an argument the model invents.",
        "An employee badge determines the filing cabinet; the form only chooses the contact preference.",
        [{}, {"customer_id": "CUS-0020", "preference": "sms"}, {"preference": "fax"}],
        [("value.saved.value", "email"), ("value.model_visible_fields", ["preference"])],
        [
            (
                'runtime.context.customer_id, "preferences"',
                '"CUS-OTHER", "preferences"',
                "Write only in the trusted customer namespace.",
            ),
            (
                '"saved_preference": preference',
                '"saved_preference": "phone"',
                "Keep the graph state consistent with the Store write.",
            ),
            (
                '{"email", "sms", "phone"}',
                '{"email", "phone"}',
                "Support the declared SMS contact preference.",
            ),
            (
                "tool_call_id=runtime.tool_call_id",
                'tool_call_id="unrelated-call"',
                "Acknowledge the tool request using its injected identity.",
            ),
        ],
        identity="trusted_context",
        state="Command_update",
        namespace="customer_scoped",
    ),
    "10-A": lab(
        "create_agent builds a standard model/tool loop on LangGraph. Start there for ordinary tool use; use a custom StateGraph when the business process requires explicit gates or branches. The compiled agent still accepts state, can be inspected as a graph, and emits normal messages.",
        "Use a standard service desk until the claim process needs a specially arranged sequence of desks.",
        [{}, {"policy_id": "MISSING"}],
        [("value.roles", ["human", "ai", "tool", "ai"]), ("value.tools", ["lookup_policy"])],
        [
            (
                "tools=[lookup_policy]",
                "tools=[]",
                "Register the requested tool with the prebuilt agent.",
            ),
            (
                'if policy_id != "POL-0001":',
                'if policy_id == "POL-0001":',
                "Reject unknown policy IDs, not the known fixture.",
            ),
            (
                '"args": {"policy_id": policy_id}',
                '"args": {"policy_id": "POL-0001"}',
                "Pass through the requested policy instead of silently substituting another.",
            ),
            (
                '"final": value["messages"][-1].content',
                '"final": value["messages"][0].content',
                "Expose the final agent answer rather than the original question.",
            ),
        ],
        abstraction="create_agent",
        escape_hatch="explicit_graph",
        effects="none",
    ),
    "10-B": lab(
        "Middleware hooks surround agent operations. before_model can update declared middleware state; wrap_model_call controls the handler; after_model observes the result. Model and tool budgets are separate: limiting one does not automatically limit the other. Hook order belongs in an explicit test.",
        "A supervisor records entry and exit at each desk and separately counts external requests.",
        [{}, {"model_limit": 1}, {"tool_limit": 0}],
        [("value.model_calls", 2), ("value.tool_calls", 1)],
        [
            (
                "run_limit=model_limit",
                "run_limit=1",
                "Allow the configured number of model operations.",
            ),
            ("run_limit=tool_limit", "run_limit=100", "Enforce the independent tool budget."),
            (
                'self.events.append("after_model")',
                'self.events.append("before_model")',
                "Distinguish the after hook from the before hook in lifecycle records.",
            ),
            (
                "response = handler(request)",
                'response = handler(request)\n        self.events.append("wrap_enter")',
                "Record exactly one wrapper entry for each model call.",
            ),
        ],
        budgets="model_and_tool",
        hooks="ordered",
        state="declared_schema",
    ),
    "10-C": lab(
        "An adapter node converts a business question into private agent messages and returns only the public explanation. The parent retains claim identity and its own process status. Sharing every internal message is convenient but widens the context and privacy boundary unnecessarily.",
        "A specialist sends a signed conclusion back to intake, not the entire scratch notebook.",
        [{}, {"claim_id": "CLM-0099", "question": "Which estimate is needed?"}],
        [("value.status", "awaiting_evidence")],
        [
            (
                'return {"explanation": result.value["messages"][-1].content}',
                "return {}",
                "Map the specialist answer into the parent explanation field.",
            ),
            (
                '"awaiting_evidence"',
                '"approved"',
                "Do not turn an explanation into payment approval.",
            ),
            (
                'result.value["messages"][-1].content',
                'result.value["messages"][0].content',
                "Select the specialist answer rather than its input question.",
            ),
            (
                'graph.add_edge("explain", "finalize")',
                'graph.add_edge("explain", END)',
                "Preserve the parent finalization step when refactoring the adapter.",
            ),
        ],
        parent="business_state",
        child="private_messages",
        output="explicit_adapter",
    ),
    "11-A": lab(
        "Checkpoint history and model context are different collections. Trimming chooses a bounded view for one call without deleting the saved conversation. A summarization node retains a short factual digest; in this small example it joins customer statements deterministically. Production summaries need factual evaluation and a token counter appropriate to the model.",
        "Keep the complete archive while giving the next adjuster a short briefing sheet.",
        [{}, {"max_messages": 4}, {"second_text": "A contractor supplied photos."}],
        [("value.saved_messages", 4), ("value.model_context_sizes", [1, 2])],
        [
            ("max_tokens=max_messages", "max_tokens=100", "Bound the messages sent to the model."),
            (
                'id="human-2"',
                'id="human-1"',
                "Use a new message ID for a new turn instead of overwriting the previous turn.",
            ),
            (
                '" | ".join(facts[-2:])',
                '" | ".join(facts[:1])',
                "Include newly supplied evidence in the summary.",
            ),
            (
                'graph.add_edge("respond", "summarize")',
                'graph.add_edge("respond", END)',
                "Retain the summarization step after responding.",
            ),
        ],
        archive="checkpoints",
        context="trimmed_view",
        summary="factual_digest",
    ),
    "11-B": lab(
        "The Store holds cross-thread memories under tuple namespaces. Semantic memory stores facts, episodic memory stores events, and procedural memory stores instructions; these are application conventions rather than special database types. Customer-scoped namespaces must be enforced from trusted context. Deleting a memory is an explicit operation.",
        "Separate facts, visit notes, and approved procedures into labeled drawers, with one cabinet per customer.",
        [{}, {"customer_id": "CUS-0033", "preference": "sms"}],
        [("value.deleted", True), ("value.other.preference", "phone")],
        [
            (
                'runtime.context.customer_id, "semantic"',
                '"shared", "semantic"',
                "Store each customer's facts in a distinct namespace.",
            ),
            (
                'store.delete(namespace, "contact")',
                'store.delete(namespace, "missing")',
                "Delete the actual memory key.",
            ),
            (
                '{"preference": state["preference"]}',
                '{"preference": "phone"}',
                "Remember the supplied contact preference.",
            ),
            (
                'context=Context("CUS-OTHER")',
                'context=Context(case["customer_id"])',
                "Keep another customer's update outside this customer's namespace.",
            ),
        ],
        categories="semantic_episodic_procedural",
        scope="customer",
        deletion="explicit",
    ),
    "11-C": lab(
        "An embedding maps text into numbers so the Store can rank similarity within a namespace. These transparent word vectors make the offline ranking reproducible. Store deletion does not delete old checkpoint contents: retention must handle both systems separately. Retrieval is evidence selection, never an authorization check.",
        "A catalog search locates related folders; shredding a catalog card does not shred archived copies.",
        [{}, {"query": "theft"}, {"query": "unrelated", "customer_id": "CUS-0040"}],
        [("value.ranking", ["water", "theft"]), ("value.checkpoint_deleted_separately", True)],
        [
            (
                'store.search(namespace, query=case["query"], limit=2)',
                'store.search(("customers",), query=case["query"], limit=2)',
                "Scope semantic search to the authenticated customer.",
            ),
            (
                'saver.delete_thread("retention-demo")',
                'saver.delete_thread("wrong-thread")',
                "Delete checkpoint history separately from Store records.",
            ),
            (
                'store.delete(namespace, "water")',
                'store.delete(namespace, "theft")',
                "Delete the requested memory while preserving unrelated evidence.",
            ),
            (
                "-(item.score or 0)",
                "(item.score or 0)",
                "Rank the highest similarity first with a stable tie-breaker.",
            ),
        ],
        retrieval="namespace_then_similarity",
        retention="store_and_checkpoints",
        embeddings="deterministic_teaching_vectors",
    ),
    "12-A": lab(
        "Prompt chaining fixes the order of model operations. A deterministic gate compares extracted facts with the authoritative policy before allowing a draft. The validated category can route work, but a model cannot override the gate. A blocked extraction should not consume a drafting call.",
        "Verify the measurements before asking the writer to prepare a settlement letter.",
        [
            {},
            {"category": "documents"},
            {"extracted_deductible": 90000},
            {"category": "approve"},
            {"extracted_deductible": True},
        ],
        [("value.accepted", True)],
        [
            (
                'state["extracted_deductible"] == case["policy_deductible"]',
                "True",
                "Reject contradictory extracted facts before drafting.",
            ),
            (
                '"draft" if state["accepted"] else END',
                '"draft"',
                "Stop the chain when the fact gate fails.",
            ),
            (
                'Literal["policy", "documents"]',
                "str",
                "Validate the routing category against an explicit allowlist.",
            ),
            (
                '"deductible_cents": case["policy_deductible"]',
                '"deductible_cents": 0',
                "Keep the drafted deductible tied to the authoritative policy.",
            ),
        ],
        order="classify_gate_draft",
        authority="policy_record",
        stop="failed_gate",
    ),
    "12-B": lab(
        "An orchestrator proposes a structured plan, then Send creates one worker invocation per section. Validate allowed section names, uniqueness, and size before fan-out. The reducer accumulates independent reports and a deferred assembler produces a canonical order rather than relying on worker completion timing.",
        "An editor assigns each approved section once and assembles the returned pages by heading.",
        [
            {},
            {"sections": []},
            {"sections": ["deductible"]},
            {"sections": ["coverage", "coverage"]},
            {"sections": ["payments"]},
        ],
        [("value.model_calls", 4), ("value.sections", ["coverage", "deductible", "exclusions"])],
        [
            (
                "operator.add]",
                "lambda old, new: new]",
                "Accumulate every worker result instead of overwriting sibling reports.",
            ),
            (
                "if len(value) != len(set(value)):",
                "if False:",
                "Reject a plan that delegates the same section twice.",
            ),
            (
                'key=lambda item: item["section"]',
                'key=lambda item: item["text"]',
                "Assemble reports by stable section identity.",
            ),
            (
                'for section in state["sections"]',
                'for section in state["sections"][:1]',
                "Run every approved worker in the plan.",
            ),
        ],
        plan="bounded_validated",
        work="Send",
        assembly="canonical_order",
    ),
    "12-C": lab(
        "The evaluator names concrete factual and tone defects; the optimizer receives that feedback before another draft. Stop on success or a strict attempt budget. A deterministic substring check is deliberately limited: it teaches loop control and must not be mistaken for a production factuality evaluator.",
        "A letter editor returns a short checklist, but has a fixed number of revision rounds.",
        [
            {},
            {"budget": 1},
            {"drafts": ["Wrong amount."], "budget": 2},
            {"drafts": ["Thank you. Your deductible is 100000 cents."]},
            {"budget": 0},
        ],
        [("value.accepted", True), ("value.attempts", 2)],
        [
            (
                'state["attempts"] >= state["budget"]',
                "False",
                "Stop unsuccessful revision at the configured budget.",
            ),
            (
                '"100000 cents" not in state["draft"]',
                "False",
                "Require the authoritative deductible fact.",
            ),
            (
                '"thank" not in state["draft"].lower()',
                "False",
                "Keep the respectful-tone criterion separate from the factual criterion.",
            ),
            (
                'state["accepted"] or state["attempts"]',
                'False or state["attempts"]',
                "Stop immediately once both criteria pass.",
            ),
        ],
        feedback="specific_criteria",
        stop="success_or_budget",
        evaluation="local_and_limited",
    ),
}
