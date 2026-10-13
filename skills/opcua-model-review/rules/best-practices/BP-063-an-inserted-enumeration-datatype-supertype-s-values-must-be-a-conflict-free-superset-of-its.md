---
id: "BP-063"
title: "An inserted Enumeration DataType supertype's values must be a conflict-free superset of its subtypes' values"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.10"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.10"]
---

# BP-063 - An inserted Enumeration DataType supertype's values must be a conflict-free superset of its subtypes' values

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

For Enumeration DataTypes, an inserted supertype may have more Enumeration values than its subtypes; it shall have at least the union of all Enumeration values defined by any of its subtypes. If the numeric values of those subtypes' entries would conflict, creating such a supertype is not possible at all.

## Applicability

Conditional on BP-061's carve-out, Enumeration DataTypes specifically.

## Exceptions and evidence limits

None  -  a numeric conflict makes the insertion infeasible outright, not merely discouraged.

## Audit

**NodeSet XML:** Confirm the inserted supertype's `EnumValueType` set is a superset (by value) of each subtype's set, and that no subtype assigns a conflicting name/meaning to the same numeric value.

**Document:** Compare enumeration value tables across the proposed hierarchy.

**Assessment:** Static-checkable (given the candidate hierarchy).

**Source wording:** MUST (as a feasibility precondition)

## Source

- [OPC 11030 v1.03.03, clause 3.2.10](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.10)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
