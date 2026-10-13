---
id: "BP-219"
title: "A released Companion Specification Namespace must not contain breaking changes"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["14.3.1"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/14.3.1"]
---

# BP-219 - A released Companion Specification Namespace must not contain breaking changes

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Breaking changes are not allowed in a released NamespaceUri of a Companion Specification; a needed breaking change requires a new NamespaceUri (cross-ref clause 3.3/clause 11.3).

## Applicability

Released Companion Specification Namespaces.

## Exceptions and evidence limits

None  -  restates BP-203/BP-112 at this location.

## Audit

**NodeSet XML:** Same as BP-203.

**Document:** Same as BP-203.

**Assessment:** Static-checkable.

**Source wording:** MUST NOT / MUST (new Namespace instead)

## Source notes

Explicit restatement of clause 3.3/clause 11.3's rule, given here as the premise for why deprecation (rather than silent breakage) is the relevant in-Namespace tool.

## Source

- [OPC 11030 v1.03.03, clause 14.3.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/14.3.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
