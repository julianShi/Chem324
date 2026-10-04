#!/usr/bin/env python3
"""
myst_slice.py - structurally slice a MyST-Markdown page into translatable
paragraphs plus verbatim literals, so a translator (human or LLM) never touches,
and therefore cannot damage, Markdown / MathJax / directive / HTML syntax.

The invariant this tool enforces:

  Every literal block is copied byte-for-byte from the source.  Literals are
  YAML frontmatter, fenced code, $$ math blocks, ::: directive fences and their
  :option: lines, raw HTML blocks, and link targets.  Only three kinds of thing
  are ever translated: ordinary paragraph text, headings, and directive titles.

  `verify` re-parses the finished page with the same parser and fails if any
  literal byte, inline math span, URL, or markdown marker changed, vanished or
  was duplicated.  So a hallucinating translator produces a FAIL report, never a
  silently broken page.

Subcommands
  slice  src.md [...]              -> items.json + template.md + segs.json
  apply  items.json -t zh.json     -> out.md   (-a ann.json injects notes)
  verify src.md out.md             -> structural + inline invariant report
  terms  zh.json -g glossary.tsv   -> glossary terms left bare in English

Read the segs.json / zh.json files with any editor or model; they are plain JSON
keyed by stable segment id, so translations can be produced in batches, reviewed,
and re-applied after the source page changes.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- inline spans
# Ordered alternation: math first so that $...{...}$ is never mistaken for a role.
INLINE_RE = re.compile(
    r"(?P<math>\$[^$\n]+\$)"
    r"|(?P<code>`{1,3}[^`\n]+`{1,3})"
    r"|(?P<role>\{[a-zA-Z][a-zA-Z0-9_\-]*(?:[^{}]|\{[^{}]*\})*\})"
    r"|(?P<imglink>!\[(?P<ialt>[^\]\n]*)\]\((?P<iurl>[^)\n]*)\))"
    r"|(?P<link>\[(?P<ltext>[^\]\n]*)\]\((?P<lurl>[^)\n]*)\))"
    r"|(?P<url><https?://[^>\s]+>)"
)

BACKTICK_DIRECTIVE_RE = re.compile(r"^(\s*)(`{3,})\{([a-zA-Z0-9_\-]+)\}(.*)$")
FENCE_RE = re.compile(r"^(\s*)(`{3,}|~{3,})(.*)$")
DIRECTIVE_OPEN_RE = re.compile(r"^(\s*)(:{3,})\{([a-zA-Z0-9_\-]+)\}(.*)$")
DIRECTIVE_CLOSE_RE = re.compile(r"^(\s*)(:{3,})\s*$")
OPTION_RE = re.compile(r"^\s*:[a-zA-Z0-9_\-]+:")
HEADING_RE = re.compile(r"^(#{1,6})(\s+)(.*)$")
BULLET_RE = re.compile(r"^(\s*)([-*+]|\d+[.)])(\s+)")
LINKDEF_RE = re.compile(r"^\s*\([^)]+\)\s*=\s*$")
HTML_RE = re.compile(r"^\s*</?[a-zA-Z!]")
INDENTED_CODE_RE = re.compile(r"^(?: {4}|\t)\S")

# Directives whose text after the name is NOT a title (language, filename, latex).
OPAQUE_DIRECTIVES = {"marimo", "code-cell", "code", "raw", "include", "math", "nbinput"}

CJK_RE = re.compile(r"[\u3000-\u303f\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff00-\uffef]")


# ------------------------------------------------------------------ line kinds
def _frontmatter_span(lines: list[str]) -> int:
    if not lines or lines[0].rstrip() != "---":
        return 0
    for i in range(1, len(lines)):
        if lines[i].rstrip() in ("---", "..."):
            return i + 1
    return 0


def _math_block_end(lines: list[str], i: int) -> int:
    r"""Return the index after the end of the $$ math block starting at line i.

    A display closes with `$$`, with `...$$` (text before the marker), or with a
    LABEL: `$$(fsw_odd_states_equ)`. Only testing `endswith("$$")` misses the
    labelled form, so the block is then read as a single line and the formula
    becomes a translatable "paragraph" -- which inserts a block inside the
    equation and breaks it. Testing startswith covers `$$`, `$$(label)` and
    `$$\psi$$`.
    """
    head = lines[i].strip()
    if "$$" in head[2:]:
        return i + 1
    for j in range(i + 1, len(lines)):
        s = lines[j].strip()
        if s.startswith("$$") or s.endswith("$$"):
            return j + 1
        if s == "" or (FENCE_RE.match(lines[j]) or DIRECTIVE_OPEN_RE.match(lines[j])):
            return i + 1  # unterminated: treat as one line rather than eating the file
    return i + 1


def _fence_end(lines: list[str], i: int) -> int:
    m = FENCE_RE.match(lines[i])
    marker = m.group(2)
    for j in range(i + 1, len(lines)):
        m2 = FENCE_RE.match(lines[j])
        if m2 and m2.group(2)[0] == marker[0] and len(m2.group(2)) >= len(marker):
            return j + 1
    return len(lines)


def _html_end(lines: list[str], i: int) -> int:
    for j in range(i + 1, len(lines)):
        if lines[j].strip() == "":
            return j
    return len(lines)


# ----------------------------------------------------------------- the slicer
class Slicer:
    """Turns a page into an ordered item stream: ('lit', text, line) | ('tr', ...)."""

    def __init__(self, lines: list[str], trailing_newline: bool = True):
        self.lines = lines
        # Whether the source file ended with a newline. The literal stream must
        # reproduce that exactly: some pages end with `$$` and no newline, others
        # with four blank lines. A missing or invented final newline changes the
        # file, so it is recorded rather than assumed.
        self.trailing_newline = trailing_newline
        self.items: list[dict] = []
        self._next_id = 1

    # -- emitters ----------------------------------------------------------
    def lit(self, text: str, line: int) -> None:
        if text:
            self.items.append({"t": "lit", "s": text, "line": line})

    def lit_line(self, text: str, line: int) -> None:
        """Emit one whole source line. The newline is part of the line: dropping
        it is what silently welds `:::{grid}` onto `:gutter: 2`."""
        self.items.append({"t": "lit", "s": text + "\n", "line": line})

    def tr(self, text: str, kind: str, line: int, line_map: list[int]) -> None:
        if not text.strip():
            self.lit(text, line)
            return
        self.items.append(
            {
                "t": "tr",
                "id": f"S{self._next_id:04d}",
                "kind": kind,
                "s": text,
                "line": line,
                "lines": line_map,
            }
        )
        self._next_id += 1

    # -- helpers -----------------------------------------------------------
    @staticmethod
    def _strip_heading(line: str) -> tuple[str, str]:
        m = HEADING_RE.match(line)
        if not m:
            return "", line
        return m.group(1) + m.group(2), m.group(3)

    @staticmethod
    def _strip_bullet(line: str) -> tuple[str, str]:
        m = BULLET_RE.match(line)
        if not m:
            return "", line
        return m.group(0), line[m.end():]

    # -- main walk ---------------------------------------------------------
    def run(self) -> list[dict]:
        # `load_source` already stripped the file's final newline and recorded it
        # in self.trailing_newline. Do NOT strip again here: a page ending in
        # blank lines would lose one and gain a phantom elsewhere.
        lines = self.lines
        n = len(lines)
        i = _frontmatter_span(lines)
        if i:
            self.lit("\n".join(lines[:i]) + "\n", 1)

        para: list[str] = []
        para_line0 = 0
        para_lines: list[int] = []

        def flush(terminate: bool = True) -> None:
            """Emit the open paragraph and ALWAYS terminate its last line.

            This single rule makes the walk lossless: every source line ends in
            exactly one newline, and flush() is the only place that supplies it
            for text. Marker branches call plain flush() and emit nothing extra,
            so a following bullet / fence / ::: gets exactly the one newline it
            needs, while the blank-line branch adds the blank line's own "\\n" on
            top and yields "- item\\n\\n".

            `terminate=False` is only for EOF, where the source line has no
            trailing newline to reproduce."""
            nonlocal para, para_line0, para_lines
            if para:
                self.tr("\n".join(para), "para", para_line0, list(para_lines))
                if terminate:
                    self.lit("\n", para_lines[-1])
            para, para_line0, para_lines = [], 0, []

        while i < n:
            line = lines[i]

            if line.strip() == "":
                # A blank line is its own literal "\n". The preceding paragraph
                # does NOT emit one: it is the blank line that terminates it.
                # Whitespace-only lines are verbatim source (some pages pad with
                # spaces), so they keep their spaces.
                flush()
                self.lit(line + "\n", i + 1)
                i += 1
                continue

            m = HEADING_RE.match(line)
            if m:
                flush()
                self.lit(m.group(1) + m.group(2), i + 1)
                self.tr(m.group(3), "heading", i + 1, [i + 1])
                self.lit("\n", i + 1)
                i += 1
                continue

            fm = FENCE_RE.match(line)
            if fm:
                if para:
                    flush()
                end = _fence_end(lines, i)
                self.lit("\n".join(lines[i:end]) + "\n", i + 1)
                i = end
                continue

            if line.strip().startswith("$$"):
                flush()
                end = _math_block_end(lines, i)
                self.lit("\n".join(lines[i:end]) + "\n", i + 1)
                i = end
                continue

            dm = DIRECTIVE_OPEN_RE.match(line)
            if dm:
                if para:
                    flush()
                indent, colon, name, rest = dm.groups()
                self.lit(indent + colon + "{" + name + "}", i + 1)
                if rest.strip() and name.lower() not in OPAQUE_DIRECTIVES:
                    self.lit(rest[: len(rest) - len(rest.lstrip())], i + 1)
                    self.tr(rest.strip(), "directive_title", i + 1, [i + 1])
                    self.lit("\n", i + 1)
                else:
                    self.lit_line(rest, i + 1)
                end = self._directive_body(i + 1, len(colon))
                i = end
                continue

            if DIRECTIVE_CLOSE_RE.match(line):
                flush()
                self.lit_line(line, i + 1)
                i += 1
                continue

            if OPTION_RE.match(line) or LINKDEF_RE.match(line):
                flush()
                self.lit_line(line, i + 1)
                i += 1
                continue

            if HTML_RE.match(line):
                flush()
                end = _html_end(lines, i)
                self.lit("\n".join(lines[i:end]) + "\n", i + 1)
                i = end
                continue

            if INDENTED_CODE_RE.match(line) and not para:
                end = i
                while end < n and (lines[end].strip() == "" or INDENTED_CODE_RE.match(lines[end])):
                    if lines[end].strip() == "":
                        break
                    end += 1
                self.lit("\n".join(lines[i:end]) + "\n", i + 1)
                i = end
                continue

            # ordinary text: accumulate into the current paragraph
            bm = BULLET_RE.match(line)
            if bm:
                flush()
                self.lit(bm.group(0), i + 1)
                rest = line[bm.end():]
                if rest.strip():
                    para = [rest]
                    para_line0 = i + 1
                    para_lines = [i + 1]
                else:
                    self.lit("\n", i + 1)
                i += 1
                continue

            if not para:
                para_line0 = i + 1
                para_lines = [i + 1]
            para.append(line)
            para_lines.append(i + 1)
            i += 1

        # At EOF flush() without the terminator: `load_source` has already
        # stripped the final newline (or, when the file ended without one, there
        # is nothing to add). Emitting it here would add a phantom blank line.
        flush(terminate=False)
        return self.items

    def _directive_body(self, i: int, colon_len: int) -> int:
        """Slice the inside of a directive opened before line index i."""
        lines = self.lines
        n = len(lines)
        para: list[str] = []
        para_line0 = 0
        para_lines: list[int] = []

        def flush(terminate: bool = True) -> None:
            """Emit the open paragraph and ALWAYS terminate its last line.

            This single rule makes the walk lossless: every source line ends in
            exactly one newline, and flush() is the only place that supplies it
            for text. Marker branches call plain flush() and emit nothing extra,
            so a following bullet / fence / ::: gets exactly the one newline it
            needs, while the blank-line branch adds the blank line's own "\\n" on
            top and yields "- item\\n\\n".

            `terminate=False` is only for EOF, where the source line has no
            trailing newline to reproduce."""
            nonlocal para, para_line0, para_lines
            if para:
                self.tr("\n".join(para), "para", para_line0, list(para_lines))
                if terminate:
                    self.lit("\n", para_lines[-1])
            para, para_line0, para_lines = [], 0, []

        while i < n:
            line = lines[i]

            if line.strip() == "":
                # A blank line is its own literal "\n". The preceding paragraph
                # does NOT emit one: it is the blank line that terminates it.
                # Whitespace-only lines are verbatim source (some pages pad with
                # spaces), so they keep their spaces.
                flush()
                self.lit(line + "\n", i + 1)
                i += 1
                continue

            dm = DIRECTIVE_OPEN_RE.match(line)
            if dm and len(dm.group(2)) != colon_len:
                # A nested directive may use MORE colons than its parent (the
                # convention) or FEWER (this repo does it: `:::{grid-item-card}`
                # inside `::::{grid}`). Either way it opens a block whose closer
                # matches ITS OWN colon count, so recurse with that width instead
                # of handing the line to a translator as prose.
                if para:
                    flush()
                indent, colon, name, rest = dm.groups()
                self.lit(indent + colon + "{" + name + "}", i + 1)
                if rest.strip() and name.lower() not in OPAQUE_DIRECTIVES:
                    self.lit(rest[: len(rest) - len(rest.lstrip())], i + 1)
                    self.tr(rest.strip(), "directive_title", i + 1, [i + 1])
                    self.lit("\n", i + 1)
                else:
                    self.lit_line(rest, i + 1)
                i = self._directive_body(i + 1, len(colon))
                continue

            cm = DIRECTIVE_CLOSE_RE.match(line)
            if cm and len(cm.group(2)) == colon_len:
                flush()
                self.lit_line(line, i + 1)
                return i + 1

            if OPTION_RE.match(line) or LINKDEF_RE.match(line):
                flush()
                self.lit_line(line, i + 1)
                i += 1
                continue

            fm = FENCE_RE.match(line)
            if fm:
                # NOTE: a `````{admonition} **Title**`` line is matched here as a
                # plain fence and its title stays English. Its closer is `::::`,
                # so it cannot be handled by the backtick-fence machinery without
                # eating the lines in between. Only one such line exists in the
                # whole book (ch03/05); translate it by hand.
                flush()
                end = _fence_end(lines, i)
                self.lit("\n".join(lines[i:end]) + "\n", i + 1)
                i = end
                continue

            if line.strip().startswith("$$"):
                flush()
                end = _math_block_end(lines, i)
                self.lit("\n".join(lines[i:end]) + "\n", i + 1)
                i = end
                continue

            if HTML_RE.match(line):
                flush()
                end = _html_end(lines, i)
                self.lit("\n".join(lines[i:end]) + "\n", i + 1)
                i = end
                continue

            m = HEADING_RE.match(line)
            if m:
                flush()
                self.lit(m.group(1) + m.group(2), i + 1)
                self.tr(m.group(3), "heading", i + 1, [i + 1])
                self.lit("\n", i + 1)
                i += 1
                continue

            bm = BULLET_RE.match(line)
            if bm:
                flush()
                self.lit(bm.group(0), i + 1)
                rest = line[bm.end():]
                if rest.strip():
                    para = [rest]
                    para_line0 = i + 1
                    para_lines = [i + 1]
                else:
                    self.lit("\n", i + 1)
                i += 1
                continue

            if not para:
                para_line0 = i + 1
                para_lines = [i + 1]
            para.append(line)
            para_lines.append(i + 1)
            i += 1

        flush(terminate=False)
        return i


# ------------------------------------------------------------ text rendering
def join_newlines(text: str) -> str:
    """Drop the soft-wrap newline between two CJK chars; keep it as a space otherwise."""
    out = []
    for i, ch in enumerate(text):
        if ch == "\n":
            prev = text[i - 1] if i > 0 else " "
            nxt = text[i + 1] if i + 1 < len(text) else " "
            out.append("" if (CJK_RE.match(prev) and CJK_RE.match(nxt)) else " ")
        else:
            out.append(ch)
    return "".join(out)


NO_LINE_START = "，。、；：？！）」』】〉”’%…"
NO_LINE_END = "（「『【〈“‘"

EMPH_RE = re.compile(r"(\*\*|__|\*|_)(?=\S)(.+?)(?<=\S)\1", re.S)


def _atomic_pieces(text: str) -> list[tuple[str, str]]:
    """Split into ('lit', span) and ('txt', span) so wrapping never cuts a span."""
    pieces: list[tuple[str, str]] = []
    last = 0
    for m in INLINE_RE.finditer(text):
        if m.start() > last:
            pieces.extend(_split_emphasis(text[last:m.start()]))
        pieces.append(("lit", m.group(0)))
        last = m.end()
    if last < len(text):
        pieces.extend(_split_emphasis(text[last:]))
    return pieces


def _split_emphasis(run: str) -> list[tuple[str, str]]:
    """Keep **bold** / *italic* spans atomic so a wrap cannot break them."""
    out: list[tuple[str, str]] = []
    pos = 0
    for m in EMPH_RE.finditer(run):
        if m.start() > pos:
            out.append(("txt", run[pos:m.start()]))
        out.append(("lit", m.group(0)))
        pos = m.end()
    if pos < len(run):
        out.append(("txt", run[pos:]))
    return out


def _units(piece: str) -> list[str]:
    """Breakable units: each CJK char is its own unit; Latin words stay whole."""
    units: list[str] = []
    buf = ""
    for ch in piece:
        if CJK_RE.match(ch) or ch == " ":
            if buf:
                units.append(buf)
                buf = ""
            units.append(ch)
        else:
            buf += ch
    if buf:
        units.append(buf)
    return units


def wrap_zh(text: str, width: int = 88) -> str:
    """Greedy CJK-aware wrap that never splits math, code, links or emphasis."""
    units: list[tuple[str, bool]] = []  # (text, is_space)
    for kind, piece in _atomic_pieces(text):
        if kind == "lit":
            units.append((piece, False))
        else:
            units.extend((u, u == " ") for u in _units(piece))

    lines: list[str] = []
    cur = ""
    for txt, is_space in units:
        if not cur:
            cur = txt
            continue
        # never start a line with CJK closing punctuation, never end one with opening
        if txt and txt[0] in NO_LINE_START:
            cur += txt
            continue
        visible = len(cur) + (0 if is_space else len(txt))
        if visible > width and not is_space and cur[-1] not in NO_LINE_END:
            lines.append(cur.rstrip())
            cur = txt
        else:
            cur += txt
    if cur:
        lines.append(cur.rstrip())
    return "\n".join(lines)


# --------------------------------------------------------------- invariants
def inline_invariants(text: str) -> list[str]:
    out = []
    for m in INLINE_RE.finditer(text):
        g = m.groupdict()
        if g["math"]:
            out.append("math:" + g["math"])
        elif g["code"]:
            out.append("code:" + g["code"])
        elif g["role"]:
            out.append("role:" + g["role"])
        elif g["imglink"]:
            out.append("url:" + g["iurl"])
        elif g["link"]:
            out.append("url:" + g["lurl"])
        elif g["url"]:
            out.append("url:" + g["url"])
    return sorted(out)


def markers(text: str) -> dict:
    return {
        "$$_or_$": text.count("$"),
        "bold": text.count("**"),
        "italic": text.count("*") - 2 * text.count("**"),
        "backtick": text.count("`"),
        "link_close": text.count("]("),
    }


# ------------------------------------------------------------- subcommands
def load_glossary(path: str | None) -> dict[str, dict]:
    if not path:
        return {}
    rows = []
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        rows.append([c.strip() for c in raw.split("\t")])
    hdr = rows[0]
    out: dict[str, dict] = {}
    for r in rows[1:]:
        rec = dict(zip(hdr, r))
        out[rec["en"].lower()] = rec
    return out


# The fence used for inserted bilingual blocks. Six backticks, because backtick
# fences nest reliably in mystmd where colon fences do not (see block() below).
FENCE = "`" * 6


def load_source(path: str) -> tuple[list[str], bool]:
    """Split a source file into lines the way an editor does, plus whether it
    ended with a newline (both must round-trip byte-for-byte)."""
    return load_source_str(Path(path).read_text(encoding="utf-8"))


def load_source_str(text: str) -> tuple[list[str], bool]:
    trailing = text.endswith("\n")
    lines = text.split("\n")
    if trailing:
        lines = lines[:-1]
    return lines, trailing


def cmd_slice(a) -> int:
    items_all = []
    segs_all = []
    templates = []
    ntrans = 0
    for src in a.src:
        p = Path(src)
        lines, trailing = load_source(src)
        items = Slicer(lines, trailing).run()
        ntrans += sum(1 for it in items if it["t"] == "tr")
        items_all.append({"src": src, "trailing_newline": trailing, "items": items})
        for it in items:
            if it["t"] == "tr":
                prev = ""
                for back in reversed(items):
                    if back["t"] == "lit" and back["s"].strip():
                        prev = back["s"].strip().split("\n")[-1][:70]
                        break
                segs_all.append(
                    {
                        "id": it["id"],
                        "src": src,
                        "line": it["line"],
                        "kind": it["kind"],
                        "en": it["s"],
                        "context_after_literal": prev,
                    }
                )
        templates.append(render(items, {}))

    outdir = Path(a.out)
    outdir.mkdir(parents=True, exist_ok=True)
    for entry in items_all:
        name = Path(entry["src"]).stem
        (outdir / f"{name}.items.json").write_text(
            json.dumps({"trailing_newline": entry["trailing_newline"], "items": entry["items"]},
                       ensure_ascii=False, indent=1),
            encoding="utf-8",
        )
        (outdir / f"{name}.template.md").write_text(templates.pop(0), encoding="utf-8")
    (outdir / "segs.json").write_text(json.dumps(segs_all, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"sliced {len(a.src)} file(s): {ntrans} translatable segments")
    print(f"  -> {outdir}/segs.json, *.items.json, *.template.md")
    return 0


def render(items: list[dict], zh: dict[str, str]) -> str:
    parts: list[str] = []
    for it in items:
        if it["t"] == "lit":
            parts.append(it["s"])
        else:
            txt = zh.get(it["id"])
            parts.append(txt if txt is not None else "{{%s}}" % it["id"])
    page = "".join(parts)
    if not page.endswith("\n"):
        page += "\n"
    return page


WRAP_WIDTH = 0  # 0 = keep the translator's own line breaks verbatim


def render_text(txt: str) -> str:
    """width 0 = emit exactly what the translator supplied (identity-safe);
    width > 0 = reflow, dropping source soft-wrap breaks between CJK chars."""
    return txt if not WRAP_WIDTH else wrap_zh(join_newlines(txt), WRAP_WIDTH)


def _offsets_for_item(it: dict, start: int) -> list[tuple[int, int]]:
    """(source_line, char_offset_in_page) pairs contributed by one item."""
    out: list[tuple[int, int]] = []
    if it["t"] == "tr":
        return [(ln, start) for ln in it.get("lines", [])]
    body, off = it["s"], start
    j = 0
    while True:
        out.append((it["line"] + j, off))
        nl = body.find("\n", off - start)
        if nl == -1:
            break
        off = start + nl + 1
        j += 1
    return out


def _inside_protected(page_lines: list[str], idx: int) -> bool:
    """True if line idx sits inside a fenced code block or a $$ math block."""
    fence: str | None = None
    math_open = False
    for i in range(idx):
        s = page_lines[i].strip()
        fm = FENCE_RE.match(page_lines[i])
        if fence:
            if fm and fm.group(2)[0] == fence[0] and len(fm.group(2)) >= len(fence):
                fence = None
            continue
        if math_open:
            if s.endswith("$$") or s == "$$":
                math_open = False
            continue
        if fm:
            fence = fm.group(2)
        elif s.startswith("$$"):
            math_open = not (s.endswith("$$") and len(s) > 2)
    return fence is not None or math_open


def cmd_apply(a) -> int:
    global WRAP_WIDTH
    WRAP_WIDTH = a.wrap
    items_doc = json.loads(Path(a.items).read_text(encoding="utf-8"))
    if isinstance(items_doc, dict):
        items = items_doc["items"]
        trailing_newline = bool(items_doc.get("trailing_newline", True))
    else:
        items = items_doc
        trailing_newline = True
    zh = json.loads(Path(a.translations).read_text(encoding="utf-8"))
    ids = {it["id"] for it in items if it["t"] == "tr"}
    extra = sorted(set(zh) - ids)
    if extra:
        print(f"WARN: {len(extra)} unknown id(s) ignored: {extra[:12]}", file=sys.stderr)

    mode = getattr(a, "mode", "replace")
    min_words = getattr(a, "min_words", 8)
    translate_tables = getattr(a, "translate_tables", False)

    text_of = {it["id"]: it["s"] for it in items if it["t"] == "tr"}

    def worth_translating(text: str) -> bool:
        # Two rules only, deliberately: simple rules survive maintenance.
        #  1. leave tables alone -- cells are short phrases, and a table with a
        #     few Chinese words among English ones reads worse than an untouched
        #     table (opt back in with --translate-tables).
        #  2. skip fragments under --min-words. Everything else is already
        #     excluded structurally (headings, code, maths, directive options
        #     are literals the applier never sees), so no threshold list is
        #     needed. 8 words keeps 74% of this book's paragraphs.
        if not translate_tables and text.lstrip().startswith("|"):
            return False
        return len(text.split()) >= min_words

    # Demand a translation for exactly the segments that will be inserted, no
    # more. Requiring every paragraph would make the rules unusable: the ones the
    # rules skip by design (tables, short fragments) have no translation, and
    # failing on them would reject every run.
    if mode == "interleave":
        require = {it["id"] for it in items
                   if it["t"] == "tr" and it.get("kind") == "para"
                   and worth_translating(it["s"])}
    else:
        require = ids
    missing = sorted(require - set(zh))
    if missing:
        print(f"FAIL: {len(missing)} of {len(require)} segment(s) untranslated: "
              f"{missing[:12]}", file=sys.stderr)
        return 2

    def is_list_item(idx: int) -> bool:
        """True when item idx is the text of a bullet/numbered list entry: its
        immediately preceding literal is the marker itself."""
        if idx <= 0 or items[idx - 1]["t"] != "lit":
            return False
        return bool(re.match(r"^\s*(?:[-*+]|\d+[.)])\s+$", items[idx - 1]["s"]))

    # Render each item, then place insertions by character offset so both
    # interleaved Chinese and errata notes can be inserted from the end
    # backwards without invalidating each other's positions.
    chunks: list[str] = []
    for it in items:
        if it["t"] == "lit":
            chunks.append(it["s"])
        elif mode == "interleave":
            # interleave NEVER rewrites the source: the English paragraph is
            # emitted byte-identical (the identity round-trip proves it["s"] is
            # the original text) and the Chinese is only ever ADDED after it.
            chunks.append(it["s"])
        else:
            chunks.append(render_text(zh[it["id"]]))

    offs: list[int] = []
    p = 0
    for c in chunks:
        offs.append(p)
        p += len(c)
    page = "".join(chunks)

    # source line -> character offset, for anchoring errata notes
    offsets: list[tuple[int, int]] = []
    for it, off in zip(items, offs):
        offsets.extend(_offsets_for_item(it, off))

    if trailing_newline and not page.endswith("\n"):
        page += "\n"
    elif not trailing_newline and page.endswith("\n"):
        page = page.rstrip("\n")

    def after_item(idx: int) -> int:
        """Offset just past item idx and the newline literal that follows it."""
        end = offs[idx] + len(chunks[idx])
        if idx + 1 < len(items) and items[idx + 1]["t"] == "lit" and items[idx + 1]["s"] == "\n":
            end += 1
        return end

    inserts: list[tuple[int, str]] = []

    def block(text: str, label: str = "中文翻译") -> str:
        # BACKTICKS, not colons. Measured against mystmd 1.11 with a build:
        # colon fences do NOT nest reliably -- a 4-colon block inside a 3-colon
        # note leaks as literal text, and a 6-colon block inside a grid-item-card
        # leaks *and* closes the enclosing note early, silently dropping the next
        # heading. Backticks nest correctly in every context tested: top level,
        # inside `:::{note}`, inside `:::{grid-item-card}` inside `::::{grid}`,
        # and inside the source's own 4-backtick directive. Five or six work;
        # six leaves room for one more level.
        # Two newlines below: at EOF a paragraph has no trailing-newline literal
        # after it, so a single "\n" would leave the directive glued to the text.
        return (
            "\n\n" + FENCE + "{admonition} " + label + "\n"
            ":class: dropdown\n\n"
            + text + "\n"
            + FENCE + "\n"
        )

    BULLET_ONLY_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+$")
    if mode == "interleave":
        run: list[str] = []
        run_end = 0
        for idx, it in enumerate(items):
            if it["t"] == "tr" and is_list_item(idx):
                run.append(it["id"])
                run_end = after_item(idx)
                continue
            # Structural glue inside a list (the newline after each entry, and
            # the next entry's marker) must not be read as the end of the run,
            # or every bullet gets its own block instead of one block per list.
            if it["t"] == "lit" and (it["s"] == "\n" or BULLET_ONLY_RE.match(it["s"])):
                continue
            if run:
                # Re-emit the list markers: without them the joined translations
                # form a single run-on paragraph, because consecutive Markdown
                # lines with no blank line between them are one paragraph.
                # Index zh defensively: a cache missing one bullet must degrade to
                # a shorter block, not raise mid-write and leave a half-written page.
                avail = [i for i in run if i in zh]
                if avail and worth_translating("\n".join(text_of[i] for i in run)):
                    inserts.append((run_end, block("\n".join("- " + zh[i] for i in avail))))
                run = []
            if (it["t"] == "tr" and it.get("kind") == "para"
                    and worth_translating(it["s"])):
                inserts.append((after_item(idx), block(zh[it["id"]])))
        if run:
            avail = [i for i in run if i in zh]
            if avail and worth_translating("\n".join(text_of[i] for i in run)):
                inserts.append((run_end, block("\n".join("- " + zh[i] for i in avail))))

    def to_backtick(note: str) -> str:
        # Errata notes are authored with `:::{note}` fences, but a 3-colon fence
        # does not nest inside a 3-colon grid-item-card: verified against a real
        # mystmd build, where such a note leaks as literal text and drags the
        # whole grid into a code block with it. Rewrite the fences to the same
        # nesting-safe backtick form used for the translation blocks.
        out = []
        for ln in note.split("\n"):
            if re.match(r"^:{3,}\{", ln):
                out.append(FENCE + ln[ln.index("{"):])
            elif re.match(r"^:{3,}\s*$", ln):
                out.append(FENCE)
            else:
                out.append(ln)
        return "\n".join(out)

    inserted = 0
    if a.annotations:
        ann = json.loads(Path(a.annotations).read_text(encoding="utf-8"))
        for anchor in ann:
            best = 0
            for src_line, off in offsets:
                if src_line <= int(anchor):
                    best = off
                else:
                    break
            lines = page.split("\n")
            if _inside_protected(lines, page.count("\n", 0, best)):
                print(f"WARN: annotation for line {anchor} skipped (inside a "
                      f"code/math block)", file=sys.stderr)
                continue
            # Blank line on both sides: a directive glued to the end of a list
            # item becomes a lazy continuation of that paragraph and renders as
            # literal colons instead of a callout.
            inserts.append((best, "\n\n" + to_backtick(ann[anchor].rstrip("\n")) + "\n\n"))
            inserted += 1

    for off, text in sorted(inserts, key=lambda t: -t[0]):
        page = page[:off] + text + page[off:]

    # Record exactly what was added, so `verify --strip-interleaved` can remove
    # it by identity rather than by a regex that has to guess the layout.
    Path(str(a.out) + ".inserted.json").write_text(
        json.dumps([t for _, t in inserts], ensure_ascii=False), encoding="utf-8")

    Path(a.out).write_text(page, encoding="utf-8")
    print(f"applied {len(ids)} segments, {inserted} note(s), "
          f"{len(inserts) - inserted} translation block(s) -> {a.out}")
    return 0


def cmd_verify(a) -> int:
    src_text = Path(a.src).read_text(encoding="utf-8")
    out_text = Path(a.out).read_text(encoding="utf-8")

    if getattr(a, "strip_interleaved", False):
        # Interleave mode only ADDS regions, so the gate inverts: remove exactly
        # what apply recorded adding, and the remainder must equal the source
        # byte-for-byte. Removing by identity (not by regex) keeps the check
        # exact: if any inserted region were missing from the sidecar, or had
        # perturbed a neighbouring byte, the comparison fails.
        sidecar = Path(str(a.out) + ".inserted.json")
        if not sidecar.exists():
            print(f"FAIL: {sidecar} missing (run apply before verify)", file=sys.stderr)
            return 1
        for ins in json.loads(sidecar.read_text(encoding="utf-8")):
            if ins not in out_text:
                print(f"FAIL: recorded insertion not found verbatim in output: {ins[:60]!r}",
                      file=sys.stderr)
                return 1
            out_text = out_text.replace(ins, "", 1)

    s_items = Slicer(*load_source_str(src_text)).run()
    o_items = Slicer(*load_source_str(out_text)).run()

    s_lit = "".join(it["s"] for it in s_items if it["t"] == "lit")
    o_lit = "".join(it["s"] for it in o_items if it["t"] == "lit")
    ok = True

    # Declared deviations: constructs the slicer cannot reach (e.g. a title on a
    # backtick-fence directive, whose closer is `::::`). Each must be listed here
    # so the gate stays strict for everything else instead of being loosened.
    allowed = []
    if a.allow:
        allowed = [ln.strip() for ln in Path(a.allow).read_text(encoding="utf-8").splitlines()
                   if ln.strip() and not ln.startswith("#")]
    for pat in allowed:
        s_lit = re.sub(pat, "", s_lit)
        o_lit = re.sub(pat, "", o_lit)

    if s_lit != o_lit:
        ok = False
        print("FAIL: literal stream changed (frontmatter / code / $$math / ::: / options / html)")
        for a_, b_ in zip(s_lit.split("\n"), o_lit.split("\n")):
            if a_ != b_:
                print(f"  - src: {a_[:160]}")
                print(f"  + out: {b_[:160]}")
                break

    s_tr = [it for it in s_items if it["t"] == "tr"]
    o_tr = [it for it in o_items if it["t"] == "tr"]
    if len(s_tr) != len(o_tr):
        ok = False
        print(f"FAIL: translatable segment count {len(s_tr)} -> {len(o_tr)}")
    else:
        for s, o in zip(s_tr, o_tr):
            if s["kind"] != o["kind"]:
                ok = False
                print(f"FAIL {s['id']}: kind {s['kind']} -> {o['kind']}")
            si, oi = inline_invariants(s["s"]), inline_invariants(o["s"])
            if si != oi:
                ok = False
                print(f"FAIL {s['id']} (line {s['line']}): inline math/code/link changed")
                print(f"  src: {si}")
                print(f"  out: {oi}")
            sm, om = markers(s["s"]), markers(o["s"])
            for k in sm:
                if sm[k] != om[k]:
                    ok = False
                    print(f"FAIL {s['id']} (line {s['line']}): marker '{k}' {sm[k]} -> {om[k]}")
                    print(f"  src: {s['s'][:200]}")
                    print(f"  out: {o['s'][:200]}")

    untranslated = [it["id"] for it in o_tr if "{{" + it["id"] + "}}" in it["s"]]
    if untranslated:
        ok = False
        print(f"FAIL: {len(untranslated)} placeholder(s) left: {untranslated[:10]}")

    n_cjk = sum(1 for it in o_tr if CJK_RE.search(it["s"]))
    print(f"{'OK' if ok else 'FAILED'}: {len(s_tr)} segments, {n_cjk} containing CJK, "
          f"{len(s_lit)} chars of literal syntax byte-identical")
    return 0 if ok else 1


def cmd_terms(a) -> int:
    zh = json.loads(Path(a.translations).read_text(encoding="utf-8"))
    gloss = load_glossary(a.glossary)
    if not gloss:
        print("no glossary rows")
        return 0
    pat = {en: re.compile(r"(?<![A-Za-z])" + re.escape(en) + r"(?![A-Za-z])", re.I) for en in gloss}
    hits = 0
    for sid, txt in zh.items():
        for en, g in gloss.items():
            if pat[en].search(txt):
                hits += 1
                zh_term = g.get("zh", "")
                bracketed = zh_term and f"（{en}" in txt or f"({en}" in txt
                flag = "ok " if bracketed or g.get("bracket", "0") == "0" else "TIGHT"
                if not bracketed and g.get("bracket", "0") == "1":
                    flag = "BARE"
                print(f"{flag} {sid}: '{en}' -> '{zh_term}' in: {txt[:90]}")
    print(f"{hits} glossary mention(s) checked")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("slice")
    s.add_argument("src", nargs="+")
    s.add_argument("-o", "--out", default="translation_work")
    s.set_defaults(func=cmd_slice)

    s = sub.add_parser("apply")
    s.add_argument("items")
    s.add_argument("-t", "--translations", required=True)
    s.add_argument("-o", "--out", required=True)
    s.add_argument("-a", "--annotations")
    s.add_argument("-w", "--wrap", type=int, default=0,
                   help="reflow translated paragraphs to this width (0 = keep source wrapping)")
    s.add_argument("-m", "--mode", choices=["replace", "interleave"], default="replace",
                   help="replace: substitute translations (monolingual output). "
                        "interleave: keep the English verbatim and insert a collapsible "
                        "Chinese block after each paragraph or list (bilingual output).")
    s.add_argument("--min-words", type=int, default=8,
                   help="interleave: skip any paragraph/list run with fewer words than "
                        "this (default 8). This is the only length rule; everything "
                        "else is excluded structurally.")
    s.add_argument("--translate-tables", action="store_true",
                   help="interleave: also translate Markdown table cells. Off by default: "
                        "cells are short phrases, and a half-translated table reads worse "
                        "than one left in English")
    s.set_defaults(func=cmd_apply)

    s = sub.add_parser("verify")
    s.add_argument("src")
    s.add_argument("out")
    s.add_argument("-a", "--allow", help="file of regexes naming declared literal deviations")
    s.add_argument("--strip-interleaved", action="store_true",
                   help="interleave gate: remove inserted blocks from OUT, then require "
                        "OUT to equal SRC byte-for-byte (proves English was not rewritten)")
    s.set_defaults(func=cmd_verify)

    s = sub.add_parser("terms")
    s.add_argument("translations")
    s.add_argument("-g", "--glossary")
    s.set_defaults(func=cmd_terms)

    a = ap.parse_args()
    return a.func(a)


if __name__ == "__main__":
    raise SystemExit(main())