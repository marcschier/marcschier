---
id: "P3-073"
title: "Model EventTypes as BaseEventType-derived ObjectTypes"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.7.2", "9.1", "9.2", "9.3", "9.4", "9.5", "9.6", "9.7", "9.8", "9.9", "9.10", "9.11", "9.12", "9.13", "9.14", "9.15", "9.16", "9.17", "9.18", "9.19", "9.20", "9.21", "9.22", "9.23", "9.24", "9.25", "9.26", "9.27", "9.28", "9.29", "9.30", "9.31"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.7.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.4", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.5", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.6", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.7", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.8", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.9", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.10", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.11", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.12", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.13", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.14", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.15", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.16", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.17", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.18", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.19", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.20", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.21", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.22", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.23", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.24", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.25", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.26", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.27", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.28", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.29", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.30", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.31"]
---

# P3-073 - Model EventTypes as BaseEventType-derived ObjectTypes

## Rule

EventTypes are ObjectTypes under BaseEventType, with semantics consistent with the selected standard EventType. Event occurrences are not a new NodeClass.

## Audit

Review the chosen EventType ancestry and event meaning. Companion EventTypes may be non-abstract; standard abstract types are not ordinary Object instances.

## Source

- [OPC 10000-3 v1.05.06, clause 4.7.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.7.2)
- [OPC 10000-3 v1.05.06, clause 9.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.1)
- [OPC 10000-3 v1.05.06, clause 9.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.2)
- [OPC 10000-3 v1.05.06, clause 9.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.3)
- [OPC 10000-3 v1.05.06, clause 9.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.4)
- [OPC 10000-3 v1.05.06, clause 9.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.5)
- [OPC 10000-3 v1.05.06, clause 9.6](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.6)
- [OPC 10000-3 v1.05.06, clause 9.7](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.7)
- [OPC 10000-3 v1.05.06, clause 9.8](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.8)
- [OPC 10000-3 v1.05.06, clause 9.9](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.9)
- [OPC 10000-3 v1.05.06, clause 9.10](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.10)
- [OPC 10000-3 v1.05.06, clause 9.11](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.11)
- [OPC 10000-3 v1.05.06, clause 9.12](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.12)
- [OPC 10000-3 v1.05.06, clause 9.13](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.13)
- [OPC 10000-3 v1.05.06, clause 9.14](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.14)
- [OPC 10000-3 v1.05.06, clause 9.15](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.15)
- [OPC 10000-3 v1.05.06, clause 9.16](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.16)
- [OPC 10000-3 v1.05.06, clause 9.17](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.17)
- [OPC 10000-3 v1.05.06, clause 9.18](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.18)
- [OPC 10000-3 v1.05.06, clause 9.19](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.19)
- [OPC 10000-3 v1.05.06, clause 9.20](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.20)
- [OPC 10000-3 v1.05.06, clause 9.21](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.21)
- [OPC 10000-3 v1.05.06, clause 9.22](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.22)
- [OPC 10000-3 v1.05.06, clause 9.23](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.23)
- [OPC 10000-3 v1.05.06, clause 9.24](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.24)
- [OPC 10000-3 v1.05.06, clause 9.25](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.25)
- [OPC 10000-3 v1.05.06, clause 9.26](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.26)
- [OPC 10000-3 v1.05.06, clause 9.27](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.27)
- [OPC 10000-3 v1.05.06, clause 9.28](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.28)
- [OPC 10000-3 v1.05.06, clause 9.29](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.29)
- [OPC 10000-3 v1.05.06, clause 9.30](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.30)
- [OPC 10000-3 v1.05.06, clause 9.31](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.31)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
