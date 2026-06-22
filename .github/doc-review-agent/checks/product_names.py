"""Check: product name casing rules (case-insensitive match, exact-case enforcement)."""
import re


def run(path: str, content: str, cfg: dict) -> list[dict]:
    rules: dict = cfg.get("rules", {})
    issues = []
    for lineno, line in enumerate(content.splitlines(), 1):
        clean = re.sub(r"`[^`]+`", "", line)          # ignore inline code
        clean = re.sub(r"https?://\S+", "", clean)    # ignore URLs (e.g. spacemit.com)
        for wrong, correct in rules.items():
            # Match the wrong casing but not the correct one
            for m in re.finditer(re.escape(wrong), clean, re.IGNORECASE):
                if m.group() != correct:
                    issues.append({"line": lineno,
                                   "msg": f"Product name casing: use '{correct}' not '{m.group()}'"})
    return issues
