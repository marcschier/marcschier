---
id: "BP-207"
title: "Define both content-oriented and behavior-oriented Conformance Units"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["12.1"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/12.1"]
---

# BP-207 - Define both content-oriented and behavior-oriented Conformance Units

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is beneficial to consider both Conformance Units concerning the model's contents (verifying model elements are implemented correctly, with independent parts testable/implementable separately  -  worked example: energy-usage model parts independent of component-structure model parts) and Conformance Units concerning the model's behavior (verifying functionality that can't be captured in the model alone, e.g. conditional constraints like "exclusive or" / "if A then B," or a Method's actual behavior).

## Applicability

Conformance Unit design for a Companion Specification.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** N/A.

**Document:** Review whether both categories of Conformance Unit are present where applicable.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 12.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/12.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
