"""Check Markdown paths and anchors offline; --external also checks public URLs."""

import argparse
import concurrent.futures
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from common.data import ROOT
from common.files import source_files


def prose(text: str) -> str:
    return re.sub(r"^(`{3,}|~{3,}).*?^\1\s*$", "", text, flags=re.MULTILINE | re.DOTALL)


def anchors(path: Path) -> set[str]:
    result = set()
    occurrences: dict[str, int] = {}
    for line in prose(path.read_text("utf-8-sig")).splitlines():
        match = re.match(r"^#{1,6}\s+(.+)", line)
        if not match:
            continue
        title = re.sub(r"<[^>]+>", "", match.group(1)).lower()
        slug = "".join(
            char for char in title if char in "-_ " or unicodedata.category(char)[0] in "LN"
        ).replace(" ", "-")
        count = occurrences.get(slug, 0)
        occurrences[slug] = count + 1
        result.add(slug if count == 0 else f"{slug}-{count}")
    return result


def check_external(url: str) -> str | None:
    for attempt in range(3):
        try:
            request = urllib.request.Request(
                url, headers={"User-Agent": "LarkspurCourseLinkCheck/1.0"}
            )
            with urllib.request.urlopen(request, timeout=20) as response:
                if response.status < 400:
                    return None
        except (urllib.error.URLError, OSError, ValueError) as error:
            if attempt == 2:
                return f"{url}: {error}"
            time.sleep(0.25 * (attempt + 1))
    return f"{url}: no successful response"


def check_links(root: Path = ROOT, *, external: bool = False) -> tuple[int, list[str]]:
    count = 0
    errors = []
    urls = set()
    for file in source_files(root):
        if file.suffix.lower() != ".md":
            continue
        text = prose(file.read_text("utf-8-sig"))
        for match in re.finditer(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", text):
            target = match.group(1).strip("<>")
            if target.startswith(("http://", "https://")):
                urls.add(target)
                continue
            if re.match(r"^[a-z]+:", target):
                continue
            path, _, fragment = target.partition("#")
            resolved = (file.parent / urllib.parse.unquote(path)).resolve() if path else file
            count += 1
            if not resolved.exists():
                errors.append(f"{file.relative_to(root)}: missing {path}")
            elif (
                fragment
                and resolved.suffix == ".md"
                and urllib.parse.unquote(fragment) not in anchors(resolved)
            ):
                errors.append(f"{file.relative_to(root)}: missing anchor {target}")
    if external:
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            errors.extend(error for error in pool.map(check_external, sorted(urls)) if error)
        count += len(urls)
    return count, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--external", action="store_true")
    arguments = parser.parse_args()
    count, errors = check_links(external=arguments.external)
    for error in errors:
        print(error)
    print(f"{count} links checked; {len(errors)} problems.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
