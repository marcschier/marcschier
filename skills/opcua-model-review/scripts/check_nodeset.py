from __future__ import annotations

import argparse
import base64
import binascii
from collections import defaultdict
from dataclasses import dataclass, field
import html
import json
from pathlib import Path
import re
import sys
from typing import Iterable
from urllib.parse import unquote
import uuid
import xml.etree.ElementTree as ET
from xml.parsers import expat


UA_URI = "http://opcfoundation.org/UA/"
XML_URI = "http://opcfoundation.org/UA/2011/03/UANodeSet.xsd"
CLASSES = {
    "UAObject", "UAVariable", "UAMethod", "UAObjectType", "UAVariableType",
    "UAReferenceType", "UADataType", "UAView",
}
TYPES = {"ObjectType", "VariableType", "ReferenceType", "DataType"}
INSTANCE_CLASSES = {"Object", "Variable", "Method"}
ROOT = Path(__file__).resolve().parent.parent


class InputError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class NodeId:
    namespace: str
    kind: str
    value: str
    server: str = ""

    def text(self) -> str:
        prefix = f"server={self.server};" if self.server else ""
        return f"{prefix}nsu={self.namespace};{self.kind}={self.value}"

    def is_null(self) -> bool:
        return not self.server and self.namespace == UA_URI and (
            (self.kind == "i" and self.value == "0")
            or (self.kind in {"s", "b"} and not self.value)
            or (self.kind == "g" and self.value == "00000000-0000-0000-0000-000000000000")
        )


def standard(value: int) -> NodeId:
    return NodeId(UA_URI, "i", str(value))


@dataclass(frozen=True, order=True)
class QualifiedName:
    namespace: str
    name: str

    def text(self) -> str:
        return f"{{{self.namespace}}}{self.name}"


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def child(element: ET.Element | None, name: str) -> ET.Element | None:
    if element is None:
        return None
    return next((item for item in element if local_name(item.tag) == name), None)


def child_text(element: ET.Element | None, name: str, default: str = "") -> str:
    item = child(element, name)
    return default if item is None else (item.text or "")


def boolean(text: str, context: str) -> bool:
    text = text.strip()
    if text in {"true", "1"}:
        return True
    if text in {"false", "0"}:
        return False
    raise InputError(f"{context}: invalid XML Boolean {text!r}")


def integer(text: str, context: str) -> int:
    if not re.fullmatch(r"[+-]?[0-9]+", text.strip()):
        raise InputError(f"{context}: invalid integer {text!r}")
    return int(text)


@dataclass
class Resolver:
    namespaces: list[str]
    servers: list[str]
    aliases: dict[str, str]
    file: str

    def namespace(self, index: int) -> str:
        if index < 0 or index > 65535 or index >= len(self.namespaces):
            raise InputError(f"{self.file}: namespace index {index} has no valid table entry")
        return self.namespaces[index]

    def node_id(self, text: str, seen: frozenset[str] = frozenset()) -> NodeId:
        if text in self.aliases:
            if text in seen:
                raise InputError(f"{self.file}: cyclic alias {text!r}")
            return self.node_id(self.aliases[text], seen | {text})
        match = re.fullmatch(
            r"(?:(?:svr=([0-9]+));)?(?:(?:ns=([0-9]+)|nsu=([^;]+));)?([isgb])=(.*)",
            text, re.DOTALL,
        )
        if match is None:
            raise InputError(f"{self.file}: invalid or unresolved NodeId/alias {text!r}")
        server_index, namespace_index, namespace_uri, kind, value = match.groups()
        server = ""
        if server_index and int(server_index):
            index = int(server_index)
            if index > 4294967295 or index > len(self.servers):
                raise InputError(f"{self.file}: unresolved ServerIndex {index}")
            server = self.servers[index - 1]
        namespace = unquote(namespace_uri) if namespace_uri else self.namespace(int(namespace_index or "0"))
        if kind == "i":
            if not value.isascii() or not value.isdigit() or int(value) > 4294967295:
                raise InputError(f"{self.file}: invalid UInt32 NodeId {text!r}")
            value = str(int(value))
        elif kind == "g":
            try:
                value = str(uuid.UUID(value))
            except ValueError as error:
                raise InputError(f"{self.file}: invalid GUID NodeId {text!r}") from error
        elif kind == "b":
            try:
                value = base64.b64encode(base64.b64decode(value, validate=True)).decode("ascii")
            except (ValueError, binascii.Error) as error:
                raise InputError(f"{self.file}: invalid opaque NodeId {text!r}") from error
        return NodeId(namespace, kind, value, server)

    def browse_name(self, text: str) -> QualifiedName:
        match = re.fullmatch(r"([0-9]+):(.*)", text, re.DOTALL)
        return QualifiedName(self.namespace(int(match[1])), match[2]) if match else QualifiedName(UA_URI, text)


@dataclass
class Node:
    key: NodeId
    node_class: str
    browse_name: QualifiedName
    attributes: dict[str, str]
    resolver: Resolver
    raw_id: str
    line: int | None
    element: ET.Element | None = None
    primary: bool = False
    partial: bool = False

    def bool(self, attribute: str, default: bool = False) -> bool:
        return boolean(self.attributes.get(attribute, str(default).lower()), f"{self.resolver.file}:{self.raw_id}:{attribute}")

    def number(self, attribute: str, default: int) -> int:
        return integer(self.attributes.get(attribute, str(default)), f"{self.resolver.file}:{self.raw_id}:{attribute}")

    def rank(self) -> int:
        return self.number("ValueRank", -1)

    def dimensions(self) -> list[int]:
        text = self.attributes.get("ArrayDimensions", "").strip()
        result = [integer(value, f"{self.raw_id}:ArrayDimensions") for value in text.split(",")] if text else []
        if any(value < 0 or value > 4294967295 for value in result):
            raise InputError(f"{self.resolver.file}:{self.raw_id}: ArrayDimensions is not UInt32[]")
        return result

    def datatype(self) -> NodeId:
        return self.resolver.node_id(self.attributes.get("DataType", "i=24"))

    def scalar_value(self) -> str | None:
        value = child(self.element, "Value")
        return next(iter(value)).text if value is not None and len(value) == 1 else None


@dataclass(frozen=True)
class Edge:
    source: NodeId
    reference: NodeId
    target: NodeId


@dataclass
class Declaration:
    node: Node
    references: set[NodeId] = field(default_factory=set)


