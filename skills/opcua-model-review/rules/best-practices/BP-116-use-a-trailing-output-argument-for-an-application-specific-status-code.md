---
id: "BP-116"
title: "Use a trailing output Argument for an application-specific status code"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["5.1"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/5.1"]
---

# BP-116 - Use a trailing output Argument for an application-specific status code

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Because StatusCodes cannot be extended (cross-ref clause 4/BP-114) but a Method call may need a more detailed, application-specific, program-readable failure reason, the last Output Argument of a Method should carry that application-specific error/status code.

## Applicability

Any Method needing to surface more detail than the call-level StatusCode provides.

## Exceptions and evidence limits

Only applies when such detail is actually needed; ordinary Methods need not add this argument.

## Audit

**NodeSet XML:** For Methods documented as needing application-specific status detail, confirm the last entry in `OutputArguments` serves this purpose (cross-check against BP-120's naming/typing convention).

**Document:** Review Method definitions for this trailing-argument pattern where application-specific errors are described.

**Assessment:** Semantically reviewable (need is a design judgement); static-checkable once the pattern is adopted (argument position/type, see BP-120).

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 5.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/5.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
