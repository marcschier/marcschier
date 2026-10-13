---
id: "BP-193"
title: "Reuse existing Companion Specifications to maximize interoperability"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["10.1"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/10.1"]
---

# BP-193 - Reuse existing Companion Specifications to maximize interoperability

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is recommended that both vendors and authors of new Companion Specifications reuse existing Companion Specifications to increase Information-Model-level interoperability; the Online Reference (reference.opcfoundation.org) can be used to discover candidates addressing specific domains (e.g. robots, vision systems, machine tools, injection-moulding machines) or providing generic, reusable base concepts (worked examples named: OPC 10000-100 Devices; OPC 10000-110 Asset Management Basics; OPC 10000-200 Industrial Automation; OPC 10031-4 ISA-95 Job Control; OPC 30050 PackML; OPC 40001-1 Machinery Basic Building Blocks). These generic specifications are typically built as building blocks so a model can selectively reuse only the concepts it needs (not all-or-nothing), and more recent specifications tend to favor Interfaces/AddIns (cross-ref clause 7.2.4/clause 7.2.6) over inheritance-based reuse specifically to ease this picking-and-choosing.

## Applicability

New Companion Specification and vendor model design.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Not independently mechanical (requires a cross-model survey); a tool could flag concepts that closely resemble an existing base/generic specification's concern as reuse candidates for human review.

**Document:** Review the specification's stated reuse of existing Companion Specifications.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source notes

The named example specifications (Devices, Asset Management Basics, Industrial Automation, ISA-95 Job Control, PackML, Machinery Basic Building Blocks) are listed by 11030 only as illustrative pointers; their own content is out of scope for this extraction.

## Source

- [OPC 11030 v1.03.03, clause 10.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/10.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
