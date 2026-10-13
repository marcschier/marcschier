---
id: "BP-157"
title: "Use a plain array Variable for the simplest list-of-values case"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.6"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.6"]
---

# BP-157 - Use a plain array Variable for the simplest list-of-values case

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The simplest approach to exposing a set is a Variable holding an array of (potentially structured) values: order is automatic, Clients can subscribe to changes and write the whole array at once, and (if supported) read individual entries/ranges. Trade-offs: no entry can be independently referenced from elsewhere, and no extra metadata (e.g., engineering unit) can be attached to individual entries.

## Applicability

Modelling a set/list where individual-entry referencing or per-entry metadata is not needed.

## Exceptions and evidence limits

See BP-158-BP-160 for cases needing more capability.

## Audit

**NodeSet XML:** Not independently mechanical (a design-time choice).

**Document:** Review rationale for the chosen list/array approach.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.6](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.6)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
