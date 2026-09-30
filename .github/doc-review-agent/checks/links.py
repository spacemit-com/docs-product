"""Check: link, image, and anchor targets.

Validates relative .md links, markdown images, HTML <img src="...">, and HTML
<a href="...">, then resolves ``#fragment`` anchors against the real
headings/ids of the target page.

Verification is intentionally case-sensitive so it behaves identically on
Windows/macOS (case-insensitive) and Linux/CI (case-sensitive). A reference
that matches a real file only by case is reported as a wrong-case reference,
*with the corrected reference text*: the fix is always to correct the
reference, never to rename the file. Every path segment is compared, so a
wrong-case directory (e.g. ``Static/``) is caught too.
"""
import os

from . import _paths

_HINT = "fix the reference to match the file name exactly (do not rename the file)"

_EXT_SUFFIXES = ("", ".md", ".html", ".htm")


def _exact(target: str) -> bool:
    """True only when the on-disk entry matches `target` exactly, case included."""
    return _paths.case_mismatches(target) == []


def _classify(href: str, kind: str) -> str:
    """Return 'image' or 'link' for messaging purposes."""
    if kind == "Image" or href.lower().endswith(_paths.IMG_EXTS):
        return "image"
    return "link"


def _anchor_file(raw: str, base: str):
    """Return (scope, path) for an href that carries a fragment.

    scope is "file" (path resolved), "self" (in-page anchor), or "external"
    (skip). ``path`` is the file whose anchors should be checked.
    """
    path_part = raw.partition("#")[0]
    if not path_part:
        return "self", ""
    if path_part.startswith(("http://", "https://", "//", "/")):
        return "external", ""     # remote or site-absolute
    target = os.path.normpath(os.path.join(base, path_part))
    if _exact(target):
        return "file", target
    for suffix in _EXT_SUFFIXES[1:]:
        if _exact(target + suffix):
            return "file", target + suffix
    return "external", ""         # path already reported: do not double-report


def run(path: str, content: str, cfg: dict) -> list[dict]:
    issues = []
    base = os.path.dirname(path)
    cache: dict = {}
    for lineno, line in _paths.iter_content_lines(content):
        clean = _paths.strip_code_spans(line)
        for kind, raw in _paths.iter_targets(clean):
            path_part, _, frag = raw.partition("#")
            label = _classify(raw, kind)

            if path_part and not _paths.is_external(path_part):
                if path_part.startswith("/"):
                    continue          # site-absolute, resolved by the static site
                target = os.path.normpath(os.path.join(base, path_part))
                if not _exact(target):
                    bad = _paths.case_mismatches(target)
                    if bad:
                        fixed = _paths.apply_case_fix(path_part, bad)
                        shown = fixed + (f"#{frag}" if frag else "")
                        issues.append({"line": lineno, "msg": (
                            f"{label.capitalize()} path case mismatch: {raw!r}; "
                            f"use {shown!r}. {_HINT}")})
                    else:
                        issues.append({"line": lineno,
                                       "msg": f"Missing {label}: {raw!r}"})
                    continue

            # '..md#frag' or in-page '#frag'
            if not frag:
                continue
            scope, tgt = _anchor_file(raw, base)
            if scope == "external":
                continue
            if scope == "self":
                tgt = path
            ids = cache.get(tgt)
            if ids is None:
                try:
                    with open(tgt, encoding="utf-8") as fh:
                        ids = _paths.heading_ids(fh.read())
                except OSError:
                    continue
                cache[tgt] = ids
            if frag.lower() not in ids:
                where = (os.path.basename(path) if tgt == path
                         else os.path.relpath(tgt, base))
                issues.append({"line": lineno, "msg": (
                    f"Missing anchor: '#{frag}' not found in '{where}'")})
    return issues