def read_xml(path: Path) -> tuple[ET.Element, dict[str, int]]:
    data = path.read_bytes()
    parser = expat.ParserCreate(namespace_separator="}")
    lines: dict[str, int] = {}
    depth = 0

    def start(name: str, attributes: dict[str, str]) -> None:
        nonlocal depth
        depth += 1
        if depth == 2 and local_name(name) in CLASSES and "NodeId" in attributes:
            lines.setdefault(attributes["NodeId"], parser.CurrentLineNumber)

    def end(_name: str) -> None:
        nonlocal depth
        depth -= 1

    def reject(*_args: object) -> None:
        raise InputError(f"{path}: DTDs and entity declarations are not accepted")

    parser.StartElementHandler = start
    parser.EndElementHandler = end
    parser.StartDoctypeDeclHandler = reject
    parser.EntityDeclHandler = reject
    parser.ExternalEntityRefHandler = reject
    try:
        parser.Parse(data, True)
        root = ET.fromstring(data)
    except (expat.ExpatError, ET.ParseError) as error:
        raise InputError(f"{path}: malformed XML: {error}") from error
    if root.tag != f"{{{XML_URI}}}UANodeSet":
        raise InputError(f"{path}: expected a namespace-qualified UANodeSet root")
    return root, lines


class Model:
    def __init__(self) -> None:
        self.nodes: dict[NodeId, Node] = {}
        self.edges: set[Edge] = set()
        self.serialized: list[tuple[Node, bool, NodeId, NodeId]] = []
        self.duplicate_nodes: list[Node] = []
        self.gaps: set[str] = set()
        self.declaration_cache: dict[NodeId, dict[tuple[QualifiedName, ...], Declaration]] = {}
        self.files: list[str] = []
        self.unresolved: set[NodeId] = set()
        self.outgoing: dict[NodeId, list[Edge]] = defaultdict(list)
        self.incoming: dict[NodeId, list[Edge]] = defaultdict(list)
        self.parent_map: dict[NodeId, set[NodeId]] = defaultdict(set)
        self.ambiguous_paths: set[tuple[NodeId, bool, tuple[QualifiedName, ...]]] = set()
        self.names: dict[str, NodeId] = {}

    def load_standard(self) -> None:
        metadata = json.loads((ROOT / "scripts" / "ua_namespace0.json").read_text(encoding="utf-8"))
        resolver = Resolver([UA_URI], [], {}, metadata["source"])
        for record in metadata["nodes"]:
            key = resolver.node_id(record["id"])
            node = Node(key, record["class"], QualifiedName(UA_URI, record["name"]),
                        record["attributes"], resolver, record["id"], None, partial=True)
            self.nodes[key] = node
            self.names[record["name"]] = key
            for parent in record["parents"]:
                self.edges.add(Edge(resolver.node_id(parent), standard(45), key))
            for target in record.get("type", []):
                self.edges.add(Edge(key, standard(40), resolver.node_id(target)))

    def load(self, path: Path, primary: bool) -> None:
        root, lines = read_xml(path)
        namespaces = [UA_URI] + [item.text or "" for item in root.findall(f"{{{XML_URI}}}NamespaceUris/{{{XML_URI}}}Uri")]
        if any(not value for value in namespaces):
            raise InputError(f"{path}: empty namespace URI")
        servers = [item.text or "" for item in root.findall(f"{{{XML_URI}}}ServerUris/{{{XML_URI}}}Uri")]
        aliases: dict[str, str] = {}
        for item in root.findall(f"{{{XML_URI}}}Aliases/{{{XML_URI}}}Alias"):
            name = item.get("Alias")
            if not name or name in aliases:
                raise InputError(f"{path}: missing or duplicate Alias name")
            aliases[name] = item.text or ""
        resolver = Resolver(namespaces, servers, aliases, str(path))
        local_ids: set[NodeId] = set()
        for item in root:
            tag = local_name(item.tag)
            if tag in {"NamespaceUris", "ServerUris", "Models", "Aliases", "Extensions"}:
                continue
            if not tag.startswith("UA") or "NodeId" not in item.attrib or "BrowseName" not in item.attrib:
                raise InputError(f"{path}: unsupported node element or missing NodeId/BrowseName: {tag}")
            key = resolver.node_id(item.attrib["NodeId"])
            if key.server:
                raise InputError(f"{path}: a declared Node cannot have a remote ServerIndex")
            node = Node(key, tag[2:], resolver.browse_name(item.attrib["BrowseName"]), dict(item.attrib),
                        resolver, item.attrib["NodeId"], lines.get(item.attrib["NodeId"]), item, primary)
            if key in local_ids:
                self.duplicate_nodes.append(node)
                continue
            local_ids.add(key)
            existing = self.nodes.get(key)
            if existing is not None and not existing.partial:
                if existing.node_class != node.node_class or existing.browse_name != node.browse_name or existing.attributes != node.attributes:
                    raise InputError(f"{path}: conflicting definition of {key.text()} already supplied by {existing.resolver.file}")
                existing.primary |= primary
            else:
                self.nodes[key] = node
            for ref in item.findall(f"{{{XML_URI}}}References/{{{XML_URI}}}Reference"):
                if "ReferenceType" not in ref.attrib or ref.text is None:
                    raise InputError(f"{path}:{node.raw_id}: incomplete Reference")
                reference = resolver.node_id(ref.attrib["ReferenceType"])
                target = resolver.node_id(ref.text)
                forward = boolean(ref.get("IsForward", "true"), f"{path}:{node.raw_id}:IsForward")
                self.edges.add(Edge(key, reference, target) if forward else Edge(target, reference, key))
                self.serialized.append((node, forward, reference, target))
        self.files.append(str(path))

    def index(self) -> None:
        subtype_references = {standard(45)}
        changed = True
        while changed:
            changed = False
            for edge in self.edges:
                target = self.nodes.get(edge.target)
                if (edge.reference in subtype_references and edge.source in subtype_references
                        and edge.target not in subtype_references and target is not None
                        and target.node_class == "ReferenceType"):
                    subtype_references.add(edge.target)
                    changed = True
        for edge in sorted(self.edges, key=lambda item: (item.source, item.reference, item.target)):
            self.outgoing[edge.source].append(edge)
            self.incoming[edge.target].append(edge)
            if edge.reference in subtype_references:
                self.parent_map[edge.target].add(edge.source)
            for key in (edge.source, edge.reference, edge.target):
                if key not in self.nodes:
                    self.unresolved.add(key)
        if any(node.partial for node in self.nodes.values()):
            self.gaps.add("The bundled namespace-zero metadata contains type facts, not complete standard member declarations. Supply the matching full standard NodeSet for inherited-member review.")
        for node in self.nodes.values():
            if node.node_class in {"Variable", "VariableType"}:
                datatype = node.datatype()
                if datatype not in self.nodes:
                    self.unresolved.add(datatype)

    def parents(self, key: NodeId) -> list[NodeId]:
        return sorted(self.parent_map[key])

    def is_subtype(self, actual: NodeId, expected: NodeId) -> bool | None:
        pending = [actual]
        visited: set[NodeId] = set()
        unknown = False
        while pending:
            current = pending.pop()
            if current == expected:
                return True
            if current in visited:
                continue
            visited.add(current)
            if current not in self.nodes:
                self.unresolved.add(current)
                unknown = True
                continue
            pending.extend(self.parent_map[current])
        return None if unknown else False

    def links(self, key: NodeId, reference: int, incoming: bool = False) -> list[Edge]:
        return [edge for edge in (self.incoming[key] if incoming else self.outgoing[key])
                if self.is_subtype(edge.reference, standard(reference)) is True]

    def type_of(self, node: Node) -> NodeId | None:
        links = self.links(node.key, 40)
        return links[0].target if len(links) == 1 else None

    def uncertain_references(self, key: NodeId, incoming: bool = False) -> bool:
        edges = self.incoming[key] if incoming else self.outgoing[key]
        return any(self.is_subtype(edge.reference, standard(31)) is None for edge in edges)

    def is_property(self, node: Node) -> bool:
        return node.node_class == "Variable" and bool(self.links(node.key, 46, incoming=True))

    def modelling_rule(self, node: Node) -> NodeId | None:
        links = self.links(node.key, 37)
        return links[0].target if len(links) == 1 else None

    def hierarchical_children(self, key: NodeId) -> list[tuple[Edge, Node]]:
        return [(edge, self.nodes[edge.target]) for edge in self.outgoing[key]
                if edge.target in self.nodes and self.is_subtype(edge.reference, standard(33)) is True]

    def declaration_owners(self) -> dict[NodeId, set[NodeId]]:
        owners: dict[NodeId, set[NodeId]] = defaultdict(set)
        for root in self.nodes.values():
            if root.node_class not in {"ObjectType", "VariableType"}:
                continue
            pending = [root.key]
            seen: set[NodeId] = set()
            while pending:
                current = pending.pop()
                if current in seen:
                    continue
                seen.add(current)
                for _, node in self.hierarchical_children(current):
                    if node.node_class in INSTANCE_CLASSES and self.modelling_rule(node) is not None:
                        owners[node.key].add(root.key)
                        pending.append(node.key)
        return owners

    def paths(self, key: NodeId, declarations: bool) -> dict[tuple[QualifiedName, ...], Declaration]:
        result: dict[tuple[QualifiedName, ...], Declaration] = {}
        pending: list[tuple[NodeId, tuple[QualifiedName, ...], frozenset[NodeId]]] = [(key, (), frozenset({key}))]
        while pending:
            current, path, ancestors = pending.pop()
            if len(result) >= 10000:
                self.gaps.add(f"BrowsePath expansion limit reached at {key.text()}; remaining paths need manual review.")
                break
            for edge, node in self.hierarchical_children(current):
                if node.node_class not in INSTANCE_CLASSES or (declarations and self.modelling_rule(node) is None):
                    continue
                next_path = path + (node.browse_name,)
                entry = result.get(next_path)
                if entry is None:
                    result[next_path] = Declaration(node, {edge.reference})
                elif entry.node.key == node.key:
                    entry.references.add(edge.reference)
                else:
                    self.ambiguous_paths.add((key, declarations, next_path))
                    self.gaps.add(f"Ambiguous BrowsePath under {key.text()}; duplicate targets require contextual review.")
                if node.key in ancestors:
                    self.gaps.add(f"Cyclic hierarchical declaration/instance path at {node.key.text()}; finite path expansion is incomplete.")
                    continue
                if declarations and self.modelling_rule(node) in {standard(11508), standard(11510)} and node.node_class != "Method":
                    continue
                pending.append((node.key, next_path, ancestors | {node.key}))
        return result

    def declarations(self, key: NodeId, stack: frozenset[NodeId] = frozenset()) -> dict[tuple[QualifiedName, ...], Declaration]:
        if key in self.declaration_cache:
            return self.declaration_cache[key]
        if key in stack:
            self.gaps.add(f"Cyclic type ancestry at {key.text()}.")
            return {}
        if len(stack) >= 256:
            self.gaps.add(f"Type ancestry expansion limit reached at {key.text()}; deeper ancestry requires manual review.")
            return {}
        node = self.nodes.get(key)
        if node is None:
            self.unresolved.add(key)
            return {}
        parents = self.parents(key)
        result: dict[tuple[QualifiedName, ...], Declaration] = {}
        if len(parents) > 1 and node.node_class in {"ObjectType", "VariableType"}:
            self.gaps.add(f"Multiple inheritance at {key.text()}: Part 3 specifies only single-inheritance semantics; no blanket prohibition was inferred.")
        elif parents:
            result.update(self.declarations(parents[0], stack | {key}))
        result.update(self.paths(key, declarations=True))
        self.declaration_cache[key] = result
        return result

    def property(self, key: NodeId, name: str) -> Node | None:
        return next((self.nodes[edge.target] for edge in self.links(key, 46)
                     if edge.target in self.nodes and self.nodes[edge.target].browse_name == QualifiedName(UA_URI, name)), None)


