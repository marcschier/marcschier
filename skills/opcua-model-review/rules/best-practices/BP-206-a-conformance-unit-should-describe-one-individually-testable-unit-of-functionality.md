---
id: "BP-206"
title: "A Conformance Unit should describe one individually testable unit of functionality"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["12.1"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/12.1"]
---

# BP-206 - A Conformance Unit should describe one individually testable unit of functionality

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A Conformance Unit is supposed to describe an individual testable functionality  -  either Information Model content or additional rules in the Information Model's context.

## Applicability

Conformance Unit design.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** N/A (Conformance Unit granularity is a specification/registry-level concept, not a NodeSet attribute).

**Document:** Review Conformance Unit definitions for testability/atomicity.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD / Definitional

## Source

- [OPC 11030 v1.03.03, clause 12.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/12.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
