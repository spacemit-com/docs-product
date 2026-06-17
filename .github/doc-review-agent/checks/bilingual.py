"""Check: bilingual mirror parity between en/ and zh/."""
import os


def run(repo_root: str, changed_files: list[str], cfg: dict) -> list[dict]:
    src = cfg.get("source_dir", "en")
    tgt = cfg.get("target_dir", "zh")
    issues = []
    for f in changed_files:
        # Normalize to forward slashes for comparison
        rel = f.replace("\\", "/")
        if rel.startswith(src + "/"):
            mirror = tgt + rel[len(src):]
            if not os.path.exists(os.path.join(repo_root, mirror)):
                issues.append({"file": f, "line": 1, "msg": f"No '{tgt}/' mirror for '{f}'"})
        elif rel.startswith(tgt + "/"):
            mirror = src + rel[len(tgt):]
            if not os.path.exists(os.path.join(repo_root, mirror)):
                issues.append({"file": f, "line": 1, "msg": f"No '{src}/' mirror for '{f}'"})
    return issues
