---
id: "BP-075"
title: "Do not insert a new ReferenceType into an existing hierarchy chain"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.15"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.15"]
---

# BP-075 - Do not insert a new ReferenceType into an existing hierarchy chain

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is also not allowed to add new ReferenceTypes "inside the Hierarchy"  -  i.e., positioned such that old Clients would silently ignore it (safe) but new Clients connecting to old Servers would expect the ReferenceType to already be available and used for filtering (unsafe).

## Applicability

ReferenceType hierarchies, across versions sharing a NamespaceUri.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Same insertion-detection approach as BP-054/BP-061, applied to ReferenceType `HasSubtype` chains.

**Document:** Compare ReferenceType hierarchy diagrams across versions.

**Assessment:** Impossible without dependencies (requires prior version); otherwise static-checkable.

**Source wording:** MUST NOT

## Source notes

**Ambiguity flagged explicitly.** Unlike clause 3.2.9/clause 3.2.10 (ObjectType/VariableType/DataType hierarchies), this clause does not cross-reference a figure, does not restate the "allowed if absolutely necessary, subject to constraints X/Y/Z" carve-out, and does not define precisely what "inside the Hierarchy" means beyond the rationale sentence. This extraction reads it, by analogy to clause 3.2.9/clause 3.2.10's insertion concept, as prohibiting insertion of a new type as an intermediate ancestor of existing ReferenceTypes (as opposed to BP-073's permitted leaf-subtype addition)  -  but the source text itself (exact location: clause 3.2.15, second paragraph) does not spell out this reading as explicitly as it does for ObjectTypes/VariableTypes/DataTypes, nor does it confirm or deny an "absolutely necessary" escape hatch for ReferenceTypes. Treat this rule's scope boundary as unconfirmed pending closer reading against Part 3's ReferenceType hierarchy semantics (out of scope here).

## Source

- [OPC 11030 v1.03.03, clause 3.2.15](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.15)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