def load_catalog() -> list[dict[str, object]]:
    result = []
    for path in sorted((ROOT / "rules").rglob("*.md")):
        if not re.match(r"(?:P3|P5|BP)-[0-9]{3}-", path.name):
            continue
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.DOTALL)
        if match is None:
            raise InputError(f"{path}: missing rule metadata")
        metadata: dict[str, object] = {}
        for line in match[1].splitlines():
            name, separator, value = line.partition(": ")
            if not separator or name in metadata:
                raise InputError(f"{path}: invalid or duplicate rule metadata")
            try:
                metadata[name] = json.loads(value)
            except json.JSONDecodeError as error:
                raise InputError(f"{path}: metadata values must use JSON-compatible YAML scalars/arrays") from error
        required = {"id", "title", "strength", "targets", "check", "sources"}
        if not required.issubset(metadata) or not path.name.startswith(f"{metadata['id']}-"):
            raise InputError(f"{path}: inconsistent rule metadata")
        metadata["file"] = str(path.relative_to(ROOT))
        result.append(metadata)
    if not result or len({row["id"] for row in result}) != len(result):
        raise InputError("Rule catalog is empty or contains duplicate identifiers")
    return result


class Review:
    def __init__(self, model: Model, catalog: list[dict[str, object]]) -> None:
        self.model = model
        self.catalog = {str(row["id"]): row for row in catalog}
        self.findings: list[dict[str, object]] = []
        self.seen: set[tuple[str, NodeId, str]] = set()
        self.owners = model.declaration_owners()

    def emit(self, rule: str, node: Node, message: str, related: NodeId | None = None) -> None:
        if not node.primary:
            return
        key = (rule, node.key, message)
        if key in self.seen:
            return
        self.seen.add(key)
        metadata = self.catalog[rule]
        strength = str(metadata["strength"])
        self.findings.append({
            "rule": rule,
            "severity": "error" if strength in {"MUST", "MUST NOT"} and metadata.get("authority") != "guidance" else "warning",
            "file": node.resolver.file, "line": node.line, "node_id": node.raw_id,
            "canonical_node_id": node.key.text(), "browse_name": node.browse_name.text(),
            "message": message, "related": related.text() if related else None,
            "sources": metadata["sources"],
        })

    def identity(self) -> None:
        types: dict[tuple[str, QualifiedName], list[Node]] = defaultdict(list)
        for node in self.model.nodes.values():
            if f"UA{node.node_class}" not in CLASSES:
                self.emit("P3-001", node, f"Unsupported NodeClass {node.node_class}.")
            if node.key.is_null():
                self.emit("P3-009", node, "A declared Node has a null NodeId.")
            if node.key.kind == "s" and (len(node.key.value) > 4096 or control_characters(node.key.value)):
                self.emit("P3-010", node, "String NodeId exceeds its bounds or contains control characters.")
            if node.key.kind == "b" and len(base64.b64decode(node.key.value)) > 4096:
                self.emit("P3-010", node, "Opaque NodeId exceeds 4096 decoded bytes.")
            if len(node.browse_name.name) > 512 or control_characters(node.browse_name.name):
                self.emit("P3-011", node, "BrowseName exceeds 512 characters or contains control characters.")
            if node.element is not None and any(
                local_name(item.tag) == "DisplayName" and len(item.text or "") > 512
                for item in node.element
            ):
                self.emit("P3-200", node, "DisplayName text exceeds 512 characters.")
            if node.node_class in TYPES:
                category = "TypeDefinition" if node.node_class in {"ObjectType", "VariableType"} else node.node_class
                types[(category, node.browse_name)].append(node)
        for nodes in types.values():
            if len(nodes) > 1:
                for node in nodes:
                    self.emit("P3-012", node, "Two distinct types in the same category have the same qualified BrowseName.")
        for node in self.model.duplicate_nodes:
            self.emit("P3-009", node, "The input defines the same canonical NodeId more than once.")

    def types(self) -> None:
        for node in self.model.nodes.values():
            links = self.model.links(node.key, 40)
            if node.node_class in {"Object", "Variable"}:
                if len(links) != 1:
                    if self.model.uncertain_references(node.key):
                        self.model.gaps.add(f"TypeDefinition cardinality at {node.key.text()} needs unresolved ReferenceType definitions.")
                    else:
                        self.emit("P3-017", node, f"Expected one HasTypeDefinition, found {len(links)}.")
                    continue
                target = self.model.nodes.get(links[0].target)
                expected = "ObjectType" if node.node_class == "Object" else "VariableType"
                if target is not None:
                    if target.node_class != expected:
                        self.emit("P3-017", node, f"HasTypeDefinition target is {target.node_class}, not {expected}.", target.key)
                    elif target.bool("IsAbstract") and node.key not in self.owners:
                        self.emit("P3-018", node, "A real instance uses an abstract type.", target.key)
            elif links:
                self.emit("P3-017", node, "HasTypeDefinition source is neither Object nor Variable.")

    def properties(self) -> None:
        for node in self.model.nodes.values():
            if node.node_class != "Variable":
                continue
            properties = self.model.links(node.key, 46, incoming=True)
            components = self.model.links(node.key, 47, incoming=True)
            if not properties and not components:
                metadata_context = self.model.links(node.key, 19815, incoming=True) or self.model.links(node.key, 19819, incoming=True)
                if metadata_context:
                    pass
                elif self.model.uncertain_references(node.key, incoming=True):
                    self.model.gaps.add(f"Variable parent role at {node.key.text()} needs unresolved ReferenceType definitions.")
                else:
                    self.emit("P3-019", node, "Variable has no represented Property or DataVariable parent.")
            if properties and components:
                self.emit("P3-020", node, "Variable is used as both Property and DataVariable.")
            if properties:
                if self.model.type_of(node) not in {None, standard(68)}:
                    self.emit("P3-021", node, "Property does not use exact PropertyType.")
                if any(self.model.is_subtype(edge.reference, standard(33)) is True for edge in self.model.outgoing[node.key]):
                    self.emit("P3-022", node, "Property is the source of a hierarchical Reference.")
            for edge in components:
                parent = self.model.nodes.get(edge.source)
                argument_metadata = self.model.is_subtype(edge.reference, standard(129)) is True
                allowed = {"Object", "ObjectType", "Variable", "VariableType"} | ({"Method"} if argument_metadata else set())
                if parent is not None and (parent.node_class not in allowed
                                           or self.model.is_property(parent)):
                    self.emit("P3-024", node, "DataVariable has an invalid HasComponent parent.", parent.key)
        for parent in self.model.nodes.values():
            if any(edge.target.server for edge in self.model.links(parent.key, 46)):
                self.emit("P3-022", parent, "Node and its referenced Property reside in different Servers.")
            names: dict[QualifiedName, set[NodeId]] = defaultdict(set)
            for edge in self.model.links(parent.key, 46):
                if edge.target in self.model.nodes:
                    names[self.model.nodes[edge.target].browse_name].add(edge.target)
            if any(len(nodes) > 1 for nodes in names.values()):
                self.emit("P3-023", parent, "Parent references distinct Properties with the same qualified BrowseName.")

    def references(self) -> None:
        serialized: set[tuple[NodeId, bool, NodeId, NodeId]] = set()
        for node, forward, reference, target in self.model.serialized:
            key = (node.key, forward, reference, target)
            if key in serialized:
                self.emit("P3-049", node, "Reference is repeated in the same serialized direction.")
            serialized.add(key)
        concrete_edges: dict[tuple[NodeId, NodeId, NodeId], set[NodeId]] = defaultdict(set)
        for edge in self.model.edges:
            source, target, reference = (self.model.nodes.get(key) for key in (edge.source, edge.target, edge.reference))
            if reference is not None:
                if reference.node_class != "ReferenceType":
                    if source is not None:
                        self.emit("P3-051", source, "ReferenceType identifier names a non-ReferenceType Node.", reference.key)
                    continue
                if source is not None and reference.bool("IsAbstract"):
                    self.emit("P3-051", source, "Reference uses an abstract ReferenceType.", reference.key)
                ancestors = [reference.key]
                visited: set[NodeId] = set()
                concrete = reference.key
                while ancestors:
                    current = ancestors.pop()
                    if current in visited:
                        continue
                    visited.add(current)
                    current_node = self.model.nodes.get(current)
                    if current_node is not None and not current_node.bool("IsAbstract"):
                        concrete = current
                    ancestors.extend(self.model.parents(current))
                concrete_edges[(edge.source, concrete, edge.target)].add(edge.reference)
            if source is None or target is None:
                continue
            if source.node_class == "View" and self.model.is_subtype(edge.reference, standard(32)) is True:
                self.emit("P3-040", source, "View is a NonHierarchical Reference source.", target.key)
            if source.node_class == "ReferenceType" and not (
                self.model.is_subtype(edge.reference, standard(45)) is True
                or self.model.is_subtype(edge.reference, standard(46)) is True
            ):
                if reference is not None:
                    self.emit("P3-056", source, "ReferenceType Node has an unsupported outgoing Reference.", target.key)
            if self.model.is_subtype(edge.reference, standard(47)) is True:
                allowed = {"Object", "ObjectType", "Variable", "VariableType"} if target.node_class == "Variable" else {"Object", "ObjectType"}
                if target.node_class == "Variable" and self.model.is_subtype(edge.reference, standard(129)) is True:
                    allowed.add("Method")
                if target.node_class not in {"Object", "Variable", "Method"} or source.node_class not in allowed:
                    self.emit("P3-061", source, "HasComponent has an invalid source/target NodeClass pair.", target.key)
            if self.model.is_subtype(edge.reference, standard(46)) is True and target.node_class != "Variable":
                self.emit("P3-062", source, "HasProperty target is not a Variable.", target.key)
            if self.model.is_subtype(edge.reference, standard(35)) is True and source.node_class not in {"Object", "ObjectType", "View"}:
                self.emit("P3-065", source, "Organizes has an invalid source NodeClass.", target.key)
        for (source, _, target), references in concrete_edges.items():
            if len(references) > 1 and source in self.model.nodes:
                self.emit("P3-049", self.model.nodes[source], "References duplicate one concrete ReferenceType identity using its subtypes.", target)
        for node in self.model.nodes.values():
            if node.node_class != "ReferenceType":
                continue
            inverse = child(node.element, "InverseName")
            has_inverse = inverse is not None if not node.partial else node.attributes.get("HasInverseName") == "true"
            if node.bool("Symmetric") == has_inverse:
                self.emit("P3-053", node, "Symmetric ReferenceTypes omit InverseName; non-symmetric ones provide it.")
            for parent in self.model.parents(node.key):
                pending = [parent]
                seen: set[NodeId] = set()
                while pending:
                    key = pending.pop()
                    if key in seen:
                        continue
                    seen.add(key)
                    ancestor = self.model.nodes.get(key)
                    if ancestor is not None and not ancestor.bool("IsAbstract") and ancestor.bool("Symmetric") != node.bool("Symmetric"):
                        self.emit("P3-054", node, "Symmetric differs from a concrete ReferenceType ancestor.", ancestor.key)
                    pending.extend(self.model.parents(key))

    def subtypes(self) -> None:
        for edge in self.model.edges:
            if self.model.is_subtype(edge.reference, standard(45)) is not True:
                continue
            source, target = self.model.nodes.get(edge.source), self.model.nodes.get(edge.target)
            if source is not None and target is not None:
                if source.node_class not in TYPES or target.node_class != source.node_class:
                    self.emit("P3-063", target, "HasSubtype does not connect matching type NodeClasses.", source.key)
                if source.key == standard(68):
                    self.emit("P5-001", target, "PropertyType cannot be subtyped.", source.key)
                if source.key in {standard(24), standard(26), standard(27), standard(28)} and target.key.namespace != UA_URI:
                    self.emit("P3-130", target, "Direct subtype of a reserved abstract DataType root is outside namespace zero.", source.key)
        for node in self.model.nodes.values():
            if node.node_class == "ReferenceType" and node.key != standard(31) and len(self.model.parents(node.key)) != 1:
                self.emit("P3-055", node, "ReferenceType does not have exactly one represented supertype.")

    def hierarchies(self) -> None:
        graph: dict[NodeId, set[NodeId]] = defaultdict(set)
        for edge in self.model.edges:
            source = self.model.nodes.get(edge.source)
            if source is not None and edge.source == edge.target and self.model.is_subtype(edge.reference, standard(33)) is True:
                self.emit("P3-059", source, "Hierarchical self-Reference.")
            if self.model.is_subtype(edge.reference, standard(34)) is True:
                graph[edge.source].add(edge.target)
        active: set[NodeId] = set()
        route: list[NodeId] = []
        visited: set[NodeId] = set()
        for start in list(graph):
            if start in visited:
                continue
            stack: list[tuple[NodeId, bool]] = [(start, False)]
            while stack:
                key, exiting = stack.pop()
                if exiting:
                    active.discard(key)
                    if route and route[-1] == key:
                        route.pop()
                    visited.add(key)
                    continue
                if key in active:
                    cycle = route[route.index(key):]
                    for current in cycle:
                        if current in self.model.nodes:
                            self.emit("P3-060", self.model.nodes[current], "Node lies on a HasChild cycle.", key)
                    continue
                if key in visited:
                    continue
                active.add(key)
                route.append(key)
                stack.append((key, True))
                stack.extend((target, False) for target in graph[key])

    def declarations(self) -> None:
        for node in self.model.nodes.values():
            links = self.model.links(node.key, 37)
            if len(links) > 1 or (links and node.node_class not in INSTANCE_CLASSES):
                self.emit("P3-068", node, "HasModellingRule has an invalid source class or cardinality.")
            for edge in links:
                target = self.model.nodes.get(edge.target)
                if target is not None and (target.node_class != "Object" or self.model.is_subtype(self.model.type_of(target) or target.key, standard(77)) is False):
                    self.emit("P3-068", node, "HasModellingRule does not target a ModellingRule Object.", target.key)
            if len(self.owners.get(node.key, set())) > 1:
                self.emit("P3-076", node, "InstanceDeclaration is explicitly owned by more than one TypeDefinition.")
            if node.node_class in {"ObjectType", "VariableType"} or node.key in self.owners:
                names: dict[QualifiedName, set[NodeId]] = defaultdict(set)
                for _, target in self.model.hierarchical_children(node.key):
                    names[target.browse_name].add(target.key)
                if any(len(targets) > 1 for targets in names.values()):
                    self.emit("P3-078", node, "Declaration context has distinct hierarchical targets with the same qualified BrowseName.")

    def values(self) -> None:
        for node in self.model.nodes.values():
            if node.node_class in {"Variable", "VariableType"}:
                datatype = node.datatype()
                target = self.model.nodes.get(datatype)
                if datatype.is_null() or (target is not None and target.node_class != "DataType"):
                    self.emit("P3-026", node, "DataType is null or identifies a non-DataType Node.", datatype)
                rank, dimensions = node.rank(), node.dimensions()
                if rank < -3 or (rank > 0 and dimensions and len(dimensions) != rank) or (
                    dimensions and (rank == -1 or (node.node_class == "VariableType" and rank <= 0))
                ):
                    self.emit("P3-027", node, "ValueRank and ArrayDimensions are inconsistent.")
                if self.model.property(node.key, "MaxStringLength") and self.model.property(node.key, "MaxCharacters"):
                    self.emit("P3-030", node, "Both MaxStringLength and MaxCharacters are supplied.")
                fixed = self.model.property(node.key, "FixedSizeArray")
                if fixed is not None and fixed.scalar_value() is not None and boolean(fixed.scalar_value() or "", fixed.raw_id):
                    if rank <= 0 or len(dimensions) != rank or not all(dimensions):
                        self.emit("P3-032", node, "FixedSizeArray requires a fixed positive rank and positive ArrayDimensions.")
            for user, general in (("UserWriteMask", "WriteMask"), ("UserAccessLevel", "AccessLevel")):
                if user in node.attributes:
                    default = 1 if general == "AccessLevel" else 0
                    if node.number(user, default) & ~node.number(general, default):
                        self.emit("P3-034", node, f"{user} grants bits not present in {general}.")
            if node.node_class == "Variable":
                access = node.number("AccessLevel", 1)
                user_access = node.number("UserAccessLevel", 1)
                if access < 0 or access > 255 or access & 0x80 or user_access < 0 or user_access > 255 or user_access & 0x80:
                    self.emit("P3-171", node, "AccessLevel/UserAccessLevel contains invalid or reserved bits.")
                if "AccessLevelEx" in node.attributes:
                    extended = node.number("AccessLevelEx", 0)
                    if extended < 0 or extended > 4294967295 or extended & 0xFFFFC080 or extended & 0xFF != access:
                        self.emit("P3-162", node, "AccessLevelEx disagrees with AccessLevel or sets reserved bits.")
            if node.node_class in {"Object", "View"}:
                notifier = node.number("EventNotifier", 0)
                if notifier < 0 or notifier > 255 or notifier & ~0x0D:
                    self.emit("P3-163", node, "EventNotifier sets reserved or invalid bits.")
            for name in ("WriteMask", "UserWriteMask"):
                if name in node.attributes:
                    mask = node.number(name, 0)
                    if mask < 0 or mask > 4294967295 or mask & 0xFC000000 or (node.node_class == "Variable" and mask & (1 << 21)):
                        self.emit("P3-164", node, f"{name} sets reserved or inapplicable ValueForVariableType bits.")

    def arguments(self, node: Node, name: str) -> list[dict[str, object]]:
        prop = self.model.property(node.key, name)
        value = child(prop.element, "Value") if prop is not None else None
        result: list[dict[str, object]] = []
        if value is None or prop is None:
            return result
        for argument in value.iter():
            if local_name(argument.tag) != "Argument":
                continue
            data = child(argument, "DataType")
            identifier = child_text(data, "Identifier")
            if not identifier:
                raise InputError(f"{prop.resolver.file}:{prop.raw_id}: Argument has no DataType Identifier")
            result.append({
                "name": child_text(argument, "Name"), "datatype": prop.resolver.node_id(identifier),
                "rank": integer(child_text(argument, "ValueRank", "-1"), prop.raw_id),
            })
        if len(value) and not result:
            container = next(iter(value))
            if len(container):
                self.model.gaps.add(f"Unsupported Argument value representation at {prop.key.text()}; Method signatures need manual review.")
        return result

    def methods(self) -> None:
        for node in self.model.nodes.values():
            if node.node_class != "Method":
                continue
            parents = self.model.links(node.key, 47, incoming=True)
            if not parents and self.model.uncertain_references(node.key, incoming=True):
                self.model.gaps.add(f"Method context at {node.key.text()} needs unresolved ReferenceType definitions.")
            elif not parents or any(self.model.nodes[edge.source].node_class not in {"Object", "ObjectType"}
                                  for edge in parents if edge.source in self.model.nodes):
                self.emit("P3-043", node, "Method lacks a valid Object/ObjectType HasComponent context.")
            if not node.bool("Executable", True) and node.bool("UserExecutable", True):
                self.emit("P3-044", node, "UserExecutable is true while Executable is false.")
            inputs, outputs = self.arguments(node, "InputArguments"), self.arguments(node, "OutputArguments")
            names = [str(argument["name"]) for argument in inputs + outputs]
            if len(names) != len(set(names)):
                self.emit("P3-046", node, "Method argument names are not unique across input and output arguments.")
            descriptions: dict[str, list[Node]] = defaultdict(list)
            optional: set[str] = set()
            for edge in self.model.links(node.key, 129):
                target = self.model.nodes.get(edge.target)
                if target is None:
                    continue
                descriptions[target.browse_name.name].append(target)
                arguments = [argument for argument in inputs + outputs if argument["name"] == target.browse_name.name]
                if target.node_class != "Variable" or len(arguments) != 1 or target.datatype() != arguments[0]["datatype"]:
                    self.emit("P3-047", node, "Argument description has an unmatched name, wrong class, or wrong DataType.", target.key)
                if node.key in self.owners and self.model.modelling_rule(target) != standard(78):
                    self.emit("P3-047", node, "Method declaration argument metadata is not Mandatory.", target.key)
                if self.model.is_subtype(edge.reference, standard(131)) is True:
                    optional.add(target.browse_name.name)
            if any(len(descriptors) > 1 for descriptors in descriptions.values()):
                self.emit("P3-047", node, "More than one metadata Variable describes the same argument.")
            encountered_optional = False
            for argument in inputs:
                if argument["name"] in optional:
                    encountered_optional = True
                elif encountered_optional:
                    self.emit("P3-048", node, "A required input follows an optional input.")

    def compare(self, actual: Node, expected: Node, subject: Node, preserve_identity: bool = True,
                identity_rule: str = "P3-079") -> None:
        if preserve_identity and (actual.node_class != expected.node_class or actual.browse_name != expected.browse_name):
            self.emit(identity_rule, subject, "Corresponding member changes NodeClass or qualified BrowseName.", actual.key)
            return
        if actual.node_class in {"Object", "Variable"}:
            actual_type, expected_type = self.model.type_of(actual), self.model.type_of(expected)
            if actual_type is not None and expected_type is not None and self.model.is_subtype(actual_type, expected_type) is False:
                self.emit(identity_rule, subject, "Corresponding member has an incompatible TypeDefinition.", actual.key)
        if actual.node_class in {"Variable", "VariableType"}:
            if self.model.is_subtype(actual.datatype(), expected.datatype()) is False:
                self.emit("P3-081", subject, "Corresponding Variable DataType widens or changes its inherited domain.", actual.key)
            if not rank_narrows(actual.rank(), expected.rank()):
                self.emit("P3-082", subject, "Corresponding Variable ValueRank is not an allowed restriction.", actual.key)
            old, new = expected.dimensions(), actual.dimensions()
            if old and (len(old) != len(new) or any(before and before != after for before, after in zip(old, new))):
                self.emit("P3-083", subject, "Corresponding Variable changes a specified inherited ArrayDimensions bound.", actual.key)

    def inheritance(self) -> None:
        for node in self.model.nodes.values():
            if not node.primary:
                continue
            if node.node_class in {"ObjectType", "VariableType"}:
                parents = self.model.parents(node.key)
                if len(parents) != 1:
                    if len(parents) > 1:
                        self.model.declarations(node.key)
                    continue
                parent = self.model.nodes.get(parents[0])
                if parent is None:
                    continue
                if node.node_class == "VariableType":
                    self.compare(node, parent, node, preserve_identity=False)
                inherited = self.model.declarations(parent.key)
                for path, entry in self.model.paths(node.key, declarations=True).items():
                    if path not in inherited:
                        continue
                    original = inherited[path].node
                    self.compare(entry.node, original, node)
                    old_rule, new_rule = self.model.modelling_rule(original), self.model.modelling_rule(entry.node)
                    if old_rule == standard(78) and new_rule != old_rule:
                        self.emit("P3-091", node, "Override weakens a Mandatory declaration.", entry.node.key)
                    if old_rule == standard(80) and new_rule not in {standard(78), standard(80)}:
                        self.emit("P3-091", node, "Override replaces Optional with an incompatible ModellingRule.", entry.node.key)
            elif node.node_class in {"Object", "Variable"}:
                type_id = self.model.type_of(node)
                if type_id is None:
                    continue
                type_node = self.model.nodes.get(type_id)
                if type_node is not None and node.node_class == "Variable":
                    self.compare(node, type_node, node, preserve_identity=False)
                actual = self.model.paths(node.key, declarations=False)
                for path, declaration in sorted(self.model.declarations(type_id).items(), key=lambda item: len(item[0])):
                    rule = self.model.modelling_rule(declaration.node)
                    if rule not in {standard(78), standard(80)}:
                        continue
                    if any((node.key, False, path[:index]) in self.model.ambiguous_paths for index in range(1, len(path) + 1)):
                        continue
                    if any(parent not in actual for parent in (path[:index] for index in range(1, len(path)))):
                        continue
                    candidate = actual.get(path)
                    if candidate is None:
                        if rule == standard(78):
                            self.emit("P3-094", node, "Missing Mandatory member at " + "/".join(part.text() for part in path), declaration.node.key)
                    else:
                        self.compare(candidate.node, declaration.node, node)

    def interfaces(self) -> None:
        base = standard(17602)
        interface_reference = 17603
        for node in self.model.nodes.values():
            interface = self.model.is_subtype(node.key, base) is True
            if interface:
                if node.node_class != "ObjectType" or not node.bool("IsAbstract"):
                    self.emit("P3-104", node, "Interface is not an abstract ObjectType.")
                if self.model.links(node.key, interface_reference):
                    self.emit("P3-106", node, "Interface is a HasInterface source.")
                for declaration in self.model.declarations(node.key).values():
                    if self.model.modelling_rule(declaration.node) not in {standard(78), standard(80)}:
                        self.emit("P3-105", node, "Interface declaration uses a ModellingRule other than Mandatory or Optional.", declaration.node.key)
            if node.node_class in {"Object", "Variable"}:
                type_id = self.model.type_of(node)
                if type_id is not None and self.model.is_subtype(type_id, base) is True:
                    self.emit("P3-106", node, "HasTypeDefinition targets BaseInterfaceType or an Interface.", type_id)
            links = self.model.links(node.key, interface_reference)
            if not links:
                continue
            if node.node_class not in {"Object", "ObjectType"} or interface:
                self.emit("P3-192", node, "HasInterface source is not a non-Interface Object/ObjectType.")
            available = self.model.declarations(node.key) if node.node_class == "ObjectType" else self.model.paths(node.key, declarations=False)
            requirements: dict[tuple[QualifiedName, ...], Node] = {}
            for edge in links:
                target = self.model.nodes.get(edge.target)
                if target is None:
                    continue
                if target.node_class != "ObjectType" or edge.target == base or self.model.is_subtype(edge.target, base) is False:
                    self.emit("P3-192", node, "HasInterface target is not an Interface subtype.", target.key)
                    continue
                for path, declaration in self.model.declarations(target.key).items():
                    expected = declaration.node
                    if node.node_class == "Object" and any(
                        path[:index] not in available for index in range(1, len(path))
                    ):
                        continue
                    original = requirements.get(path)
                    if original is not None:
                        left, right = self.model.type_of(original), self.model.type_of(expected)
                        if original.node_class != expected.node_class or (
                            left is not None and right is not None
                            and self.model.is_subtype(left, right) is False
                            and self.model.is_subtype(right, left) is False
                        ):
                            self.emit("P3-111", node, "Applied Interfaces require incompatible Nodes at the same qualified path.", expected.key)
                    requirements[path] = expected
                    if any((node.key, node.node_class == "ObjectType", path[:index]) in self.model.ambiguous_paths for index in range(1, len(path) + 1)):
                        continue
                    candidate = available.get(path)
                    mandatory = self.model.modelling_rule(expected) == standard(78)
                    if candidate is None:
                        if mandatory:
                            self.emit("P3-109", node, "Missing Mandatory Interface member at " + "/".join(part.text() for part in path), expected.key)
                        continue
                    self.compare(candidate.node, expected, node, identity_rule="P3-109" if mandatory else "P3-110")
                    if mandatory and node.node_class == "ObjectType" and self.model.modelling_rule(candidate.node) != standard(78):
                        self.emit("P3-109", node, "Mandatory Interface member is not declared Mandatory.", candidate.node.key)
                    if node.node_class == "ObjectType" and self.model.modelling_rule(candidate.node) not in {standard(78), standard(80)}:
                        if not mandatory:
                            self.emit("P3-198", node, "Optional Interface declaration should use Mandatory or Optional.", candidate.node.key)

    def addins(self) -> None:
        for node in self.model.nodes.values():
            default = self.model.property(node.key, "DefaultInstanceBrowseName")
            if default is not None and (node.node_class != "ObjectType" or self.model.modelling_rule(default) is not None):
                self.emit("P3-037", node, "DefaultInstanceBrowseName is not type-only metadata without a ModellingRule.", default.key)
            for edge in self.model.links(node.key, 17604):
                target = self.model.nodes.get(edge.target)
                if node.node_class not in {"Object", "ObjectType"} or (target is not None and target.node_class != "Object"):
                    self.emit("P3-114", node, "HasAddIn does not connect an Object/ObjectType to an Object.", edge.target)
                if target is None:
                    continue
                type_id = self.model.type_of(target)
                if type_id is None:
                    continue
                pending = [type_id]
                seen: set[NodeId] = set()
                found = False
                incomplete = False
                while pending:
                    current = pending.pop()
                    if current in seen:
                        continue
                    seen.add(current)
                    current_node = self.model.nodes.get(current)
                    if current_node is None:
                        incomplete = True
                    elif current_node.partial:
                        if "HasDefaultInstanceBrowseName" not in current_node.attributes:
                            incomplete = True
                        elif current_node.bool("HasDefaultInstanceBrowseName"):
                            found = True
                    if self.model.property(current, "DefaultInstanceBrowseName") is not None:
                        found = True
                    pending.extend(self.model.parents(current))
                if not found and not incomplete:
                    self.emit("P3-115", node, "AddIn ObjectType has no DefaultInstanceBrowseName.", type_id)
                elif not found:
                    self.model.gaps.add(f"AddIn default-name check needs complete type declarations for {type_id.text()}.")

    def run(self) -> dict[str, object]:
        methods = {
            "identity": self.identity, "types": self.types, "properties": self.properties,
            "references": self.references, "subtypes": self.subtypes, "hierarchies": self.hierarchies,
            "declarations": self.declarations, "values": self.values, "methods": self.methods,
            "inheritance": self.inheritance, "interfaces": self.interfaces, "addins": self.addins,
        }
        requested = {str(row["check"]) for row in self.catalog.values()} - {"manual"}
        unknown = requested - methods.keys()
        if unknown:
            raise InputError(f"Unknown check groups in catalog: {', '.join(sorted(unknown))}")
        for name, method in methods.items():
            if name in requested:
                method()
        coverage = []
        failed = {str(finding["rule"]) for finding in self.findings}
        for rule in self.catalog.values():
            coverage.append({
                "rule": rule["id"], "title": rule["title"], "rule_file": rule["file"],
                "strength": rule["strength"], "targets": rule["targets"],
                "status": "violation" if rule["id"] in failed else "not_assessed",
                "automated_group": rule["check"],
                "reason": ("Confirmed static evidence is reported; remaining semantic obligations still need review."
                           if rule["id"] in failed else
                           "Static candidate checks ran; read the rule and verify its complete applicability, exceptions, and evidence."
                           if rule["check"] != "manual" else
                           "Requires contextual document/model review or runtime evidence."),
            })
        findings = sorted(self.findings, key=lambda row: (str(row["rule"]), str(row["file"]), int(row["line"] or 0), str(row["message"])))
        return {
            "scope": "Static candidate findings only; this is not a complete conformance audit.",
            "complete": False,
            "inputs": self.model.files,
            "summary": {"rules": len(coverage), "findings": len(findings),
                        "errors": sum(row["severity"] == "error" for row in findings),
                        "warnings": sum(row["severity"] == "warning" for row in findings)},
            "findings": findings, "coverage": coverage,
            "unresolved_nodes": sorted(key.text() for key in self.model.unresolved),
            "evidence_gaps": sorted(self.model.gaps),
            "exit_code": 1 if findings else 3,
        }


