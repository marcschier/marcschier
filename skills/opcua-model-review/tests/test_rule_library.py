from pathlib import Path, PurePosixPath
import json
import re
import sys
import unittest
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_nodeset as checker


class RuleLibraryTests(unittest.TestCase):
    def test_every_rule_has_a_unique_stable_identifier(self):
        catalog = checker.load_catalog()
        expected = {f"P3-{number:03}" for number in range(1, 208)}
        expected |= {f"BP-{number:03}" for number in range(1, 227)}
        expected.add("P5-001")
        self.assertEqual(expected, {row["id"] for row in catalog})
        self.assertEqual(434, len(catalog))
        for row in catalog:
            with self.subTest(rule=row["id"]):
                self.assertTrue(row["sources"])
                self.assertTrue(row["targets"])
                self.assertIn(row["strength"], {"MUST", "MUST NOT", "SHOULD", "SHOULD NOT", "MAY", "INFORMATIVE"})
                for url in row["sources"]:
                    self.assertRegex(url, r"^https://reference\.opcfoundation\.org/specs/OPC-(?:10000-[35]|11030)/v[0-9]+\.[0-9]+\.[0-9]+/")

    def test_best_practice_authority_is_explicitly_advisory(self):
        for row in checker.load_catalog():
            if row["id"].startswith("BP-"):
                with self.subTest(rule=row["id"]):
                    self.assertEqual("guidance", row["authority"])
                    text = (ROOT / row["file"]).read_text(encoding="utf-8")
                    self.assertIn("non-mandatory whitepaper", text)
                    if row["strength"] == "MAY":
                        self.assertIn("Permission guard", text)

    def test_relative_markdown_links_resolve(self):
        for path in ROOT.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
            text = re.sub(r"`[^`\n]*`", "", text)
            for target in re.findall(r"\[[^\]\n]+\]\(([^)\s]+)\)", text):
                if "://" in target or target.startswith(("#", "mailto:")):
                    continue
                filename = unquote(target.split("#", 1)[0])
                if not filename:
                    continue
                resolved = path.parent.joinpath(*PurePosixPath(filename).parts).resolve()
                with self.subTest(file=path.relative_to(ROOT), link=target):
                    self.assertTrue(resolved.exists(), resolved)

    def test_source_coverage_accounts_for_both_complete_documents(self):
        text = (ROOT / "rules" / "COVERAGE.md").read_text(encoding="utf-8")
        part3, best_practices = text.split("## OPC 11030", 1)
        best_practices = best_practices.split("## Explicit supplement", 1)[0]
        self.assertEqual(323, len(re.findall(r"^\| \[[^\]]+\]\(https://reference\.opcfoundation\.org/specs/OPC-10000-3/", part3, re.MULTILINE)))
        self.assertEqual(119, len(re.findall(r"^\| \[[^\]]+\]\(https://reference\.opcfoundation\.org/specs/OPC-11030/", best_practices, re.MULTILINE)))
        for row in checker.load_catalog():
            self.assertIn(row["id"], text)

    def test_standard_metadata_is_pinned_and_not_a_full_model(self):
        metadata = json.loads((ROOT / "scripts" / "ua_namespace0.json").read_text(encoding="utf-8"))
        self.assertEqual("1.05.06", metadata["version"])
        self.assertIn("36d5fcead17f52844fc32b917bca767d09ccf535", metadata["source"])
        self.assertRegex(metadata["source_sha256"], r"^[0-9a-f]{64}$")
        self.assertIn("Does not include complete standard member declarations", metadata["scope"])
        ids = [node["id"] for node in metadata["nodes"]]
        self.assertEqual(len(ids), len(set(ids)))


if __name__ == "__main__":
    unittest.main()
