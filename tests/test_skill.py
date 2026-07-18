from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "scripts" / "check_draft.py"
PIPELINE = ROOT / "distillation" / "pipeline.py"
TRACKED = ROOT / "scripts" / "apply_tracked_changes.py"
RATIONALE = ROOT / "scripts" / "build_rationale_docx.py"
FIXTURE = ROOT / "tests" / "fixtures" / "sample_manuscript.txt"


class SkillTests(unittest.TestCase):
    def run_command(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, *args],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_check_draft_help(self) -> None:
        result = self.run_command(str(CHECK), "--help")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("--study-family", result.stdout)
        self.assertIn("--profile", result.stdout)

    def test_general_profile_skips_specialty_targets(self) -> None:
        result = self.run_command(
            str(CHECK),
            str(FIXTURE),
            "--study-family",
            "observational",
            "--profile",
            "general",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("does not enforce specialty-derived numeric ranges", result.stdout)
        self.assertNotIn("# neurovascular fingerprint", result.stdout)

    def test_legacy_genre_enables_neurovascular_profile(self) -> None:
        result = self.run_command(str(CHECK), str(FIXTURE), "--genre", "B")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("profile neurovascular", result.stdout)
        self.assertIn("# neurovascular fingerprint", result.stdout)

    def test_pipeline_workspace_validation(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            init = self.run_command(str(PIPELINE), "init", "--workspace", str(root))
            self.assertEqual(init.returncode, 0, init.stderr)
            corpus = root / "_corpus" / "paper01.txt"
            corpus.write_text(FIXTURE.read_text(encoding="utf-8"), encoding="utf-8")
            metadata = {
                "id": "paper01",
                "genre": "A",
                "study_type": "prognostic-predictor",
                "primary_endpoint": "90-day functional independence",
                "claim_gradient": "associational",
            }
            (root / "_meta" / "paper01.json").write_text(json.dumps(metadata), encoding="utf-8")
            metrics = self.run_command(str(PIPELINE), "metrics", "--workspace", str(root))
            self.assertEqual(metrics.returncode, 0, metrics.stderr)
            validate = self.run_command(str(PIPELINE), "validate", "--workspace", str(root))
            self.assertEqual(validate.returncode, 0, validate.stderr)
            self.assertIn("workspace valid", validate.stdout)

    def test_public_tree_has_no_forbidden_artifacts_or_paths(self) -> None:
        result = self.run_command(str(PIPELINE), "scan-public", "--root", str(ROOT))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("public tree clean", result.stdout)

    def test_skill_reference_paths_exist(self) -> None:
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        references = set(re.findall(r"`(references/[^` ]+\.md)`", text))
        self.assertGreaterEqual(len(references), 10)
        missing = [reference for reference in references if not (ROOT / reference).is_file()]
        self.assertEqual(missing, [])

    def test_public_manifest_distribution(self) -> None:
        manifest = ROOT / "distillation" / "corpus_manifest.public.csv"
        rows = manifest.read_text(encoding="utf-8").splitlines()[1:]
        self.assertEqual(len(rows), 32)
        genres = [row.split(",")[1] for row in rows]
        self.assertEqual({genre: genres.count(genre) for genre in "ABC"}, {"A": 13, "B": 7, "C": 12})

    def test_tracked_change_replace_is_reversible_ooxml(self) -> None:
        document = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body><w:p><w:r><w:t>Original clinical sentence.</w:t></w:r></w:p></w:body>
</w:document>
"""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            word = root / "unpacked" / "word"
            word.mkdir(parents=True)
            (word / "document.xml").write_text(document, encoding="utf-8")
            edits = root / "edits.json"
            edits.write_text(
                json.dumps([
                    {
                        "type": "replace",
                        "find": "Original clinical sentence.",
                        "replace": "Revised clinical sentence.",
                    }
                ]),
                encoding="utf-8",
            )
            result = self.run_command(
                str(TRACKED), str(root / "unpacked"), str(edits), "--author", "Codex"
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("applied=1", result.stdout)
            revised = (word / "document.xml").read_text(encoding="utf-8")
            self.assertIn("w:del", revised)
            self.assertIn("w:ins", revised)
            self.assertIn("Original clinical sentence.", revised)
            self.assertIn("Revised clinical sentence.", revised)
            self.assertIn("Codex", revised)

    def test_rationale_docx_builds(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "rationale.md"
            output = root / "rationale.docx"
            source.write_text("# 修改理由\n1. **改动**：调整临床表述。\n", encoding="utf-8")
            result = self.run_command(str(RATIONALE), str(source), str(output))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(output.is_file())
            with zipfile.ZipFile(output) as archive:
                xml = archive.read("word/document.xml").decode("utf-8")
            self.assertIn("修改理由", xml)


if __name__ == "__main__":
    unittest.main()
