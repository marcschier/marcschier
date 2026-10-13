---
id: "BP-159"
title: "Expose a dynamic, order-independent set of complex things as referenced Objects"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.6"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.6"]
---

# BP-159 - Expose a dynamic, order-independent set of complex things as referenced Objects

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

To expose a set of entries needing the full capability of Objects (including Methods), with no ordering requirement, use referenced Objects (typically combined with a grouping Object per clause 7.2.8). Each Object must be accessed individually; if the set is dynamic, `NodeVersion` and `ModelChangeEvent` should be used to inform Clients of membership changes.

## Applicability

Set/list modelling needing full Object capability (e.g., per-entry Methods) without order semantics.

## Exceptions and evidence limits

See BP-160 for when order does matter.

## Audit

**NodeSet XML:** For a documented dynamic Object set, confirm the parent/NamespaceMetadata exposes `NodeVersion` and that `ModelChangeEvent` generation is documented.

**Document:** Review the specification's description of set dynamics.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.6](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.6)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
