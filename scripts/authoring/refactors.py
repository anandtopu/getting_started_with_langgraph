"""Behavior-preserving starters with independently checked structural targets."""

import ast


def refactor(group: str, source: str) -> tuple[str, str, str, str]:
    """Return solution, working baseline, structural check, and learner contract."""
    if group == "13-A":
        start = source.index('    graph.add_node("fraud_checks", build_fraud_graph())')
        end = source.index('    graph.add_edge("route", END)', start)
        flattened = """    def check_amount(state):
        return {"flags": ["high_value"] if state["amount_cents"] > 500000 else []}
    def check_evidence(state):
        return {"flags": [] if state["documents"] else ["missing_evidence"]}
    graph.add_node("check_amount", check_amount)
    graph.add_node("check_evidence", check_evidence)
    graph.add_node("route", route)
    graph.add_edge(START, "check_amount")
    graph.add_edge(START, "check_evidence")
    graph.add_edge(["check_amount", "check_evidence"], "route")
"""
        baseline = source[:start] + flattened + source[end:]
        check = """
def test_reusable_fraud_subgraph_is_connected(candidate):
    children = dict(candidate.build_graph().get_subgraphs())
    assert "fraud_checks" in children, "LARKSPUR: connect a reusable compiled fraud subgraph"
    assert {"check_amount", "check_evidence"} <= set(children["fraud_checks"].get_graph().nodes)
"""
        return (
            source,
            baseline,
            check,
            "Extract parallel fraud checks into a reusable subgraph; keep both workflow outputs and rejection cases unchanged.",
        )
    if group == "15-A":
        baseline = source.replace(
            "from langgraph.func import entrypoint, task",
            "from langgraph.graph import StateGraph, START, END\nfrom typing import TypedDict",
        )
        start = baseline.index("@task")
        end = baseline.index("\ndef run(", start)
        baseline = (
            baseline[:start]
            + """class State(TypedDict):
    claim_id: str
    description: str
    amount_cents: int
    route: str

def normalize(claim):
    if type(claim["amount_cents"]) is not int or claim["amount_cents"] < 0:
        raise ValueError("Amount must be nonnegative integer cents")
    return {"description": claim["description"].strip()}

def assign_route(claim):
    return {"route": "needs_information" if not claim["description"] else "fast_track" if claim["amount_cents"] <= 100000 else "standard"}

builder = StateGraph(State)
builder.add_node("normalize", normalize)
builder.add_node("assign_route", assign_route)
builder.add_edge(START, "normalize")
builder.add_edge("normalize", "assign_route")
builder.add_edge("assign_route", END)
intake = builder.compile()

"""
            + baseline[end:]
        )
        check = """
def test_functional_entrypoint_and_task_boundaries(candidate_path):
    import ast
    tree = ast.parse(candidate_path.read_text("utf-8"))
    decorated = {node.name: [ast.unparse(item) for item in node.decorator_list]
                 for node in tree.body if isinstance(node, ast.FunctionDef)}
    assert "entrypoint()" in decorated.get("intake", []), "LARKSPUR: use an entrypoint for orchestration"
    assert all("task" in decorated.get(name, []) for name in ("normalize", "route")), "LARKSPUR: retain task boundaries"
"""
        return (
            source,
            baseline,
            check,
            "Convert the working Graph API pipeline to an entrypoint with normalize and route tasks, preserving every existing result and validation error.",
        )
    node = next(
        item
        for item in ast.parse(source).body
        if isinstance(item, ast.FunctionDef) and item.name == "run"
    )
    lines = source.splitlines(keepends=True)
    body = "".join(lines[node.lineno : node.end_lineno])
    body = body.replace("DEFAULT_CASE if case is None else case", "case")
    body = body.replace("    case = case\n", "")
    lines[node.lineno : node.end_lineno] = ["    case = prepare_case(case)\n" + body]
    solution = "".join(lines)
    helper = '''def prepare_case(case: dict | None = None) -> dict:
    """Own a fresh input snapshot; do not mutate the caller or shared defaults."""
    from copy import deepcopy
    return deepcopy(DEFAULT_CASE if case is None else case)


'''
    solution = solution.replace("def run(", helper + "def run(", 1)
    check = """
def test_input_preparation_is_a_separate_owned_boundary(candidate, candidate_path):
    import ast
    from copy import deepcopy
    helper = getattr(candidate, "prepare_case", None)
    assert callable(helper), "LARKSPUR: extract prepare_case(case) from orchestration"
    original = {"nested": {"items": ["original"]}}
    before = deepcopy(original)
    prepared = helper(original)
    assert prepared == before and prepared is not original
    prepared["nested"]["items"].append("changed")
    assert original == before, "LARKSPUR: isolate nested caller-owned inputs"
    defaults = deepcopy(candidate.DEFAULT_CASE)
    prepared = helper()
    assert prepared == defaults and prepared is not candidate.DEFAULT_CASE
    assert helper({}) == {}, "LARKSPUR: an empty input is not a request for defaults"
    tree = ast.parse(candidate_path.read_text("utf-8"))
    run = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "run")
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "prepare_case" for node in ast.walk(run)), "LARKSPUR: use the extracted boundary in run"
"""
    return (
        solution,
        source,
        check,
        "Separate input preparation from orchestration in prepare_case(case). Preserve all results/errors, distinguish None from {}, and copy nested inputs so caller data and shared defaults stay independent.",
    )


def typescript_refactor(group: str, source: str) -> tuple[str, str, str]:
    if group == "B1-C":
        start = source.index("  const fake =")
        end = source.index("  const inputState", start)
        solution = (
            source[:start]
            + "  const manual = createAgent({ model: model(), tools: [lookup] });\n"
            + source[end:]
        )
        target = "createAgent({ model: model(), tools: [lookup] })"
        reason = "Replace the manual model/tool loop with createAgent, keeping message roles, call IDs, errors, and final text unchanged."
    else:
        start = source.index("const graph = new StateGraph")
        end = source.index(";", source.index(".compile(", start)) + 1
        block = source[start:end]
        expression = block.removeprefix("const graph = ").removesuffix(";")
        parameter = "saver: SqliteSaver" if group == "B1-B" else ""
        argument = "saver" if group == "B1-B" else ""
        solution = source[:start] + f"const graph = buildGraph({argument});" + source[end:]
        solution = solution.replace(
            "export async function run",
            f"export function buildGraph({parameter}) {{\n  return {expression};\n}}\n\nexport async function run",
            1,
        )
        target = "buildGraph("
        reason = "Extract reusable graph construction into buildGraph; keep invocation, saver lifetime, stream counts, and all old behavior unchanged."
    check = f"""
def test_typescript_structure(candidate_path):
    source = candidate_path.with_suffix(".ts").read_text("utf-8")
    assert {target!r} in source, "LARKSPUR: implement the requested TypeScript construction boundary"
"""
    if group == "B1-C":
        check += (
            '    assert "new StateGraph(" not in source, "LARKSPUR: remove the manual agent loop"\n'
        )
    else:
        check += '    assert "export function buildGraph(" in source and source.count("buildGraph(") >= 2, "LARKSPUR: call the extracted builder"\n'
    return solution, check, reason
