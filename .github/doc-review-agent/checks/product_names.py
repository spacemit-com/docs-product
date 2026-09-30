"""Check: product name casing rules (case-insensitive match, exact-case enforcement).

Only prose is checked. Link/image targets are file paths whose casing is
governed by the file on disk, not by branding rules, so they are excluded
(along with inline code, HTML tags, and URLs). Applying branding rules to
paths is what pushes authors to rename references and break case-sensitive
builds.
"""
import re

from . import _paths

_HTML_TAG_RE = re.compile(r"<[^>]+>")
_URL_RE = re.compile(r"https?://\S+")


def _prose_only(line: str) -> str:
    """Reduce a line to prose: drop code, links/paths, HTML tags, and URLs."""
    text = _paths.strip_code_spans(line)
    # Keep a link's display text but drop its target path.
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    # Drop bare HTML image/script tags and standalone path-like tokens.
    text = _HTML_TAG_RE.sub("", text)
    text = _URL_RE.sub("", text)
    # Any remaining token that looks like a path or filename is not prose.
    text = re.sub(r"\S*[/\\]\S*", "", text)
    text = re.sub(r"\S+\.(?:md|png|jpe?g|gif|webp|svg|ya?ml|json|pdf|xls[x]?|brd|dsn)\b",
                  "", text, flags=re.IGNORECASE)
    return text


def run(path: str, content: str, cfg: dict) -> list[dict]:
    rules: dict = cfg.get("rules", {})
    issues = []
    for lineno, line in _paths.iter_content_lines(content):
        clean = _prose_only(line)
        for wrong, correct in rules.items():
            for m in re.finditer(re.escape(wrong), clean, re.IGNORECASE):
                if m.group() != correct:
                    issues.append({"line": lineno,
                                   "msg": f"Product name casing: use '{correct}' not '{m.group()}'"})
    return issues
