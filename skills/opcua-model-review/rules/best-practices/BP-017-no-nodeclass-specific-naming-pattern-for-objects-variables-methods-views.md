---
id: "BP-017"
title: "No NodeClass-specific naming pattern for Objects, Variables, Methods, Views"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.3"]
strength: "INFORMATIVE"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3"]
---

# BP-017 - No NodeClass-specific naming pattern for Objects, Variables, Methods, Views

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The document explicitly states BrowseNames for Objects, Variables, Methods, and Views "have no specific rules" beyond the general conventions in clause 2.1.2 (PascalCase, character restriction).

## Applicability

Object, Variable, Method, View NodeClasses.

## Exceptions and evidence limits

N/A.

## Audit

**NodeSet XML:** A review tool must **not** apply ObjectType/VariableType/DataType/ReferenceType suffix or verb-naming checks (BP-008-BP-016) to these NodeClasses.

**Document:** None.

**Assessment:** Static-checkable only as a negative guardrail (absence of extra checks).

**Source wording:** Informative (explicit absence-of-rule)

**Context guard:** Informative framing does not independently establish a conformance violation.

## Source notes

Recorded specifically to prevent a rule library from inventing naming constraints the source does not impose.

## Source

- [OPC 11030 v1.03.03, clause 2.1.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
