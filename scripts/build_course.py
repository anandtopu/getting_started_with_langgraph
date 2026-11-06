"""Build teaching packages from authored cases and faults, then validate them separately."""

import argparse
import ast
import inspect
import json
import os
import pprint
import re
import subprocess
import sys
import textwrap
from copy import deepcopy
from pathlib import Path

from common.config import ROOT
from common.exercises import observe, read_path
from common.loading import load_module
from scripts.authoring.bonuses import LABS as BONUSES
from scripts.authoring.extensions import extend
from scripts.authoring.refactors import refactor, typescript_refactor
from scripts.authoring.tier1 import LABS as INTRO
from scripts.authoring.tier1_durable import LABS as DURABLE
from scripts.authoring.tier2 import LABS as MODELS
from scripts.authoring.tier3 import LABS as COMPOSITION
from scripts.authoring.tier4 import LABS as PRODUCTION
from scripts.authoring.traces import capture

FENCE = chr(96) * 3
LABS = {**INTRO, **DURABLE, **MODELS, **COMPOSITION, **PRODUCTION, **BONUSES}


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def write_json(path: Path, value) -> None:
    write(path, json.dumps(value, indent=2, ensure_ascii=False))


def replace_function(source: str, name: str, replacement: str) -> str:
    tree = ast.parse(source)
    function = next(
        node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == name
    )
    lines = source.splitlines(keepends=True)
    lines[function.lineno - 1 : function.end_lineno] = [replacement.rstrip() + "\n"]
    return "".join(lines)


def task_source(source: str, title: str) -> str:
    tree = ast.parse(source)
    if isinstance(tree.body[0], ast.Expr) and isinstance(tree.body[0].value, ast.Constant):
        source = "\n".join(source.splitlines()[tree.body[0].end_lineno :])
    source = '"""' + title + '. Run this file with Python. No live model or network. """\n' + source
    # Make the known failure visible without a traceback in the starter's demo.
    # Imports still fail normally, so an installation error cannot masquerade as a task.
    tree = ast.parse(source)
    main = next(
        node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "main"
    )
    body = source.splitlines()[main.lineno : main.end_lineno]
    replacement = "def main() -> None:\n    try:\n" + "\n".join("    " + line for line in body)
    replacement += '\n    except Exception as error:\n        print_state({"observed_error": type(error).__name__})\n'
    return replace_function(source, "main", replacement)


def answer_source(source: str, cases: list[dict], cause: str | None) -> str:
    source = re.sub(r"^def run\(", "def scenario(", source, count=1, flags=re.MULTILINE)
    footer = source.index("\nif __name__")
    source = source[:footer]
    body = (
        "\ndef run() -> dict:\n"
        "    observations = []\n"
        f"    for case in {pprint.pformat(cases, width=85)}:\n"
        "        try:\n"
        '            observations.append({"value": scenario(case)})\n'
        "        except Exception as error:\n"
        '            observations.append({"error": type(error).__name__})\n'
        f'    return {{"observations": observations, "cause": {cause!r}}}\n'
    )
    source += body
    if "--worker" not in source:
        source = replace_function(source, "main", "def main() -> None:\n    print_state(run())")
    return source + '\n\nif __name__ == "__main__":\n    main()\n'


def task_tests(
    folder: Path,
    *,
    answer: bool = False,
    purity: str | None = None,
    structural: str = "",
    batch: bool = False,
) -> None:
    if answer:
        content = '''
"""Compare the learner's written prediction with the checked execution."""
import json
from pathlib import Path

def test_written_prediction(answer):
    expected = json.loads(Path(__file__).with_name("expected_answer.json").read_text("utf-8"))
    assert answer == expected, "LARKSPUR: compare each observation and the stated cause"
'''
    else:
        content = '''
"""Grade the selected learner file, not the reference implementation."""
import json
from pathlib import Path
import pytest
from common.exercises import observe

CASES = json.loads(Path(__file__).with_name("cases.json").read_text("utf-8"))

@pytest.mark.parametrize("case", CASES, ids=[str(index) for index in range(len(CASES))])
def test_behavior(candidate, case):
    actual = observe(candidate, case["input"])
    assert actual == case["expected"], "LARKSPUR: preserve the declared state, routing, and boundary contracts"
'''
        if purity:
            content += f"""
def test_node_returns_a_partial_update_without_mutation(candidate):
    state = dict(candidate.DEFAULT_CASE)
    before = dict(state)
    update = candidate.{purity}(state)
    assert state == before, "LARKSPUR: a node must not mutate its input"
    assert set(update) == {{"description"}}, "LARKSPUR: return only the changed field"
"""
    if batch:
        content += """
def test_batch_preserves_order_errors_and_input_ownership(candidate):
    from copy import deepcopy
    batch = getattr(candidate, "run_batch", None)
    assert callable(batch), "LARKSPUR: implement the batch extension"
    selected = [CASES[0], CASES[-1], CASES[0]]
    inputs = [deepcopy(row["input"]) for row in selected]
    before = deepcopy(inputs)
    assert batch([]) == [], "LARKSPUR: an empty batch has no observations"
    assert batch(inputs) == [row["expected"] for row in selected], "LARKSPUR: preserve order and isolate each claim"
    assert inputs == before, "LARKSPUR: do not mutate the caller's batch"
"""
    write(folder / "test_task.py", textwrap.dedent(content).strip() + "\n" + structural)


