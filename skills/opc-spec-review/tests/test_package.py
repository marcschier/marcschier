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

    def test_opcua_model_review_precedes_prose_and_preserves_contracts(self):
        skill = " ".join((ROOT / "SKILL.md").read_text(encoding="utf-8").split())
        model_review = skill.split("## Review OPC UA models before prose", 1)[1].split(
            "## Review the composed edition", 1
        )[0]
        for requirement in (
            "separate tasks",
            "Validate the model against OPC 10000-3 and OPC 11030 before drafting",
            "Use `opcua-model-review` for model and NodeSet conformance",
            "Preserve each declaration's `ModellingRule`, including `Optional`",
            "A `QualifiedName` contains a `NamespaceIndex` and a String `Name`",
            "server's `NamespaceArray`",
            "xRegistry String identifier",
            "Write normative mappings as testable requirements",
            "Conformance Test Tool (CTT) cases that cover the behavior",
            "authoritative specification text or direct evidence",
            "Keep private review comments and reviewer identity out",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, model_review)

    def test_opc_references_and_affirmative_requirements(self):
        skill = " ".join((ROOT / "SKILL.md").read_text(encoding="utf-8").split())
        section = skill.split("## Write references and requirements in OPC style", 1)[1].split(
            "## Review the composed edition", 1
        )[0]
        for requirement in (
            "Write Markdown heading text as plain text",
            "without formatting characters such as backticks, asterisks, or underscores",
            "Do not apply inline code, bold, or italics in headings",
            "Keep the Markdown heading markers and supported clause anchors",
            "Apply semantic emphasis in body prose, not headings",
            "give the unchanged identifier in the body",
            "without a section symbol",
            '"OPC 10000-20, 4.2"',
            "`(see [](#sec-anchor))`",
            "a hard-coded number goes stale",
            "Conformance Unit and Profile descriptions",
            "State requirements and permissions affirmatively",
            "Keep a negative form only when the prohibition is itself the requirement",
            "noun phrases in normal spelling",
            "leave the ModellingRule column empty on a `HasInterface` row",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, section)

    def test_marc_writer_replaces_shortened_labels_without_banning_compounds(self):
        writer = REPO / "skills" / "marc-writer"
        style = " ".join((writer / "STYLE.md").read_text(encoding="utf-8").split())
        section = style.split("## 6. Use Technical Density Deliberately", 1)[1].split(
            "## 7. Prefer Mechanisms over Adjectives", 1
        )[0]
        for requirement in (
            'Do not coin or retain shortened technical labels such as "document-write target" or "model-source"',
            "Prefer a full sentence that explains the entity, operation, and relationship",
            "Use the established technical term",
            'write it without hyphens and put it in quotation marks, such as "model source"',
            "The client writes the document to this file.",
            "This file supplies the model.",
            "Do not merely remove the hyphens from an unexplained label",
            'Keep conventional compounds such as "read-only" and "server-specific"',
            'the "non-" prefix is also allowed',
            "Preserve exact identifiers, official names, code, commands, paths, URLs, and quotations from sources",
            "Preserve technical meaning and normative force",
            "When the intended meaning is unclear, flag it rather than inventing a replacement",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, section)
        skill = (writer / "SKILL.md").read_text(encoding="utf-8")
        precedence = skill.split("## Precedence with microsoft-writing-style", 1)[
            1
        ].split("## Factual and editing boundaries", 1)[0]
        self.assertIn('| Shortened technical labels | Replace labels such as "model-source"', precedence)
        self.assertIn('keep conventional compounds and allow "non-"', precedence)

    def test_opc_shortened_labels_use_evidenced_terms_and_optional_explanations(self):
        skill = " ".join((ROOT / "SKILL.md").read_text(encoding="utf-8").split())
        section = skill.split("## Write references and requirements in OPC style", 1)[
            1
        ].split("## Apply the Companion Specification template", 1)[0]
        for requirement in (
            'Replace shortened technical labels such as "document-write target" and "model-source"',
            "Prefer a full sentence explaining the relationship",
            "use the exact applicable OPC UA term or information model name",
            "When an explanation is needed, put words without hyphens in parentheses after the term or name",
            "*DocumentFile* (the file that receives the document)",
            "Do not require an explanation on every occurrence",
            "without evidence from the specification or model",
            "Retain the specification's semantic emphasis conventions and do not rename model elements",
            'write it without hyphens in quotation marks, such as "model source"',
            "explain its meaning before relying on it",
            "Do not merely remove the hyphens from an unexplained label",
            'Keep conventional compounds such as "read-only" and "server-specific"',
            'the "non-" prefix is also allowed',
            "Preserve exact identifiers, official names, code, commands, paths, URLs, and quotations from sources",
            "Preserve technical meaning and normative force",
            "flag unclear meaning rather than inventing a replacement",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, section)

    def test_companion_template_structure_and_authoring_guidance(self):
        skill = " ".join(
            (ROOT / "SKILL.md").read_text(encoding="utf-8").split()
        )
        template = (ROOT / "references" / "template.md").read_text(encoding="utf-8")
        section = " ".join(template.split())
        headings = (
            "## Publication information",
            "## Scope",
            "## Normative references",
            "## Terms, definitions, and abbreviations",
            "## General information",
            "## Use cases",
            "## Information Model overview",
            "## Model definitions",
            "## Authoring checks (not publication clauses)",
            "### Tables in Markdown and rendered HTML",
            "## Profiles and Conformance Units",
            "## Namespaces",
            "## Normative Annex A",
            "## Bibliography",
            "## Reading order",
        )
        positions = [section.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))
        model_headings = (
            "### OPC UA ObjectTypes",
            "### OPC UA EventTypes",
            "### OPC UA VariableTypes",
            "### OPC UA DataTypes",
            "### OPC UA ReferenceTypes",
            "### Instances",
            "### Well-Known BrowseNames",
        )
        model_positions = [section.index(heading) for heading in model_headings]
        self.assertEqual(model_positions, sorted(model_positions))
        for requirement in (
            "not a replacement for the publisher repository's source contract",
            "source contract",
            "which content authors supply, which content is generated",
            "document number, full title and part, version, date",
            "Do not rewrite approved legal text",
            "dated reference selects that edition",
            "undated reference selects the latest edition",
            "Italicize OPC UA terms and terms defined in the specification",
            "Write Markdown heading text as plain text",
            "without formatting characters such as backticks, asterisks, or underscores",
            "Do not apply inline code, bold, or italics in headings",
            "Keep the Markdown heading markers and supported clause anchors",
            "Apply semantic emphasis in body prose, not headings",
            "give the unchanged identifier in the body",
            "do not use italics for emphasis",
            "does not define a general bold convention for prose concepts",
            "Use bold for the revision classifications",
            "Do not add a generic conventions section",
            "The published specification's model chapters use these names",
            "`<some>Type definition`",
            "`Overview` and `ObjectType definition`",
            "`<some>Method`",
            "`ExampleStateMachineType`",
            "`<some>EventType`",
            "`<some>VariableType`",
            "`<someStructure>`",
            "`<someUnion>`",
            "`<someEnumeration>`",
            "`<someOptionSet>`",
            "`<someReferenceType>`",
            "`<someInstance>`",
            "`Well-Known <Type> BrowseNames`",
            "include only model groups that apply",
            "a table has a header row, a separator row, and data rows",
            "each item beginning `- ` or `1. `",
            "Put one Markdown caption and anchor before each logical table group",
            "The main type-definition group contains an Attribute/Value block",
            "Keep the six-column References grid intact",
            "Additional References",
            "`SourceBrowsePath`, `Reference Type`, `Is Forward`, `TargetBrowsePath`",
            "`Optional` column only when fields can be optional",
            "`datatype=<DataType>`",
            "Inspect the publisher's rendered HTML for each changed table group",
            "A correct Markdown source or a GitHub preview alone does not establish",
            "long text and width constraints may require wrapping",
            "do not add manual widths or styles",
            "State inheritance as a \"Subtype of\" relationship",
            "do not add a `HasSubtype` reference",
            "keep the NodeSet classification consistent",
            "Distinguish a BrowseName's `NamespaceIndex`, namespace URI, and String `Name`",
            "For structures, distinguish optional fields from fields that allow subtypes",
            "use `EnumStrings` for zero-based sequential values and `EnumValues` otherwise",
            "Define OptionSet values by bit position",
            "Include at least one Profile or Facet",
            "informative snapshot or the normative definition",
            "namespace metadata and the NodeSet agree",
            "publication date, subset status, and static NodeId policy",
            "a local clause anchor for an in-document reference",
            "follow it from beginning to end without searching ahead to learn a term or concept",
            "Forward references are appropriate for more detail",
            "Presentation belongs to the template and publisher owners",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, section)
        self.assertIn("(references/template.md)", skill)
        self.assertIn("Do not prescribe or edit publisher-owned presentation", skill)
        self.assertIn(
            "inspect their rendered HTML for lost headers, cells, values, grouping, or links",
            skill,
        )
        examples = re.findall(r"```markdown\n(.*?)\n```", template, re.DOTALL)
        table_examples = [example for example in examples if "| **Attribute** |" in example]
        self.assertEqual(len(table_examples), 1)
        table_example = table_examples[0]
        blocks = [
            block for block in table_example.split("\n\n") if block.startswith("|")
        ]
        self.assertEqual(len(blocks), 3)
        for block in blocks:
            self.assertEqual(block.splitlines()[1], "| --- | --- | --- | --- | --- | --- |")
        for line in table_example.splitlines():
            if line.startswith("|"):
                with self.subTest(table_row=line):
                    self.assertEqual(line.count("|") - 1, 6)
        for excluded in ("figure", "TOC", "term index", "table borders", "font size"):
            with self.subTest(excluded=excluded):
                self.assertNotRegex(
                    section.lower(), rf"\b{re.escape(excluded.lower())}\b"
                )
        self.assertNotRegex(section, r"\]\([^)]*\.docx")
        self.assertNotIn("Word template", template)

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

    def test_word_capture_bounds_distinguish_dpi_cropping_from_document_clipping(self):
        review = " ".join(
            (ROOT / "references" / "review.md").read_text(encoding="utf-8").split()
        )
        for requirement in (
            "Before treating screenshot-edge cropping as document clipping",
            "compare the capture bounds and pixel dimensions",
            "actual visible page",
            "Word used 168 DPI",
            "virtualized 1267x1133 window rectangle",
            "physical 2217x1983 rectangle",
            "capture-boundary error, not document clipping",
            "one verified Windows option",
            "not required on other hosts",
            "does not authorize bypassing Computer Use controls",
            "bounds and pixels use the same coordinate space",
            "Recapture the intended page without editing it",
            "record the capture method, DPI and bounds",
            "leave the cropped region unreviewed",
            "persists in a correctly bounded view of the current artifact",
            "Correct bounds for one page do not establish full pagination coverage",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, review)
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        row = next(
            line for line in acceptance.splitlines()
            if line.startswith("| Word DPI capture bounds |")
        )
        for requirement in (
            "another host cannot resolve its capture mismatch",
            "same coordinate space",
            "not a cross-host requirement or Computer Use bypass",
            "leave unresolved regions unreviewed",
            "do not infer full pagination coverage",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, row)

    def test_word_page_metafiles_do_not_establish_live_or_print_coverage(self):
        review = " ".join(
            (ROOT / "references" / "review.md").read_text(encoding="utf-8").split()
        )
        for requirement in (
            "Page-navigation ranges and page metafiles are separate evidence",
            "`GoTo(2)` returned the same zero-length range and physical page",
            "`Pages.Item(2)` exposed zero rectangles",
            "live view did not independently show page 2",
            "without concluding that the inaccessible page is blank",
            "visual coverage remains unreviewed",
            "https://learn.microsoft.com/en-us/office/vba/api/word.page.enhmetafilebits",
            "as a picture representation",
            "GDI+ conversion of `Pages.Item(1).EnhMetaFileBits`",
            "fully visible in the live Word screenshot",
            "Record the conversion method",
            "they are not interchangeable",
            "converted image is not proof of print output",
            "Neither zero rectangles nor a white conversion establishes a blank page",
            "keep any conversion discrepancy unresolved",
            "does not extend coverage to uninspected pages",
            "bring PDF layout/rendering into scope",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, review)
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        row = next(
            line for line in acceptance.splitlines()
            if line.startswith("| Word page metafile limits |")
        )
        for requirement in (
            "without independent live page-2 evidence",
            "Keep page 2 visually unreviewed rather than declaring it blank",
            "proof of print output",
            "leave the discrepancy unresolved",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, row)

    def test_word_process_ownership_does_not_establish_document_ownership(self):
        review = " ".join(
            (ROOT / "references" / "review.md").read_text(encoding="utf-8").split()
        )
        for requirement in (
            "A task-started Word process does not establish that every document",
            "`WINWORD.EXE /n`",
            "at least three visible `OpusApp` windows with `_WwG`",
            "Their document identities were not inspected",
            "their contents and the cause remain unknown",
            "Only the task-started PID was closed/stopped",
            "Before updating fields or quitting an instance",
            "verify each affected document's identity and task ownership",
            "Do not save or close an unidentified document",
            "stop only that specific PID when termination is authorized",
            "not as a separate-process guarantee",
            "Starting Office with multiple switches is unsupported",
            "verify the actual document inventory",
            "do not authorize shell launch or focus workarounds",
            "Close only verified task-owned documents without saving",
            "instance contains no other documents",
            "report any ownership or cleanup uncertainty",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, review)
        self.assertIn(
            "https://support.microsoft.com/en-us/office/lifecycle/"
            "command-line-switches-for-microsoft-office-products",
            review,
        )
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        for scenario, requirements in (
            ("Word process and document ownership", (
                "document identities were not inspected",
                "unknown contents and cause",
                "leave unidentified documents unchanged",
                "recorded task-started PID",
                "unsupported combined switches",
            )),
            ("Verified Word cleanup", (
                "Recheck the document inventory",
                "confirm its PID exited",
                "leave the other Word process and document unchanged",
            )),
        ):
            row = next(
                line for line in acceptance.splitlines()
                if line.startswith(f"| {scenario} |")
            )
            for requirement in requirements:
                with self.subTest(scenario=scenario, requirement=requirement):
                    self.assertIn(requirement, row)

    def test_word_process_identity_uses_verified_window_handle(self):
        review = " ".join(
            (ROOT / "references" / "review.md").read_text(encoding="utf-8").split()
        )
        for requirement in (
            "verified Word window's [`Window.Hwnd`]",
            "https://learn.microsoft.com/en-us/office/vba/api/word.window.hwnd",
            "resolve that handle to its process ID",
            "compare it with the recorded task-started PID",
            "on `Window`, not `Application.Hwnd`",
            "Do not assume an empty application has a usable document window",
            "If no verified window or handle is available",
            "report process identity as unverified",
            "rather than substituting another Word window",
            "A handle-to-PID match does not establish ownership of every document",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, review)
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        row = next(
            line for line in acceptance.splitlines()
            if line.startswith("| Word window handle |")
        )
        for requirement in (
            "another has no verified document window",
            "verified window's `Window.Hwnd`",
            "report process identity as unverified",
            "do not substitute another Word window",
            "matching PID does not establish ownership of every document",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, row)

    def test_word_open_waits_for_verified_document_window(self):
        review = " ".join(
            (ROOT / "references" / "review.md").read_text(encoding="utf-8").split()
        )
        for requirement in (
            "wait for the actual document window",
            "A split Open control can expand its menu",
            "Return in the filename field can dismiss that menu",
            "not a prescribed keystroke sequence",
            "Before retrying an apparently unchanged dialog",
            "enumerate Word windows again with `list_apps`",
            "read the candidate with `get_window_state`",
            "may have opened in a separate window",
            "Re-verify its full path, artifact hash, part number and title",
            "fresh state confirms the intended document is not open",
            "the dialog still targets that artifact",
            "If the Computer Use transport closes",
            "last confirmed window state and exact transport failure",
            "leave unperformed field and pagination checks unreviewed",
            "resume with window discovery and identity verification",
            "an open document alone does not establish inspection or a publication defect",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, review)
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        row = next(
            line for line in acceptance.splitlines()
            if line.startswith("| Delayed Word Open dialog |")
        )
        for requirement in (
            "separate Word window",
            "transport then closes before inspection",
            "Wait and enumerate windows before retrying",
            "leave field and pagination checks unreviewed",
        ):
            with self.subTest(acceptance=requirement):
                self.assertIn(requirement, row)

    def test_blank_figure_capture_is_inconclusive_until_reproduced(self):
        review = " ".join(
            (ROOT / "references" / "review.md").read_text(encoding="utf-8").split()
        )
        for requirement in (
            "If a figure appears blank in a capture, treat that capture as inconclusive",
            "Refresh the view without editing the document",
            "use a non-editing click in the page",
            "move to another page and return",
            "Confirm the capture still shows the intended page and region",
            "check whether the DOCX contains the referenced media",
            "both SVG and raster representations may be present",
            "One empty capture does not prove that the publication omits artwork",
            "only when the blank result is reproducible in a refreshed view",
            "Otherwise record the capture as transient or unresolved",
            "If a figure becomes visible after a non-editing click",
            "the initial blank capture is not a missing-figure finding",
            "The cause remains unknown",
            "does not establish full pagination coverage",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, review)
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        self.assertIn("| Blank figure capture |", acceptance)
        self.assertIn("| Part 31 update and transient figure |", acceptance)
        self.assertIn("3,899 of 3,899 words selected", acceptance)
        self.assertIn("separate contents, figures and tables dialogs", acceptance)
        self.assertIn("the click does not establish full pagination coverage", acceptance)

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

    def test_format_inspection_and_fixes_require_opt_in_with_exclusion_default(self):
        for relative in ("SKILL.md", "README.md", "references/review.md"):
            text = (ROOT / relative).read_text(encoding="utf-8")
            normalized = " ".join(text.split())
            with self.subTest(file=relative):
                self.assertIn("Dark-mode behavior".lower(), normalized.lower())
                self.assertIn("layout/rendering", normalized)
                self.assertIn("outside", normalized)
                self.assertIn("Exclude (default)", normalized)
                self.assertIn("Inspect only", normalized)
                self.assertIn("Inspect and fix", normalized)
                self.assertIn("PDF and Word inspection and fixes", normalized)
                self.assertNotIn(
                    "Dark-mode behavior and PDF layout/rendering", normalized
                )
        skill = " ".join((ROOT / "SKILL.md").read_text(encoding="utf-8").split())
        for requirement in (
            "use `ask_user`",
            "one format at a time",
            "Record the answer separately for PDF and Word",
            "Default to excluding both inspection and fixes when no answer is available",
            "general approval to fix findings does not opt either format in",
            "Resolve any conflict with an explicit read-only request before editing",
            "outside the agreed scope, not as blocked or implicitly reviewed",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, skill)
        review = " ".join(
            (ROOT / "references" / "review.md").read_text(encoding="utf-8").split()
        )
        for requirement in (
            "unless the user has already made that choice explicit",
            "This gate includes PDF text extraction and DOCX XML/field-result inspection",
            "Enter this branch only when the user has included Word inspection",
            "Enter this branch only when the user has included PDF inspection",
            "only when PDF inspection is also included, export a PDF",
            "Inspect only does not authorize field updates",
            "Agree the page range",
            "text extraction alone cannot establish layout/rendering coverage",
            "Shared source or generator changes may regenerate excluded formats",
            "apply the approved correction there, regenerate and reinspect",
            "Do not patch generated files alone",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, review)
        revisions = " ".join(
            (ROOT / "references" / "revisions.md").read_text(encoding="utf-8").split()
        )
        self.assertIn("General fix approval does not opt them in", revisions)
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        for scenario, requirement in (
            ("Format opt-in default", "exclude both inspection and fixes without an answer"),
            ("Independent format choices", "do not inspect or fix Word"),
            ("Inspection without fixes", "without changing sources, field results or generated output"),
            ("Word fixes without PDF", "rather than exporting a PDF for inspection"),
            ("Out-of-scope layout", "continuing dark-mode exclusion"),
        ):
            row = next(
                line for line in acceptance.splitlines()
                if line.startswith(f"| {scenario} |")
            )
            with self.subTest(scenario=scenario):
                self.assertIn(requirement, row)

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

    def test_main_story_update_requires_fresh_selection_with_menus_dismissed(self):
        review = " ".join(
            (ROOT / "references" / "review.md").read_text(encoding="utf-8").split()
        )
        for requirement in (
            "Dismiss context menus and other open menus before selecting the main story",
            "close that menu first, then reselect all",
            "Immediately before invoking `FieldsUpdate`",
            "fresh accessibility state that verifies menus are dismissed",
            "selected and total word counts in the status bar",
            "an earlier count is not sufficient",
            "If selection is absent or uncertain, reselect and verify it",
            "42,699 of 42,699 words",
            "selection was no longer present",
            "Repeat Update Fields and all three lists remained placeholders",
            "verifying the same count in the status bar",
            "eventually populated the contents, figures and tables lists",
            "without assuming the first activation updated the intended selection",
            "Neither Repeat Update Fields nor Undo Update Fields proves list correctness",
            "inspect the actual results independently",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, review)
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        row = next(
            line for line in acceptance.splitlines()
            if line.startswith("| Open menu before field update |")
        )
        for requirement in (
            "42,699 of 42,699",
            "selection disappears",
            "Repeat Update Fields",
            "Undo Update Fields",
            "fresh accessibility state",
            "immediately before invoking",
            "list correctness or pagination coverage",
        ):
            with self.subTest(acceptance=requirement):
                self.assertIn(requirement, row)

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

    def test_customization_target_mismatch_requires_cancellation(self):
        review = " ".join(
            (ROOT / "references" / "review.md").read_text(encoding="utf-8").split()
        )
        for requirement in (
            "Before adding or applying a customization",
            "customization target names the intended task-owned copy",
            "Quick Access Toolbar > More Commands from a background Word window",
            "If the target differs or cannot be verified, cancel without applying changes",
            "report the intended copy and offered target as a UI limitation",
            "Re-establish document identity before retrying",
            "do not customize the other document",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, review)
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        self.assertIn("| Customization target mismatch |", acceptance)

    def test_docx_relationship_id_equivalence_is_pre_update_only(self):
        review = " ".join(
            (ROOT / "references" / "review.md").read_text(encoding="utf-8").split()
        )
        for requirement in (
            "Record both package SHA-256 hashes",
            "compare ZIP member sets and each member's uncompressed bytes",
            "compare element structure, text and non-relationship attributes",
            "Resolve every changed relationship ID through its owning part's relationship file",
            "same relationship type, target and target mode at that location",
            "do not simply strip IDs",
            "Compare relationship-attribute multisets within each relationship file",
            "with only `Id` excluded",
            "preserving duplicate counts and all other attributes",
            "A matching multiset alone cannot detect targets swapped",
            "Require all other members to be byte-identical",
            "missing relationships or changed targets prevent an ID-only equivalence",
            "only the compared pre-update package content",
            "not field-update results or visual pagination",
            "The copy filename, environment and later Word actions",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, review)
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        for scenario in (
            "Regenerated DOCX relationship IDs",
            "Non-equivalent DOCX relationships",
        ):
            with self.subTest(scenario=scenario):
                self.assertIn(f"| {scenario} |", acceptance)

    def test_bulk_ledger_refinement_preserves_rule_specific_reasons(self):
        review = " ".join(
            (ROOT / "references" / "review.md").read_text(encoding="utf-8").split()
        )
        for requirement in (
            "preflight the selected rows and their existing rule-specific reasons",
            "Select by stable row identity and applicable rule",
            "not by a generic subject alone",
            "Preserve each existing reason",
            "explicitly accounts for its replacement",
            "Check the proposed before/after rows before writing",
            "verify afterward that unrelated reasons remain unchanged",
            "leave ambiguous matches untouched",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, review)
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        row = next(
            line for line in acceptance.splitlines()
            if line.startswith("| Bulk ledger reasons |")
        )
        self.assertIn("refine only R-A", row)
        self.assertIn("preserve R-B's reason unchanged", row)
        self.assertIn("before writing", row)

    def test_non_list_comparison_attributes_changed_field_results(self):
        review = " ".join(
            (ROOT / "references" / "review.md").read_text(encoding="utf-8").split()
        )
        for requirement in (
            "Compare non-list text before and after field updates",
            "A `FILENAME` result can change from the template name",
            "Identify each changed field by its instruction and location",
            "record its before/after result",
            "attribute a legitimate change to the copy's identity or evaluation environment",
            "exclude all field results from comparison",
            "unchanged when a field result changed",
            "Keep unexplained differences open",
            "Compare non-list field results by instruction and document location",
            "simple fields (`w:fldSimple` with `w:instr`)",
            "complex fields (`w:fldChar` begin/separate/end with `w:instrText`)",
            "Reconstruct split instructions and result runs",
            "respecting nested fields",
            "Match corresponding fields across representations",
            "an XML form change alone is not a text change",
            "an ambiguous match remains unresolved",
            "custom display label with the table number",
            "Do not assume a field update preserved link labels",
            "instruction, target bookmark and location",
            "investigate unexpected changes against the source link and composed table",
            "Distinguish the update-induced change from the Publisher's original stored result",
            "does not justify accepting unrelated `REF` changes",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, review)
        acceptance = (ROOT / "tests" / "acceptance.md").read_text(encoding="utf-8")
        self.assertIn("| Changed non-list field result |", acceptance)
        for scenario in ("Updated REF custom label", "Simple and complex field comparison"):
            with self.subTest(scenario=scenario):
                row = next(
                    line for line in acceptance.splitlines()
                    if line.startswith(f"| {scenario} |")
                )
                self.assertIn("instruction and location", row)
                self.assertIn("`AllowedModes` becoming `7`", row)

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
