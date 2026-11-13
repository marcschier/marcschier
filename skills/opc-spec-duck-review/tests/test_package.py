from pathlib import Path, PurePosixPath
import json
import re
import unittest
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]


def prose(path):
    return " ".join((ROOT / path).read_text(encoding="utf-8").split())


class PackageTests(unittest.TestCase):
    def test_marketplace_entry_and_discoverable_skill(self):
        catalog = json.loads(
            (REPO / ".plugin" / "marketplace.json").read_text(encoding="utf-8")
        )
        entries = [
            item for item in catalog["plugins"]
            if item["name"] == "opc-spec-duck-review"
        ]
        self.assertEqual(1, len(entries))
        entry = entries[0]
        self.assertEqual(ROOT, REPO.joinpath(*PurePosixPath(entry["source"]).parts))
        manifest = json.loads(
            (ROOT / ".plugin" / "plugin.json").read_text(encoding="utf-8")
        )
        self.assertEqual(manifest, {k: v for k, v in entry.items() if k != "source"})
        self.assertEqual(["./"], manifest["skills"])
        self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        frontmatter = text.split("---", 2)[1]
        self.assertRegex(frontmatter, r"(?m)^name: opc-spec-duck-review$")
        self.assertIn("rubber-duck dialogue", frontmatter)
        self.assertNotIn("disable-model-invocation: true", frontmatter)

    def test_scope_and_write_permissions_are_separate(self):
        text = prose("SKILL.md").split("## 1. Agree the scope", 1)[1].split(
            "## 2.", 1
        )[0]
        for rule in (
            "ask the user which specifications to review",
            "only each specification's source folder or also its Publisher-rendered HTML",
            "Ask one question at a time",
            "A request for review alone authorizes no edits",
            "Keep other specifications outside the edit scope",
            "including manifest terms and profile descriptions",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, text)

    def test_agents_and_domain_knowledge_are_isolated(self):
        skill = prose("SKILL.md")
        reader = prose("references/roles.md").split("## Reader", 1)[1].split(
            "## Editor", 1
        )[0]
        for rule in (
            "one dedicated editor agent and retain it",
            "a separate reader agent for each full pass",
            "without inherited conversation",
            "Separate agents are mandatory",
            "honor host model defaults",
            "Both agents must use the OPC UA knowledge-base MCP tools",
            "https://reference.opcfoundation.org/",
            "Never upload private drafts or models",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, skill)
        for rule in (
            "dependent OPC UA specifications, including preceding parts",
            "Start without knowledge",
            "do not use that recognition to fill a gap",
            "Non-OPC UA references, even normative ones",
            "rather than silently researching that domain",
            "cannot edit sources or generated publications",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, reader)

    def test_forward_reading_has_exhaustive_located_judgments(self):
        reader = prose("references/roles.md").split("## Reader", 1)[1].split(
            "## Editor", 1
        )[0]
        for rule in (
            "sentence by sentence, without skipping",
            "complete separate forward read of the published edition",
            "Source knowledge must not conceal",
            "accepted, concern, or unresolved judgment",
            "short specific reason",
            "read the entire containing paragraph and re-judge",
            "Preserve the initial obstacle",
            "headings, table cells and field descriptions",
            "examples, and figures",
            "last completed unit and the next unread unit",
            "still cannot explain",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, reader)

    def test_editor_companions_and_first_pass_obligations(self):
        editor = prose("references/roles.md").split("## Editor", 1)[1]
        skill = prose("SKILL.md")
        for rule in (
            "Read `SKILL.md`, `rules.md` and `examples.md`",
            "repository's `skills/opcua-spec-style/`",
            "shared temporary safeguards",
            "Only you may make source fixes",
            "Preserve normative force",
            "first full pass, keep rewriting when the reader is not satisfied",
            "provide a faithful alternative",
            "Rebuild selected HTML with the pinned Publisher",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, editor)
        self.assertIn("Only the editor may change specification sources", skill)
        self.assertIn("without filtering out requests", skill)
        self.assertIn("recommendations, not unapplied changes", skill)

    def test_style_authority_is_required_for_both_isolated_roles(self):
        skill = prose("SKILL.md")
        roles = prose("references/roles.md")
        for rule in (
            "Resolve `opc-spec-review` through the host's skill mechanism",
            "do not assume installed sibling directories",
            "`<repository root>/skills/opcua-spec-style/`",
            "Record the target repository revision and paths read",
            "file hashes or dirty state",
            "Both agents independently read all three target-repository files and the shared safeguards",
            "stop before style review, proposal or writing",
            "report each missing or unreadable path",
            "Do not fall back to a host-resolved or remote style skill",
            "upstream rules outrank contradictory examples",
            "does not grant the reader domain knowledge, previous findings or editor history",
            "Generic report-writing helpers may be used for non-specification deliverables only",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, skill)
        reader, editor = roles.split("## Reader", 1)[1].split("## Editor", 1)
        for role in (reader, editor):
            for requirement in ("`skills/opcua-spec-style/`", "`SKILL.md`", "`rules.md`", "`examples.md`",
                                "shared temporary safeguards"):
                with self.subTest(requirement=requirement):
                    self.assertIn(requirement, role)
            self.assertNotIn("microsoft-writing-style", role)
            self.assertNotIn("claudism-killer", role)

    def test_fresh_pass_challenges_and_closure(self):
        text = prose("SKILL.md").split("## 5. Repeat with a fresh reader", 1)[1]
        for rule in (
            "new reader agent",
            "withhold that history from the new reader",
            "Reset learned domain knowledge between full passes",
            "second full pass onward, the editor may challenge",
            "exact sentence, the reader's interpretation",
            "An editor rejection alone does not close",
            "Bring a persistent disagreement to the user",
            "user-imposed resource limit",
            "Every change requires another fresh full pass",
            "no new or unresolved issues",
            "no coverage gaps",
            "Otherwise report the precise incomplete state",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, text)

    def test_final_audit_uses_shared_guidance_without_leaking_reader_history(self):
        skill = prose("SKILL.md")
        audit = skill.split("## 6. Final information-preservation audit", 1)[1].split(
            "## 7. Deliver the result", 1
        )[0]
        for requirement in (
            "the editor and coordinator must read and apply",
            "`references/revisions.md` section \"Final information-preservation audit\"",
            "host-resolved `opc-spec-review` package",
            "not an assumed sibling directory",
            "lacks that section", "withhold completion",
            "after the final draft or rewrite and last authorized regeneration",
            "fixed pre-change baseline and complete information inventory",
            "For new drafting use agreed source inputs and requirements",
            "in findings-only mode audit proposed text without editing",
            "Missing baseline evidence or unresolved loss prevents acceptance",
            "not the fresh reader",
            "another fresh full reading pass and another final audit",
            "read-only mode reports loss without writing commands or edits",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, audit)
        shared = (REPO / "skills" / "opc-spec-review" / "references" /
                  "revisions.md").read_text(encoding="utf-8")
        self.assertIn("## Final information-preservation audit", shared)
        editor = prose("references/roles.md").split("## Editor", 1)[1]
        self.assertIn("mandatory final information-preservation audit", editor)
        self.assertIn("Keep baseline and audit history out of fresh-reader prompts", editor)
        self.assertIn("| Preservation | Baseline and final revisions or hashes", skill)
        scenarios = prose("tests/acceptance.md")
        for scenario in (
            "Final audit after agreement", "Final audit isolation and correction",
            "Missing final audit evidence", "Findings-only final audit",
        ):
            self.assertIn(f"| {scenario} |", scenarios)

    def test_relative_document_links_resolve_and_scenarios_cover_failures(self):
        for path in ROOT.rglob("*.md"):
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text("utf-8")):
                if "://" in target or target.startswith("#"):
                    continue
                relative = unquote(target.split("#", 1)[0])
                with self.subTest(path=path, target=target):
                    self.assertTrue((path.parent / relative).exists())
        scenarios = prose("tests/acceptance.md")
        for scenario in (
            "Non-OPC prerequisite",
            "Prior OPC UA part",
            "Coverage gap",
            "First pass dissatisfaction",
            "Unsafe requested rewrite",
            "Later challenge",
            "Fresh pass isolation",
            "Missing tools or agents",
            "Successful closure",
            "Shared authority and fresh reader",
            "Missing authority or safeguards",
            "Conflicting example",
            "Generated region",
            "Semantic preservation",
            "Cross-part and tables",
            "Proposals and retirement",
        ):
            with self.subTest(scenario=scenario):
                self.assertIn(scenario, scenarios)


if __name__ == "__main__":
    unittest.main()
