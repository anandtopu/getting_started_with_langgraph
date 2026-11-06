"""Build linked coverage, concrete bug cases, and five single-page printable guides."""

import html
import json

from common.config import ROOT
from common.exercises import observe
from common.loading import load_module
from scripts.build_course import LABS

TERMS = {
    "State": "Named data a graph carries between steps.",
    "Channel": "One state field together with the rule for accepting its updates.",
    "Node": "A unit of work that reads state and returns changes.",
    "Edge": "A connection that schedules later work.",
    "Conditional edge": "A connection whose destination depends on a routing function.",
    "Router": "A function that chooses the next node or completion.",
    "Partial update": "A dictionary containing only fields a node changes.",
    "Reducer": "A function that combines an old field value and a new update.",
    "Overwrite": "Replacing a field instead of accumulating its previous value.",
    "Associativity": "Combining updates in different groupings gives the same result.",
    "Commutativity": "Swapping update order leaves the result unchanged.",
    "Idempotence": "Repeating an operation has the same effect as doing it once.",
    "Superstep": "A batch of scheduled nodes that read the same previous state boundary.",
    "Barrier": "The point where sibling work finishes and its updates are merged.",
    "Fan-out": "Scheduling several independent branches.",
    "Fan-in": "Combining or continuing after parallel branches.",
    "Map-reduce": "Apply work to many items, then combine their results.",
    "Send": "An instruction that schedules a node with a particular input.",
    "Command": "An object carrying control-flow changes, state updates, or resume values.",
    "START": "The graph's entry connection.",
    "END": "The graph's completion destination.",
    "Compile": "Turn a graph definition into an executable graph.",
    "Invoke": "Run a graph until it completes or pauses.",
    "GraphOutput": "The v2 invocation wrapper containing values and interrupts.",
    "Stream": "A sequence of observations emitted while work executes.",
    "Stream namespace": "The location of an event within nested graph execution.",
    "Checkpoint": "A saved execution boundary used for inspection and recovery.",
    "Checkpointer": "The component that stores and retrieves checkpoints.",
    "Thread": "The persistent history associated with one configured thread ID.",
    "Snapshot": "An inspectable view of state and pending work at a saved boundary.",
    "Pending write": "A recorded task result that can survive another task's failure.",
    "Interrupt": "A durable request to stop and wait for an external answer.",
    "Resume": "Continue a saved execution with the requested answer.",
    "Replay": "Execute from a saved boundary; later work may run again.",
    "Fork": "Continue an alternative history from an earlier checkpoint.",
    "Durability": "How reliably committed execution progress survives process failure.",
    "Subgraph": "A graph used as a component inside another graph.",
    "Adapter": "Code that translates one component's input and output into another's schema.",
    "Private state": "Internal fields intentionally excluded from a public component boundary.",
    "Context": "Trusted invocation data such as identity or dependencies, separate from mutable state.",
    "Runtime": "The node's access to invocation context, Store, and execution facilities.",
    "Store": "A namespaced place for memory shared across threads.",
    "Namespace": "A tuple or path that groups records, often by customer and memory type.",
    "Short-term memory": "Conversation state retained within one thread.",
    "Long-term memory": "Information retained across conversations or threads.",
    "Semantic memory": "Stored facts or preferences, rather than an event transcript.",
    "Episodic memory": "Stored descriptions of earlier events or experiences.",
    "Embedding": "A numeric vector representing content for similarity comparisons.",
    "Vector search": "Retrieval using similarity between numeric representations.",
    "RAG": "Retrieval-augmented generation: supply retrieved evidence when producing an answer.",
    "Citation": "A reference to the evidence supporting a statement.",
    "LLM": "A model that predicts and generates language-like sequences.",
    "Token": "A unit of model input or output, often part of a word.",
    "Context window": "The maximum input and output context a model can handle together.",
    "Temperature": "A generation setting affecting sampling; zero still does not guarantee a provider's reproducibility.",
    "Prompt": "Instructions and content supplied to a model.",
    "System message": "Instructions describing the model's role or behavior.",
    "Human message": "A message representing user input.",
    "AI message": "A model response, possibly containing tool calls.",
    "Tool message": "The result associated with a particular tool-call ID.",
    "Tool": "A callable capability with a declared input schema and description.",
    "Tool call": "A model's structured request to invoke a named capability.",
    "Structured output": "A response validated against an explicit schema.",
    "Agent": "A system that can choose actions dynamically within given capabilities and limits.",
    "Workflow": "A process whose control-flow structure is chosen by its author.",
    "ReAct loop": "An agent cycle of model decisions, tool execution, and model continuation.",
    "Middleware": "Hooks around agent execution for state changes, policies, or interception.",
    "Supervisor": "A coordinator that chooses which scoped specialist to consult.",
    "Handoff": "A transfer of control and selected context to another agent or graph.",
    "Functional API": "Durable orchestration expressed with entrypoint and task functions.",
    "Future": "A handle for a result that may still be computing.",
    "Retry": "A bounded repeat after a selected transient failure.",
    "Timeout": "A limit on how long an operation may run.",
    "Cancellation": "A request to stop work, requiring cleanup of resources.",
    "Backoff": "Increasing delays between retries to avoid overwhelming a failing dependency.",
    "Idempotency key": "A stable operation identifier used to reject duplicate or conflicting effects.",
    "Lease": "Temporary exclusive ownership of work, such as one running thread.",
    "MCP": "Model Context Protocol, a standard way to expose tools and resources to clients.",
    "stdio transport": "A local process protocol carried over standard input and output.",
    "SSE": "Server-sent events: a one-way HTTP stream from server to client.",
    "Evaluation": "Measuring behavior against explicit expected outcomes or criteria.",
    "Trajectory": "The ordered messages and tool actions taken during an agent run.",
    "Trace": "A diagnostic record of nested operations, inputs, outputs, and timing.",
    "Prompt injection": "Untrusted text attempting to redirect the system's instructions or authority.",
    "Authorization": "The server's decision about which authenticated actor may perform an action.",
    "Schema validation": "Checking that a value has the required fields, types, and constraints.",
    "Delta channel": "A Beta channel that retains incremental writes and reconstructs accumulated state.",
    "Beta": "An explicitly experimental API whose contract may change before stabilization.",
}

