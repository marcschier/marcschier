---
id: "BP-189"
title: "Prefer Methods on the owning parent instance over purely type-level Methods"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["8.4.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.4.2"]
---

# BP-189 - Prefer Methods on the owning parent instance over purely type-level Methods

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

An alternative, taking instance ownership into account: provide add/remove Methods on the parent Object where the new Node is to be attached/detached, rather than (only) on the TypeDefinition. This is described as more intuitive for Client users (they directly see where the new Node appears) and fits better with where a Server developer would naturally implement the functionality. Worked example from OPC 10000-14's PubSub configuration: `PubSubConnectionType` exposes `AddWriterGroup`/`AddReaderGroup` Methods to add groups (which become direct children of the connection instance) and a `RemoveGroup` Method to remove them; a Server may have several connection instances, and the instance a Method is called on gives the context for where the add/remove applies.

## Applicability

AddressSpace configuration-change Method placement design, especially for smaller/incremental changes (cross-ref clause 8.5/BP-190's larger-change counterpart).

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** For add/remove Methods, confirm they are attached to the owning parent instance's ObjectType (propagated to instances) rather than solely as class Methods on an unrelated/distant TypeDefinition.

**Document:** Review Method placement against the PubSub-style pattern.

**Assessment:** Static-checkable.

**Source wording:** SHOULD

## Source notes

Figure reference: https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.4.2#fig_8_example-of-methods-at-the-place-the-instance-is-located-take (Figure 8, reproduced from OPC 10000-14).

## Source

- [OPC 11030 v1.03.03, clause 8.4.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.4.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
