"""Check: broken relative .md links and missing image files."""
import os
import re


_LINK_RE = re.compile(r"\[.*?\]\(([^)]+)\)")
_IMG_RE  = re.compile(r"!\[.*?\]\(([^)]+)\)")


def _is_external(href: str) -> bool:
    return href.startswith(("http://", "https://", "//", "mailto:"))


def run(path: str, content: str, cfg: dict) -> list[dict]:
    issues = []
    base = os.path.dirname(path)
    lines = content.splitlines()
    for lineno, line in enumerate(lines, 1):
        for m in _LINK_RE.finditer(line):
            href = m.group(1).split("#")[0]
            if not href or _is_external(href):
                continue
            target = os.path.normpath(os.path.join(base, href))
            if not os.path.exists(target):
                issues.append({"line": lineno, "msg": f"Broken link: '{href}'"})
        for m in _IMG_RE.finditer(line):
            src = m.group(1)
            if _is_external(src):
                continue
            target = os.path.normpath(os.path.join(base, src))
            if not os.path.exists(target):
                issues.append({"line": lineno, "msg": f"Missing image: '{src}'"})
    return issues