def control_characters(text: str) -> bool:
    return any(ord(character) < 32 or 127 <= ord(character) <= 159 for character in text)


def rank_narrows(actual: int, expected: int) -> bool:
    return actual >= -3 and (actual == expected or expected == -2
                           or (expected == -3 and actual in {-1, 1})
                           or (expected == 0 and actual > 0))


def markdown_value(value: object) -> str:
    return html.escape(str(value)).replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def render_markdown(report: dict[str, object]) -> str:
    lines = ["# OPC UA static candidate review", "", "**Incomplete audit:** all rules require a final contextual assessment.", ""]
    summary = report["summary"]
    lines.append(f"Rules: {summary['rules']}; candidate findings: {summary['findings']}; errors: {summary['errors']}; warnings: {summary['warnings']}.")
    lines.extend(["", "| Rule | Severity | Location | NodeId | Evidence |", "|---|---|---|---|---|"])
    for finding in report["findings"]:
        location = f"{finding['file']}:{finding['line']}" if finding["line"] else finding["file"]
        lines.append("| " + " | ".join(markdown_value(value) for value in (
            finding["rule"], finding["severity"], location, finding["node_id"], finding["message"]
        )) + " |")
    lines.extend(["", "## Evidence gaps", ""])
    lines.extend(f"- {markdown_value(gap)}" for gap in report["evidence_gaps"])
    lines.extend(f"- Unresolved: {markdown_value(node)}" for node in report["unresolved_nodes"])
    lines.extend(["", "## Complete rule ledger", "", "| Rule | Strength | Status | Reason |", "|---|---|---|---|"])
    for entry in report["coverage"]:
        lines.append("| " + " | ".join(markdown_value(entry[key]) for key in ("rule", "strength", "status", "reason")) + " |")
    return "\n".join(lines) + "\n"


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Find static OPC UA modelling candidates and seed an exhaustive, explicitly incomplete rule ledger.")
    parser.add_argument("nodeset", type=Path)
    parser.add_argument("--dependency", action="append", default=[], type=Path, help="A local dependency NodeSet; repeat for each dependency.")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--output", type=Path, help="Write the full report to this file instead of stdout.")
    arguments = parser.parse_args(argv)
    try:
        catalog = load_catalog()
        model = Model()
        model.load_standard()
        for dependency in arguments.dependency:
            model.load(dependency.resolve(), primary=False)
        model.load(arguments.nodeset.resolve(), primary=True)
        model.index()
        report = Review(model, catalog).run()
        output = json.dumps(report, indent=2, ensure_ascii=True) + "\n" if arguments.format == "json" else render_markdown(report)
        if arguments.output is None:
            if hasattr(sys.stdout, "reconfigure"):
                sys.stdout.reconfigure(encoding="utf-8")
            print(output, end="")
        else:
            arguments.output.write_text(output, encoding="utf-8")
        return int(report["exit_code"])
    except (InputError, OSError, json.JSONDecodeError) as error:
        print(f"Input/configuration error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
