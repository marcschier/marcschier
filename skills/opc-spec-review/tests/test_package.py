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


if __name__ == "__main__":
    unittest.main()
