from pathlib import Path
import runpy
import unittest


plan = runpy.run_path(str(Path(__file__).resolve().parents[1] / "chunks.py"))["plan"]


class ChunkPlanTests(unittest.TestCase):
    def test_prefers_real_headings_to_blank_lines_and_fenced_headings(self):
        first = "## First\n\n~" + "~~\n## Fake\n~~~\n\n"
        second = "## Second\n\n" + "Prose. " * 8
        parts = list(plan(first + second, limit=50))
        self.assertEqual(parts[0]["end"], len(first))
        self.assertEqual(parts[1]["first_line"], 7)
        self.assertEqual(parts[0]["protected"], [(first.index("~~~"), first.rindex("~~~") + 4)])

    def test_reconstructs_large_file_and_preserves_protection_across_chunks(self):
        block = "<!-- BEGIN GENERATED -->\r\n" + "é" * 270_000 + "\r\n<!-- END GENERATED -->\r\n"
        tail = "\r\n## Last\r\nFinal prose.\r\n"
        text = block + tail
        chunks = list(plan(text))
        self.assertTrue(all(0 < c["end"] - c["start"] <= 10_000 for c in chunks))
        self.assertEqual("".join(text[c["start"]:c["end"]] for c in chunks), text)
        protected = [span for c in chunks for span in c["protected"]]
        self.assertEqual("".join(text[lo:hi] for lo, hi in protected), block)
        self.assertEqual(chunks[-1]["last_line"], len(text.splitlines()))

    def test_unclosed_fence_remains_protected_through_eof(self):
        text = "Intro.\n````md\n```\n# Still code\n"
        chunks = list(plan(text, limit=18))
        protected = [span for c in chunks for span in c["protected"]]
        self.assertEqual("".join(text[lo:hi] for lo, hi in protected), text[7:])
