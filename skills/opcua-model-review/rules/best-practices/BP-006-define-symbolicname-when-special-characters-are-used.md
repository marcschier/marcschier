---
id: "BP-006"
title: "Define SymbolicName when special characters are used"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.2"]
---

# BP-006 - Define SymbolicName when special characters are used

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If special characters (e.g. `&`, `<`) are used in a Node's name despite BP-005, the UANodeSet should define that Node's optional `SymbolicName` so that code generation remains possible.

## Applicability

Any Node whose BrowseName departs from the BP-005 character restriction.

## Exceptions and evidence limits

Only triggered conditionally (only applies when special characters are actually used).

## Audit

**NodeSet XML:** For `UANode` elements whose BrowseName contains characters outside `[A-Za-z0-9_<>]`, confirm a `SymbolicName` child element is present.

**Document:** N/A (NodeSet-only artifact).

**Assessment:** Static-checkable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 2.1.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
