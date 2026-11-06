"""Validate catalog structure now and complete course coverage with --release."""

import argparse
import json

from common.data import ROOT
from gym.catalog import Catalog


def check_coverage(*, release: bool = False) -> list[str]:
    catalog = Catalog()
    source = json.loads((ROOT / "docs/planning/course_catalog.json").read_text("utf-8"))
    errors = []
    required_sections = (
        "Prerequisites",
        "Learning objectives",
        "The big idea",
        "How it works",
        "Key APIs at a glance",
        "Walkthrough",
        "When to use it, and when not to",
        "Real-world use case",
        "Common bugs",
        "Practice",
        "Quiz",
        "Key takeaways",
        "Go deeper",
        "Next:",
    )
    for module in source["modules"]:
        tasks = [task for group in module["groups"] for task in group["tasks"]]
        if len(tasks) < 6 or len({task["type"] for task in tasks}) < 4:
            errors.append(f"{module['id']}: insufficient planned task coverage.")
        if {task["level"] for task in tasks} != {"easy", "medium", "hard"}:
            errors.append(f"{module['id']}: missing difficulty levels.")
        for group in module["groups"]:
            if len(group["tasks"]) < 6:
                errors.append(f"{group['id']}: fewer than six planned feature tasks.")
        if release:
            directory = ROOT / module["path"]
            readme = directory / "README.md"
            if not readme.is_file():
                errors.append(f"{module['id']}: module README not released.")
                continue
            content = readme.read_text("utf-8")
            for section in required_sections:
                if section not in content:
                    errors.append(f"{module['id']}: missing README section {section}.")
            if "Predict, then run" not in content:
                errors.append(f"{module['id']}: no prediction exercise.")
            for group in module["groups"]:
                if not (directory / "examples" / group["example"]).is_file():
                    errors.append(f"{group['id']}: example missing.")
            for leaf in ("quiz.md", "notebook.ipynb"):
                if not (directory / leaf).is_file():
                    errors.append(f"{module['id']}: {leaf} missing.")
    if release and len(catalog.available()) != len(catalog.tasks):
        errors.append("The complete task catalog is not yet released.")
    if release:
        capstones = list((ROOT / "capstones").glob("[0-9][0-9]_*"))
        if len(capstones) != 5:
            errors.append("Release requires five capstones.")
        for folder in capstones:
            for leaf in (
                "README.md",
                "diagram.mmd",
                "starter.py",
                "solution.py",
                "tests/test_solution.py",
                "eval/cases.jsonl",
                "rubric.md",
                "extend_it.md",
            ):
                if not (folder / leaf).is_file():
                    errors.append(f"{folder.name}: missing {leaf}")
        for leaf in (
            "MENTAL_MODEL.md",
            "CHOOSING_THE_RIGHT_DESIGN.md",
            "COMMON_BUGS.md",
            "GLOSSARY.md",
            "TROUBLESHOOTING.md",
            "DEPLOYMENT.md",
        ):
            if not (ROOT / "docs" / leaf).is_file():
                errors.append(f"Missing course guide: {leaf}")
        for name in ("tier_1", "tier_2", "tier_3", "tier_4", "api_at_a_glance"):
            if not (ROOT / "cheatsheets" / (name + ".pdf")).is_file():
                errors.append(f"Missing printable: {name}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release", action="store_true")
    arguments = parser.parse_args()
    errors = check_coverage(release=arguments.release)
    for error in errors:
        print(error)
    print(f"{'Release' if arguments.release else 'Planning'} coverage: {len(errors)} problems.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
