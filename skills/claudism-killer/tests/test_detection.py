from pathlib import Path
import json
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


def contextual_patterns():
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    block = text.split("# Context-sensitive candidates:", 1)[1]
    block = block.split("# Tier 2 candidates", 1)[0]
    return [
        re.compile(line, re.IGNORECASE)
        for line in block.splitlines()
        if line.startswith(r"\b")
    ]


def raw_candidates(text):
    normalized = text.replace("\u2019", "'")
    paragraphs = [
        re.sub(r"\s*\n\s*", " ", paragraph)
        for paragraph in normalized.split("\n\n")
    ]
    normalized = "\n\n".join(paragraphs)
    matches = [
        (match.start(), match.end(), match.group())
        for pattern in contextual_patterns()
        for match in pattern.finditer(normalized)
    ]
    selected = []
    for start, end, value in sorted(matches, key=lambda row: (row[0], -row[1])):
        if not selected or start >= selected[-1][1]:
            selected.append((start, end, value))
    return [value for _, _, value in selected]


class ContextualDetectionTests(unittest.TestCase):
    def test_catalogue_patterns_match_synthetic_candidates(self):
        cases = json.loads((ROOT / "tests" / "cases.json").read_text(encoding="utf-8"))
        self.assertEqual(2, len(contextual_patterns()))
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertEqual(case["candidates"], raw_candidates(case["text"]))

    def test_wrapped_conformance_phrase_is_one_occurrence(self):
        self.assertEqual(
            ["conformance claims", "worked"],
            raw_candidates("The conformance\nclaims accompany the worked\nexample."),
        )

    def test_hyphenated_family_is_not_double_counted(self):
        self.assertEqual(
            ["conformance-claims", "claims", "claiming", "claimable", "claimed"],
            raw_candidates("conformance-claims claims claiming claimable claimed"),
        )

    def test_paragraph_boundaries_do_not_form_a_phrase(self):
        self.assertEqual(["claims"], raw_candidates("conformance\n\nclaims"))

    def test_empty_and_unrelated_prose_have_no_candidates(self):
        for text in ("", "The server returns the identifier.", "reworked acclaimed claimant"):
            with self.subTest(text=text):
                self.assertEqual([], raw_candidates(text))

    def test_judgment_cases_require_reasons_and_preserve_unresolved_text(self):
        cases = json.loads((ROOT / "tests" / "cases.json").read_text(encoding="utf-8"))
        self.assertEqual(len(cases), len({case["id"] for case in cases}))
        self.assertEqual(
            {"rewrite", "protect", "unresolved"},
            {case["disposition"] for case in cases},
        )
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertTrue(case["reason"].strip())
                if case["disposition"] == "rewrite":
                    self.assertIsInstance(case["revision"], str)
                    self.assertNotEqual(case["text"], case["revision"])
                else:
                    self.assertIsNone(case["revision"])


if __name__ == "__main__":
    unittest.main()
