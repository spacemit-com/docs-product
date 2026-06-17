"""Check: heading hierarchy — single H1, no skipped levels."""
import re


def run(path: str, content: str, cfg: dict) -> list[dict]:
    issues = []
    headings = [(i + 1, len(m.group(1)), m.group(2).strip())
                for i, line in enumerate(content.splitlines())
                if (m := re.match(r"^(#{1,6})\s+(.*)", line))]

    h1s = [h for h in headings if h[1] == 1]
    if len(h1s) == 0:
        issues.append({"line": 1, "msg": "No H1 heading found"})
    elif len(h1s) > 1:
        for lineno, _, text in h1s[1:]:
            issues.append({"line": lineno, "msg": f"Duplicate H1: '{text}'"})

    prev_level = 0
    for lineno, level, text in headings:
        if level > prev_level + 1 and prev_level != 0:
            issues.append({"line": lineno, "msg": f"Heading level skipped: H{prev_level} → H{level} ('{text}')"})
        prev_level = level
    return issues
