---
id: "BP-190"
title: "Use FileTransfer for large, atomic, multi-Node configuration deployments"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["8.4.3"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.4.3"]
---

# BP-190 - Use FileTransfer for large, atomic, multi-Node configuration deployments

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

As a special case, the standardized OPC UA file-transfer mechanism (OPC 10000-20's `FileType`) can be used for larger AddressSpace changes needing one atomic operation (not just a small set of instances based on one TypeDefinition). Worked example: OPC 10000-14's `PubSubConfigurationType` is a subtype of `FileType` letting a whole PubSub configuration be read or a new one deployed in a defined file format; other use cases (e.g., downloading a recipe to a machine) may use a different file format.

## Applicability

Large/atomic AddressSpace configuration deployments.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** For documented bulk-configuration-deployment capability, confirm a `FileType` subtype is used.

**Document:** Review the specification's description of the chosen file format/semantics.

**Assessment:** Static-checkable (type usage) / semantically reviewable (format design).

**Source wording:** MAY (recommended for bulk/atomic changes; cross-ref clause 8.5)

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source notes

clause 8.5's Conclusion restates and combines BP-189 (small/incremental changes) and BP-190 (large configuration deployments) as its final recommendation; not separately atomized as it adds no new content beyond those two rules. Source: https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.5

## Source

- [OPC 11030 v1.03.03, clause 8.4.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.4.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