SHEETS = {
    "tier_1": (
        "Tier 1 | Predict graph execution",
        [
            (
                "State and updates",
                "Nodes read state and return only changed fields. TypedDict describes shape; it does not enforce input validity at runtime.",
            ),
            (
                "Reducers",
                "Use Annotated[field_type, reducer] for accumulation. Parallel overwrite writes conflict. Test associativity and boundary cases.",
            ),
            (
                "Routing",
                "Use conditional edges for a pure destination decision, Command for update plus routing, and Send for per-item work.",
            ),
            (
                "Supersteps",
                "Siblings read the same previous snapshot. Merge their writes before downstream nodes run. Add an explicit loop exit.",
            ),
            (
                "Persistence",
                "Compile with a saver. Invoke with configurable.thread_id. SQLite contexts must close before reopening on Windows.",
            ),
            (
                "Approval",
                "Call interrupt(request). Resume the same thread with Command(resume=answer). Validate the answer; the node restarts.",
            ),
            (
                "Replay",
                "Inspect get_state and get_state_history. Fork a checkpoint deliberately. External effects need independent idempotency.",
            ),
            (
                "Read output",
                "invoke(..., version='v2') returns GraphOutput: use .value and .interrupts. Stream parts contain type, ns, data.",
            ),
            (
                "Practice",
                "Modules 00-07; guided tasks end in 01, 02, 09, 10, 17, 18. Checkpoint project: Claims Intake Engine.",
            ),
        ],
    ),
    "tier_2": (
        "Tier 2 | Add models without losing control",
        [
            (
                "Model factory",
                "Use common.models.get_chat_model(). Graded runs use scripted responses, temperature zero, no credentials, and no network.",
            ),
            (
                "Message history",
                "Preserve AI tool-call IDs and matching tool responses. Use add_messages for message identity-aware updates.",
            ),
            (
                "Structured output",
                "Validate fields with Pydantic and explicit constraints. Model text cannot grant approval or establish ownership.",
            ),
            (
                "Tools",
                "Expose the smallest capability. Validate arguments and trust runtime context, not a model-supplied customer ID.",
            ),
            (
                "Agent loop",
                "Use create_agent for a standard model/tool loop. Use an explicit graph when routing or authorization must be fixed.",
            ),
            (
                "Middleware",
                "Place limits and hooks at the boundary they control. Bound model calls, tool calls, and recursion separately.",
            ),
            (
                "Memory",
                "Checkpoints retain a thread. Store namespaces retain cross-thread facts. Trim or summarize deliberately; do not erase pending tool pairs.",
            ),
            (
                "RAG",
                "Retrieve evidence, retain source IDs, answer only from support, and abstain when the corpus does not answer the question.",
            ),
            (
                "Practice",
                "Modules 08-12; compare default, missing, malformed, and rejection cases. Checkpoint project: Policy Q&A with Memory.",
            ),
        ],
    ),
    "tier_3": (
        "Tier 3 | Compose and recover",
        [
            (
                "Subgraphs",
                "Share only intended state fields. Use adapters for private schemas. Choose inherited or independent checkpoint ownership explicitly.",
            ),
            (
                "Multiple agents",
                "Use specialists for distinct contexts or capabilities. A supervisor adds latency and coordination work; compare a single-agent baseline.",
            ),
            (
                "Handoffs",
                "Command.PARENT transfers control to the parent. Preserve matched tool responses and keep state contracts compatible.",
            ),
            (
                "Functional API",
                "entrypoint orchestrates; task saves repeatable work results. Entry code may re-enter while a completed task result is reused.",
            ),
            (
                "External calls",
                "Use timeouts, bounded retries, cancellation cleanup, and a stable idempotency key tied to a canonical payload.",
            ),
            (
                "MCP",
                "Own the client session lifetime. Local stdio needs no network. Keep protocol stdout free of logs and expose read-only tools first.",
            ),
            (
                "Fault recovery",
                "Test a crash after effect commit but before task completion. A checkpoint and an external transaction are separate boundaries.",
            ),
            (
                "Long waits",
                "Persist before waiting; reopen the same thread after restart. Never keep a Python process asleep for days to represent a business wait.",
            ),
            (
                "Practice",
                "Modules 13-17; inject failures at boundaries. Checkpoint project: Fraud Investigation Team.",
            ),
        ],
    ),
    "tier_4": (
        "Tier 4 | Operate a bounded application",
        [
            (
                "Streaming",
                "Project public updates and tokens. Keep internal checkpoints private. On reconnect fetch a snapshot; do not duplicate the initial input.",
            ),
            (
                "HTTP boundary",
                "Authenticate each request, verify thread ownership, validate inputs, and recheck the current interrupt inside the execution lease.",
            ),
            (
                "Testing",
                "Test nodes, reducers, graph routes, recovery, and API behavior. Use independent expected answers instead of copying observed outputs blindly.",
            ),
            (
                "Evaluation",
                "Measure routing and tool trajectories. Distinguish strict ordering from acceptable unordered parallel calls.",
            ),
            (
                "Observability",
                "Log allowlisted identifiers, nodes, status, and durations. Tracing is opt-in; credentials and customer text do not belong in logs.",
            ),
            (
                "Security",
                "Treat retrieved documents and model output as untrusted. Use trusted roles, strict schemas, scoped tools, and explicit approvals.",
            ),
            (
                "Persistence",
                "SQLite serves a local single process. Postgres supports shared checkpoints, Store, ownership, leases, and payload-bound effect keys.",
            ),
            (
                "Deployment",
                "Health-check dependencies, close resources on shutdown, preserve durable volumes, and test restoring a paused claim.",
            ),
            (
                "Practice",
                "Modules 18-22; finish the Claims Copilot and Design Your Own capstones. Live providers and hosted deployment are separate checks.",
            ),
        ],
    ),
    "api_at_a_glance": (
        "LangGraph | API at a glance",
        [
            (
                "StateGraph(State)",
                "Define named state channels and optional input/output/context schemas.",
            ),
            (
                "add_node / add_edge",
                "Register work and fixed connections. START enters; END completes.",
            ),
            (
                "add_conditional_edges",
                "Map a router's result to the next destination; cover every possible result.",
            ),
            (
                "Command / Send",
                "Update and route, resume an interrupt, or schedule parameterized parallel work.",
            ),
            (
                "compile(checkpointer=...)",
                "Create a runnable with an explicit persistence lifecycle.",
            ),
            ("invoke / ainvoke", "Pass version='v2'; inspect result.value and result.interrupts."),
            ("stream / astream", "Pass version='v2'; handle each part's type, ns, and data."),
            (
                "interrupt / Command(resume=...)",
                "Save a request, then continue the same thread with validated answers.",
            ),
            (
                "get_state / get_state_history",
                "Inspect current and earlier snapshots, including next scheduled work.",
            ),
            (
                "update_state",
                "Create a state update at a selected boundary; use checkpoint configuration deliberately.",
            ),
            (
                "Runtime / Store",
                "Read trusted context and scoped cross-thread memory inside a node.",
            ),
            ("entrypoint / task", "Use ordinary Python orchestration with durable task results."),
            (
                "create_agent",
                "Build a bounded model/tool loop from langchain.agents and the shared model factory.",
            ),
            (
                "Beta: stream_events / DeltaChannel",
                "Optional B4 only; v3 events use method/params, unlike core v2 parts.",
            ),
        ],
    ),
}


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8", newline="\n")


