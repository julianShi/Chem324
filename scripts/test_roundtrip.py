#!/usr/bin/env python3
"""Lossless roundtrip test: slice -> identity translate -> apply, on every page.

Run from the repo root. Exits non-zero if any page fails, printing the first
differing line for each failure so the cause is obvious.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "myst_slice.py"

sys.path.insert(0, str(ROOT / "scripts"))
from myst_slice import Slicer, load_source  # noqa: E402


def render(p):
    items = Slicer(*load_source(str(p))).run()
    zh = {x["id"]: x["s"] for x in items if x["t"] == "tr"}
    page = "".join(x["s"] if x["t"] == "lit" else zh[x["id"]] for x in items)
    _, trailing = load_source(str(p))
    if trailing and not page.endswith("\n"):
        page += "\n"
    elif not trailing and page.endswith("\n"):
        page = page.rstrip("\n")
    return page


pages = sorted(
    str(p.relative_to(ROOT))
    for p in ROOT.rglob("*.md")
    if ".git" not in p.parts
    and "slides" not in p.parts
    and "_build" not in p.parts
    # translation_work holds slicer scratch templates (*.template.md), not pages
    and "translation_work" not in p.parts
)

fails = []
for f in pages:
    src = Path(ROOT / f)
    if render(f) != src.read_text(encoding="utf-8"):
        a = src.read_text(encoding="utf-8").split("\n")
        b = render(f).split("\n")
        first = next(
            (i for i in range(max(len(a), len(b)))
             if (a[i] if i < len(a) else None) != (b[i] if i < len(b) else None)),
            None,
        )
        got = a[first][:120] if first is not None and first < len(a) else "<EOF>"
        exp = b[first][:120] if first is not None and first < len(b) else "<EOF>"
        at = (first + 1) if first is not None else 0
        fails.append(f"  {f}\n    src[{at}]: {got!r}\n    out[{at}]: {exp!r}")

print(f"roundtrip: {len(pages) - len(fails)}/{len(pages)} pages byte-identical")
for f in fails:
    print(f"FAIL {f}")
sys.exit(1 if fails else 0)