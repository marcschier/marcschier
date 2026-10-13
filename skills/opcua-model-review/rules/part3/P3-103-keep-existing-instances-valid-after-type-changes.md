---
id: "P3-103"
title: "Keep existing instances valid after type changes"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.5"]
strength: "MUST"
targets: ["document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.5"]
---

# P3-103 - Keep existing instances valid after type changes

## Rule

A type change must leave all existing instances and subtypes satisfying the type constraints; otherwise reconcile them or reject the change.

## Audit

Compare versions and migration behavior. Adding a Mandatory member requires updating existing instances or rejecting the addition.

## Source

- [OPC 10000-3 v1.05.06, clause 6.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.5)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
