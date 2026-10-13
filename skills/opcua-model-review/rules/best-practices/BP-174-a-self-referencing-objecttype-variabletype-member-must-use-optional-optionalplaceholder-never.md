---
id: "BP-174"
title: "A self-referencing ObjectType/VariableType member must use Optional/OptionalPlaceholder, never Mandatory"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.10"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.10"]
---

# BP-174 - A self-referencing ObjectType/VariableType member must use Optional/OptionalPlaceholder, never Mandatory

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If an ObjectType or VariableType unavoidably contains an InstanceDeclaration of itself, that member must not use `Mandatory` or `MandatoryPlaceholder`  -  either would make the type impossible to instantiate, or force indirect infinite self-reference. `Optional`/`OptionalPlaceholder` may be used instead; implementations instantiating such a type must still guard against infinite instantiation loops.

## Applicability

ObjectTypes/VariableTypes that unavoidably contain an InstanceDeclaration of themselves.

## Exceptions and evidence limits

None  -  the Mandatory/MandatoryPlaceholder prohibition is absolute for this specific self-referencing case.

## Audit

**NodeSet XML:** For a type containing a (direct or indirect) InstanceDeclaration whose TypeDefinition is itself or an ancestor, confirm its ModellingRule is Optional/OptionalPlaceholder, not Mandatory/MandatoryPlaceholder.

**Document:** Review self-referencing type definitions for the ModellingRule used.

**Assessment:** Static-checkable.

**Source wording:** MUST NOT (Mandatory/MandatoryPlaceholder) / MAY (Optional/OptionalPlaceholder)

## Source notes

The implementation-side infinite-loop guard is a runtime engineering concern, not itself a NodeSet-structural property (Runtime-only for that part).

## Source

- [OPC 11030 v1.03.03, clause 7.10](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.10)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
