"""Check: YAML frontmatter presence and required keys."""
import re


def run(path: str, content: str, cfg: dict) -> list[dict]:
    issues = []
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        issues.append({"line": 1, "msg": "Missing YAML frontmatter block"})
        return issues
    import yaml
    try:
        fm = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as e:
        issues.append({"line": 1, "msg": f"Invalid YAML frontmatter: {e}"})
        return issues
    for key in cfg.get("required_keys", []):
        if key not in fm:
            issues.append({"line": 1, "msg": f"Frontmatter missing required key: '{key}'"})
    return issues
