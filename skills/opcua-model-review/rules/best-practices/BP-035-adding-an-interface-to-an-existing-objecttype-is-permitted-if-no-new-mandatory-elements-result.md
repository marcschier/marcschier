---
id: "BP-035"
title: "Adding an Interface to an existing ObjectType is permitted if no new mandatory elements result"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.3"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.3"]
---

# BP-035 - Adding an Interface to an existing ObjectType is permitted if no new mandatory elements result

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is allowed to add an Interface to an existing ObjectType as long as doing so does not add any *new* mandatory InstanceDeclaration to that ObjectType. A new Interface may be defined based on InstanceDeclarations that already exist (optionally already Mandatory) on the ObjectType, in which case the ObjectType can be declared to implement that Interface without introducing anything new.

## Applicability

ObjectType Nodes, across versions sharing a NamespaceUri.

## Exceptions and evidence limits

The condition itself ("no new mandatory InstanceDeclarations added") is the limiting factor, not a separate exception.

## Audit

**NodeSet XML:** Diff two NodeSet versions; for an ObjectType that gained a `HasInterface` reference, confirm no InstanceDeclaration newly became Mandatory/MandatoryPlaceholder as a side effect.

**Document:** Review specification text describing the new Interface's relationship to the pre-existing ObjectType members.

**Assessment:** Impossible without dependencies (requires prior-version comparison); otherwise static-checkable.

**Source wording:** MAY (conditional)

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 3.2.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