def build_group(module: dict, group: dict, spec: dict, manifest: dict) -> None:
    path = ROOT / module["path"] / "examples" / group["example"]
    typescript = path.suffix == ".ts"
    script_path = path.with_suffix(".py")
    templates = ROOT / "scripts/authoring/sources" / module["id"]
    for target in {path, script_path}:
        template = templates / (target.name + ".in")
        if template.is_file():
            write(target, template.read_text("utf-8"))
    source = script_path.read_text("utf-8")
    implementation = path.read_text("utf-8") if typescript else source
    loaded = load_module(script_path)
    cases = [
        {**deepcopy(loaded.DEFAULT_CASE), **deepcopy(overrides)} for overrides in spec["cases"]
    ]
    expected = [observe(loaded, case) for case in cases]
    assert "value" in expected[0], (group["id"], "reference default failed", expected[0])
    for key, wanted in spec["checks"]:
        assert read_path(expected[0], key) == wanted, (group["id"], key, expected[0])
    spec["observations"] = expected
    spec["inputs"] = cases
    write_json(
        path.parent.parent / "tests" / (group["slug"] + ".json"),
        [{"input": case, "expected": result} for case, result in zip(cases, expected, strict=True)],
    )
    for task in group["tasks"]:
        folder = ROOT / task["folder"]
        kind = task["type"]
        index = {"build": 0, "fix": 1, "extend": 2, "refactor": 3, "trace": 1}.get(kind, 0)
        old, new, reason = spec["faults"][index]
        task["description"] = (
            f"Predict {group['slug'].replace('_', ' ')} across the declared cases"
            if kind == "predict"
            else f"Design {group['slug'].replace('_', ' ')} and justify the boundary policies"
            if kind == "design"
            else f"Diagnose {group['slug'].replace('_', ' ')} from execution evidence"
            if kind == "trace"
            else f"{kind.title()} {group['slug'].replace('_', ' ')}: {reason}"
        )
        if old not in implementation:
            raise ValueError(f"{task['id']}: authored fault anchor missing: {old!r}")
        broken_implementation = implementation.replace(old, new, 1)
        broken = source if typescript else broken_implementation
        if typescript:
            write(
                folder / "solution.ts", broken_implementation if kind == "trace" else implementation
            )
            write(
                folder / "starter.ts",
                "// YOUR CODE HERE: repair the task contract.\n" + broken_implementation,
            )
            if kind == "trace":
                write(folder / "trace.ts", broken_implementation)
        task_cases, task_expected, solution_source = cases, expected, source
        structural = ""
        if kind == "refactor" and group["id"] != "01-A":
            if typescript:
                ts_solution, structural, reason = typescript_refactor(group["id"], implementation)
                write(folder / "solution.ts", ts_solution)
                write(folder / "starter.ts", implementation)
                broken = source
            else:
                solution_source, broken, structural, reason = refactor(group["id"], source)
        extension = extend(group["id"], source) if kind == "extend" else None
        if extension is not None:
            solution_source, broken, extras, reason = extension
            task_cases = cases + [{**deepcopy(loaded.DEFAULT_CASE), **row} for row in extras]
            write(folder / "solution.py", task_source(solution_source, task["description"]))
            reference = load_module(folder / "solution.py")
            task_expected = [observe(reference, case) for case in task_cases]
            assert "value" in task_expected[0], (task["id"], task_expected[0])
            old, new = (
                "the new node or boundary contract described above",
                "the deliberately incomplete extension",
            )
            if typescript:
                write(folder / "starter.ts", implementation)
            write_json(
                folder / "baseline_cases.json",
                [
                    {"input": case, "expected": result}
                    for case, result in zip(cases, expected, strict=True)
                ],
            )
            structural += """
@pytest.mark.parametrize("case", json.loads(Path(__file__).with_name("baseline_cases.json").read_text("utf-8")))
def test_original_contract_survives_extension(candidate, case):
    from common.exercises import preserves_original
    assert preserves_original(case["expected"], observe(candidate, case["input"])), "LARKSPUR: retain the original fields, list prefix, and errors when adding a feature"
"""
        if kind in {"extend", "refactor"}:
            task["description"] = f"{kind.title()} {group['slug'].replace('_', ' ')}: {reason}"
        if kind == "refactor" and group["id"] != "01-A":
            old, new = "the original behavioral contract", "an unextracted design boundary"
        if kind in {"predict", "trace"}:
            trace = kind == "trace"
            oracle = answer_source(
                task_source(broken if trace else source, task["description"]),
                cases[:2] if trace else cases,
                reason if trace else None,
            )
            write(folder / "solution.py", oracle)
            answer = load_module(folder / "solution.py").run()
            write_json(folder / "expected_answer.json", answer)
            write_json(folder / "answer.json", {"observations": [], "cause": None})
            if trace:
                write(folder / "trace.py", task_source(broken, task["description"]))
                write_json(
                    folder / "trace.json", capture(load_module(folder / "trace.py"), cases[:2])
                )
            task_tests(folder, answer=True)
        elif kind == "design":
            plan = spec["design"]
            solution = (
                '"""Executable design constraints; the written rubric remains essential."""\n'
                "from common.pretty import print_state\n\n"
                f"def run(case: dict | None = None) -> dict:\n    return {pprint.pformat(plan, width=80)}\n\n"
                'def main() -> None:\n    print_state(run())\n\nif __name__ == "__main__":\n    main()\n'
            )
            write(folder / "solution.py", solution)
            write(
                folder / "starter.py",
                solution.replace(
                    pprint.pformat(plan, width=80), repr({key: "unreviewed" for key in plan})
                ).replace(
                    "    return",
                    "    # YOUR CODE HERE: choose and justify each policy.\n    return",
                    1,
                ),
            )
            write_json(folder / "cases.json", [{"input": {}, "expected": {"value": plan}}])
            task_tests(folder)
            write(
                folder / "design.md",
                "# Design review\n\nDescribe the claim scenario, justify every choice in your function, give one rejected alternative, and name a failure test. Then score the rubric honestly.",
            )
            write(
                folder / "rubric.md",
                "# Self-review rubric\n\nScore each dimension 0 (missing), 1 (partial), or 2 (specific and tested):\n\n- Correct state and control-flow boundary.\n- Failure, retry, or missing-input behavior.\n- Clear explanation tied to synthetic claim evidence.\n- One rejected alternative and its tradeoff.\n- Concrete acceptance tests.\n\nTarget 8/10 with no zero. Mechanical tests validate choices only. After writing your review, declare it with gym check ID --self-reviewed.",
            )
            write(
                folder / "solution_design.md",
                "# Worked design review\n\n"
                + spec["idea"]
                + "\n\n"
                + "\n".join(
                    f"- {key}: choose {value}; this preserves the boundary exercised by the example."
                    for key, value in plan.items()
                )
                + "\n\nRejected alternative: combine all decisions in an unvalidated, mutable global state. It hides ownership and makes independent failure checks harder. Validate normal, boundary, and rejected cases; retain the original synthetic input for comparison. This reference earns full marks only when those checks and the written rationale are both present.",
            )
        else:
            write(folder / "solution.py", task_source(solution_source, task["description"]))
            # A visible marker identifies the repair region; no missing bodies are emitted.
            broken = broken.replace(
                "\ndef run(",
                "\n# YOUR CODE HERE: repair the contract described in task.md.\ndef run(",
                1,
            )
            write(folder / "starter.py", task_source(broken, task["description"]))
            write_json(
                folder / "cases.json",
                [
                    {"input": case, "expected": result}
                    for case, result in zip(task_cases, task_expected, strict=True)
                ],
            )
            task_tests(
                folder,
                structural=structural,
                batch=kind == "extend" and "def run_batch(" in solution_source,
                purity="normalize_description"
                if group["id"] == "01-A" and kind == "refactor"
                else None,
            )
        package_input = cases[:2] if kind == "trace" else task_cases
        guide = f"# {task['id']} — {task['description']}\n\nType: {kind}. Difficulty: {task['level']}. No live model, key, or network is required.\n\n"
        guide += f"## The claim scenario\n\n{spec['idea']}\n\n"
        guide += f"## Your task\n\n{reason if kind not in {'predict', 'design', 'trace'} else task['description']} "
        guide += (
            "Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result."
            if kind == "trace"
            else "Predict each result before running the example. Keep the observations in the listed input order."
            if kind == "predict"
            else "Implement the choices in run and complete design.md using the rubric."
            if kind == "design"
            else "Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture."
        )
        guide += f"\n\n## Inputs and acceptance\n\n{FENCE}json\n{json.dumps(package_input, indent=2)}\n{FENCE}\n\n"
        if kind == "trace":
            guide += (
                "Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:\n\n"
                + "\n".join("- " + json.dumps(fault[2]) for fault in spec["faults"])
                + "\n\n"
            )
        if kind == "refactor":
            guide += "The starter already satisfies the original behavior cases. It fails the separate structural requirement. Keep those original tests green while changing the design; a renamed function alone does not establish the required boundary.\n\n"
        if kind == "extend":
            guide += "The new capability is checked in addition to the original cases. For run_batch, edit the Python orchestration interface (including in the TypeScript bonus); leave run(case) behavior intact. A batch is sequential and each case owns a new workflow invocation, not a shared durable thread.\n\n"
        if kind not in {"predict", "trace", "design"}:
            guide += "cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.\n\n"
        guide += "The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.\n\n"
        guide += f"## Commands\n\n{FENCE}text\nuv run gym start {task['id']}\nuv run gym check {task['id']}\nuv run gym hint {task['id']}\n{FENCE}\n\n"
        guide += f"## Reading\n\n[Module lesson](../../../../{module['path']}/README.md) · [Official guide]({group['source']})\n"
        write(folder / "task.md", guide)
        write(
            folder / "hints.md",
            f"# Hints\n\n## Hint 1\n\n{spec['analogy']} Compare the first differing field with the task's required behavior.\n\n## Hint 2\n\n{reason} Inspect the operation that owns this update or routing choice.\n\n## Hint 3\n\nThe reference contract uses this operation: {old}. Check every boundary input after the repair; a default-case pass alone is insufficient.\n",
        )
        write(
            folder / "explanation.md",
            f"# Why the solution works\n\n{spec['idea']}\n\n{reason} The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.\n\nThe deliberate fault changes {old!r} to {new!r}. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.\n\nRun the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.",
        )
        if kind == "refactor":
            write(
                folder / "explanation.md",
                f"# Why the refactor works\n\n{spec['idea']}\n\n{reason}\n\nThe starter is a working behavioral baseline. The reference changes its design, then runs the same case fixtures and a separate structural check. Inspect both test groups: matching one happy-path output does not prove equivalence. Preserve rejection/error behavior and input ownership as well as successful results.\n\nRun the selected workspace file through gym check. Viewing the reference is recorded as assisted study.",
            )
        manifest["tasks"][task["id"]] = {
            "prerequisites": [],
            "timeout": 120 if group["id"] in {"05-B", "17-A", "16-C"} else 45,
            "expected_failure": "LARKSPUR",
        }


