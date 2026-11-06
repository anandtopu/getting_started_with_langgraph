"""An owned worker failure must reach its supervisor as a failed process."""

import json
import sys

from common.config import ROOT
from common.process import offline_environment, run_process


def test_generated_durability_worker_preserves_error_exit_and_details(tmp_path):
    script = ROOT / "gym/tasks/17/17-03_durable_side_effects_predict/solution.py"
    result = run_process(
        [
            sys.executable,
            "-m",
            "common.offline",
            str(script),
            "--worker",
            str(tmp_path),
            json.dumps({"claim_id": "CLM-0001"}),
            "resume",
        ],
        cwd=ROOT,
        env=offline_environment(),
    )
    assert result.returncode != 0
    assert "KeyError" in result.stdout and "durability" in result.stdout
    assert "observed_error" not in result.stdout
