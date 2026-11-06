"""Real feature additions for Extend tasks whose baseline does not contain the feature."""

import ast


def replace_function(source: str, name: str, body: str) -> str:
    node = next(
        item
        for item in ast.parse(source).body
        if isinstance(item, ast.FunctionDef) and item.name == name
    )
    lines = source.splitlines(keepends=True)
    lines[node.lineno - 1 : node.end_lineno] = [body.strip() + "\n"]
    return "".join(lines)


def extend(group: str, source: str):
    """Return solution, starter, extra input overrides, and the feature contract."""
    if group == "01-A":
        function = 'def normalize_contact(state: State) -> dict:\n    return {"contact": str(state.get("contact", "email")).strip().lower()}\n\n'
        source = source.replace("def build_graph", function + "def build_graph")
        source = source.replace(
            'builder.add_edge("normalize_amount", END)',
            'builder.add_node("normalize_contact", normalize_contact)\n    builder.add_edge("normalize_amount", "normalize_contact")\n    builder.add_edge("normalize_contact", END)',
        )
        broken = source.replace(
            'str(state.get("contact", "email")).strip().lower()', 'state.get("contact", "email")'
        )
        return (
            source,
            broken,
            [{"contact": " SMS "}, {"contact": " Email "}],
            "Add a contact-normalization node without erasing claim identity.",
        )
    if group == "01-B":
        source = source.replace(
            "    steps: list[str]", "    steps: list[str]\n    receipt_number: str"
        )
        function = 'def issue_receipt(state: State) -> dict:\n    return {"receipt_number": "RCPT-" + state["claim_id"], "steps": [*state["steps"], "receipt"]}\n\n'
        source = source.replace("def build_graph", function + "def build_graph")
        source = source.replace(
            'graph.add_edge("acknowledge", END)',
            'graph.add_node("issue_receipt", issue_receipt)\n    graph.add_edge("acknowledge", "issue_receipt")\n    graph.add_edge("issue_receipt", END)',
        )
        broken = source.replace(
            'graph.add_edge("acknowledge", "issue_receipt")', 'graph.add_edge("acknowledge", END)'
        )
        return (
            source,
            broken,
            [{"claim_id": "CLM-0088"}],
            "Connect the receipt-number node after acknowledgment and before termination.",
        )
    if group == "01-C":
        source = source.replace(
            "    acknowledged: bool", "    acknowledged: bool\n    eligible: bool"
        )
        source = source.replace(
            "def build_graph",
            'def check_eligibility(state: State) -> dict:\n    return {"eligible": state["valid"] and bool(state["claim_id"])}\n\ndef build_graph',
        )
        source = source.replace(
            'graph.add_edge("validate", "acknowledge")',
            'graph.add_node("check_eligibility", check_eligibility)\n    graph.add_edge("validate", "check_eligibility")\n    graph.add_edge("check_eligibility", "acknowledge")',
        )
        broken = source.replace('state["valid"] and bool(state["claim_id"])', "True")
        return (
            source,
            broken,
            [{"claim_id": ""}],
            "Add an eligibility node and verify both its diagram connection and runtime update.",
        )
    if group == "02-A":
        source = source.replace(
            "    status: str\n", "    status: str\n    loss_date: str | None\n", 1
        )
        source = source.replace(
            '    status: str = "received"',
            '    status: str = "received"\n    loss_date: str | None = None',
        )
        source = source.replace(
            'return {"status": "validated"}',
            'return {"status": "validated", "loss_date": values.get("loss_date")}',
        )
        broken = source.replace("    loss_date: str | None = None", "", 1)
        return (
            source,
            broken,
            [
                {"kind": "dataclass", "loss_date": "2026-02-01"},
                {"kind": "typed", "loss_date": None},
            ],
            "Preserve an optional loss date and its None default across all three schema styles.",
        )
    if group == "02-C":
        source = source.replace("AnyMessage, HumanMessage", "AIMessage, AnyMessage, HumanMessage")
        source = replace_function(
            source,
            "correct_message",
            """def correct_message(state: Internal) -> dict:
    return {"messages": [
        HumanMessage(content=state["text"].strip(), id="customer-1"),
        AIMessage(content="We received your claim and will review the evidence.", id="receipt-1"),
    ]}""",
        )
        broken = source.replace(
            '"We received your claim and will review the evidence."', 'state["private_notes"]'
        )
        return (
            source,
            broken,
            [],
            "Append a customer-safe explanation without exposing internal notes or duplicating the original message.",
        )
    if group == "03-A":
        source = source.replace(
            'return "needs_information"',
            'return "needs_information"\n    if state["claim_type"] == "jewelry":\n        return "jewelry_specialist"',
        )
        source = source.replace("destinations = [", 'destinations = ["jewelry_specialist", ')
        broken = source.replace('return "jewelry_specialist"', 'return "specialist"')
        return (
            source,
            broken,
            [{"claim_type": "jewelry", "amount_cents": 50000}],
            "Add a distinct jewelry-specialist path while preserving amount and missing-evidence guards.",
        )
    if group == "06-A":
        source = source.replace(
            "from langgraph.checkpoint.memory",
            "from langchain_core.runnables import RunnableConfig\nfrom langgraph.checkpoint.memory",
        )
        source = source.replace("    status: str", "    status: str\n    approved_by: str")
        source = replace_function(
            source,
            "review",
            """def review(state: State, config: RunnableConfig) -> dict:
    response = interrupt({"kind": "payout_review", "amount_cents": state["amount_cents"]})
    adjuster = config["configurable"]["adjuster_id"]
    if adjuster not in {"ADJ-001", "ADJ-002"}:
        raise PermissionError("The trusted session is not an authorized adjuster")
    if not isinstance(response, dict) or type(response.get("approved")) is not bool:
        raise ValueError("Approval must contain an approved boolean")
    return {"status": "approved" if response["approved"] else "rejected", "approved_by": adjuster}""",
        )
        source = source.replace(
            '{"thread_id": "review-claim"}',
            '{"thread_id": "review-claim", "adjuster_id": case.get("adjuster_id", "ADJ-001")}',
        )
        broken = source.replace(
            'adjuster = config["configurable"]["adjuster_id"]',
            'adjuster = response.get("adjuster_id", "ADJ-001")',
        )
        return (
            source,
            broken,
            [{"adjuster_id": "unknown", "decision": {"approved": True, "adjuster_id": "ADJ-001"}}],
            "Validate adjuster identity from the trusted invocation configuration, independently of the response payload.",
        )
    return None
