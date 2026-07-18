#!/usr/bin/env python3
"""Check a clinical draft for AI tells and optional neurovascular voice drift.

Examples:
    python3 check_draft.py draft.txt --study-family observational --profile general
    python3 check_draft.py draft.txt --study-family imaging --profile neurovascular
    python3 check_draft.py draft.txt --genre A  # legacy alias; implies neurovascular
"""
from __future__ import annotations

import argparse
import importlib.util
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("clinical_metrics", HERE / "metrics.py")
M = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(M)

TARGETS = {
    "A": {"mean_len": (31, 27, 37), "sd_len": (43, 38, 63), "burstiness": (24, 19, 37),
          "short%": (25, 20, 31), "long%": (13, 9, 16), "hedge_R": (0.7, 0, 1.6),
          "hedge_D": (11, 8, 12), "passive_M": (0.56, 0.46, 0.67)},
    "B": {"mean_len": (30, 28, 33), "sd_len": (38, 32, 42), "burstiness": (21, 21, 26),
          "short%": (26, 23, 29), "long%": (13, 12, 16), "hedge_R": (1.4, 0, 2.3),
          "hedge_D": (11, 9, 14), "passive_M": (0.72, 0.50, 0.78)},
    "C": {"mean_len": (35, 31, 37), "sd_len": (52, 44, 60), "burstiness": (31, 28, 33),
          "short%": (30, 23, 34), "long%": (20, 16, 23), "hedge_R": (0.7, 0, 0.9),
          "hedge_D": (8, 6, 11), "passive_M": (0.55, 0.43, 0.59)},
}

FAMILY_TO_GENRE = {
    "observational": "A",
    "procedural": "A",
    "procedural-comparative": "A",
    "imaging": "B",
    "diagnostic-imaging": "B",
    "trial": "C",
    "trial-secondary": "C",
}
BANNED_INITIAL = [
    "moreover", "furthermore", "additionally", "notably", "importantly",
    "consequently", "nevertheless",
]
APHORISM_HINTS = [
    r"\bThe \w+ is elsewhere\b",
    r"\bNothing here\b",
    r"\bis speculative\b",
    r"\bmoved in the opposite direction\b",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("draft", type=Path, help="plain-text or Markdown manuscript/section")
    parser.add_argument(
        "--study-family",
        choices=sorted(FAMILY_TO_GENRE),
        default="observational",
        help="clinical study family (default: observational)",
    )
    parser.add_argument(
        "--profile",
        choices=("general", "neurovascular"),
        default=None,
        help="general scans AI tells; neurovascular also compares the 32-paper fingerprint",
    )
    parser.add_argument(
        "--genre",
        choices=("A", "B", "C", "a", "b", "c"),
        help="legacy alias for the original corpus genre; implies --profile neurovascular",
    )
    return parser.parse_args()


def outside_iqr(value: float, target: tuple[float, float, float]) -> str:
    return "  <-- outside IQR" if value < target[1] or value > target[2] else ""


def print_fingerprint(text: str, sections: dict[str, str], genre: str) -> None:
    sentences = M.split_sentences(sections.get("all", text))
    stats = M.sentence_stats(sentences)
    target = TARGETS[genre]
    rows = [
        ("mean_len", stats.get("mean_len", 0)),
        ("sd_len", stats.get("sd_len", 0)),
        ("burstiness", stats.get("burstiness_masd", 0)),
        ("short%", stats.get("pct_short_le15", 0)),
        ("long%", stats.get("pct_long_ge40", 0)),
    ]
    print("\n# neurovascular fingerprint")
    print(f"{'metric':12} {'draft':>7}   {'target median[IQR]':22}")
    for key, value in rows:
        selected = target[key]
        print(
            f"{key:12} {value:>7}   {selected[0]} "
            f"[{selected[1]}–{selected[2]}]{outside_iqr(value, selected)}"
        )

    section_metrics = (
        ("results", "hedge_R", M.hedge_density),
        ("discussion", "hedge_D", M.hedge_density),
    )
    for section, key, measure in section_metrics:
        if section in sections:
            value = measure(sections[section])
            selected = target[key]
            print(
                f"{key:12} {value:>7}   {selected[0]} "
                f"[{selected[1]}–{selected[2]}]{outside_iqr(value, selected)}"
            )
    if "methods" in sections:
        value = M.passive_ratio(M.split_sentences(sections["methods"]))
        selected = target["passive_M"]
        print(
            f"{'passive_M':12} {value:>7}   {selected[0]} "
            f"[{selected[1]}–{selected[2]}] (Methods may intentionally remain passive)"
        )
    em_dashes = text.count("—")
    warning = "  <-- off-profile for A/B" if em_dashes and genre in {"A", "B"} else ""
    print(f"{'em-dash(—)':12} {em_dashes:>7}{warning}")


def scan_ai_tells(text: str) -> list[str]:
    tells: list[str] = []
    for word in BANNED_INITIAL:
        count = len(re.findall(r"(?:^|[.!?]\s+|\n)\s*" + word + r"\b", text, re.I))
        if count:
            tells.append(f"sentence-initial '{word.capitalize()}' ×{count}")
    fractions = re.findall(
        r"\b(?:nearly|about|roughly|almost)\s+one\s+in\s+"
        r"(?:two|three|four|five|ten|\d+)\b",
        text,
        re.I,
    )
    if fractions:
        tells.append(f"rhetorical fraction frame ×{len(fractions)}; prefer a recoverable n/N (%)")
    for pattern in APHORISM_HINTS:
        if re.search(pattern, text, re.I):
            tells.append(f"possible aphoristic closer: /{pattern}/")
    return tells


def main() -> None:
    args = parse_args()
    if not args.draft.is_file():
        raise SystemExit(f"draft not found: {args.draft}")

    genre = args.genre.upper() if args.genre else FAMILY_TO_GENRE[args.study_family]
    profile = args.profile or ("neurovascular" if args.genre else "general")
    text = args.draft.read_text(encoding="utf-8", errors="ignore")
    sections = M.find_sections(text)

    print(
        f"# check: {args.draft.name} "
        f"(study-family {args.study_family}; profile {profile}; legacy genre {genre})"
    )
    tells = scan_ai_tells(text)
    print("\n# AI-tell scan")
    if not tells:
        print("  clean — no configured connective, fraction-frame, or aphorism tells")
    else:
        for tell in tells:
            print("  ! " + tell)

    if profile == "neurovascular":
        print_fingerprint(text, sections, genre)
    else:
        print("\n# profile note\n  general mode does not enforce specialty-derived numeric ranges")


if __name__ == "__main__":
    main()