def main():
    catalog = json.loads((ROOT / "docs/planning/course_catalog.json").read_text("utf-8"))
    rows = [
        "# Feature map — coverage contract",
        "",
        "Each link points to a shipped lesson, executable example, cumulative use case, and graded tasks. The six tasks cover the group's contracts across normal and boundary cases; individual tasks focus on different failures. Beta behavior is isolated in B4. See [verification notes](VERIFICATION_NOTES.md) for API choices and integration limits.",
        "",
        "| Group / lesson | Features | Example | Use case | Tasks | Official guide |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    bugs = [
        "# Common bugs",
        "",
        "These are observed faults in runnable starters. Each entry includes an actual counterexample, its wrong output or exception type, the cause, and the repair practiced in the linked Fix task. Run from the repository root after installing the lesson's dependencies.",
        "",
    ]
    count = 0
    for module in catalog["modules"]:
        for group in module["groups"]:
            tasks = " ".join(
                f"[{task['id']}](../{task['folder']}/task.md)" for task in group["tasks"]
            )
            rows.append(
                f"| [{group['id']}](../{module['path']}/README.md) | {'; '.join(group['features'])} | [{group['example']}](../{module['path']}/examples/{group['example']}) | [Copilot v{module['copilot_version']:02d}](../{module['path']}/use_case/claims_copilot.py) | {tasks} | [Guide]({group['source']}) |"
            )
            if group["id"] not in LABS or count >= 30:
                continue
            task = next(task for task in group["tasks"] if task["type"] == "fix")
            source = load_module(ROOT / task["folder"] / "starter.py")
            cases = json.loads((ROOT / task["folder"] / "cases.json").read_text("utf-8"))
            failing = next(
                (case for case in cases if observe(source, case["input"]) != case["expected"]), None
            )
            assert failing, task["id"]
            actual = observe(source, failing["input"])
            old, new, cause = LABS[group["id"]]["faults"][1]
            count += 1
            bugs.extend(
                [
                    f"## {count}. {group['slug'].replace('_', ' ').title()}",
                    "",
                    f"**Symptom:** input `{json.dumps(failing['input'])}` produces:",
                    "",
                    "```json",
                    json.dumps(actual, indent=2),
                    "```",
                    "",
                    f"**Cause:** the faulty operation is `{new}`. {cause}",
                    "",
                    f"**Fix:** restore `{old}` and compare every declared case. The required result for this counterexample is:",
                    "",
                    "```json",
                    json.dumps(failing["expected"], indent=2),
                    "```",
                    "",
                    f"[Practice Fix {task['id']}](../{task['folder']}/task.md) · [Lesson](../{module['path']}/README.md)",
                    "",
                ]
            )
    write(ROOT / "docs/FEATURE_MAP.md", "\n".join(rows))
    write(ROOT / "docs/COMMON_BUGS.md", "\n".join(bugs))
    write(
        ROOT / "docs/GLOSSARY.md",
        "# Glossary\n\n"
        + "\n\n".join(f"**{term}.** {definition}" for term, definition in TERMS.items()),
    )
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

    for slug, (title, items) in SHEETS.items():
        folder = ROOT / "cheatsheets"
        write(
            folder / (slug + ".md"),
            f"# {title}\n\n"
            + "\n\n".join(f"## {name}\n\n{text}" for name, text in items)
            + "\n\nVerified course API family: 2026-11-06. See docs/VERIFICATION_NOTES.md and the lockfiles.",
        )
        doc = SimpleDocTemplate(
            str(folder / (slug + ".pdf")),
            pagesize=letter,
            rightMargin=42,
            leftMargin=42,
            topMargin=36,
            bottomMargin=36,
            title=title,
            author="Larkspur LangGraph Course",
        )
        heading = ParagraphStyle(
            "heading",
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=22,
            textColor=colors.HexColor("#153C4A"),
            spaceAfter=10,
        )
        body = ParagraphStyle(
            "body",
            fontName="Helvetica",
            fontSize=9.3,
            leading=12.5,
            alignment=TA_LEFT,
            spaceAfter=10,
        )
        story = [
            Paragraph(html.escape(title), heading),
            Paragraph("LARKSPUR CLAIMS | OFFLINE-FIRST PRACTICE COURSE", body),
            Spacer(1, 5),
        ]
        for name, text in items:
            story.append(
                Paragraph("<b>" + html.escape(name) + "</b><br/>" + html.escape(text), body)
            )
        story.extend(
            [
                Spacer(1, 8),
                Paragraph(
                    "Verified 2026-11-06. Core Python output: v2. Optional Beta APIs: B4.<br/>Sources and pinned versions: docs/VERIFICATION_NOTES.md",
                    body,
                ),
            ]
        )
        doc.build(story)
    print(
        f"Wrote 81 linked feature rows, {count} observed bugs, {len(TERMS)} glossary terms, and five printable guides."
    )


if __name__ == "__main__":
    main()
