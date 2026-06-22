"""Post inline PR comments and a summary comment via GitHub REST API."""
import os
import requests

_GH = "https://api.github.com"


def _headers() -> dict:
    return {
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def _diff_position(diff_hunk: str, target_line: int) -> int | None:
    """Map a file line number to a diff position (1-based line in the hunk)."""
    pos = 0
    current = 0
    for diff_line in diff_hunk.splitlines():
        if diff_line.startswith("@@"):
            import re
            m = re.search(r"\+(\d+)", diff_line)
            current = int(m.group(1)) - 1 if m else 0
        elif not diff_line.startswith("-"):
            current += 1
            pos += 1
            if current == target_line:
                return pos
    return None


def post_inline(repo: str, pr_number: int, commit_sha: str,
                path: str, line: int, body: str, diff_hunk: str) -> None:
    pos = _diff_position(diff_hunk, line)
    if pos is None:
        return  # line not in diff — skip inline, will appear in summary
    requests.post(
        f"{_GH}/repos/{repo}/pulls/{pr_number}/comments",
        headers=_headers(),
        json={
            "body": body,
            "commit_id": commit_sha,
            "path": path,
            "position": pos,
        },
        timeout=15,
    ).raise_for_status()


_BOT_MARKER = "## 📝 Doc-Review Agent Report"


def _delete_previous_summary(repo: str, pr_number: int) -> None:
    """Delete any existing bot summary comment to avoid duplicates on re-runs."""
    resp = requests.get(
        f"{_GH}/repos/{repo}/issues/{pr_number}/comments",
        headers=_headers(),
        params={"per_page": 100},
        timeout=15,
    )
    if not resp.ok:
        return
    for comment in resp.json():
        if _BOT_MARKER in comment.get("body", ""):
            requests.delete(
                f"{_GH}/repos/{repo}/issues/comments/{comment['id']}",
                headers=_headers(),
                timeout=15,
            )


def post_summary(repo: str, pr_number: int, body: str) -> None:
    _delete_previous_summary(repo, pr_number)
    requests.post(
        f"{_GH}/repos/{repo}/issues/{pr_number}/comments",
        headers=_headers(),
        json={"body": body},
        timeout=15,
    ).raise_for_status()
