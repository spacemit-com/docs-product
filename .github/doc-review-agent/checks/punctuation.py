"""Check: half-width punctuation in zh/ files that should be full-width."""
import re

# Half-width → full-width mapping for common sentence-ending / clause punctuation
_RULES = [
    (re.compile(r"(?<=[^\d/\w])\.(?![a-zA-Z0-9])"  ), "。", "."),   # exclude decimals, file paths, and extensions
    (re.compile(r","             ), "，", ","),
    (re.compile(r"\?"           ), "？", "?"),
    (re.compile(r"!(?!\[)"      ), "！", "!"),   # exclude markdown image syntax ![...]
]


def run(path: str, content: str, cfg: dict) -> list[dict]:
    scope = cfg.get("scope", "zh")
    if not path.replace("\\", "/").startswith(scope + "/"):
        return []
    issues = []
    for lineno, line in enumerate(content.splitlines(), 1):
        # Skip code blocks and inline code
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("|"):
            continue
        # Remove inline code spans before checking
        clean = re.sub(r"`[^`]+`", "", line)
        for regex, full, half in _RULES:
            if regex.search(clean):
                issues.append({"line": lineno, "msg": f"Use full-width '{full}' instead of '{half}'"})
    return issues
