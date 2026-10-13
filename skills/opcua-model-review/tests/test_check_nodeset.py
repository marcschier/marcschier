from pathlib import Path
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_nodeset as checker


U = checker.XML_URI
V = "http://opcfoundation.org/UA/2008/02/Types.xsd"


class NodeSet:
    def __init__(self, namespaces=("urn:example:model",)):
        self.root = ET.Element(f"{{{U}}}UANodeSet")
        uris = ET.SubElement(self.root, f"{{{U}}}NamespaceUris")
        for uri in namespaces:
            ET.SubElement(uris, f"{{{U}}}Uri").text = uri
        self.nodes = {}

    def node(self, kind, identifier, name, references=(), **attributes):
        element = ET.SubElement(self.root, f"{{{U}}}UA{kind}", NodeId=identifier, BrowseName=name, **attributes)
        self.nodes[identifier] = element
        refs = ET.SubElement(element, f"{{{U}}}References")
        for reference, target, forward in references:
            ET.SubElement(refs, f"{{{U}}}Reference", ReferenceType=reference, IsForward=str(forward).lower()).text = target
        return element

    def object(self, identifier, name, type_id="i=58", references=()):
        return self.node("Object", identifier, name, [("i=40", type_id, True), *references])

    def variable(self, identifier, name, parent, datatype="i=6", rule=None, reference="i=47", type_id="i=63", **attributes):
        refs = [("i=40", type_id, True), (reference, parent, False)]
        if rule is not None:
            refs.append(("i=37", rule, True))
        return self.node("Variable", identifier, name, refs, DataType=datatype, **attributes)

    def property(self, identifier, name, parent, datatype="i=6", rule=None, **attributes):
        return self.variable(identifier, name, parent, datatype, rule, reference="i=46", type_id="i=68", **attributes)

    def type(self, identifier, name, parent="i=58", abstract=False, references=()):
        return self.node("ObjectType", identifier, name, [("i=45", parent, False), *references],
                         IsAbstract=str(abstract).lower())

    def scalar(self, node, kind, text):
        value = ET.SubElement(node, f"{{{U}}}Value")
        ET.SubElement(value, f"{{{V}}}{kind}").text = text

    def arguments(self, parent, identifier, name, arguments):
        prop = self.property(identifier, name, parent, datatype="i=296", ValueRank="1")
        values = ET.SubElement(ET.SubElement(prop, f"{{{U}}}Value"), f"{{{V}}}ListOfExtensionObject")
        for argument_name, datatype in arguments:
            argument = ET.SubElement(ET.SubElement(ET.SubElement(values, f"{{{V}}}ExtensionObject"),
                                                  f"{{{V}}}Body"), f"{{{V}}}Argument")
            ET.SubElement(argument, f"{{{V}}}Name").text = argument_name
            ET.SubElement(ET.SubElement(argument, f"{{{V}}}DataType"), f"{{{V}}}Identifier").text = datatype
            ET.SubElement(argument, f"{{{V}}}ValueRank").text = "-1"
        return prop

    def write(self, path):
        ET.ElementTree(self.root).write(path, encoding="utf-8", xml_declaration=True)


class ReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = checker.load_catalog()

    def review(self, document, dependencies=()):
        with tempfile.TemporaryDirectory() as directory:
            model = checker.Model()
            model.load_standard()
            for index, dependency in enumerate(dependencies):
                path = Path(directory) / f"dependency-{index}.xml"
                dependency.write(path)
                model.load(path, primary=False)
            path = Path(directory) / "subject.xml"
            document.write(path)
            model.load(path, primary=True)
            model.index()
            return checker.Review(model, self.catalog).run(), model

    def rules(self, report):
        return {finding["rule"] for finding in report["findings"]}

    def device(self, supply_speed=True):
        document = NodeSet()
        document.type("ns=1;i=100", "1:DeviceType")
        document.variable("ns=1;i=101", "1:Speed", "ns=1;i=100", datatype="i=11", rule="i=78")
        document.object("ns=1;i=200", "1:Device", "ns=1;i=100")
        if supply_speed:
            document.variable("ns=1;i=201", "1:Speed", "ns=1;i=200", datatype="i=11")
        return document

    def test_valid_device_has_no_candidate_findings_and_is_not_certified(self):
        report, _ = self.review(self.device())
        self.assertEqual([], report["findings"])
        self.assertFalse(report["complete"])
        self.assertEqual(3, report["exit_code"])
        self.assertEqual(len(self.catalog), len(report["coverage"]))
        self.assertEqual({"not_assessed"}, {row["status"] for row in report["coverage"]})

    def test_namespace_indexes_are_resolved_per_file(self):
        dependency = NodeSet(("urn:example:dependency", "urn:example:model"))
        dependency.type("ns=1;i=100", "1:BaseType")
        document = NodeSet(("urn:example:model", "urn:example:dependency"))
        document.type("ns=1;i=101", "1:DerivedType", parent="ns=2;i=100")
        report, model = self.review(document, [dependency])
        key = checker.NodeId("urn:example:model", "i", "101")
        self.assertEqual([checker.NodeId("urn:example:dependency", "i", "100")], model.parents(key))
        self.assertEqual([], report["findings"])

    def test_namespace_uri_case_is_not_normalized(self):
        document = NodeSet(("urn:example:model", "URN:example:model"))
        document.object("ns=1;i=100", "1:Parent")
        document.property("ns=1;i=101", "1:Limit", "ns=1;i=100")
        document.property("ns=2;i=101", "2:Limit", "ns=1;i=100")
        report, _ = self.review(document)
        self.assertNotIn("P3-009", self.rules(report))
        self.assertNotIn("P3-023", self.rules(report))

    def test_string_nodeid_whitespace_is_identity(self):
        document = NodeSet()
        document.type("ns=1;s=foo", "1:FirstType")
        document.type("ns=1;s=foo ", "1:SecondType")
        report, model = self.review(document)
        self.assertNotIn("P3-009", self.rules(report))
        self.assertIn(checker.NodeId("urn:example:model", "s", "foo "), model.nodes)

    def test_propertytype_cannot_be_subtyped_through_inverse_reference(self):
        document = NodeSet()
        document.node("VariableType", "ns=1;i=100", "1:ForbiddenPropertyType", [("i=45", "i=68", False)])
        report, _ = self.review(document)
        self.assertIn("P5-001", self.rules(report))
        self.assertNotIn("P3-079", self.rules(report))

    def test_property_is_a_leaf_even_with_an_unresolved_target(self):
        document = NodeSet()
        document.object("ns=1;i=100", "1:Parent")
        prop = document.property("ns=1;i=101", "1:Limit", "ns=1;i=100")
        ET.SubElement(prop.find(f"{{{U}}}References"), f"{{{U}}}Reference", ReferenceType="i=47").text = "ns=1;i=999"
        report, _ = self.review(document)
        self.assertIn("P3-022", self.rules(report))
        self.assertTrue(any("i=999" in key for key in report["unresolved_nodes"]))

    def test_distinct_properties_with_one_qualified_name_are_rejected(self):
        document = NodeSet()
        document.object("ns=1;i=100", "1:Parent")
        document.property("ns=1;i=101", "1:Limit", "ns=1;i=100")
        document.property("ns=1;i=102", "1:Limit", "ns=1;i=100")
        report, _ = self.review(document)
        self.assertIn("P3-023", self.rules(report))

    def test_ordinary_instance_child_names_need_not_be_unique(self):
        document = NodeSet()
        document.object("ns=1;i=100", "1:Parent")
        document.object("ns=1;i=101", "1:Child", references=[("i=47", "ns=1;i=100", False)])
        document.object("ns=1;i=102", "1:Child", references=[("i=47", "ns=1;i=100", False)])
        report, _ = self.review(document)
        self.assertNotIn("P3-078", self.rules(report))
        self.assertEqual([], report["findings"])

    def test_declaration_context_child_names_are_unique(self):
        document = NodeSet()
        document.type("ns=1;i=100", "1:ParentType")
        document.variable("ns=1;i=101", "1:Limit", "ns=1;i=100", rule="i=78")
        document.variable("ns=1;i=102", "1:Limit", "ns=1;i=100", rule="i=80")
        report, _ = self.review(document)
        self.assertIn("P3-078", self.rules(report))

    def optional_branch(self, include_branch):
        document = NodeSet()
        document.type("ns=1;i=100", "1:ParentType")
        document.object("ns=1;i=101", "1:Branch", references=[
            ("i=47", "ns=1;i=100", False), ("i=37", "i=80", True),
        ])
        document.variable("ns=1;i=102", "1:Leaf", "ns=1;i=101", rule="i=78")
        document.object("ns=1;i=200", "1:Parent", "ns=1;i=100")
        if include_branch:
            document.object("ns=1;i=201", "1:Branch", references=[("i=47", "ns=1;i=200", False)])
        return document

    def test_mandatory_descendant_below_absent_optional_parent_is_not_required(self):
        report, _ = self.review(self.optional_branch(False))
        self.assertNotIn("P3-094", self.rules(report))

    def test_mandatory_descendant_is_required_when_optional_parent_is_present(self):
        report, _ = self.review(self.optional_branch(True))
        self.assertIn("P3-094", self.rules(report))

    def test_inherited_mandatory_declarations_are_not_repeated_on_subtypes(self):
        document = self.device(False)
        document.type("ns=1;i=300", "1:DerivedType", parent="ns=1;i=100")
        references = document.nodes["ns=1;i=200"].find(f"{{{U}}}References")
        references.find(f"{{{U}}}Reference").text = "ns=1;i=300"
        report, _ = self.review(document)
        self.assertIn("P3-094", self.rules(report))
        self.assertNotIn("P3-076", self.rules(report))

    def test_an_abstract_typedefinition_is_allowed_on_a_declaration(self):
        document = NodeSet()
        document.type("ns=1;i=100", "1:ParentType")
        document.type("ns=1;i=101", "1:AbstractFeatureType", abstract=True)
        document.object("ns=1;i=102", "1:Feature", "ns=1;i=101", references=[
            ("i=47", "ns=1;i=100", False), ("i=37", "i=78", True),
        ])
        report, _ = self.review(document)
        self.assertNotIn("P3-018", self.rules(report))

    def test_an_abstract_typedefinition_is_not_allowed_on_a_real_instance(self):
        document = NodeSet()
        document.type("ns=1;i=100", "1:AbstractType", abstract=True)
        document.object("ns=1;i=101", "1:RealInstance", "ns=1;i=100")
        report, _ = self.review(document)
        self.assertIn("P3-018", self.rules(report))

    def test_mandatory_modelling_rule_cannot_be_weakened(self):
        document = self.device()
        document.type("ns=1;i=300", "1:DerivedType", parent="ns=1;i=100")
        document.variable("ns=1;i=301", "1:Speed", "ns=1;i=300", datatype="i=11", rule="i=80")
        report, _ = self.review(document)
        self.assertIn("P3-091", self.rules(report))

    def test_optional_modelling_rule_can_be_promoted(self):
        document = NodeSet()
        document.type("ns=1;i=100", "1:ParentType")
        document.variable("ns=1;i=101", "1:Speed", "ns=1;i=100", rule="i=80")
        document.type("ns=1;i=200", "1:DerivedType", parent="ns=1;i=100")
        document.variable("ns=1;i=201", "1:Speed", "ns=1;i=200", rule="i=78")
        report, _ = self.review(document)
        self.assertNotIn("P3-091", self.rules(report))
        self.assertEqual([], report["findings"])

    def variable_types(self, old_rank, new_rank, old_dimensions="", new_dimensions="", old_datatype="i=6", new_datatype="i=6"):
        document = NodeSet()
        document.node("VariableType", "ns=1;i=100", "1:BaseValueType", [("i=45", "i=63", False)],
                      DataType=old_datatype, ValueRank=str(old_rank), ArrayDimensions=old_dimensions)
        document.node("VariableType", "ns=1;i=101", "1:DerivedValueType", [("i=45", "ns=1;i=100", False)],
                      DataType=new_datatype, ValueRank=str(new_rank), ArrayDimensions=new_dimensions)
        return document

    def test_variabletype_browse_name_changes_are_valid(self):
        report, _ = self.review(self.variable_types(-2, -1))
        self.assertNotIn("P3-079", self.rules(report))
        self.assertNotIn("P3-082", self.rules(report))

    def test_fixed_rank_cannot_be_widened(self):
        report, _ = self.review(self.variable_types(1, 0))
        self.assertIn("P3-082", self.rules(report))

    def test_nonzero_inherited_dimension_cannot_be_changed_even_to_smaller_value(self):
        report, _ = self.review(self.variable_types(1, 1, "10", "5"))
        self.assertIn("P3-083", self.rules(report))

    def test_abstract_datatype_can_be_narrowed(self):
        report, _ = self.review(self.variable_types(-1, -1, old_datatype="i=26", new_datatype="i=6"))
        self.assertNotIn("P3-081", self.rules(report))

    def test_unrelated_datatype_is_not_a_narrowing(self):
        report, _ = self.review(self.variable_types(-1, -1, old_datatype="i=11", new_datatype="i=6"))
        self.assertIn("P3-081", self.rules(report))

    def interface(self, apply=False, placeholder=False, abstract=True):
        document = NodeSet()
        document.type("ns=1;i=100", "1:IFeatureType", parent="i=17602", abstract=abstract)
        document.variable("ns=1;i=101", "1:Reading", "ns=1;i=100", rule="i=11508" if placeholder else "i=78")
        if apply:
            document.type("ns=1;i=200", "1:DeviceType", references=[("i=17603", "ns=1;i=100", True)])
        return document

    def test_interface_definition_must_be_abstract(self):
        report, _ = self.review(self.interface(abstract=False))
        self.assertIn("P3-104", self.rules(report))

    def test_interface_declarations_cannot_use_placeholders(self):
        report, _ = self.review(self.interface(placeholder=True))
        self.assertIn("P3-105", self.rules(report))

    def test_interface_is_not_a_typedefinition_even_for_declarations(self):
        document = self.interface()
        document.type("ns=1;i=200", "1:ContainerType")
        document.object("ns=1;i=201", "1:Feature", "ns=1;i=100", references=[
            ("i=47", "ns=1;i=200", False), ("i=37", "i=78", True),
        ])
        report, _ = self.review(document)
        self.assertIn("P3-106", self.rules(report))

    def test_applying_an_interface_requires_its_mandatory_declarations(self):
        report, _ = self.review(self.interface(apply=True))
        self.assertIn("P3-109", self.rules(report))

    def test_optional_interface_modelling_rule_advice_is_not_a_normative_error(self):
        document = self.interface(apply=True)
        declaration = document.nodes["ns=1;i=101"].find(f"{{{U}}}References")
        next(ref for ref in declaration if ref.get("ReferenceType") == "i=37").text = "i=80"
        document.variable("ns=1;i=201", "1:Reading", "ns=1;i=200", rule="i=11508")
        report, _ = self.review(document)
        advice = [finding for finding in report["findings"] if finding["rule"] == "P3-198"]
        self.assertEqual(1, len(advice))
        self.assertEqual("warning", advice[0]["severity"])
        self.assertNotIn("P3-110", self.rules(report))

    def test_displayname_length_counts_text_not_xml_encoding(self):
        document = NodeSet()
        node = document.object("ns=1;i=100", "1:Device")
        ET.SubElement(node, f"{{{U}}}DisplayName").text = "&" * 513
        report, _ = self.review(document)
        self.assertIn("P3-200", self.rules(report))

    def test_interface_instance_optional_parent_is_not_forced_into_existence(self):
        document = NodeSet()
        document.type("ns=1;i=100", "1:IFeatureType", parent="i=17602", abstract=True)
        document.object("ns=1;i=101", "1:Branch", references=[
            ("i=47", "ns=1;i=100", False), ("i=37", "i=80", True),
        ])
        document.variable("ns=1;i=102", "1:Leaf", "ns=1;i=101", rule="i=78")
        document.type("ns=1;i=200", "1:DeviceType", references=[("i=17603", "ns=1;i=100", True)])
        document.object("ns=1;i=201", "1:Branch", references=[
            ("i=47", "ns=1;i=200", False), ("i=37", "i=80", True),
        ])
        document.variable("ns=1;i=202", "1:Leaf", "ns=1;i=201", rule="i=78")
        document.object("ns=1;i=300", "1:Device", "ns=1;i=200", references=[("i=17603", "ns=1;i=100", True)])
        report, _ = self.review(document)
        self.assertNotIn("P3-109", self.rules(report))

    def test_addin_needs_default_browse_name(self):
        document = NodeSet()
        document.type("ns=1;i=100", "1:FeatureType")
        document.object("ns=1;i=200", "1:Parent")
        document.object("ns=1;i=201", "1:Feature", "ns=1;i=100", references=[("i=17604", "ns=1;i=200", False)])
        report, _ = self.review(document)
        self.assertIn("P3-115", self.rules(report))

    def test_default_browse_name_is_valid_type_only_metadata_without_modelling_rule(self):
        document = NodeSet()
        document.type("ns=1;i=100", "1:FeatureType")
        document.property("ns=1;i=101", "DefaultInstanceBrowseName", "ns=1;i=100", datatype="i=20")
        document.object("ns=1;i=200", "1:Parent")
        document.object("ns=1;i=201", "1:Feature", "ns=1;i=100", references=[("i=17604", "ns=1;i=200", False)])
        report, _ = self.review(document)
        self.assertNotIn("P3-037", self.rules(report))
        self.assertNotIn("P3-115", self.rules(report))
        self.assertNotIn("P3-094", self.rules(report))

    def test_multiple_objecttype_inheritance_is_not_invented_as_a_prohibition(self):
        document = NodeSet()
        document.type("ns=1;i=100", "1:FirstType")
        document.type("ns=1;i=101", "1:SecondType")
        document.type("ns=1;i=102", "1:CompositeType", parent="ns=1;i=100",
                      references=[("i=45", "ns=1;i=101", False)])
        report, _ = self.review(document)
        self.assertNotIn("P3-055", self.rules(report))
        self.assertTrue(any("Multiple inheritance" in gap for gap in report["evidence_gaps"]))

    def test_referencetype_multiple_inheritance_is_prohibited(self):
        document = NodeSet()
        node = document.node("ReferenceType", "ns=1;i=100", "1:HasFeature", [
            ("i=45", "i=47", False), ("i=45", "i=35", False),
        ])
        ET.SubElement(node, f"{{{U}}}InverseName").text = "FeatureOf"
        report, _ = self.review(document)
        self.assertIn("P3-055", self.rules(report))

    def test_concrete_reference_symmetry_is_inherited(self):
        document = NodeSet()
        document.node("ReferenceType", "ns=1;i=100", "1:OrganizesSymmetrically",
                      [("i=45", "i=35", False)], Symmetric="true")
        report, _ = self.review(document)
        self.assertIn("P3-054", self.rules(report))

    def test_organizes_loops_are_not_haschild_cycles(self):
        document = NodeSet()
        document.object("ns=1;i=100", "1:First", references=[("i=35", "ns=1;i=101", True)])
        document.object("ns=1;i=101", "1:Second", references=[("i=35", "ns=1;i=100", True)])
        report, _ = self.review(document)
        self.assertNotIn("P3-060", self.rules(report))

    def test_haschild_cycle_reports_cycle_members_not_the_acyclic_ancestor(self):
        document = NodeSet()
        document.object("ns=1;i=100", "1:Ancestor", references=[("i=47", "ns=1;i=101", True)])
        document.object("ns=1;i=101", "1:First", references=[("i=47", "ns=1;i=102", True)])
        document.object("ns=1;i=102", "1:Second", references=[("i=47", "ns=1;i=101", True)])
        report, _ = self.review(document)
        nodes = {row["node_id"] for row in report["findings"] if row["rule"] == "P3-060"}
        self.assertEqual({"ns=1;i=101", "ns=1;i=102"}, nodes)

    def test_mirrored_reference_serializations_are_not_duplicates(self):
        document = NodeSet()
        document.object("ns=1;i=100", "1:Parent", references=[("i=47", "ns=1;i=101", True)])
        document.variable("ns=1;i=101", "1:Reading", "ns=1;i=100")
        report, _ = self.review(document)
        self.assertNotIn("P3-049", self.rules(report))

    def test_concrete_reference_and_its_subtype_share_reference_identity(self):
        document = NodeSet()
        document.object("ns=1;i=100", "1:Parent", references=[
            ("i=47", "ns=1;i=101", True), ("i=49", "ns=1;i=101", True),
        ])
        document.variable("ns=1;i=101", "1:Reading", "ns=1;i=100")
        report, _ = self.review(document)
        self.assertIn("P3-049", self.rules(report))

    def test_unknown_reference_type_does_not_create_false_missing_typedefinition(self):
        document = NodeSet()
        document.node("Object", "ns=1;i=100", "1:Parent", [("ns=1;i=999", "i=58", True)])
        report, _ = self.review(document)
        self.assertNotIn("P3-017", self.rules(report))
        self.assertTrue(any("i=999" in key for key in report["unresolved_nodes"]))

    def test_method_argument_metadata_has_a_valid_method_parent(self):
        document = NodeSet()
        document.type("ns=1;i=100", "1:DeviceType")
        document.node("Method", "ns=1;i=101", "1:Configure", [
            ("i=47", "ns=1;i=100", False), ("i=37", "i=78", True),
        ])
        document.arguments("ns=1;i=101", "ns=1;i=102", "InputArguments", [("Mode", "i=6")])
        document.variable("ns=1;i=103", "1:Mode", "ns=1;i=101", rule="i=78", reference="i=129")
        report, _ = self.review(document)
        self.assertNotIn("P3-024", self.rules(report))
        self.assertNotIn("P3-061", self.rules(report))
        self.assertNotIn("P3-047", self.rules(report))

    def test_method_argument_names_are_unique_across_input_and_output(self):
        document = NodeSet()
        document.object("ns=1;i=100", "1:Device")
        document.node("Method", "ns=1;i=101", "1:Configure", [("i=47", "ns=1;i=100", False)])
        document.arguments("ns=1;i=101", "ns=1;i=102", "InputArguments", [("Mode", "i=6")])
        document.arguments("ns=1;i=101", "ns=1;i=103", "OutputArguments", [("Mode", "i=6")])
        report, _ = self.review(document)
        self.assertIn("P3-046", self.rules(report))

    def test_required_method_input_cannot_follow_optional_input(self):
        document = NodeSet()
        document.object("ns=1;i=100", "1:Device")
        document.node("Method", "ns=1;i=101", "1:Configure", [("i=47", "ns=1;i=100", False)])
        document.arguments("ns=1;i=101", "ns=1;i=102", "InputArguments", [("First", "i=6"), ("Second", "i=6")])
        document.variable("ns=1;i=103", "1:First", "ns=1;i=101", reference="i=131")
        report, _ = self.review(document)
        self.assertIn("P3-048", self.rules(report))

    def test_reference_boolean_whitespace_is_supported(self):
        document = NodeSet()
        document.type("ns=1;i=100", "1:DeviceType")
        reference = document.nodes["ns=1;i=100"].find(f"{{{U}}}References/{{{U}}}Reference")
        reference.set("IsForward", " false ")
        report, _ = self.review(document)
        self.assertEqual([], report["findings"])

    def test_cyclic_aliases_are_explicit_input_errors(self):
        document = NodeSet()
        aliases = ET.SubElement(document.root, f"{{{U}}}Aliases")
        ET.SubElement(aliases, f"{{{U}}}Alias", Alias="One").text = "Two"
        ET.SubElement(aliases, f"{{{U}}}Alias", Alias="Two").text = "One"
        document.object("ns=1;i=100", "1:Device", "One")
        with self.assertRaisesRegex(checker.InputError, "cyclic alias"):
            self.review(document)

    def test_dtds_are_rejected_for_utf8_and_utf16(self):
        text = f'<?xml version="1.0" encoding="{{encoding}}"?><!DOCTYPE UANodeSet [<!ENTITY x "test">]><UANodeSet xmlns="{U}"/>'
        with tempfile.TemporaryDirectory() as directory:
            for encoding in ("utf-8", "utf-16"):
                path = Path(directory) / f"{encoding}.xml"
                path.write_bytes(text.format(encoding=encoding).encode(encoding))
                with self.subTest(encoding=encoding), self.assertRaisesRegex(checker.InputError, "DTDs"):
                    checker.read_xml(path)

    def test_markdown_report_escapes_input_content_and_contains_every_rule(self):
        document = self.device(False)
        report, _ = self.review(document)
        report["findings"][0]["message"] = "<script>bad</script>|split\nrow"
        markdown = checker.render_markdown(report)
        self.assertIn("&lt;script&gt;", markdown)
        self.assertIn("\\|split row", markdown)
        for entry in self.catalog:
            self.assertIn(entry["id"], markdown)


if __name__ == "__main__":
    unittest.main()
