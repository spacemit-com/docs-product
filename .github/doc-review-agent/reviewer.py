"""
Doc-review agent — main orchestrator.

Reads config.yml, runs enabled checks against every changed .md file,
then posts one consolidated summary comment on the PR. Never exits non-zero.
"""
import json
import os
import sys
import traceback

import requests
import yaml

# ── locate repo root and config ──────────────────────────────────────────────
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT   = os.environ.get("GITHUB_WORKSPACE", os.path.join(SCRIPT_DIR, "..", ".."))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "config.yml")

with open(CONFIG_PATH, encoding="utf-8") as f:
    CONFIG = yaml.safe_load(f)

CHECKS_CFG   = CONFIG.get("checks", {})
LLM_CFG      = CONFIG.get("llm_review", {})

# ── GitHub context ────────────────────────────────────────────────────────────
GH_TOKEN    = os.environ.get("GITHUB_TOKEN", "")
REPO        = os.environ.get("GITHUB_REPOSITORY", "")         # owner/repo
PR_NUMBER   = int(os.environ.get("PR_NUMBER", "0"))
COMMIT_SHA  = os.environ.get("GITHUB_SHA", "")

# ── check modules ─────────────────────────────────────────────────────────────
from checks import frontmatter, headings, links, placeholders, codeblocks, product_names
import llm_review
import github_poster

_GH_API = "https://api.github.com"


def gh_headers() -> dict:
    return {
        "Authorization": f"Bearer {GH_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def get_changed_md_files() -> list[dict]:
    """Return list of {filename, patch} dicts for changed .md files."""
    resp = requests.get(
        f"{_GH_API}/repos/{REPO}/pulls/{PR_NUMBER}/files",
        headers=gh_headers(),
        params={"per_page": 100},
        timeout=20,
    )
    resp.raise_for_status()
    return [f for f in resp.json() if f["filename"].endswith(".md")]


def check_cfg(name: str) -> dict | None:
    """Return check config dict if enabled, else None."""
    c = CHECKS_CFG.get(name, {})
    return c if c.get("enabled", True) else None


def run_file_checks(path: str, content: str, rel_path: str) -> list[dict]:
    issues = []
    if (c := check_cfg("frontmatter")):
        issues += [{"file": rel_path, **i} for i in frontmatter.run(path, content, c)]
    if (c := check_cfg("headings")):
        issues += [{"file": rel_path, **i} for i in headings.run(path, content, c)]
    if (c := check_cfg("links")):
        issues += [{"file": rel_path, **i} for i in links.run(path, content, c)]
    if (c := check_cfg("placeholders")):
        issues += [{"file": rel_path, **i} for i in placeholders.run(path, content, c)]
    if (c := check_cfg("codeblocks")):
        issues += [{"file": rel_path, **i} for i in codeblocks.run(path, content, c)]
    if (c := check_cfg("product_names")):
        issues += [{"file": rel_path, **i} for i in product_names.run(path, content, c)]
    return issues


def run_bilingual_check(changed_files: list[str]) -> list[dict]:
    from checks import bilingual
    c = check_cfg("bilingual")
    if not c:
        return []
    return bilingual.run(REPO_ROOT, changed_files, c)


def run_punctuation_check(path: str, content: str, rel_path: str) -> list[dict]:
    from checks import punctuation
    c = check_cfg("punctuation")
    if not c:
        return []
    return [{"file": rel_path, **i} for i in punctuation.run(rel_path, content, c)]


def build_summary(all_issues: list[dict], llm_results: dict[str, str]) -> str:
    lines = ["## 📝 Doc-Review Agent Report\n"]
    if not all_issues and not llm_results:
        lines.append("✅ No issues found.")
        return "\n".join(lines)

    by_file: dict[str, list] = {}
    for issue in all_issues:
        by_file.setdefault(issue["file"], []).append(issue)

    for fname, issues in sorted(by_file.items()):
        lines.append(f"### `{fname}`")
        for i in issues:
            lines.append(f"- Line {i.get('line', '?')}: {i['msg']}")
        if fname in llm_results:
            lines.append(f"\n**LLM review:**\n{llm_results[fname]}")
        lines.append("")

    # Files with only LLM results
    for fname, feedback in llm_results.items():
        if fname not in by_file:
            lines.append(f"### `{fname}`\n**LLM review:**\n{feedback}\n")

    lines.append("\n> ⚠️ This is an automated review. It never blocks merge.")
    return "\n".join(lines)


def main() -> None:
    if not PR_NUMBER:
        print("Not a PR context — exiting.")
        return

    try:
        pr_files = get_changed_md_files()
    except Exception:
        traceback.print_exc()
        return

    all_issues: list[dict] = []
    llm_results: dict[str, str] = {}

    for pf in pr_files:
        rel_path = pf["filename"]
        abs_path = os.path.join(REPO_ROOT, rel_path)
        patch    = pf.get("patch", "")

        try:
            with open(abs_path, encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            continue  # deleted file

        file_issues = run_file_checks(abs_path, content, rel_path)
        file_issues += run_punctuation_check(rel_path, content, rel_path)
        all_issues += file_issues

        # LLM review
        if LLM_CFG.get("enabled"):
            try:
                fb = llm_review.review(rel_path, content, LLM_CFG)
                if fb:
                    llm_results[rel_path] = fb
            except Exception:
                traceback.print_exc()

    # Bilingual mirror check (repo-wide, not per-file)
    all_issues += run_bilingual_check([pf["filename"] for pf in pr_files])

    summary = build_summary(all_issues, llm_results)
    print(summary)
    try:
        github_poster.post_summary(REPO, PR_NUMBER, summary)
    except Exception:
        traceback.print_exc()


if __name__ == "__main__":
    main()
    sys.exit(0)   # never block merge