def build_module(module: dict, modules: list[dict]) -> None:
    directory = ROOT / module["path"]
    root_prefix = "../" * len(Path(module["path"]).parts)
    write_use_case(module)
    available = [(group, LABS[group["id"]]) for group in module["groups"] if group["id"] in LABS]
    index = modules.index(module)
    previous = modules[index - 1] if index else None
    prerequisite = (
        f"[{previous['title']}]({Path(os.path.relpath(ROOT / previous['path'] / 'README.md', directory)).as_posix()})"
        if previous
        else f"[repository quick start]({root_prefix}README.md)"
    )
    level = (
        "Beginner"
        if module["id"].isdigit() and int(module["id"]) < 8
        else "Intermediate"
        if module["id"].isdigit() and int(module["id"]) < 13
        else "Advanced"
    )
    text = f"# {module['id']} — {module['title']}\n\n> After this module you can {module['use_case'][0].lower() + module['use_case'][1:]}\n\n**Time:** {module['lesson_minutes']} minutes · **Level:** {level} · **LLM needed:** No live model · **Cost:** $0 with the included fakes.\n\n**Larkspur Claims Copilot v{module['copilot_version']:02d}** · Practice takes additional time.\n\n"
    text += f"## Prerequisites\n\nComplete {prerequisite}. Read dictionary keys, functions, and Python type hints comfortably. Run uv sync from the repository root.\n\n"
    text += f"Optional installation requirements are listed in [the setup guide]({root_prefix}docs/OPTIONAL_DEPENDENCIES.md). Use `uv run --no-sync` after installing extras so subsequent commands retain that environment.\n\n"
    text += f"New to pytest, type validation, chat messages, tools, or async Python? Read the relevant section of [the beginner bridge]({root_prefix}docs/BEGINNER_BRIDGE.md) when that concept first appears.\n\n"
    if module["id"] in {"08", "09", "10", "11", "12"}:
        text += f"After the deterministic lesson, use [the optional provider lab]({root_prefix}docs/LIVE_MODEL_LAB.md) to try real extraction, scoped tool calls, and conversation memory with your configured provider. Graded results remain fake and offline.\n\n"
    text += (
        "## Learning objectives\n\n"
        + "\n".join(
            "- Implement and explain " + "; ".join(group["features"]) + "."
            for group in module["groups"]
        )
        + "\n\n"
    )
    text += (
        "## The big idea\n\n"
        + module["use_case"]
        + " Predict the state before running code, then compare the observed result. A state is the data visible to a node; a node is one unit of work; an edge selects later work. A checkpoint is a saved state boundary, not a promise that an external effect happened exactly once.\n\n"
    )
    text += "## How it works\n\n"
    if module["id"] == "00":
        text += "### Plain Python and a graph\n\nUse plain Python for a small fixed calculation. A workflow follows control flow you choose; an agent can choose tools dynamically within your constraints. LangGraph supplies stateful execution, LangChain supplies model/tool components, and LangSmith supplies optional tracing and deployment. The first example runs the same checklist both ways and asserts identical decisions.\n\n"
    for group, spec in available:
        text += f"### {group['slug'].replace('_', ' ').title()}\n\n{spec['idea']}\n\n{spec['analogy']}\n\n"
        loaded = load_module((directory / "examples" / group["example"]).with_suffix(".py"))
        builder = getattr(loaded, "build_graph", None)
        if builder and all(
            parameter.default is not inspect.Parameter.empty
            for parameter in inspect.signature(builder).parameters.values()
        ):
            diagram = builder().get_graph().draw_mermaid()
            text += f"{FENCE}mermaid\n{diagram}\n{FENCE}\n\n"
    if FENCE + "mermaid" not in text and (directory / "diagram.mmd").is_file():
        text += (
            "The checked-in diagram was generated from the executable lesson or cumulative Copilot graph. Edges describe possible work; inspect the runtime trace to see what ran.\n\n"
            + FENCE
            + "mermaid\n"
            + (directory / "diagram.mmd").read_text("utf-8")
            + "\n"
            + FENCE
            + "\n\n"
        )
    text += "## Key APIs at a glance\n\n| API / executable example | What it does | When to use it |\n| --- | --- | --- |\n"
    for group in module["groups"]:
        source_tree = ast.parse(
            (directory / "examples" / group["example"]).with_suffix(".py").read_text("utf-8")
        )
        apis = [
            alias.name
            for node in ast.walk(source_tree)
            if isinstance(node, ast.ImportFrom)
            and node.module
            and node.module.startswith(("langgraph", "langchain"))
            for alias in node.names
            if alias.name not in {"START", "END"}
        ]
        idea = LABS.get(group["id"], {"idea": "Compare a plain function and a fixed graph"})["idea"]
        text += f"| {', '.join(apis[:4]) or 'run(case)'} — [{group['example']}](examples/{group['example']}) | {'; '.join(group['features'])} | {idea.split('. ')[0]}. |\n"
    text += "\n## Walkthrough\n\nRun commands from the repository root; the same commands work in PowerShell, macOS, and Linux. Open the source alongside the output. Find the state declaration, node functions, graph connections, and invocation. For a failure, start with the earliest changed field or scheduled node.\n\n"
    for group in module["groups"]:
        command = "node" if group["example"].endswith(".ts") else "uv run --no-sync python"
        text += f"{FENCE}text\n{command} {module['path']}/examples/{group['example']}\n{FENCE}\n\n"
        if group["id"] in LABS:
            spec = LABS[group["id"]]
            text += f"**Predict, then run:** for {json.dumps(spec['inputs'][0])}, write the resulting fields and any expected error. Then test the boundary cases in tests/{group['slug']}.json.\n\n<details>\n<summary>Reveal the checked result</summary>\n\n{FENCE}json\n{json.dumps(spec['observations'][0], indent=2)}\n{FENCE}\n\n{spec['idea']}\n\n</details>\n\n"
    text += "When build_graph needs no arguments, its generated Mermaid diagram is saved beside the example. A diagram records possible edges; a runtime stream records executed work. A single sequence advances one node per superstep. Parallel nodes see the same previous boundary, so they cannot read a sibling's unfinished update.\n\n"
    text += "## When to use it, and when not to\n\nUse these contracts when the claim needs the state or control-flow behavior described above. Keep pure arithmetic and validation in ordinary functions that can be tested independently. A graph, checkpoint, or extra agent adds operational choices; justify it with a concrete failure, pause, branch, or reuse requirement.\n\n"
    text += f"## Real-world use case\n\n{module['use_case']} The executable milestone uses only fictional records and the shared v{module['copilot_version']:02d} implementation. [Read the use case](use_case/claims_copilot.py).\n\n{FENCE}text\nuv run python {module['path']}/use_case/claims_copilot.py\n{FENCE}\n\n"
    use_case_result = load_module(directory / "use_case/claims_copilot.py").run()
    text += f"Sample output from the synthetic default case:\n\n{FENCE}json\n{json.dumps(use_case_result, indent=2, default=str)}\n{FENCE}\n\nA real team would connect this boundary to validated records and authenticated roles, then retain the same rejection, ownership, and recovery checks.\n\n"
    text += "## Common bugs\n\n| Symptom or broken contract | Cause and repair | Practice |\n| --- | --- | --- |\n"
    for group, spec in available:
        for fault_index in (0, 1):
            fault = spec["faults"][fault_index]
            task = group["tasks"][fault_index]
            faulty = ROOT / task["folder"] / "starter.py"
            symptom = observe(load_module(faulty), spec["inputs"][0])
            displayed = json.dumps(symptom, ensure_ascii=False)[:220].replace("|", "&#124;")
            repair = fault[0].replace("|", "&#124;").replace("\n", " ")
            fix = next(item for item in group["tasks"] if item["type"] == "fix")
            text += f"| Observed `{displayed}`. {fault[2]} | Restore `{repair}` and check the boundary cases. | [{task['id']}]({root_prefix}{task['folder']}/task.md) · Related Fix: [{fix['id']}]({root_prefix}{fix['folder']}/task.md) |\n"
    text += "\n## Practice\n\n" + "\n".join(
        f"- [{task['id']} — {task['type']}, {task['level']}]({root_prefix}{task['folder']}/task.md): {task['description']}"
        for group in module["groups"]
        for task in group["tasks"]
    )
    text += "\n\nStart with tasks 01, 02, 09, 10, 17, and 18 in this module. Finish the other tasks for full practice. Hints are progressive; solution exposure is recorded. Predict and Trace tasks use answer JSON, not a code starter.\n\n"
    text += "## Quiz\n\nAnswer the six questions in [quiz.md](quiz.md) before opening its answers. Use a concrete claim example for every explanation.\n\n"
    text += "## Cost and safety\n\nThe default commands cost $0: deterministic Python and, in model lessons, scripted local fakes. They consume no hosted tokens and make no real payments or emails. Optional live experiments use the provider configured in .env; a short one-to-four-call exercise is usually cents, but verify your provider's current token prices and set a budget. Ollama can run locally without a hosted bill. Temporary checkpoint files are isolated from the committed dataset. Keep real customer details and credentials out of graph state.\n\n"
    text += "## Key takeaways\n\n- State visibility and update rules determine what a node can safely assume.\n- Check normal, missing, boundary, and failure cases before trusting a workflow.\n- Separate observed execution from diagrams, predictions, and durable history.\n- Model output is evidence to validate, never an authorization grant.\n- A saved checkpoint and an external effect have separate durability boundaries.\n\n"
    text += "## Go deeper\n\n" + "\n".join(
        f"- [{group['slug'].replace('_', ' ')} official guide]({group['source']})"
        for group in module["groups"]
    )
    text += "\n\n## Next:\n\n"
    text += (
        f"Continue to [module {modules[index + 1]['id']}: {modules[index + 1]['title']}]({root_prefix}{modules[index + 1]['path']}/README.md)."
        if index + 1 < len(modules)
        else "Complete the capstones and revisit the full feature map."
    )
    write(directory / "README.md", text)
    quiz = "# Quiz\n\nPredict first; explain in your own words.\n\n"
    answers = []
    for number, (group, spec) in enumerate(available):
        quiz += f"{number * 2 + 1}. Explain the contract in {group['example']} using one claim from its input cases.\n"
        quiz += f"{number * 2 + 2}. Diagnose this broken behavior: {spec['faults'][1][2]} Which observation distinguishes the repair from a default-case-only fix?\n"
        answers.extend(
            [
                spec["idea"],
                spec["faults"][1][2]
                + " Compare the normal case with the boundary fixtures and identify the first differing update.",
            ]
        )
    if len(available) == 2:
        quiz += "5. When is plain Python sufficient for intake?\n6. What is the difference between a workflow and an agent?\n"
        answers += [
            "Use a plain function for a small fixed calculation without orchestration needs.",
            "A workflow follows chosen control flow; an agent selects actions dynamically within explicit limits.",
        ]
    quiz += (
        "\n<details>\n<summary>Answers</summary>\n\n"
        + "\n".join(f"{i}. {answer}" for i, answer in enumerate(answers, 1))
        + "\n\n</details>"
    )
    write(directory / "quiz.md", quiz)
    readme = directory / "README.md"
    write(
        readme,
        readme.read_text("utf-8").replace(
            "Answer the six questions in [quiz.md](quiz.md) before opening its answers. Use a concrete claim example for every explanation.",
            quiz.removeprefix("# Quiz\n\n"),
        ),
    )
    tests = '''
"""Run each lesson against its checked boundary cases."""
import json
from pathlib import Path
import pytest
from common.exercises import observe
from common.loading import load_module

MODULE = Path(__file__).resolve().parents[1]
ROWS = []
for fixture in sorted((MODULE / "tests").glob("*.json")):
    slug = fixture.stem
    source = next((MODULE / "examples").glob("*_" + slug + ".py"))
    for row in json.loads(fixture.read_text("utf-8")):
        ROWS.append((source, row))

@pytest.mark.parametrize("source,row", ROWS)
def test_example_contract(source, row):
    from common.optional import missing_for_path
    missing = missing_for_path(source)
    if missing:
        pytest.skip(missing)
    assert observe(load_module(source), row["input"]) == row["expected"]
'''
    write(directory / "tests/test_examples.py", textwrap.dedent(tests).strip())
    cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"# {module['title']}\n",
                "Predict each example's result before running its cell. Scripts are the canonical source.\n",
            ],
        }
    ]
    for group in module["groups"]:
        cells.append(
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"## {group['slug'].replace('_', ' ')}\n",
                    "Write your prediction, run, and compare with the lesson explanation.\n",
                ],
            }
        )
        cells.append(
            {
                "cell_type": "code",
                "execution_count": None,
                "outputs": [],
                "metadata": {},
                "source": [
                    "from common.config import ROOT\n",
                    "import sys\nfrom common.process import run_process, offline_environment\n",
                    f"result = run_process([sys.executable, '-m', 'common.offline', str(ROOT / {str((Path(module['path']) / 'examples' / group['example']).with_suffix('.py')).replace(chr(92), '/')!r})], cwd=ROOT, timeout=120, env=offline_environment())\n",
                    "print(result.stdout)\nassert result.returncode == 0, result.stdout\n",
                ],
            }
        )
    for index, cell in enumerate(cells):
        cell["id"] = f"{module['id']}-cell-{index}"
    write_json(
        directory / "notebook.ipynb",
        {
            "cells": cells,
            "metadata": {
                "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}
            },
            "nbformat": 4,
            "nbformat_minor": 5,
        },
    )
    for group in module["groups"]:
        loaded = load_module((directory / "examples" / group["example"]).with_suffix(".py"))
        builder = getattr(loaded, "build_graph", None)
        if builder and all(
            parameter.default is not inspect.Parameter.empty
            for parameter in inspect.signature(builder).parameters.values()
        ):
            write(
                directory / "examples" / (Path(group["example"]).stem + ".mmd"),
                builder().get_graph().draw_mermaid(),
            )


