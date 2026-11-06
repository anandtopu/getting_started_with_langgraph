"""Refresh runtime evidence without rewriting starters, answers, or grading contracts."""

import json

from common.loading import load_module
from gym.catalog import Catalog
from scripts.authoring.traces import capture


def main():
    recorded = 0
    for task in Catalog().available():
        path = task.folder / "trace.json"
        if task.type != "trace" or not path.is_file():
            continue
        cases = [row["input"] for row in json.loads(path.read_text("utf-8"))["cases"]]
        evidence = capture(load_module(task.folder / "trace.py"), cases)
        expected = json.loads((task.folder / "expected_answer.json").read_text("utf-8"))
        if [row["observed_result"] for row in evidence["cases"]] != expected["observations"]:
            raise ValueError(f"{task.id}: trace observations disagree with its grading answer")
        path.write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        recorded += any(row["node_updates"] for row in evidence["cases"])
        print("Captured", task.id, flush=True)
    print(
        f"{recorded} generated trace packages contain in-process node updates; other packages explicitly label the limits of local callbacks."
    )


if __name__ == "__main__":
    main()
