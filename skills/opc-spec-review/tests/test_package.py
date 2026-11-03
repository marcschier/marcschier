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
            "task-owned copy",
            "record its new hash",
            "Recheck identity after regeneration",
            "Resolve relationship IDs to their targets",
            "fields whose updated results depend on the filename or environment",
            "matching body text alone does not establish equivalent pagination",
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
            "cell-level legibility separately",
            "let the view settle and reread it",
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

    def test_contents_update_does_not_establish_all_field_or_visual_coverage(self):
        review = " ".join(
            (ROOT / "references" / "review.md").read_text(encoding="utf-8").split()
        )
        for requirement in (
            '"Update Table of Contents" ribbon action can update only the contents',
            "lists of figures and tables remain placeholders",
            "Update and verify each list separately",
            "Record which fields resolved and which remain placeholders or errors",
            "does not establish that all fields were updated or that pagination "
            "was visually reviewed",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, review)
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        self.assertIn("| Contents-only update |", acceptance)

    def test_captions_ribbon_fallback_preserves_independent_coverage(self):
        review = " ".join(
            (ROOT / "references" / "review.md").read_text(encoding="utf-8").split()
        )
        for requirement in (
            "If a focused `F9` dispatch fails through UI automation",
            "place the caret inside the figures or tables placeholder",
            "References > Captions > Update Table",
            "`TableOfFiguresUpdate`",
            "find it in a fresh accessibility state",
            "act through its current node index",
            "References > Table of Contents > Update Table",
            "Reread the selected field to verify the result",
            "with the caret inside the respective field",
            "Update and verify figures and tables separately",
            "one invocation does not establish that both lists were updated",
            "Keep contents, remaining fields and visual pagination coverage independent",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, review)
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        self.assertIn("| Captions ribbon fallback |", acceptance)

    def test_scope_excludes_dark_mode_and_pdf_rendering(self):
        for relative in ("SKILL.md", "README.md", "references/review.md"):
            text = (ROOT / relative).read_text(encoding="utf-8")
            normalized = " ".join(text.split())
            with self.subTest(file=relative):
                self.assertIn("Dark-mode behavior".lower(), normalized.lower())
                self.assertIn("PDF layout/rendering", normalized)
                self.assertIn("outside", normalized)
                self.assertNotIn("unless the user expands the scope", normalized)

    def test_main_story_update_fallback_limits_evidence_and_customization(self):
        review = " ".join(
            (ROOT / "references" / "review.md").read_text(encoding="utf-8").split()
        )
        for requirement in (
            "task-owned current DOCX copy",
            "Word Options > Quick Access Toolbar",
            "Choose commands from to All Commands",
            "command named `Update` for this document only, not for all documents",
            "`FieldsUpdate`",
            "Home > Select > Select All",
            "record the selected and total word counts",
            "Handle each resulting dialog separately",
            "selecting Update entire table",
            "Update Table of Contents followed by two Update Table of Figures dialogs",
            "do not assume every document produces exactly three prompts",
            "Undo Update Fields",
            "invocation evidence does not establish their correctness",
            "Save only the authorized task-owned copy and record its new hash",
            "headers, footers or other stories",
            "or establishes visual pagination coverage",
            "retain the per-list Captions fallback above",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, review)
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        self.assertIn("| Main-story Update fallback |", acceptance)

    def test_unsupported_update_radio_action_uses_fresh_dialog_evidence(self):
        review = " ".join(
            (ROOT / "references" / "review.md").read_text(encoding="utf-8").split()
        )
        for requirement in (
            "`UIA SelectionItem.Select member not found`",
            "capture a fresh dialog screenshot",
            "coordinates from that capture through Computer Use",
            "Reinspect the dialog to confirm the selection before accepting it",
            "do not repeat the unsupported action or use stale coordinates",
            "or for the unsupported dialog action described above",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, review)
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        self.assertIn("| Unsupported update radio action |", acceptance)

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

        for scenario in (
            "Saved Word evidence copy",
            "Changed Word package",
            "Delayed Word navigation",
            "Word grid and zoom",
        ):
            with self.subTest(scenario=scenario):
                self.assertIn(f"| {scenario} |", acceptance)

    def test_first_edition_and_changed_render_evidence(self):
        skill = " ".join((ROOT / "SKILL.md").read_text(encoding="utf-8").split())
        review = " ".join((ROOT / "references" / "review.md").read_text(
            encoding="utf-8").split())
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        self.assertIn("Do not assume a first edition has an earlier contract", skill)
        self.assertIn("assess that stated target", skill)
        self.assertIn("A change to a render input makes it stale", skill)
        self.assertIn("compare a fresh publication with the reviewed output", review)
        self.assertIn("Carry forward coverage only for unchanged content and figures", review)
        self.assertIn("| First-edition interoperability |", acceptance)
        self.assertIn("| Changed model render |", acceptance)

    def test_command_probes_preserve_existing_output(self):
        skill = " ".join((ROOT / "SKILL.md").read_text(encoding="utf-8").split())
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        for requirement in (
            "an unrecognized `--help` can execute the command",
            "Do not probe an unfamiliar command against existing output directories",
            "stop the task-owned process, record the affected paths and tell the user",
            "Do not assume ignored output is disposable",
            "restore it without a verified copy of its previous contents",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, skill)
        self.assertIn("| Unsafe help probe |", acceptance)


if __name__ == "__main__":
    unittest.main()
