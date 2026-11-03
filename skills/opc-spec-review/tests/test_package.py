from pathlib import Path, PurePosixPath
import json
import re
import unittest
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]


class PackageTests(unittest.TestCase):
    def test_marketplace_entry_matches_plugin_manifest(self):
        marketplace = json.loads(
            (REPO / ".plugin" / "marketplace.json").read_text(encoding="utf-8")
        )
        names = [entry["name"] for entry in marketplace["plugins"]]
        self.assertEqual(len(names), len(set(names)))
        for name in ("opc-spec-review", "claudism-killer"):
            entry = next(row for row in marketplace["plugins"] if row["name"] == name)
            source = REPO.joinpath(*PurePosixPath(entry["source"]).parts)
            manifest = json.loads(
                (source / ".plugin" / "plugin.json").read_text(encoding="utf-8")
            )
            with self.subTest(plugin=name):
                self.assertEqual(manifest, {k: v for k, v in entry.items() if k != "source"})
                self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")
                self.assertEqual(["./"], manifest["skills"])
                self.assertTrue((source / "SKILL.md").is_file())

    def test_frontmatter_exposes_the_review_skill(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        frontmatter = text.split("---", 2)[1]
        self.assertRegex(frontmatter, r"(?m)^name: opc-spec-review$")
        self.assertRegex(frontmatter, r"(?m)^description: >$")
        self.assertNotIn("disable-model-invocation: true", frontmatter)
        self.assertIn("whole repository or named specifications", frontmatter)

    def test_relative_markdown_references_resolve_for_both_plugins(self):
        for plugin in (ROOT, REPO / "skills" / "claudism-killer"):
            for path in plugin.rglob("*.md"):
                text = path.read_text(encoding="utf-8")
                text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
                text = re.sub(r"`[^`\n]*`", "", text)
                for target in re.findall(r"\[[^\]\n]+\]\(([^)\s]+)\)", text):
                    if "://" in target or target.startswith(("#", "mailto:")):
                        continue
                    filename = unquote(target.split("#", 1)[0])
                    resolved = path.parent.joinpath(*PurePosixPath(filename).parts)
                    with self.subTest(file=path.relative_to(REPO), link=target):
                        self.assertTrue(resolved.exists(), resolved)
                        if plugin == ROOT:
                            self.assertTrue(resolved.resolve().is_relative_to(ROOT))

    def test_reference_material_is_reachable_from_skill(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for path in (ROOT / "references").glob("*.md"):
            with self.subTest(reference=path.name):
                self.assertIn(f"(references/{path.name})", skill)

    def test_required_marketplace_companions_are_registered(self):
        marketplace = json.loads(
            (REPO / ".plugin" / "marketplace.json").read_text(encoding="utf-8")
        )
        names = {entry["name"] for entry in marketplace["plugins"]}
        self.assertTrue({"marc-writer", "claudism-killer", "opcua-model-review"} <= names)
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for name in ("opc-spec-review", "marc-writer", "claudism-killer", "opcua-model-review"):
            self.assertIn(f"copilot plugin install {name}@marcschier", readme)
        self.assertIn("distributed separately", readme)

    def test_word_guidance_separates_artifact_identity_and_evidence(self):
        review = (ROOT / "references" / "review.md").read_text(encoding="utf-8")
        word = review.split("### Word documents\n", 1)[1].split(
            "### Word visual inspection and UI blockers\n", 1
        )[0]
        normalized = " ".join(word.split())
        for requirement in (
            "absolute artifact path, SHA-256 hash",
            "source/model/tool input revision or hashes",
            "verify its document's full path",
            "unsaved edits",
            "Recheck identity after regeneration",
            "populated results in the DOCX XML",
            "Separate content evidence from visual evidence",
            "Record the stored results before updating all fields",
            "Quit only a task-owned instance",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, normalized)
        self.assertNotIn("not what a reader sees", normalized)

    def test_word_visual_workflow_preserves_ui_and_verdict_boundaries(self):
        review = (ROOT / "references" / "review.md").read_text(encoding="utf-8")
        visual = review.split("### Word visual inspection and UI blockers\n", 1)[
            1
        ].split("## External dependencies", 1)[0]
        normalized = " ".join(visual.split())
        for requirement in (
            "explicitly in scope",
            "Discover its tool schemas",
            "`list_apps`",
            "`get_window_state`",
            "`start_app`",
            "TextPattern-backed",
            "`element_index` from the latest",
            "Print Layout",
            "`interrupted`",
            "retry the same action",
            "exact tool result",
            "affected artifact hash",
            "pages left unreviewed",
            "not a publication defect",
            "assessment incomplete",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, normalized)

    def test_scope_excludes_dark_mode_and_pdf_rendering(self):
        for relative in ("SKILL.md", "README.md", "references/review.md"):
            text = (ROOT / relative).read_text(encoding="utf-8")
            normalized = " ".join(text.split())
            with self.subTest(file=relative):
                self.assertIn("Dark-mode behavior".lower(), normalized.lower())
                self.assertIn("PDF layout/rendering", normalized)
                self.assertIn("outside", normalized)
                self.assertNotIn("unless the user expands the scope", normalized)

    def test_model_metadata_and_publication_gate_requirements_are_packaged(self):
        review = " ".join((ROOT / "references" / "review.md").read_text(
            encoding="utf-8").split())
        revisions = " ".join((ROOT / "references" / "revisions.md").read_text(
            encoding="utf-8").split())
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        for requirement in (
            "Check primary and RequiredModel metadata separately",
            "An XML schema namespace determines encoded QNames",
            "Validate generated schemas against their dependencies",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, review)
        for requirement in (
            "publication workflow invokes each applicable gate after rendering",
            "inspect uploaded artifacts for the sidecars",
            "Record local and CI results separately",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, revisions)
        for scenario in ("Primary model metadata", "Generated schema", "Publication gate"):
            with self.subTest(scenario=scenario):
                self.assertIn(f"| {scenario} |", acceptance)


if __name__ == "__main__":
    unittest.main()
