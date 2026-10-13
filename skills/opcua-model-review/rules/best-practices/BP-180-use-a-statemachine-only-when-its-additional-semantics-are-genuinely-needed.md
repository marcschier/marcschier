---
id: "BP-180"
title: "Use a StateMachine only when its additional semantics are genuinely needed"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.12.5"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.12.5"]
---

# BP-180 - Use a StateMachine only when its additional semantics are genuinely needed

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A StateMachine provides a set of reachable States (itself a kind of enumeration) plus additional information such as allowed transitions and potentially causes/effects or Client-triggering Methods. A StateMachine's own State set is fixed, but SubStateMachines can refine individual States. This is a more complex mechanism that should only be used when the extra StateMachine-specific functionality is needed or anticipated to be needed upon refinement.

## Applicability

Discrete-state design decisions.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Not independently mechanical (requires judging whether the extra StateMachine semantics are actually used).

**Document:** Review rationale for choosing a StateMachine over a simpler enumeration/MultiState approach.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD (conditional; implies simpler mechanisms otherwise preferred)

## Source

- [OPC 11030 v1.03.03, clause 7.12.5](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.12.5)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
