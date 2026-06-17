"""Check: TBD / TODO / FIXME placeholder text."""
import re


def run(path: str, content: str, cfg: dict) -> list[dict]:
    patterns = cfg.get("patterns", ["TBD", "TODO", "FIXME"])
    regex = re.compile(r"\b(" + "|".join(re.escape(p) for p in patterns) + r")\b")
    issues = []
    for lineno, line in enumerate(content.splitlines(), 1):
        for m in regex.finditer(line):
            issues.append({"line": lineno, "msg": f"Placeholder found: '{m.group()}'"})
    return issues
