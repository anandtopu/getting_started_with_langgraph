"""Package five working projects with independent acceptance checks and faulty starters."""

import json

from common.config import ROOT
from common.loading import load_module

PROJECTS = [
    (
        "01_claims_intake_engine",
        "Claims Intake Engine",
        "01–07",
        None,
        "As an adjuster, I can reopen a high-value claim after restart, approve or reject it, and inspect its saved history.",
        [("approved", True), ("replay_matches", True), ("waited", True)],
        [
            (
                {},
                {
                    "approved": True,
                    "waited": True,
                    "replay_matches": True,
                    "replayed_nodes": ["normalize", "validate", "review_document", "route"],
                },
            ),
            ({"approved": False}, {"approved": False}),
            ({"amount_cents": 10000}, {"approved": True, "waited": False}),
        ],
        '"approved": case["approved"]',
        '"approved": True',
        "Approval must preserve an explicit rejection; small eligible claims may auto-route.",
    ),
    (
        "02_policy_qa_with_memory",
        "Policy Q&A Agent with Memory",
        "08–12",
        None,
        "As a customer, I can ask a policy question, inspect its source, and retain my contact preference without seeing another customer's memory.",
        [("citations", ["home.md"]), ("preference", "sms")],
        [
            ({}, {"citations": ["home.md"], "preference": "sms"}),
            ({"customer_id": "CUS-0002"}, {"preference": "email"}),
            ({"question": "quasarxyz"}, {"citations": []}),
            ({"question": "renters deductible"}, {"citations": ["renters.md"]}),
        ],
        'runtime.context.customer_id), "contact"',
        '"CUS-0001"), "contact"',
        "Customer memory must use the active identity; unknown questions must abstain.",
    ),
    (
        "03_fraud_investigation_team",
        "Fraud Investigation Team",
        "13–17",
        "mcp",
        "As an investigator, I can gather read-only MCP evidence and consult two scoped specialists without treating a risk flag as a verdict.",
        [("specialists", ["fraud_analyst", "communication_specialist"])],
        [
            (
                {},
                {
                    "specialists": ["fraud_analyst", "communication_specialist"],
                    "risk_flags": ["high_value"],
                },
            ),
            ({"amount_cents": 10000}, {"risk_flags": []}),
            ({"claim_id": "CLM-0002"}, {"error": "ValueError"}),
        ],
        '"risk_flags": result["risk_flags"]',
        '"risk_flags": []',
        "The reusable fraud graph must retain evidence-review flags and reject mismatched evidence.",
    ),
    (
        "04_larkspur_claims_copilot",
        "Larkspur Claims Copilot",
        "18–22",
        "apps",
        "As a customer, I can submit a claim and see progress; as an adjuster, I can resume its durable wait and authorize a single synthetic effect.",
        [("created", 201), ("effects", 1), ("customer_approval_status", 403)],
        [
            ({}, {"effects": 1, "foreign_status": 404, "stale_status": 409, "status": "recorded"}),
            (
                {"approved": False},
                {"effects": 0, "status": "not_approved", "customer_approval_status": 403},
            ),
        ],
        'approve=case["approved"]',
        "approve=True",
        "A rejected claim must never enter the synthetic effect ledger; stale approvals and foreign access must fail.",
    ),
    (
        "05_design_your_own",
        "Design Your Own: Invoice Approval",
        "18–22",
        None,
        "As an invoice owner, I can request approval; only an authenticated approver may decide, and replay cannot duplicate the effect.",
        [("approved", True), ("effects", 1)],
        [
            ({}, {"approved": True, "effects": 1}),
            ({"approved": False}, {"approved": False, "effects": 0}),
            ({"role": "customer"}, {"error": "PermissionError"}),
            ({"amount_cents": -1}, {"error": "ValueError"}),
            ({"amount_cents": True}, {"error": "ValueError"}),
            ({"approved": "yes"}, {"error": "ValueError"}),
        ],
        'if state["approved"]:',
        "if True:",
        "Only positive integer amounts and explicit authorized approvals may produce effects.",
    ),
]


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def main():
    for slug, title, prerequisites, extra, story, checks, cases, old, new, contract in PROJECTS:
        folder = ROOT / "capstones" / slug
        source = (folder / "solution.py").read_text("utf-8")
        assert old in source, slug
        write(
            folder / "starter.py",
            source.replace(old, "# YOUR CODE HERE\n" + old, 0)
            .replace(old, new, 1)
            .replace(
                "def run(case=None):",
                "# YOUR CODE HERE: repair the acceptance contract below.\ndef run(case=None):",
            ),
        )
        module = load_module(folder / "solution.py")
        result = module.run()
        for key, expected in checks:
            assert result[key] == expected, (slug, key, result)
        diagram = module.build_graph().get_graph(xray=True).draw_mermaid()
        write(folder / "diagram.mmd", diagram)
        write(
            folder / "eval/cases.jsonl",
            "\n".join(
                json.dumps({"input": case, "expected": expected}) for case, expected in cases
            ),
        )
        package = {"mcp": "mcp", "apps": "fastapi"}.get(extra)
        skip = f"pytest.importorskip({package!r})\n" if extra else ""
        write(
            folder / "tests/test_solution.py",
            '''"""Independent acceptance checks; select an attempt with LARKSPUR_CAPSTONE_FILE."""
import json
import os
from pathlib import Path
import pytest
from common.loading import load_module
'''
            + skip
            + """
FOLDER = Path(__file__).resolve().parents[1]
CASES = [json.loads(line) for line in (FOLDER / "eval/cases.jsonl").read_text("utf-8").splitlines()]

@pytest.mark.parametrize("case", CASES)
def test_acceptance(case):
    candidate = load_module(Path(os.environ.get("LARKSPUR_CAPSTONE_FILE", FOLDER / "solution.py")))
    expected = case["expected"]
    if "error" in expected:
        with pytest.raises(Exception) as error:
            candidate.run(case["input"])
        assert type(error.value).__name__ == expected["error"]
    else:
        actual = candidate.run(case["input"])
        for key, value in expected.items():
            assert actual[key] == value, "CAPSTONE: " + key
""",
        )
        command = "uv run " + (f"--extra {extra} " if extra else "")
        text = f"# {title}\n\nComplete modules {prerequisites} first. Estimated project time: 4–8 hours. Default model calls are scripted and cost $0.\n\n## User story\n\n{story}\n\n## Acceptance criteria\n\n{contract}\n\n"
        text += "\n".join(
            f"- Input `{json.dumps(case)}` must satisfy `{json.dumps(expected)}`."
            for case, expected in cases
        )
        text += f"\n\n## Architecture\n\nGenerated from the executable reference graph with `draw_mermaid()`; [source](diagram.mmd).\n\n```mermaid\n{diagram}\n```\n\n## Build and evaluate\n\nStart with [starter.py](starter.py), which runs but contains a behavioral fault. Keep the `run(case)` contract. Read [the evaluation cases](eval/cases.jsonl) before coding. Use a copy in workspace to preserve your work.\n\n```text\n{command}python capstones/{slug}/starter.py\n{command}python scripts/check_capstone.py {slug[:2]} --candidate capstones/{slug}/starter.py\n{command}python scripts/check_capstone.py {slug[:2]} --candidate capstones/{slug}/solution.py\n```\n\nThe checker loads the selected candidate, not the reference. A mechanical pass does not replace design review. Explain the state boundary, authorization source, failure recovery, and every external effect using [the rubric](rubric.md).\n\n## Reference result\n\n```json\n{json.dumps(result, indent=2)}\n```\n\n[Extend it](extend_it.md) · [Complete reference](solution.py) · [Design choices](../../docs/CHOOSING_THE_RIGHT_DESIGN.md)\n"
        if slug.startswith("04"):
            text += "\n## Run the complete application\n\nThe solution exercises the real HTTP handlers in process. [FastAPI](../../apps/api.py), [dashboard](../../apps/dashboard.py), [server lifecycle](../../apps/server.py), and [Compose](../../compose.yaml) form the deployable application. Follow [deployment instructions](../../docs/DEPLOYMENT.md) for Postgres, streaming, restart recovery, credentials, and operational limits.\n"
        if slug.startswith("05"):
            text += "\n## Your design document\n\nChoose a business process and write: actors and trust boundaries; state schema and reducers; success and rejection paths; thread identity; durable waits; effect idempotency; data retention; failure tests; and deployment choice. The invoice reference is one worked example. If you choose another domain, replace the evaluation set with independently justified requirements before coding.\n"
        write(folder / "README.md", text)
        write(
            folder / "rubric.md",
            "# Self-review rubric\n\nScore each criterion 0 (missing), 1 (happy path only), or 2 (demonstrated including failure). Passing means at least 8/10, with 2 on authorization and recovery.\n\n- Correctness: all independent acceptance cases pass, with one learner-added boundary case.\n- Authorization: trusted identity is separate from user/model text; rejection cannot produce an effect.\n- Recovery: show the saved state or replay boundary and explain effect deduplication.\n- Design: justify workflow versus agent and identify the smallest useful component boundaries.\n- Operations: document dependencies, execution commands, costs, failure diagnostics, and a safe shutdown.\n\nRecord evidence and one remaining limitation for every score. Do not award design points solely because tests pass.\n",
        )
        write(
            folder / "extend_it.md",
            "# Extend it\n\n1. Add one adversarial input and a regression test that fails before your repair.\n2. Introduce a second customer or thread and prove its state and permissions remain isolated.\n3. Inject a failure immediately before and after an external effect; demonstrate bounded recovery without duplication.\n4. Add a retention policy with a dry-run report and scoped deletion tests.\n5. Compare this design with a plain-Python baseline using correctness, latency, and operational complexity.\n",
        )
        print("Built", slug, flush=True)


if __name__ == "__main__":
    main()
