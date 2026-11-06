"""Tier 1 cases and deliberate faults. Each fault targets a different contract."""

LABS = {
    "00-B": {
        "idea": "An environment is the interpreter and packages used by one command. A package installed for another interpreter is still missing here. An optional live provider must not block a deterministic checklist.",
        "analogy": "Check the tools in this workshop, not the tools in another building.",
        "cases": [
            {},
            {"live": True},
            {"data_present": False},
            {"packages": []},
            {"python": [3, 10]},
        ],
        "checks": [("value.ready", True)],
        "faults": [
            (
                "errors = []",
                'errors = ["Missing optional model integration"]',
                "Required and optional packages are different contracts.",
            ),
            (
                'case["live"] and not case["provider_ready"]',
                'not case["provider_ready"]',
                "A missing provider is a problem only when live mode was requested.",
            ),
            (
                'if not case["data_present"]:',
                "if False:",
                "A setup report must identify missing committed fixtures.",
            ),
            (
                'tuple(case["python"])',
                "tuple([3, 12])",
                "Use the supplied interpreter version; do not assume the recommended version is installed.",
            ),
        ],
        "design": {
            "required": "python_packages_data",
            "provider": "live_only",
            "secrets": "presence_only",
        },
    },
    "00-C": {
        "idea": "An assertion compares an observed result with an explicit requirement. A failing starter is useful when it runs and shows a wrong business result. Hints guide a repair; viewing a solution is recorded separately from independent work.",
        "analogy": "Use a measuring tape before changing the shape of a part.",
        "cases": [
            {},
            {"claim_type": "THEFT"},
            {"claim_type": None},
            {"claim_type": "  storm  "},
            {"claim_type": "unlisted"},
        ],
        "checks": [("value.label", "water")],
        "faults": [
            ('else "unknown"', 'else ""', "Unknown claim categories need an explicit label."),
            (
                "value.strip().lower()",
                "value.strip()",
                "Labels need case normalization before comparison.",
            ),
            (
                "value.strip().lower()",
                "value.lower()",
                "Leading and trailing spaces are not claim categories.",
            ),
            ('claim.get("claim_id")', "None", "The output must retain the input claim identity."),
        ],
        "design": {
            "acceptance": "known_and_unknown_labels",
            "whitespace": "strip_then_lower",
            "evidence": "passing_assertions",
        },
    },
    "01-A": {
        "idea": "State is the information available to a graph. TypedDict documents its keys. A node is a function that reads state and returns only the keys it changes; the graph merges those updates instead of replacing the whole state.",
        "analogy": "Each desk adds a note to the same claim folder rather than throwing the folder away.",
        "cases": [
            {},
            {"claim_id": "CLM-0099", "amount_cents": "250"},
            {"description": " "},
            {"amount_cents": True},
        ],
        "checks": [("value.claim_id", "CLM-0001"), ("value.amount_cents", 125000)],
        "faults": [
            (
                'state["description"].strip()',
                'state["description"]',
                "Normalize the description while preserving unrelated state.",
            ),
            (
                'return {"amount_cents": int(amount)}',
                "return str(amount)",
                "A graph node must return a mapping of state updates.",
            ),
            (
                'return {"amount_cents": int(amount)}',
                'return {"amount_cents": int(amount), "claim_id": ""}',
                "An amount update must not erase the claim identifier.",
            ),
            (
                'return {"description": state["description"].strip()}',
                'state["description"] = state["description"].strip()\n    return {"description": state["description"]}',
                "Refactor mutation into a pure partial update.",
            ),
        ],
        "design": {
            "state": "typed_keys",
            "node_result": "partial_mapping",
            "identity": "preserved",
        },
    },
    "01-B": {
        "idea": "Edges declare which node can run next. START is the entry point and END marks termination. compile checks the graph and creates an executable object. Explicit v2 invoke returns GraphOutput; its value is the final state.",
        "analogy": "A checklist needs arrows as well as boxes; an unconnected desk never receives the folder.",
        "cases": [{}, {"description": " "}, {"claim_id": "CLM-0098", "description": " theft "}],
        "checks": [
            ("value.steps", ["normalize", "validate", "acknowledge"]),
            ("value.acknowledged", True),
        ],
        "faults": [
            (
                'graph.add_edge("validate", "acknowledge")',
                'graph.add_edge("validate", END)',
                "The acknowledgment must be reachable.",
            ),
            (
                'graph.add_edge("normalize", "validate")',
                'graph.add_edge("normalize", "acknowledge")',
                "Validation must occur before acknowledging the claim.",
            ),
            (
                '"acknowledged": True',
                '"acknowledged": False',
                "A completed acknowledgment must be visible in output.",
            ),
            (
                '[*state["steps"], "validate"]',
                '["validate"]',
                "Refactoring must preserve the complete execution sequence.",
            ),
        ],
        "design": {
            "entry": "normalize",
            "validation": "before_acknowledge",
            "exit": "after_acknowledge",
        },
    },
    "01-C": {
        "idea": "A generated diagram shows the compiled edges rather than a hand-drawn guess. In a sequential graph each node runs in a later superstep, a batch of work that sees the previous batch's committed updates. Updates reveal which node actually ran.",
        "analogy": "Compare the building plan with the visitor log: one describes possibilities, the other records a visit.",
        "cases": [
            {},
            {"description": ""},
            {"claim_id": "CLM-0042", "description": " stolen watch "},
        ],
        "checks": [("value.steps", ["receive", "validate", "acknowledge"])],
        "faults": [
            (
                'graph.add_edge("receive", "validate")',
                'graph.add_edge("receive", "acknowledge")',
                "The diagram must include validation on the executed route.",
            ),
            (
                'graph.add_edge("validate", "acknowledge")',
                'graph.add_edge("validate", END)',
                "The intended final node must be connected.",
            ),
            (
                'bool(state["description"].strip())',
                "True",
                "Eligibility evidence must affect the validation result.",
            ),
            (
                'return {"acknowledged": state["received"]}',
                'return {"acknowledged": False}',
                "The final update must reflect earlier state.",
            ),
        ],
        "design": {
            "visibility": "previous_superstep",
            "diagram": "generated_from_compiled_graph",
            "termination": "acknowledge_to_end",
        },
    },
    "02-A": {
        "idea": "TypedDict describes a dictionary for type checking; it does not validate values at runtime. Dataclasses give attribute access and defaults. Pydantic checks fields at the boundary. With explicit v2 output, preserve the schema's object type before extracting its fields.",
        "analogy": "A form template, a filled form object, and a clerk checking the form are different services.",
        "cases": [
            {},
            {"kind": "typed"},
            {"kind": "dataclass"},
            {"amount_cents": -1},
            {"amount_cents": True},
            {"kind": "typed", "amount_cents": 0},
        ],
        "checks": [("value.output_type", "ClaimModel"), ("value.value.status", "validated")],
        "faults": [
            (
                'return {"status": "validated"}',
                'return {"status": "received"}',
                "A successful validation node must record its result.",
            ),
            (
                "return state.model_dump()",
                "return dict()",
                "Use Pydantic field access or model_dump instead of losing validated values.",
            ),
            ("amount <= 0", "amount < 0", "The positive-amount contract excludes zero."),
            (
                "return asdict(state) if isinstance(state, ClaimData) else dict(state)",
                "return {} if isinstance(state, ClaimData) else dict(state)",
                "Converting schema styles must preserve valid values.",
            ),
        ],
        "design": {
            "typed_dict": "static_contract",
            "dataclass": "attributes_and_defaults",
            "pydantic": "runtime_validation",
        },
    },
    "02-B": {
        "idea": "A channel is one state field together with its update rule. The default rule overwrites. An Annotated reducer combines the old and new values. Associativity means grouping updates differently does not change the result, which matters when branches complete in batches.",
        "analogy": "Merge independent evidence envelopes without treating the last envelope as the whole case.",
        "cases": [
            {},
            {"second": {"id": "estimate", "severity": 2}},
            {"first": {"id": "receipt", "severity": 4}},
            {"first": {"id": "z", "severity": 1}, "second": {"id": "a", "severity": 2}},
        ],
        "checks": [
            ("value.findings", [{"id": "receipt", "severity": 3}]),
            ("value.log", ["estimate", "receipt"]),
        ],
        "faults": [
            (
                'indexed = {item["id"]: dict(item) for item in left}',
                "indexed = {}",
                "A merge must preserve evidence from earlier updates.",
            ),
            (
                '"log": ["receipt"]',
                '"log": state["log"] + ["receipt"]',
                "Return new evidence only; the reducer already has previous values.",
            ),
            (
                'max(indexed.get(key, {}).get("severity", 0), finding["severity"])',
                'finding["severity"]',
                "Severity must not decrease when a later finding is weaker.",
            ),
            (
                "for key in sorted(indexed)",
                "for key in indexed",
                "Canonical presentation must not depend on arrival order.",
            ),
        ],
        "design": {
            "merge": "max_severity_by_id",
            "associativity": "required",
            "presentation": "sorted_ids",
        },
    },
    "02-C": {
        "idea": "Input and output schemas define an API boundary; private channels can still exist inside the graph. Messages are records with roles, text, and IDs. add_messages appends new IDs and replaces an existing ID, so correcting one message need not duplicate it.",
        "analogy": "The customer copy of a file omits the adjuster's internal worksheet.",
        "cases": [
            {},
            {"claim_id": "CLM-0022", "text": " theft "},
            {"text": " ", "private_notes": "Untrusted supplied note"},
        ],
        "checks": [
            ("value.fields", ["claim_id", "messages"]),
            ("value.messages", [{"id": "customer-1", "content": "Pipe burst"}]),
        ],
        "faults": [
            (
                "output_schema=Output",
                "output_schema=Internal",
                "Internal channels must not become public output.",
            ),
            (
                'state["text"].strip(), id="customer-1"',
                'state["text"].strip(), id="customer-2"',
                "Use the same message ID to replace the original message.",
            ),
            (
                'state["text"].strip()',
                'state["text"]',
                "Customer-facing correction must normalize text.",
            ),
            (
                "input_schema=Input",
                "input_schema=Output",
                "A refactored input boundary must still supply the fields its nodes read.",
            ),
        ],
        "design": {
            "public": "claim_id_and_messages",
            "private": "internal_only",
            "message_edits": "same_id",
        },
    },
    "03-A": {
        "idea": "A routing function chooses a label from current state. A path map connects that label to a real node. A total router has an outcome for every accepted input, including zero, missing evidence, unknown categories, and malformed amounts.",
        "analogy": "A sorting desk labels envelopes; the delivery map tells the courier which desk each label means.",
        "cases": [
            {},
            {"amount_cents": 100001},
            {"amount_cents": 500001},
            {"missing": ["loss_date"]},
            {"amount_cents": "100"},
            {"claim_type": "jewelry"},
        ],
        "checks": [("value.route", "fast_track")],
        "faults": [
            ("amount <= 100000", "amount < 100000", "The exact fast-track threshold is inclusive."),
            (
                "{label: label for label in destinations}",
                '{label: "specialist" for label in destinations}',
                "Path-map values must match each intended destination.",
            ),
            ("amount > 500000", "amount > 900000", "High-value claims require specialist review."),
            (
                'if state["missing"]:',
                "if False:",
                "Refactoring must retain the missing-evidence route.",
            ),
        ],
        "design": {
            "money": "strict_integer_cents",
            "threshold": "inclusive_fast_track",
            "unknown_type": "specialist",
        },
    },
    "03-B": {
        "idea": "Command combines state updates with a routing instruction. Its destination annotation helps describe possible edges. A static edge still runs even when a Command chooses another node, so use one routing mechanism at a decision point.",
        "analogy": "One dispatch slip records both the reason and the next desk; a second independent slip can send the same case twice.",
        "cases": [{}, {"suspicious": False}, {"claim_id": "CLM-0031", "suspicious": True}],
        "checks": [("value.visited", ["review"]), ("value.reason", "indicator")],
        "faults": [
            (
                '"review" if state["suspicious"] else "acknowledge"',
                '"acknowledge"',
                "Suspicious evidence must affect the selected destination.",
            ),
            (
                'graph.add_edge(START, "triage")',
                'graph.add_edge(START, "triage")\n    graph.add_edge("triage", "acknowledge")',
                "A competing static edge schedules an extra acknowledgment.",
            ),
            (
                '"indicator" if state["suspicious"] else "routine"',
                '"routine"',
                "The recorded reason must explain the actual decision.",
            ),
            (
                '"visited": ["review"]',
                '"visited": ["review", "review"]',
                "Equivalent control flow must not duplicate work.",
            ),
        ],
        "design": {
            "routing": "one_mechanism",
            "reason": "same_update_as_route",
            "suspicious": "review",
        },
    },
    "03-C": {
        "idea": "Termination is a routing outcome, not an exceptional Python crash. Screen invalid and duplicate claims before assigning work. The returned state should still explain why a claim ended so an adjuster can inspect it.",
        "analogy": "A rejected form still receives a reason stamp before leaving the queue.",
        "cases": [{}, {"amount_cents": -1}, {"amount_cents": True}, {"duplicate_of": "CLM-0021"}],
        "checks": [("value.assigned", True), ("value.reason", "eligible")],
        "faults": [
            (
                '"assign" if state["reason"] == "eligible" else END',
                '"assign"',
                "Rejected claims must stop before assignment.",
            ),
            ("amount < 0", "amount <= 0", "Zero is a defined boundary, not an omitted case."),
            (
                '"duplicate"\n        if state["duplicate_of"]',
                '"eligible"\n        if state["duplicate_of"]',
                "Duplicate submissions need an explicit terminal reason.",
            ),
            (
                'return {"assigned": True}',
                'return {"assigned": False}',
                "Preserve eligible-case behavior while refactoring routes.",
            ),
        ],
        "design": {"negative": "invalid", "duplicate": "end_before_assignment", "zero": "eligible"},
    },
}
