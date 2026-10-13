---
id: "BP-034"
title: "Adding new optional components is permitted"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.2"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.2"]
---

# BP-034 - Adding new optional components is permitted

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is allowed to add new optional InstanceDeclarations (ModellingRule `Optional` or `OptionalPlaceholder`) to an existing ObjectType/VariableType; old Servers simply omit them and new Clients must not assume their presence.

## Applicability

ObjectType, VariableType Nodes, across versions sharing a NamespaceUri.

## Exceptions and evidence limits

None stated (this is itself the general exception/counterpart to BP-032).

## Audit

**NodeSet XML:** Diff two NodeSet versions; new `Optional`/`OptionalPlaceholder` children on a pre-existing type are expected and compliant (not a defect).

**Document:** N/A.

**Assessment:** Static-checkable (confirms a *non*-violation), given both versions.

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 3.2.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
