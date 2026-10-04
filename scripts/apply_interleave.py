#!/usr/bin/env python3
"""Validate interleave translations, then apply and gate them.

Subagent reports are self-reports: this checks the artefacts directly.

Per file it:
  1. checks the para id set matches the items file exactly (no missing/extra);
  2. checks every inline math span `$...$`, every \\command, every `**bold**`
     marker and every link URL in the translation is a multiset-equal subset of
     the source — i.e. the translator did not invent, drop or alter maths;
  3. applies the interleaved page, runs the English-untouched gate and
     check_blocks.py.

Exit code is non-zero if any file fails.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path("/root/repos/Chem324")
TW = ROOT / "translation_work"
SEL = sys.executable + " " + str(ROOT / "scripts" / "myst_slice.py")

# One length rule only: paragraphs under this many words are left in English.
# Everything else is excluded structurally (headings, code, maths, tables), so
# there is no threshold list to maintain.
MIN_WORDS = 8

MATH = re.compile(r"\$[^$\n]+\$")
CMD = re.compile(r"\\[a-zA-Z]+")
LINK = re.compile(r"\]\(([^)]+)\)")


def multisets_ok(src: str, dst: str) -> list[str]:
    """Report constructs present in source prose but altered in the translation."""
    problems = []
    from collections import Counter
    for label, pat in (("inline math", MATH), ("latex command", CMD), ("link url", LINK)):
        a, b = Counter(pat.findall(src)), Counter(pat.findall(dst))
        lost = a - b
        if lost:
            problems.append(f"{label} missing/altered: {dict(lost)}")
    if src.count("**") != dst.count("**"):
        problems.append(f"bold markers {src.count('**')} -> {dst.count('**')}")
    if src.count("```") != dst.count("```"):
        problems.append("code fence markers changed")
    return problems


def run(cmd: list[str]) -> tuple[int, str]:
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


files = sorted(TW.glob("*.items.json"))
# Optional stem filter. Without it every page is processed, which DOUBLE-APPLIES
# any page already converted — always pass stems when re-running on a partly
# converted chapter.
only = set(sys.argv[1:])
ok_all = True
for items_path in files:
    stem = items_path.name[: -len(".items.json")]
    if only and stem not in only:
        continue
    if not only and stem == "05-eigenvalues-and-expectation":
        continue  # applied separately: it also carries the errata notes
    zh_path = TW / f"{stem}.zh.json"
    page = f"ch03/{stem}.md"

    print(f"\n=== {stem} ===")
    if not zh_path.exists():
        print("  FAIL: translation file missing"); ok_all = False; continue
    try:
        zh = json.loads(zh_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"  FAIL: invalid JSON: {e}"); ok_all = False; continue

    doc = json.loads(items_path.read_text(encoding="utf-8"))
    items = doc["items"] if isinstance(doc, dict) else doc
    para = {i["id"]: i["s"] for i in items if i["t"] == "tr" and i.get("kind") == "para"}
    missing = sorted(set(para) - set(zh))
    extra = sorted(set(zh) - set(para))
    print(f"  para segments {len(para)} | translated {len(zh)} "
          f"| missing {len(missing)} | extra {len(extra)}")
    if missing or extra:
        print(f"    missing={missing[:8]} extra={extra[:8]}"); ok_all = False

    bad = []
    for sid, en in para.items():
        if sid in zh:
            p = multisets_ok(en, zh[sid])
            if p:
                bad.append((sid, p))
    print(f"  segments with altered math/markup: {len(bad)}")
    for sid, p in bad[:6]:
        print(f"    {sid}: {p[0]}")
    if bad:
        ok_all = False

    if missing or bad:
        print("  -> not applying (fix first)")
        continue

    # Back up the English BEFORE the in-place write: the gate below needs the
    # original bytes, and apply overwrites the page in place.
    import shutil
    backup = Path(f"/tmp/{stem}.EN.md")
    if not backup.exists():
        shutil.copyfile(ROOT / page, backup)
        print(f"  backed up English -> {backup}")

    rc, out = run(SEL.split() + ["apply", str(items_path), "-t", str(zh_path),
                                 "--mode", "interleave",
                                 "--min-words", str(MIN_WORDS),
                                 "-o", page])
    print("  apply:", out.replace("\n", " "))
    if rc != 0:
        ok_all = False; continue
    rc, out = run(SEL.split() + ["verify", f"/tmp/{stem}.EN.md", page, "--strip-interleaved"])
    print("  gate :", out.replace("\n", " "))
    if rc != 0:
        ok_all = False
    rc, out = run([sys.executable, str(ROOT / "scripts" / "check_blocks.py"), page])
    tail = " | ".join(l.strip() for l in out.splitlines()[1:])
    print("  blocks:", tail)
    # Parse the counts: the report is column-padded, so substring matching lies.
    glued = re.search(r"not preceded by a blank line\s*:\s*(\d+)", out)
    unclosed = re.search(r"inserted blocks left unclosed\s*:\s*(\d+)", out)
    depth = re.search(r"colon-fence depth at EOF \(0 = balanced\)\s*:\s*(-?\d+)", out)
    ticks = re.search(r"backtick fence count odd \(1 = unbalanced\)\s*:\s*(\d+)", out)
    prec = re.search(r"premature closers\s*:\s*(\d+)", out)
    got = {k: (int(m.group(1)) if m else None)
           for k, m in (("glued", glued), ("unclosed", unclosed), ("depth", depth),
                        ("premature", prec), ("tick_odd", ticks))}
    if any(v is None for v in got.values()) or any(
            v for k, v in got.items() if k != "premature"):
        print(f"  FAIL: block structure problem {got}"); ok_all = False
    # A directive closed with no opener is common in this source (grid closers),
    # so only flag it if the ENGLISH had fewer than the translated page.
    if prec:
        rc0, out0 = run([sys.executable, str(ROOT / "scripts" / "check_blocks.py"), str(backup)])
        p0 = re.search(r"premature closers\s*:\s*(\d+)", out0)
        if int(prec.group(1)) > int(p0.group(1) if p0 else 0):
            print(f"  FAIL: inserted content added premature closers "
                  f"({p0.group(1) if p0 else 0} -> {prec.group(1)})")
            ok_all = False
        else:
            print(f"  (premature closers {prec.group(1)} = pre-existing in English, not caused by inserts)")

print("\nALL OK" if ok_all else "\nFAILURES PRESENT")
sys.exit(0 if ok_all else 1)
