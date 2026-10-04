#!/usr/bin/env python3
"""Incremental, cache-keyed Chinese translation for the Chem324 MyST site.

WHY A CACHE KEYED BY SOURCE TEXT
  The upstream notes change continuously, so re-translating the book each run would
  be wasteful and slow. The cache maps an English paragraph to its Chinese, keyed by
  the paragraph text itself. Consequences:
    * an unchanged paragraph is a cache hit and costs nothing;
    * an edited paragraph is a miss and is the only thing re-translated;
    * deleted paragraphs leave harmless orphans;
    * the cache is human-readable, so it reviews and reverts like source code.
  Keying by segment id or line number would break on every upstream edit, because
  inserting one paragraph renumbers everything after it.

PIPELINE  (each stage is independently runnable)
  slice      pages -> per-page segment files in the work directory
  translate  fill the cache for segments that are missing, in batches
  apply      cache + segments -> bilingual Markdown written back in place
  stats      coverage report
  all        slice, translate, apply

Writes only inside WORK. The Markdown it rewrites is a build input, never committed.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / ".zh-work"
CACHE = ROOT / "translation" / "zh-cache.json"
NOTES = ROOT / "translation" / "notes"
SLICER = Path(__file__).resolve().parent / "myst_slice.py"

DEFAULT_BASE = "https://openrouter.ai/api/v1"
DEFAULT_MODEL = "nemotron-3-ultra-550b-a55b:free"
MIN_WORDS = 8
USER_AGENT = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/122.0 Safari/537.36")

SYSTEM = (
    "You translate English into natural Simplified Chinese for a quantum chemistry "
    "textbook. Rules, all mandatory:\n"
    "1. Preserve every **bold** marker exactly: same count, same positions.\n"
    "2. Preserve every $...$ inline math span byte-for-byte. Never translate, reformat "
    "or reorder maths.\n"
    "3. Preserve every Markdown link target byte-for-byte; translate only the label.\n"
    "4. Keep the leading '- ' bullet marker if present.\n"
    "5. Output ONLY the translation. No commentary, no quotes, no code fence."
)


# ------------------------------------------------------------------ utilities
def pages(explicit: list[str] | None = None) -> list[Path]:
    if explicit:
        return [ROOT / p for p in explicit]
    return sorted(p for p in ROOT.rglob("*.md")
                  if not any(x in p.parts for x in
                             (".git", "_build", "slides", ".zh-work", "translation")))


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


def load_json(p: Path, default):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else default


def save_json(p: Path, obj) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                 encoding="utf-8")


def segments(items_path: Path) -> list[dict]:
    doc = load_json(items_path, {"items": []})
    items = doc["items"] if isinstance(doc, dict) else doc
    return [i for i in items if i["t"] == "tr" and i.get("kind") == "para"]


def worth(text: str, min_words: int = MIN_WORDS) -> bool:
    """Which paragraphs to TRANSLATE.

    Deliberately different from the applier's rules, and deliberately simpler:
    translate everything except tables. The `min_words` floor governs what is
    DISPLAYED, not what is cached, because a list is rendered as one block of all
    its items -- if the cache skipped a short bullet, the run would either crash
    or render a half-translated list. Caching something that is never shown costs
    one call, once, then nothing; caching too little is a bug that only appears at
    render time.

    Keeping the cache complete also means the display rules can be changed later
    without re-translating anything.
    """
    return not text.lstrip().startswith("|")


def markup_ok(src: str, dst: str) -> list[str]:
    """Constructs that must survive translation, checked as multisets."""
    from collections import Counter
    bad = []
    for label, pat in (("bold", r"\*\*"), ("inline math", r"\$[^$\n]+\$"),
                       ("link", r"\]\(([^)]+)\)")):
        a, b = Counter(re.findall(pat, src)), Counter(re.findall(pat, dst))
        if a - b:
            bad.append(f"{label} lost: {dict(a - b)}")
    return bad


# ------------------------------------------------------------------ the model
class Translator:
    def __init__(self, key: str, base: str, model: str, no_reasoning: bool = True):
        self.key, self.base, self.model = key, base.rstrip("/"), model
        self.no_reasoning = no_reasoning
        self.requests = 0

    def chat(self, prompt: str, timeout: int = 600) -> str:
        body: dict = {"model": self.model, "temperature": 0.2,
                      "messages": [{"role": "system", "content": SYSTEM},
                                   {"role": "user", "content": prompt}]}
        if self.no_reasoning:
            # This model spends thousands of tokens reasoning about a single
            # sentence, which dominates wall-clock time. Turn it off where supported.
            body["reasoning"] = {"enabled": False}
        req = urllib.request.Request(
            self.base + "/chat/completions", data=json.dumps(body).encode(),
            headers={"Authorization": f"Bearer {self.key}", "Content-Type": "application/json",
                     "User-Agent": USER_AGENT,
                     "HTTP-Referer": "https://julianshi.github.io/Chem324",
                     "X-Title": "Chem324 zh"})
        last = None
        for attempt in range(4):
            try:
                self.requests += 1
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    out = json.loads(r.read().decode())
                return (out["choices"][0]["message"].get("content") or "").strip()
            except urllib.error.HTTPError as e:
                detail = ""
                try:
                    detail = e.read().decode()[:200]
                except Exception:
                    pass
                last = f"HTTP {e.code}: {detail}"
                if e.code in (400, 401, 403, 402):   # not retryable
                    break
                time.sleep(5 * (attempt + 1))
            except Exception as e:                    # network, timeout
                last = f"{type(e).__name__}: {e}"
                time.sleep(5 * (attempt + 1))
        raise RuntimeError(last or "request failed")

    def translate_batch(self, batch: dict[str, str]) -> dict[str, str]:
        """One request for many segments; returns only the ones that came back clean."""
        prompt = ("Translate each value below. Reply with ONLY a JSON object mapping "
                  "each key to its Simplified Chinese translation, no code fence.\n\n"
                  + json.dumps(batch, ensure_ascii=False, indent=1))
        raw = self.chat(prompt)
        raw = re.sub(r"^```(?:json)?|```$", "", raw, flags=re.M).strip()
        try:
            got = json.loads(raw)
        except Exception:
            return {}
        if not isinstance(got, dict):
            return {}
        out = {}
        for k, v in got.items():
            if k in batch and isinstance(v, str) and v.strip() and not markup_ok(batch[k], v):
                out[k] = v.strip()
        return out


# ------------------------------------------------------------------ stages
def stage_slice(args) -> int:
    WORK.mkdir(parents=True, exist_ok=True)
    todo = pages(args.pages)
    total = 0
    for p in todo:
        rel = p.relative_to(ROOT)
        r = run([sys.executable, str(SLICER), "slice", str(rel), "-o", str(WORK)])
        if r.returncode != 0:
            print(f"  ! slice failed for {rel}: {r.stderr.strip()[:120]}")
            continue
        segs = segments(WORK / f"{p.stem}.items.json")
        total += len(segs)
        print(f"  {str(rel):<52} {len(segs):>4} paragraphs")
    print(f"slice: {len(todo)} pages, {total} paragraphs")
    return 0


def stage_translate(args) -> int:
    key = os.environ.get("OPENROUTER_API_KEY", "")
    if not key:
        print("ERROR: OPENROUTER_API_KEY is not set", file=sys.stderr)
        return 2
    cache: dict[str, str] = load_json(CACHE, {})
    t = Translator(key, args.base, args.model, not args.keep_reasoning)

    todo: list[str] = []
    seen = set()
    for p in pages(args.pages):
        for seg in segments(WORK / f"{p.stem}.items.json"):
            txt = seg["s"]
            if worth(txt) and txt not in cache and txt not in seen:
                seen.add(txt)
                todo.append(txt)
    # shortest first: cheap wins, and progress is visible early in a long run
    todo.sort(key=len)
    print(f"translate: {len(cache)} cached, {len(todo)} to do "
          f"(batch {args.batch}, limit {args.limit or 'none'})")
    if args.limit:
        todo = todo[: args.limit]

    done = failed = 0
    t0 = time.time()
    for i in range(0, len(todo), args.batch):
        chunk = todo[i:i + args.batch]
        batch = {f"S{n:03d}": txt for n, txt in enumerate(chunk)}
        try:
            got = t.translate_batch(batch)
        except Exception as e:
            print(f"  ! batch {i//args.batch}: {e}")
            got = {}
        for k, v in got.items():
            cache[batch[k]] = v
            done += 1
        # retry stragglers one at a time: a batch-level JSON slip should not lose them
        for k, src in batch.items():
            if k in got:
                continue
            try:
                single = t.translate_batch({"S000": src})
                if single:
                    cache[src] = next(iter(single.values()))
                    done += 1
            except Exception:
                failed += 1
        save_json(CACHE, cache)     # persist every batch: a timeout keeps progress
        print(f"  {done}/{len(todo)} done, {failed} failed, "
              f"{t.requests} requests, {time.time()-t0:.0f}s")
    print(f"translate: +{done} cached ({len(cache)} total), {failed} failed")
    return 0


def stage_apply(args) -> int:
    cache: dict[str, str] = load_json(CACHE, {})
    for p in pages(args.pages):
        rel = p.relative_to(ROOT)
        items = WORK / f"{p.stem}.items.json"
        if not items.exists():
            continue
        segs = segments(items)
        zh = {s["id"]: cache[s["s"]] for s in segs if s["s"] in cache and worth(s["s"])}
        zh_path = WORK / f"{p.stem}.zh.json"
        save_json(zh_path, zh)
        cmd = [sys.executable, str(SLICER), "apply", str(items), "-t", str(zh_path),
               "--mode", "interleave", "--min-words", str(MIN_WORDS), "-o", str(rel)]
        note = NOTES / f"{p.stem}.json"
        if note.exists():
            cmd += ["-a", str(note.relative_to(ROOT))]
        r = run(cmd)
        print(f"  {str(rel):<52} {r.stdout.strip() or r.stderr.strip()[:100]}")
    return 0


def stage_stats(args) -> int:
    cache = load_json(CACHE, {})
    tot = hit = 0
    for p in pages(args.pages):
        segs = [s for s in segments(WORK / f"{p.stem}.items.json") if worth(s["s"])]
        h = sum(1 for s in segs if s["s"] in cache)
        tot += len(segs)
        hit += h
        if segs and h != len(segs):
            print(f"  {str(p.relative_to(ROOT)):<52} {h}/{len(segs)}")
    pct = (100 * hit / tot) if tot else 0
    print(f"coverage: {hit}/{tot} translatable paragraphs ({pct:.1f}%), "
          f"cache size {len(cache)}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage", choices=["slice", "translate", "apply", "stats", "all"])
    ap.add_argument("--pages", nargs="*", help="specific pages, e.g. ch03/01-....md")
    ap.add_argument("--model", default=os.environ.get("TRANSLATE_MODEL", DEFAULT_MODEL))
    ap.add_argument("--base", default=os.environ.get("TRANSLATE_BASE_URL", DEFAULT_BASE))
    ap.add_argument("--batch", type=int, default=8)
    ap.add_argument("--limit", type=int, default=0,
                    help="translate at most N paragraphs this run (rate-limit guard)")
    ap.add_argument("--keep-reasoning", action="store_true",
                    help="do not request reasoning off (much slower)")
    a = ap.parse_args()
    if a.stage == "slice":
        return stage_slice(a)
    if a.stage == "translate":
        return stage_translate(a)
    if a.stage == "apply":
        return stage_apply(a)
    if a.stage == "stats":
        return stage_stats(a)
    stage_slice(a)
    rc = stage_translate(a)
    stage_apply(a)
    stage_stats(a)
    return rc


if __name__ == "__main__":
    sys.exit(main())