def write_use_case(module: dict) -> None:
    version = module["copilot_version"]
    bodies = {
        "B1": 'from common.config import ROOT\nfrom common.loading import load_module\nreturn load_module(ROOT / "modules/bonus/B1_langgraph_js/examples/03_typescript_agents.py").run()',
        "B2": 'from common.config import ROOT\nfrom common.loading import load_module\nreturn load_module(ROOT / "modules/bonus/B2_deep_agents/examples/03_deep_subagents.py").run()',
        "B3": 'from common.config import ROOT\nfrom common.loading import load_module\nreturn load_module(ROOT / "modules/bonus/B3_mini_langgraph/examples/02_mini_reducers.py").run()',
        "B4": 'from common.config import ROOT\nfrom common.loading import load_module\nreturn load_module(ROOT / "modules/bonus/B4_whats_new/examples/03_typed_approvals.py").run()',
        "18": "from common.app_demo import run_demo\nreturn run_demo(approve=True, stale=True)",
        "19": 'from common.evaluation import evaluate_file\nreturn evaluate_file("eval/routing.jsonl")',
        "20": 'from common.config import ROOT\nfrom common.loading import load_module\nreturn load_module(ROOT / "modules/20_observability_and_debugging/examples/03_optional_tracing.py").run()',
        "21": 'from common.app_demo import run_demo\nreturn {"approved": run_demo(approve=True), "rejected": run_demo(approve=False)}',
        "22": "from common.app_demo import run_demo\nreturn run_demo(approve=True, stale=True)",
        "13": 'result = copilot.run(load_submission(1))\nreturn {"risk_flags": result["risk_flags"], "claim_id": result["claim"]["claim_id"]}',
        "14": 'result = copilot.run(load_submission(1))\nreturn {"specialists": result["specialist_reports"], "approved": result["approved"]}',
        "15": 'result = copilot.run(load_submission(1))\nreturn {"route": result["route"], "letter": result["letter"], "risk_flags": result["risk_flags"]}',
        "16": 'from common.config import ROOT\nfrom common.loading import load_module\nmcp = load_module(ROOT / "modules/16_external_systems_and_mcp/examples/03_mcp_adapter.py").run()\nresult = copilot.run(load_submission(1))\nreturn {"mcp_evidence": mcp["claim"], "risk_flags": result["risk_flags"]}',
        "17": 'result = copilot.run(load_submission(1), approved=False)\nreturn {"waited_days": result["waited_days"], "approved": result["approved"], "documents": result["claim"]["documents"]}',
        "08": 'result = copilot.run(load_submission(1))\nreturn {"extracted": result["extracted"], "route": result["route"], "approved": result["approved"]}',
        "09": 'result = copilot.run(load_submission(1))\nreturn {"tools": [item["tool"] for item in result["policy_evidence"]], "explanation": result["agent_explanation"]}',
        "10": 'result = copilot.run({**load_submission(1), "amount_cents": 600000}, approved=False)\nreturn {"approved": result["approved"], "route": result["route"], "explanation": result["agent_explanation"]}',
        "11": 'result = copilot.run(load_submission(1), preference="sms")\nreturn {"preference": result["preference"], "audit": result["audit"]}',
        "12": 'result = copilot.run(load_submission(1))\nreturn {"letter": result["letter"], "accepted": result["letter_accepted"], "attempts": result["letter_attempts"]}',
        "00": 'return {"complete": copilot.run(load_submission(1)), "missing": copilot.run(load_submission(7))}',
        "01": 'return copilot.run({**load_submission(1), "description": "  Pipe burst  "})',
        "02": 'result = copilot.run({**load_submission(1), "description": "", "loss_date": None})\nreturn {"missing": result["missing"], "findings": result["findings"], "audit": result["audit"]}',
        "03": 'return {str(amount): copilot.run({**load_submission(1), "amount_cents": amount})["route"] for amount in (100000, 100001, 500001)}',
        "04": 'claim = {**load_submission(1), "documents": ["DOC-001", "DOC-011", "DOC-021"]}\nresult = copilot.run(claim)\nreturn {"route": result["route"], "findings": sorted(result["findings"])}',
        "05": 'graph = copilot.build_graph()\nclaim = load_submission(1)\nconfig = {"configurable": {"thread_id": claim["claim_id"]}}\ngraph.invoke({"claim": claim, "audit": [], "findings": []}, config, version="v2")\nresult = graph.invoke({"claim": {**claim, "documents": []}}, config, version="v2").value\nreturn {"audit": result["audit"], "checkpoints": len(list(graph.get_state_history(config)))}',
        "06": 'claim = {**load_submission(1), "amount_cents": 600000}\nreturn {"approved": copilot.run(claim, approved=True)["approval_reason"], "rejected": copilot.run(claim, approved=False)["approval_reason"]}',
        "07": 'graph = copilot.build_graph()\nclaim = {**load_submission(1), "amount_cents": 600000}\nconfig = {"configurable": {"thread_id": claim["claim_id"]}}\npaused = graph.invoke({"claim": claim, "audit": [], "findings": []}, config, version="v2")\nhistory = list(graph.get_state_history(config))\nreturn {"requests": [item.value for item in paused.interrupts], "pending": list(graph.get_state(config).next), "steps": sorted(item.metadata["step"] for item in history)}',
    }
    body = bodies[module["id"]]
    source = (
        f'"""Claims Copilot v{version:02d}: {module["use_case"]} No live model or external effects."""\n'
        f"from common.copilot import v{version:02d} as copilot\n"
        "from common.data import load_submission\nfrom common.pretty import print_state\n\n"
        "def run() -> dict:\n"
        + textwrap.indent(body, "    ")
        + '\n\ndef main() -> None:\n    print_state(run())\n\nif __name__ == "__main__":\n    main()\n'
    )
    write(ROOT / module["path"] / "use_case/claims_copilot.py", source)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int, default=7)
    parser.add_argument("--modules", nargs="+", help="Rebuild only selected module IDs.")
    parser.add_argument("--bonuses", action="store_true")
    parser.add_argument(
        "--docs-only",
        action="store_true",
        help="Refresh lessons from already checked fixtures without rewriting task programs.",
    )
    arguments = parser.parse_args()
    catalog = json.loads((ROOT / "docs/planning/course_catalog.json").read_text("utf-8"))
    manifest = json.loads((ROOT / "gym/manifest.json").read_text("utf-8"))
    for module in catalog["modules"]:
        if arguments.modules and module["id"] not in arguments.modules:
            continue
        if module["id"].isdigit() and int(module["id"]) > arguments.through:
            continue
        if not module["id"].isdigit() and not arguments.bonuses:
            continue
        for group in module["groups"]:
            if group["id"] in LABS:
                if arguments.docs_only:
                    cases = json.loads(
                        (ROOT / module["path"] / "tests" / (group["slug"] + ".json")).read_text(
                            "utf-8"
                        )
                    )
                    LABS[group["id"]]["inputs"] = [case["input"] for case in cases]
                    LABS[group["id"]]["observations"] = [case["expected"] for case in cases]
                else:
                    build_group(module, group, LABS[group["id"]], manifest)
        build_module(module, catalog["modules"])
        manifest["milestones"][module["id"]] = [
            module["id"] + "-" + suffix for suffix in ("01", "02", "09", "10", "17", "18")
        ]
        print(f"Built {module['id']} teaching package.", flush=True)
    manifest["phase"] = max(
        manifest["phase"],
        (
            7
            if arguments.bonuses
            else 6
            if arguments.through >= 18
            else 5
            if arguments.through >= 13
            else 4
            if arguments.through >= 8
            else 3
        ),
    )
    manifest["milestone_note"] = "Complete guided milestones are active for released modules."
    write_json(ROOT / "gym/manifest.json", manifest)
    write_json(ROOT / "docs/planning/course_catalog.json", catalog)
    # Templates retain intentional fault anchors; published code follows Ruff's style.
    subprocess.run(
        [sys.executable, "-m", "ruff", "check", "modules", "gym/tasks", "--fix"],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        [sys.executable, "-m", "ruff", "format", "modules", "gym/tasks"], cwd=ROOT, check=True
    )


if __name__ == "__main__":
    main()
