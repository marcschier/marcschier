---
id: "BP-149"
title: "Companion Specifications must not invent new Node Attributes"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.3.3"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.3.3"]
---

# BP-149 - Companion Specifications must not invent new Node Attributes

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Node Attributes are a predefined, closed set; they are not extensible by Companion Specifications  -  only the base specification may add new optional Attributes over time. If more descriptive data about a Node is needed, a Property must be used instead.

## Applicability

Companion Specifications and vendor information models.

## Exceptions and evidence limits

None  -  base specification evolution is the only sanctioned path to a new Attribute, and that is outside a companion spec's own authority.

## Audit

**NodeSet XML:** Not directly checkable from NodeSet XML alone (Attributes are a fixed, closed meta-model concept; a NodeSet does not "declare" new ones in the way it declares Nodes)  -  the violation pattern would appear in SDK/implementation artifacts outside the NodeSet.

**Document:** Review specification text for any claim of defining a new Node Attribute.

**Assessment:** Semantically reviewable (prose); largely impossible to violate structurally within a conformant NodeSet2 XML file, since the schema itself only supports the fixed Attribute set.

**Source wording:** MUST NOT

## Source

- [OPC 11030 v1.03.03, clause 7.3.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.3.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
