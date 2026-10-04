#!/usr/bin/env python3
"""Structural checks on the ADDED bilingual blocks.

The English-untouched gate proves the original survived; it cannot see defects
inside what was inserted. This checks the inserted regions themselves:

  * every inserted directive starts on its own line, preceded by a blank line
    (a directive glued to a text line is swallowed as a lazy continuation and
    renders as literal fence characters);
  * every inserted block is closed by a fence of the SAME length;
  * the page's own colon-fence nesting ends balanced at EOF;
  * the page's own backtick fences are balanced.

Fence type matters: inserted blocks use BACKTICKS because colon fences do not
nest reliably in mystmd -- a 6-colon block inside a grid-item-card leaks as
literal text and closes the enclosing note early, dropping the next heading.
"""
import re
import sys
from pathlib import Path

INSERTED = re.compile(r"^(`{3,})\{(?:admonition\}\s*中文翻译|note)\s*$")
COLON_OPEN = re.compile(r"^(:{3,})\{")
BACKTICK_ANY = re.compile(r"^\s*`{3,}")


def check(path: str) -> tuple[int, int, int, int, int]:
    lines = Path(path).read_text(encoding="utf-8").split("\n")
    glued = 0
    unclosed_insert = 0

    i = 0
    while i < len(lines):
        m = INSERTED.match(lines[i])
        if not m:
            i += 1
            continue
        if i > 0 and lines[i - 1].strip() != "":
            glued += 1
        fence = m.group(1)
        j = i + 1
        while j < len(lines) and lines[j].rstrip() != fence:
            j += 1
        if j >= len(lines):
            unclosed_insert += 1
        i = j + 1

    depth = 0
    premature = 0
    for ln in lines:
        if COLON_OPEN.match(ln):
            depth += 1
        elif re.match(r"^:{3,}\s*$", ln):
            depth -= 1
            if depth < 0:
                premature += 1
                depth = 0

    ticks = sum(1 for ln in lines if BACKTICK_ANY.match(ln))
    tick_odd = ticks % 2

    return glued, unclosed_insert, depth, premature, tick_odd


if __name__ == "__main__":
    bad = 0
    for path in sys.argv[1:]:
        glued, unclosed, depth, premature, tick_odd = check(path)
        print(path)
        print(f"  inserted directives not preceded by a blank line : {glued}")
        print(f"  inserted blocks left unclosed                    : {unclosed}")
        print(f"  net colon-fence depth at EOF (0 = balanced)      : {depth}")
        print(f"  colon premature closers                          : {premature}")
        print(f"  backtick fence count odd (1 = unbalanced)        : {tick_odd}")
        if glued or unclosed or depth or premature or tick_odd:
            bad += 1
    sys.exit(1 if bad else 0)
