#!/usr/bin/env python3
"""Check a draft (or a section) against the genre voice fingerprint + AI tells.

Usage:
    python3 check_draft.py <draft.txt> [--genre A|B|C]

Prints the draft's measured metrics beside the genre targets (median [IQR]) and
flags: values outside the IQR, banned sentence-initial AI connectives, template
frames ("nearly one in N"), em-dash overuse, and uniform-hedging risk. Pairs with
references/voice_fingerprint.md and references/clinical_ai_tells.md.
"""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("metrics", HERE / "metrics.py")
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)

# genre targets (median [q1,q3]) from the corpus fingerprint
TARGETS = {
    "A": {"mean_len": (31, 27, 37), "sd_len": (43, 38, 63), "burstiness": (24, 19, 37), "short%": (25, 20, 31),
          "long%": (13, 9, 16), "hedge_R": (0.7, 0, 1.6), "hedge_D": (11, 8, 12), "passive_M": (0.56, 0.46, 0.67)},
    "B": {"mean_len": (30, 28, 33), "sd_len": (38, 32, 42), "burstiness": (21, 21, 26), "short%": (26, 23, 29),
          "long%": (13, 12, 16), "hedge_R": (1.4, 0, 2.3), "hedge_D": (11, 9, 14), "passive_M": (0.72, 0.5, 0.78)},
    "C": {"mean_len": (35, 31, 37), "sd_len": (52, 44, 60), "burstiness": (31, 28, 33), "short%": (30, 23, 34),
          "long%": (20, 16, 23), "hedge_R": (0.7, 0, 0.9), "hedge_D": (8, 6, 11), "passive_M": (0.55, 0.43, 0.59)},
}
BANNED_INITIAL = ["moreover", "furthermore", "additionally", "notably", "importantly", "consequently", "nevertheless"]
APHORISM_HINTS = [r"\bThe \w+ is elsewhere\b", r"\bNothing here\b", r"\bis speculative\b", r"\bmoved in the opposite direction\b"]


def flag(val, tgt):
    lo, hi = tgt[1], tgt[2]
    return "  <-- outside IQR" if (val < lo or val > hi) else ""


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    path = Path(sys.argv[1])
    genre = "A"
    if "--genre" in sys.argv:
        genre = sys.argv[sys.argv.index("--genre") + 1].upper()
    text = path.read_text(errors="ignore")
    secs = M.find_sections(text)
    sents = M.split_sentences(secs.get("all", text))
    ss = M.sentence_stats(sents)
    t = TARGETS.get(genre, TARGETS["A"])
    print(f"# check: {path.name}  (genre {genre})\n")
    rows = [
        ("mean_len", ss.get("mean_len", 0)), ("sd_len", ss.get("sd_len", 0)),
        ("burstiness", ss.get("burstiness_masd", 0)), ("short%", ss.get("pct_short_le15", 0)),
        ("long%", ss.get("pct_long_ge40", 0)),
    ]
    print(f"{'metric':12} {'draft':>7}   {'target median[IQR]':22}")
    for k, v in rows:
        tg = t[k]
        print(f"{k:12} {v:>7}   {tg[0]} [{tg[1]}–{tg[2]}]{flag(v, tg)}")
    # section-bound hedging
    hR = M.hedge_density(secs["results"]) if "results" in secs else None
    hD = M.hedge_density(secs["discussion"]) if "discussion" in secs else None
    if hR is not None:
        print(f"{'hedge_R':12} {hR:>7}   {t['hedge_R'][0]} [{t['hedge_R'][1]}–{t['hedge_R'][2]}]{flag(hR, t['hedge_R'])}")
    if hD is not None:
        print(f"{'hedge_D':12} {hD:>7}   {t['hedge_D'][0]} [{t['hedge_D'][1]}–{t['hedge_D'][2]}]{flag(hD, t['hedge_D'])}")
    if "methods" in secs:
        pM = M.passive_ratio(M.split_sentences(secs["methods"]))
        print(f"{'passive_M':12} {pM:>7}   {t['passive_M'][0]} [{t['passive_M'][1]}–{t['passive_M'][2]}] (Methods should stay passive)")
    em = text.count("—")
    print(f"{'em-dash(—)':12} {em:>7}   target ~0 for A/B" + ("  <-- em-dashes present" if em else ""))

    print("\n# AI-tell scan")
    tells = []
    for w in BANNED_INITIAL:
        n = len(re.findall(r"(?:^|[.!?]\s+|\n)\s*" + w + r"\b", text, re.I))
        if n:
            tells.append(f"sentence-initial '{w.capitalize()}' ×{n}")
    frac = re.findall(r"\b(?:nearly|about|roughly|almost)\s+one\s+in\s+(?:two|three|four|five|ten|\d+)\b", text, re.I)
    if frac:
        tells.append(f"template fraction-frame ×{len(frac)} (e.g. 'nearly one in five') — use n/N (%)")
    for pat in APHORISM_HINTS:
        if re.search(pat, text):
            tells.append(f"possible aphoristic closer: /{pat}/")
    if not tells:
        print("  clean — no banned connectives / template frames / obvious aphorisms")
    for x in tells:
        print("  ! " + x)


if __name__ == "__main__":
    main()
