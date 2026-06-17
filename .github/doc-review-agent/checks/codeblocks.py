"""Check: fenced code blocks missing a language tag."""


def run(path: str, content: str, cfg: dict) -> list[dict]:
    issues = []
    for lineno, line in enumerate(content.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith("```") and stripped == "```":
            issues.append({"line": lineno, "msg": "Fenced code block has no language tag"})
    return issues
