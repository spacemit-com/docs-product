"""Shared helpers for path checks: markdown targets, HTML src/href, case-sensitive lookup."""
import os
import re

# Markdown inline link/image: optional leading '!', link text, then the target.
_LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)\)")

# Raw HTML image tags, e.g. <img src="static/x.png" width="800">
_HTML_IMG_RE = re.compile(r"""<img[^>]*?\bsrc\s*=\s*["']([^"']+)["']""", re.IGNORECASE)

# Raw HTML anchors, e.g. <a href="other.md#section">
_HTML_LINK_RE = re.compile(r"""<a[^>]*?\bhref\s*=\s*["']([^"']+)["']""", re.IGNORECASE)

_HEADING_RE = re.compile(r"^#{1,6}\s+(.*)")
_EXPLICIT_ID_RE = re.compile(r"\{#([\w\-]+)\}")
_HTML_ANCHOR_RE = re.compile(r"""<a\s+[^>]*?(?:name|id)\s*=\s*["']([^"']+)["']""", re.IGNORECASE)

_EXTERNAL_PREFIXES = ("http://", "https://", "//", "mailto:", "data:", "#")

IMG_EXTS = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp", ".avif", ".ico")


def is_external(href: str) -> bool:
    return href.startswith(_EXTERNAL_PREFIXES)


def strip_code_spans(line: str) -> str:
    """Drop `inline code` so examples inside backticks are not checked."""
    return re.sub(r"`[^`]+`", "", line)


def iter_content_lines(content: str):
    """Yield (lineno, line) for lines outside fenced ``` code blocks."""
    in_fence = False
    fence = ""
    for lineno, line in enumerate(content.splitlines(), 1):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence, fence = True, marker
            elif marker == fence:
                in_fence, fence = False, ""
            continue
        if in_fence:
            continue
        yield lineno, line


def iter_targets(line: str):
    """Yield (kind, href) for links, images, and raw HTML src/href on a line.

    The href is returned with its ``#fragment`` intact; callers split it off
    with :func:`split_href` when they need the path alone.
    """
    for m in _LINK_RE.finditer(line):
        bang, _text, href = m.group(1), m.group(2), m.group(3)
        kind = "Image" if bang else "Link"
        yield kind, href
    for m in _HTML_IMG_RE.finditer(line):
        yield "Image", m.group(1)
    for m in _HTML_LINK_RE.finditer(line):
        yield "Link", m.group(1)


def split_href(href: str):
    """Split an href into (path, fragment). Either part may be empty."""
    path, _, frag = href.partition("#")
    return path, frag


def split_components(target: str):
    """Split a path into (anchor_dir, [components]) for case walking.

    ``..`` segments are resolved first so the walk only ever descends into
    real directory entries. ``anchor_dir`` is the root the walk starts from
    (drive root, filesystem root, or '' for purely relative paths).
    """
    target = os.path.abspath(target) if os.pardir in target else target
    drive, rest = os.path.splitdrive(os.path.normpath(target))
    parts = [p for p in rest.split(os.sep) if p not in ("", ".")]
    if drive:
        anchor = drive + os.sep
    elif rest.startswith(os.sep):
        anchor = os.sep
    else:
        anchor = ""
    return anchor, parts


def case_mismatches(target: str):
    """Return [(wrong, right)] for path segments that differ only by case.

    Returns ``None`` when some segment does not exist at all — that is a
    genuinely missing target, which the caller reports separately. Every
    segment is checked, so a wrong-case *directory* (e.g. ``Static/``) is
    caught just like a wrong-case file name.
    """
    anchor, parts = split_components(target)
    if not parts:
        return None
    cur = anchor or "."
    bad = []
    for part in parts:
        try:
            entries = os.listdir(cur)
        except OSError:
            return None
        actual = {e.lower(): e for e in entries}.get(part.lower())
        if actual is None:
            return None
        if actual != part:
            bad.append((part, actual))
        cur = os.path.join(cur, actual)
    return bad


def apply_case_fix(href: str, bad) -> str:
    """Rewrite `href` replacing each wrong-case segment with its real name."""
    pairs = {wrong.lower(): right for wrong, right in bad}
    return "/".join(pairs.get(seg.lower(), seg) for seg in href.split("/"))


def slugify(text: str) -> str:
    """Approximate the heading slug GitHub/Docusaurus generate."""
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return text.replace(" ", "-")


def heading_ids(content: str) -> set:
    """Collect anchor ids a page exposes: heading slugs, {#id}, and <a name/id>."""
    ids = set()
    for _, line in iter_content_lines(content):
        m = _HEADING_RE.match(line)
        if m:
            text = m.group(1).strip()
            explicit = _EXPLICIT_ID_RE.search(text)
            if explicit:
                ids.add(explicit.group(1).lower())
                text = _EXPLICIT_ID_RE.sub("", text).strip()
            if text:
                ids.add(slugify(text))
        for aid in _EXPLICIT_ID_RE.findall(line):
            ids.add(aid.lower())
        for aid in _HTML_ANCHOR_RE.findall(line):
            ids.add(aid.lower())
    return ids
