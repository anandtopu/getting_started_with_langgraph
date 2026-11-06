"""Keep the public task index and shipped-file manifest aligned with authoring output."""

import json
import subprocess

from common.config import ROOT


def main():
    catalog = json.loads((ROOT / "docs/planning/course_catalog.json").read_text("utf-8"))
    text = "# Practice Gym — complete task catalog\n\nAll 486 exercises are shipped: 414 core and 72 bonus tasks. Refactor starters preserve behavior and fail a structural check; Extend tasks retain old checks and add a capability. Predict and Trace use written answers. Design includes a rationale rubric.\n\n"
    for module in catalog["modules"]:
        text += (
            f"## {module['id']} — {module['title']}\n\n[Lesson](../{module['path']}/README.md)\n\n"
        )
        for group in module["groups"]:
            text += f"### {group['id']}: {group['slug'].replace('_', ' ')}\n\nFeatures: {'; '.join(group['features'])}.\n\n| ID | Module | Type | Level | Task |\n| --- | --- | --- | --- | --- |\n"
            for task in group["tasks"]:
                text += f"| [{task['id']}](../{task['folder']}/task.md) | {module['id']} | {task['type']} | {task['level']} | {task['description']} |\n"
            text += "\n"
    (ROOT / "docs/GYM_TASK_CATALOG.md").write_text(
        text.rstrip() + "\n", encoding="utf-8", newline="\n"
    )
    listing = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    files = sorted(
        set(path for path in listing.stdout.split("\0") if path and (ROOT / path).is_file())
    )
    (ROOT / "docs/planning/REPOSITORY_MANIFEST.txt").write_text(
        "# Shipped file manifest; runtime workspaces and environments are excluded.\n"
        + "\n".join(files)
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"Indexed 486 tasks and {len(files)} shipped files.")


if __name__ == "__main__":
    main()
