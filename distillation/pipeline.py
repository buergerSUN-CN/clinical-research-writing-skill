#!/usr/bin/env python3
"""Portable build and validation helpers for clinical-research-writing distillation.

The deterministic phases run locally. Deep-read and critic phases are performed by a host agent
using METHOD.md and the JSON schemas, then validated here.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

PHASES = [
    "init",
    "metadata",
    "metrics",
    "section-extraction",
    "pattern-and-cognition",
    "critic-and-leave-one-out",
    "compile-and-release",
]
REQUIRED_META = {"id", "genre", "study_type", "primary_endpoint", "claim_gradient"}
REQUIRED_PATTERN = {"section", "moves", "variant_notes"}
REQUIRED_COGNITION = {"genre", "recurring_propositions", "claim_gradient_habit", "signature_moves"}
TEXT_SUFFIXES = {".md", ".txt", ".py", ".json", ".yaml", ".yml", ".csv"}
FORBIDDEN_PUBLIC_SUFFIXES = {".pdf", ".docx", ".doc", ".rtf", ".epub"}
LOCAL_PATH = re.compile(r"/(?:Users|Volumes)/[^\s)`'\"]+")
WORD = re.compile(r"[A-Za-z][A-Za-z0-9'-]*")


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def workspace(path: str) -> Path:
    return Path(path).expanduser().resolve()


def state_path(root: Path) -> Path:
    return root / ".redistill-state.json"


def load_state(root: Path) -> dict:
    path = state_path(root)
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"skill_name": "clinical-research-writing", "phases": PHASES, "completed_phases": []}


def save_state(root: Path, state: dict) -> None:
    state["updated_at"] = now()
    write_json(state_path(root), state)


def cmd_init(args: argparse.Namespace) -> None:
    root = workspace(args.workspace)
    for name in ("_corpus", "_meta", "_metrics", "_analysis", "_validation", "_output"):
        (root / name).mkdir(parents=True, exist_ok=True)
    state = load_state(root)
    state.update({
        "skill_name": "clinical-research-writing",
        "voice_scope": "general-core-plus-optional-profile",
        "phases": PHASES,
        "created_at": state.get("created_at", now()),
    })
    completed = set(state.get("completed_phases", []))
    completed.add("init")
    state["completed_phases"] = [phase for phase in PHASES if phase in completed]
    save_state(root, state)
    print(root)


def load_metrics_module(skill_root: Path):
    metrics_path = skill_root / "scripts" / "metrics.py"
    spec = importlib.util.spec_from_file_location("clinical_distill_metrics", metrics_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {metrics_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def cmd_metrics(args: argparse.Namespace) -> None:
    root = workspace(args.workspace)
    skill_root = Path(__file__).resolve().parents[1]
    subprocess.run(
        [sys.executable, str(skill_root / "scripts" / "metrics.py"), str(root)],
        check=True,
    )
    state = load_state(root)
    completed = set(state.get("completed_phases", []))
    completed.add("metrics")
    state["completed_phases"] = [phase for phase in PHASES if phase in completed]
    save_state(root, state)


def cmd_export_sections(args: argparse.Namespace) -> None:
    root = workspace(args.workspace)
    metrics = load_metrics_module(Path(__file__).resolve().parents[1])
    corpus = root / "_corpus"
    meta = root / "_meta"
    out = root / "_analysis" / "sections"
    for section in ("head", "introduction", "methods", "results", "discussion"):
        (out / section).mkdir(parents=True, exist_ok=True)
    rows: list[tuple[str, str, str]] = []
    for source in sorted(corpus.glob("paper*.txt")):
        paper_id = source.stem
        text = source.read_text(encoding="utf-8", errors="ignore")
        sections = metrics.find_sections(text)
        body = metrics.strip_back_matter(text)
        starts: list[int] = []
        offset = 0
        for line in body.split("\n"):
            if any(regex.match(line) for regex in metrics.HEADER_LINE.values()):
                starts.append(offset)
            offset += len(line) + 1
        head = body[: min(starts)] if starts else body[:2500]
        (out / "head" / f"{paper_id}.txt").write_text(head, encoding="utf-8")
        present = ["head"]
        for section in ("introduction", "methods", "results", "discussion"):
            if section in sections and len(metrics.words(sections[section])) > 40:
                (out / section / f"{paper_id}.txt").write_text(sections[section], encoding="utf-8")
                present.append(section)
        metadata_path = meta / f"{paper_id}.json"
        genre = "?"
        if metadata_path.exists():
            genre = json.loads(metadata_path.read_text(encoding="utf-8")).get("genre", "?")
        rows.append((paper_id, genre, ";".join(present)))
    with (out / "index.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(("id", "genre", "sections"))
        writer.writerows(rows)
    state = load_state(root)
    completed = set(state.get("completed_phases", []))
    completed.add("section-extraction")
    state["completed_phases"] = [phase for phase in PHASES if phase in completed]
    save_state(root, state)
    print(f"exported sections for {len(rows)} papers")


def require_keys(path: Path, required: set[str]) -> list[str]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path}: invalid JSON ({exc})"]
    missing = required - set(payload)
    return [f"{path}: missing {', '.join(sorted(missing))}"] if missing else []


def collect_counts(root: Path) -> dict[str, int]:
    return {
        "corpus": len(list((root / "_corpus").glob("paper*.txt"))),
        "metadata": len(list((root / "_meta").glob("paper*.json"))),
        "paper_metrics": len(list((root / "_metrics").glob("paper*.json"))),
        "genre_metrics": len(list((root / "_metrics").glob("genre_*.json"))),
        "section_patterns": len(list((root / "_analysis").glob("patterns_*.json"))),
        "cognition_profiles": len(list((root / "_analysis").glob("cognition_*.json"))),
        "validation_artifacts": len([path for path in (root / "_validation").glob("*") if path.is_file()]),
    }


def validate_workspace(root: Path) -> tuple[dict[str, int], list[str]]:
    counts = collect_counts(root)
    errors: list[str] = []
    if counts["corpus"] != counts["metadata"]:
        errors.append(f"corpus/metadata mismatch: {counts['corpus']} vs {counts['metadata']}")
    for path in (root / "_meta").glob("paper*.json"):
        errors.extend(require_keys(path, REQUIRED_META))
    for path in (root / "_analysis").glob("patterns_*.json"):
        errors.extend(require_keys(path, REQUIRED_PATTERN))
    for path in (root / "_analysis").glob("cognition_*.json"):
        errors.extend(require_keys(path, REQUIRED_COGNITION))
    if counts["corpus"] and counts["paper_metrics"] != counts["corpus"]:
        errors.append(f"paper metrics incomplete: {counts['paper_metrics']}/{counts['corpus']}")
    return counts, errors


def cmd_validate(args: argparse.Namespace) -> None:
    root = workspace(args.workspace)
    counts, errors = validate_workspace(root)
    print(json.dumps(counts, indent=2))
    if errors:
        for error in errors:
            print("ERROR:", error, file=sys.stderr)
        raise SystemExit(1)
    print("workspace valid")


def iter_public_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or any(
            part in {".git", "__pycache__", "_archive"} for part in path.parts
        ):
            continue
        yield path


def word_ngrams(text: str, size: int) -> set[tuple[str, ...]]:
    words = [word.lower() for word in WORD.findall(text)]
    return {tuple(words[index:index + size]) for index in range(len(words) - size + 1)}


def scan_public(root: Path, corpus: Path | None, overlap_words: int) -> list[str]:
    errors: list[str] = []
    corpus_ngrams: set[tuple[str, ...]] = set()
    if corpus:
        for path in corpus.glob("paper*.txt"):
            corpus_ngrams.update(word_ngrams(path.read_text(encoding="utf-8", errors="ignore"), overlap_words))
    for path in iter_public_files(root):
        rel = path.relative_to(root)
        if path.suffix.lower() in FORBIDDEN_PUBLIC_SUFFIXES:
            errors.append(f"forbidden public artifact: {rel}")
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in LOCAL_PATH.finditer(text):
            errors.append(f"local absolute path in {rel}: {match.group(0)}")
        if corpus_ngrams and rel.parts[0] in {"references", "SKILL.md"}:
            overlap = word_ngrams(text, overlap_words) & corpus_ngrams
            if overlap:
                sample = " ".join(next(iter(overlap)))
                errors.append(f"{overlap_words}-word corpus overlap in {rel}: {sample}")
    return errors


def cmd_scan_public(args: argparse.Namespace) -> None:
    root = workspace(args.root)
    corpus = workspace(args.corpus) if args.corpus else None
    errors = scan_public(root, corpus, args.overlap_words)
    if errors:
        for error in errors:
            print("ERROR:", error, file=sys.stderr)
        raise SystemExit(1)
    print("public tree clean")


def cmd_compile(args: argparse.Namespace) -> None:
    root = workspace(args.workspace)
    source = root / "_output" / "clinical-research-writing"
    destination = workspace(args.out)
    if not (source / "SKILL.md").is_file():
        raise SystemExit(f"compiled skill missing: {source / 'SKILL.md'}")
    errors = scan_public(source, root / "_corpus", args.overlap_words)
    if errors:
        for error in errors:
            print("ERROR:", error, file=sys.stderr)
        raise SystemExit(1)
    if destination.exists():
        if not args.replace:
            raise SystemExit(f"destination exists; pass --replace: {destination}")
        shutil.rmtree(destination)
    shutil.copytree(source, destination)
    print(destination)


def cmd_report(args: argparse.Namespace) -> None:
    root = workspace(args.workspace)
    counts, errors = validate_workspace(root)
    state = load_state(root)
    payload = {
        "skill": "clinical-research-writing",
        "generated_at": now(),
        "counts": counts,
        "completed_phases": state.get("completed_phases", []),
        "validation": "pass" if not errors else "fail",
        "errors": errors,
        "publication_policy": {
            "raw_corpus_public": False,
            "long_verbatim_exemplars_public": False,
            "local_paths_public": False,
        },
    }
    output = Path(args.out).expanduser().resolve()
    write_json(output, payload)
    print(output)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name, function in (
        ("init", cmd_init),
        ("metrics", cmd_metrics),
        ("export-sections", cmd_export_sections),
        ("validate", cmd_validate),
        ("report", cmd_report),
    ):
        item = sub.add_parser(name)
        item.add_argument("--workspace", required=True)
        item.set_defaults(function=function)
    report = sub.choices["report"]
    report.add_argument("--out", required=True)

    scan = sub.add_parser("scan-public")
    scan.add_argument("--root", required=True)
    scan.add_argument("--corpus")
    scan.add_argument("--overlap-words", type=int, default=12)
    scan.set_defaults(function=cmd_scan_public)

    compile_parser = sub.add_parser("compile")
    compile_parser.add_argument("--workspace", required=True)
    compile_parser.add_argument("--out", required=True)
    compile_parser.add_argument("--replace", action="store_true")
    compile_parser.add_argument("--overlap-words", type=int, default=12)
    compile_parser.set_defaults(function=cmd_compile)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    args.function(args)


if __name__ == "__main__":
    main()
