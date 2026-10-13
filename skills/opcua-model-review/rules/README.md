# OPC UA modelling rule library

**434 named and numbered documents:** 207 Part 3 rules, 226 best-practice entries, and one explicitly sourced Part 5 supplement.

IDs are this library's identifiers, not OPC Foundation clause numbers. Keep existing IDs stable; append new IDs rather than renumbering published entries.

Read [SOURCES.md](SOURCES.md) for editions, [COVERAGE.md](COVERAGE.md) for every source section's disposition, and [SOURCE-NOTES.md](SOURCE-NOTES.md) for source tensions.

## Assessment policy

A rule document is the source of truth for its predicate, applicability, exceptions, and audit procedure. Its frontmatter contains JSON-compatible YAML values for offline tooling.

- Part 3 and the Part 5 supplement identify normative requirements; informative Annex A/B guidance does not become a conformance prohibition.
- OPC 11030 is a non-mandatory whitepaper. The displayed strength preserves its own wording; all BP entries remain advisory unless a separate normative source or an explicitly adopted policy establishes an obligation.
- Compound source wording is retained inside the rule. A leading MAY never erases a stated condition or converts the alternative into a requirement.
- Permissions, explanatory examples, optional features, and recommended naming conventions are not unconditional prohibitions.
- PASS requires evidence for the whole applicable rule. No search hit or no script finding is not a PASS.
- Distinguish NOT_APPLICABLE (established scope exclusion) from NOT_ASSESSED (missing evidence, dependencies, previous releases, runtime behavior, or an unresolved source conflict).
- Keep version comparison separate from instantiation and subtyping. A legal narrowing in an instance or subtype can still be a breaking change to a released definition with the same identity.
- Resolve namespaces by URI, not by indexes copied between files. Normalize Reference direction without requiring mirrored XML entries.
- Review all identified subjects and report all evidenced findings. Do not stop after the first representative violation.
- Static check groups are candidate collectors, not exhaustive implementations of a rule; manual review completes the ledger.

The source coverage map accounts for all 323 Part 3 and 119 OPC 11030 TOC sections. Some sections are definitions, overviews, repeated illustrations, or descriptive context rather than independent requirements.

## Part 3 - Address Space Model

| Rule | Name | Source clauses | Wording | Candidate group |
|---|---|---|---|---|
| [P3-001](part3/P3-001-use-only-the-defined-nodeclasses.md) | Use only the defined NodeClasses | 4.4.2, 8.29 | MUST NOT | identity |
| [P3-002](part3/P3-002-keep-the-standard-attribute-set.md) | Keep the standard Attribute set | 3.3.2, 4.4.3, 5.9 | MUST NOT | manual |
| [P3-003](part3/P3-003-honor-nodeclass-attribute-and-reference-cardinality.md) | Honor NodeClass attribute and reference cardinality | 3.3.2, 5.9 | MUST | manual |
| [P3-004](part3/P3-004-separate-table-optionality-from-modellingrules.md) | Separate table optionality from ModellingRules | 3.3.2 | MUST | manual |
| [P3-005](part3/P3-005-qualify-standard-properties-with-the-standard-namespace.md) | Qualify standard Properties with the standard namespace | 3.3.2, 5.2.4 | MUST | manual |
| [P3-006](part3/P3-006-compare-namespace-uris-as-opaque-case-sensitive-strings.md) | Compare namespace URIs as opaque case-sensitive strings | 4.2, 8.2.2 | MUST | manual |
| [P3-007](part3/P3-007-choose-readable-authority-controlled-uris.md) | Choose readable authority-controlled URIs | 4.2 | SHOULD | manual |
| [P3-008](part3/P3-008-persist-canonical-nodeid-identity-rather-than-namespace-indexes.md) | Persist canonical NodeId identity rather than namespace indexes | 5.2.2, 8.2.2, 8.2.3 | MUST | manual |
| [P3-009](part3/P3-009-assign-unique-non-null-nodeids.md) | Assign unique non-null NodeIds | 5.2.2, 8.2.1, 8.2.4 | MUST | identity |
| [P3-010](part3/P3-010-respect-nodeid-identifier-bounds.md) | Respect NodeId identifier bounds | 8.2.3, 8.2.4 | MUST | identity |
| [P3-011](part3/P3-011-validate-qualified-browsenames.md) | Validate qualified BrowseNames | 5.2.4, 8.3 | MUST | identity |
| [P3-012](part3/P3-012-give-types-and-entry-points-unique-browsenames.md) | Give types and entry points unique BrowseNames | 5.2.4, 5.3.2 | MUST | identity |
| [P3-013](part3/P3-013-use-the-defining-authority-s-namespace-for-standard-types.md) | Use the defining authority's namespace for standard types | 5.2.4 | MUST | manual |
| [P3-014](part3/P3-014-preserve-case-sensitive-browsepath-identity.md) | Preserve case-sensitive BrowsePath identity | 5.2.4 | MUST | manual |
| [P3-015](part3/P3-015-use-localized-displaynames-for-presentation.md) | Use localized DisplayNames for presentation | 5.2.4, 5.2.5, 8.5.1 | SHOULD | manual |
| [P3-016](part3/P3-016-explain-a-node-when-providing-description.md) | Explain a Node when providing Description | 5.2.6 | MUST | manual |
| [P3-017](part3/P3-017-bind-objects-and-variables-to-exactly-one-type.md) | Bind Objects and Variables to exactly one type | 4.6.1, 5.5.1, 5.6.2, 7.13 | MUST | types |
| [P3-018](part3/P3-018-instantiate-concrete-types-while-allowing-abstract-declarations.md) | Instantiate concrete types while allowing abstract declarations | 5.5.2, 5.6.5, 6.2.1 | MUST | types |
| [P3-019](part3/P3-019-define-variables-in-a-containing-context.md) | Define Variables in a containing context | 5.6.2, 5.8.5.2, 5.8.6.1 | MUST | properties |
| [P3-020](part3/P3-020-separate-property-and-datavariable-relationships.md) | Separate Property and DataVariable relationships | 5.6.3, 5.6.4 | MUST | properties |
| [P3-021](part3/P3-021-use-exact-propertytype-for-properties.md) | Use exact PropertyType for Properties | 5.6.3 | MUST | properties |
| [P3-022](part3/P3-022-keep-properties-at-hierarchy-leaves.md) | Keep Properties at hierarchy leaves | 4.5.2, 5.6.3, 7.3, 7.8 | MUST NOT | properties |
| [P3-023](part3/P3-023-give-a-parent-s-properties-distinct-qualified-names.md) | Give a parent's Properties distinct qualified names | 4.5.2, 5.6.3 | MUST | properties |
| [P3-024](part3/P3-024-use-permitted-datavariable-parents.md) | Use permitted DataVariable parents | 5.6.4, 7.7, 5.7.2, 5.7.3 | MUST | properties |
| [P3-025](part3/P3-025-expose-only-actual-parts-of-complex-variable-values.md) | Expose only actual parts of complex Variable values | 4.5.3, 5.6.4 | MUST | manual |
| [P3-026](part3/P3-026-point-datatype-attributes-to-valid-non-null-datatypes.md) | Point DataType Attributes to valid non-null DataTypes | 5.6.2, 5.6.5, 5.8.1 | MUST | values |
| [P3-027](part3/P3-027-keep-valuerank-and-arraydimensions-consistent.md) | Keep ValueRank and ArrayDimensions consistent | 5.6.2, 5.6.5, 8.6 | MUST | values |
| [P3-028](part3/P3-028-describe-instance-values-as-narrowly-as-possible.md) | Describe instance values as narrowly as possible | 5.6.2 | SHOULD | manual |
| [P3-029](part3/P3-029-apply-standard-value-metadata-only-to-supported-value-kinds.md) | Apply standard value metadata only to supported value kinds | 5.6.2 | MUST | manual |
| [P3-030](part3/P3-030-choose-one-string-length-convention.md) | Choose one string length convention | 5.6.4 | MUST NOT | values |
| [P3-031](part3/P3-031-publish-known-string-and-byte-string-length-limits-only.md) | Publish known string and byte-string length limits only | 5.6.4 | MUST NOT | manual |
| [P3-032](part3/P3-032-specify-positive-dimensions-for-fixed-size-arrays.md) | Specify positive dimensions for fixed-size arrays | 5.6.2 | MUST | values |
| [P3-033](part3/P3-033-honor-explicit-nullability-restrictions.md) | Honor explicit nullability restrictions | 5.6.2 | MUST | manual |
| [P3-034](part3/P3-034-restrict-user-access-masks-to-general-capabilities.md) | Restrict user access masks to general capabilities | 5.2.8, 5.6.2 | MUST | values |
| [P3-035](part3/P3-035-mark-changing-semantic-properties-and-signal-changes.md) | Mark changing semantic Properties and signal changes | 5.6.2, 8.57, 9.33.1 | MUST | manual |
| [P3-036](part3/P3-036-distinguish-historizing-activity-from-history-availability.md) | Distinguish historizing activity from history availability | 5.6.2 | MUST | manual |
| [P3-037](part3/P3-037-keep-defaultinstancebrowsename-on-the-objecttype.md) | Keep DefaultInstanceBrowseName on the ObjectType | 5.5.2 | MUST | addins |
| [P3-038](part3/P3-038-make-view-contents-reachable-and-loop-claims-truthful.md) | Make View contents reachable and loop claims truthful | 5.4 | MUST | manual |
| [P3-039](part3/P3-039-exclude-the-server-object-from-view-contents.md) | Exclude the Server Object from View contents | 5.4 | MUST NOT | manual |
| [P3-040](part3/P3-040-use-only-hierarchical-outgoing-references-on-views.md) | Use only hierarchical outgoing References on Views | 5.4 | MUST NOT | references |
| [P3-041](part3/P3-041-maintain-viewversion-for-changes-of-view-contents.md) | Maintain ViewVersion for changes of View contents | 5.4, 9.32.3 | MUST | manual |
| [P3-042](part3/P3-042-reserve-objecttype-create-methods-for-creation.md) | Reserve ObjectType Create Methods for creation | 5.5.4 | SHOULD NOT | manual |
| [P3-043](part3/P3-043-give-each-method-an-object-or-objecttype-context.md) | Give each Method an Object or ObjectType context | 4.8, 5.7.1, 7.7 | MUST | methods |
| [P3-044](part3/P3-044-do-not-grant-userexecutable-when-executable-is-false.md) | Do not grant UserExecutable when Executable is false | 5.7.1 | MUST | methods |
| [P3-045](part3/P3-045-describe-method-arguments-with-argument-arrays.md) | Describe Method arguments with Argument arrays | 5.7.1, 8.6 | MUST | manual |
| [P3-046](part3/P3-046-use-unique-method-argument-names.md) | Use unique Method argument names | 5.7.1 | MUST | methods |
| [P3-047](part3/P3-047-match-argument-metadata-to-the-described-argument.md) | Match argument metadata to the described argument | 5.7.1, 5.7.2 | MUST | methods |
| [P3-048](part3/P3-048-place-optional-method-inputs-after-required-inputs.md) | Place optional Method inputs after required inputs | 5.7.3 | MUST | methods |
| [P3-049](part3/P3-049-avoid-duplicate-logical-references.md) | Avoid duplicate logical References | 4.4.4 | MUST | references |
| [P3-050](part3/P3-050-allow-legitimate-remote-and-unresolved-reference-targets.md) | Allow legitimate remote and unresolved Reference targets | 4.4.4, 4.6.1, 6.4.2 | MAY | manual |
| [P3-051](part3/P3-051-instantiate-concrete-referencetypes-only.md) | Instantiate concrete ReferenceTypes only | 5.3.1, 5.3.2, 7.2 | MUST NOT | references |
| [P3-052](part3/P3-052-place-concrete-referencetypes-under-the-appropriate-root.md) | Place concrete ReferenceTypes under the appropriate root | 7.2, 7.3, 7.4 | MUST | manual |
| [P3-053](part3/P3-053-define-inversename-according-to-symmetry.md) | Define InverseName according to symmetry | 5.3.2 | MUST | references |
| [P3-054](part3/P3-054-preserve-a-concrete-referencetype-s-symmetry-in-subtypes.md) | Preserve a concrete ReferenceType's symmetry in subtypes | 5.3.2 | MUST NOT | references |
| [P3-055](part3/P3-055-use-single-inheritance-for-referencetypes.md) | Use single inheritance for ReferenceTypes | 5.3.3.3, 7.10 | MUST | subtypes |
| [P3-056](part3/P3-056-restrict-outgoing-references-of-referencetype-nodes.md) | Restrict outgoing References of ReferenceType Nodes | 5.3.3.1, 5.3.3.2 | MUST NOT | references |
| [P3-057](part3/P3-057-tighten-inherited-referencetype-semantics-and-constraints.md) | Tighten inherited ReferenceType semantics and constraints | 5.3.3.3 | MUST | manual |
| [P3-058](part3/P3-058-expose-bidirectional-hierarchical-references-when-possible.md) | Expose bidirectional hierarchical References when possible | 5.3.2 | SHOULD | manual |
| [P3-059](part3/P3-059-forbid-hierarchical-self-references.md) | Forbid hierarchical self-References | 7.3 | MUST NOT | hierarchies |
| [P3-060](part3/P3-060-keep-haschild-hierarchies-acyclic.md) | Keep HasChild hierarchies acyclic | 7.5, 7.6, 7.10 | MUST NOT | hierarchies |
| [P3-061](part3/P3-061-use-valid-hascomponent-endpoints.md) | Use valid HasComponent endpoints | 7.7, 5.7.2, 5.7.3 | MUST | references |
| [P3-062](part3/P3-062-use-variable-targets-for-hasproperty.md) | Use Variable targets for HasProperty | 7.8 | MUST | references |
| [P3-063](part3/P3-063-subtype-only-between-compatible-type-nodeclasses.md) | Subtype only between compatible type NodeClasses | 6.3.1, 7.10 | MUST | subtypes |
| [P3-064](part3/P3-064-expose-a-subtype-s-inverse-link-to-its-supertype.md) | Expose a subtype's inverse link to its supertype | 5.3.3.3, 5.5.2, 5.6.5, 5.8.3 | MUST | manual |
| [P3-065](part3/P3-065-use-permitted-organizes-sources.md) | Use permitted Organizes sources | 7.11 | MUST | references |
| [P3-066](part3/P3-066-use-foldertype-for-organizing-objects.md) | Use FolderType for organizing Objects | 5.5.3, 7.11 | SHOULD | manual |
| [P3-067](part3/P3-067-return-ordered-components-in-a-stable-order.md) | Return ordered components in a stable order | 7.9 | MUST | manual |
| [P3-068](part3/P3-068-bind-at-most-one-modellingrule-to-an-eligible-node.md) | Bind at most one ModellingRule to an eligible Node | 5.5.1, 5.6.2, 5.7.1, 6.4.4.1, 7.12 | MUST | declarations |
| [P3-069](part3/P3-069-use-event-source-links-only-in-a-valid-notifier-context.md) | Use event-source links only in a valid notifier context | 5.5.1, 7.17 | MUST | manual |
| [P3-070](part3/P3-070-connect-and-propagate-subscribing-notifier-objects.md) | Connect and propagate subscribing notifier Objects | 7.18 | MUST | manual |
| [P3-071](part3/P3-071-reference-eventtypes-from-valid-generation-contexts.md) | Reference EventTypes from valid generation contexts | 5.5.2, 5.6.5, 5.7.1, 7.15 | MUST | manual |
| [P3-072](part3/P3-072-honor-alwaysgeneratesevent-on-successful-method-calls.md) | Honor AlwaysGeneratesEvent on successful Method calls | 5.7.1, 7.16 | MUST | manual |
| [P3-073](part3/P3-073-model-eventtypes-as-baseeventtype-derived-objecttypes.md) | Model EventTypes as BaseEventType-derived ObjectTypes | 4.7.2, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 9.10, 9.11, 9.12, 9.13, 9.14, 9.15, 9.16, 9.17, 9.18, 9.19, 9.20, 9.21, 9.22, 9.23, 9.24, 9.25, 9.26, 9.27, 9.28, 9.29, 9.30, 9.31 | MUST | manual |
| [P3-074](part3/P3-074-use-subscription-addressable-event-field-modellingrules.md) | Use subscription-addressable Event field ModellingRules | 4.7.2 | MUST | manual |
| [P3-075](part3/P3-075-provide-the-standard-server-event-notifier-when-eventing.md) | Provide the standard Server event notifier when eventing | 4.7.1, 5.4 | MUST | manual |
| [P3-076](part3/P3-076-give-each-instancedeclaration-one-owning-typedefinition.md) | Give each InstanceDeclaration one owning TypeDefinition | 6.2.1, 6.2.3 | MUST | declarations |
| [P3-077](part3/P3-077-exclude-type-only-nodes-from-instantiation-and-inheritance.md) | Exclude type-only Nodes from instantiation and inheritance | 6.2.2, 6.3.3.2 | MUST | declarations |
| [P3-078](part3/P3-078-keep-forward-hierarchical-child-names-unique-in-declaration-contexts.md) | Keep forward hierarchical child names unique in declaration contexts | 5.5.1, 5.5.2, 5.6.4, 5.6.5, 5.7.1, 6.2.6 | MUST | declarations |
| [P3-079](part3/P3-079-preserve-similarity-when-overriding-or-instantiating-declarations.md) | Preserve similarity when overriding or instantiating declarations | 6.2.4, 6.2.7, 6.3.3.3, 6.4.1 | MUST | inheritance |
| [P3-080](part3/P3-080-retain-required-attribute-information-in-overrides.md) | Retain required Attribute information in overrides | 6.2.7, 6.3.2, 6.3.3.3, 6.4.2 | MUST | manual |
| [P3-081](part3/P3-081-narrow-inherited-variable-datatypes-rather-than-widening-them.md) | Narrow inherited Variable DataTypes rather than widening them | 6.2.8 | MUST | inheritance |
| [P3-082](part3/P3-082-restrict-inherited-valuerank-only-by-the-allowed-transitions.md) | Restrict inherited ValueRank only by the allowed transitions | 6.2.8 | MUST | inheritance |
| [P3-083](part3/P3-083-preserve-specified-inherited-array-dimension-limits.md) | Preserve specified inherited array dimension limits | 6.2.8 | MUST | inheritance |
| [P3-084](part3/P3-084-evaluate-the-fully-inherited-declaration-hierarchy.md) | Evaluate the fully inherited declaration hierarchy | 6.3.3.1, 6.3.3.2 | MUST | inheritance |
| [P3-085](part3/P3-085-treat-multiple-declaration-browsepaths-independently.md) | Treat multiple declaration BrowsePaths independently | 6.3.3.2, 6.4.4.4.2 | MUST | manual |
| [P3-086](part3/P3-086-override-ancestors-before-overriding-an-indirect-declaration.md) | Override ancestors before overriding an indirect declaration | 6.3.3.3 | MUST | manual |
| [P3-087](part3/P3-087-respect-reference-replacement-and-cardinality-on-overrides.md) | Respect Reference replacement and cardinality on overrides | 6.3.3.3 | MUST | manual |
| [P3-088](part3/P3-088-preserve-inherited-method-argument-contracts.md) | Preserve inherited Method argument contracts | 6.2.4, 6.3.3.3 | MUST NOT | manual |
| [P3-089](part3/P3-089-give-overrides-their-own-type-and-modellingrule-links.md) | Give overrides their own type and ModellingRule links | 6.3.3.3 | MUST | inheritance |
| [P3-090](part3/P3-090-avoid-unchanged-declaration-overrides.md) | Avoid unchanged declaration overrides | 6.3.3.3 | SHOULD NOT | manual |
| [P3-091](part3/P3-091-do-not-weaken-inherited-modellingrules.md) | Do not weaken inherited ModellingRules | 6.4.4.2, 6.4.4.4.4, 6.4.4.4.5 | MUST NOT | inheritance |
| [P3-092](part3/P3-092-allow-ordinary-instances-to-omit-or-change-their-own-modellingrule.md) | Allow ordinary instances to omit or change their own ModellingRule | 6.4.4.3 | MAY | manual |
| [P3-093](part3/P3-093-preserve-nested-declaration-modellingrules-on-type-composition.md) | Preserve nested declaration ModellingRules on type composition | 6.4.4.3 | MUST | manual |
| [P3-094](part3/P3-094-instantiate-mandatory-declarations-on-existing-paths.md) | Instantiate Mandatory declarations on existing paths | 6.4.4.4.1, 6.4.4.4.2 | MUST | inheritance |
| [P3-095](part3/P3-095-validate-optional-declarations-when-present.md) | Validate Optional declarations when present | 6.4.4.4.2 | MUST | inheritance |
| [P3-096](part3/P3-096-reserve-fixed-declaration-browsepaths-in-instances.md) | Reserve fixed declaration BrowsePaths in instances | 6.4.2 | MUST | manual |
| [P3-097](part3/P3-097-preserve-parallel-direct-references-between-instantiated-members.md) | Preserve parallel direct References between instantiated members | 6.4.3 | MUST | manual |
| [P3-098](part3/P3-098-apply-exposesitsarray-in-its-specified-variabletype-context.md) | Apply ExposesItsArray in its specified VariableType context | 6.4.4.4.3 | MUST | manual |
| [P3-099](part3/P3-099-do-not-require-descendants-of-object-or-variable-placeholders.md) | Do not require descendants of Object or Variable placeholders | 6.4.4.4.4, 6.4.4.4.5 | MUST | manual |
| [P3-100](part3/P3-100-supply-at-least-one-compatible-mandatoryplaceholder-member.md) | Supply at least one compatible MandatoryPlaceholder member | 6.4.4.4.5 | MUST | manual |
| [P3-101](part3/P3-101-use-angle-bracket-names-for-object-and-variable-placeholders.md) | Use angle-bracket names for Object and Variable placeholders | 6.4.4.4.4, 6.4.4.4.5 | SHOULD | manual |
| [P3-102](part3/P3-102-complete-method-placeholders-using-class-specific-rules.md) | Complete Method placeholders using class-specific rules | 6.4.4.4.4, 6.4.4.4.5 | MUST | manual |
| [P3-103](part3/P3-103-keep-existing-instances-valid-after-type-changes.md) | Keep existing instances valid after type changes | 6.5 | MUST | manual |
| [P3-104](part3/P3-104-define-interfaces-as-abstract-baseinterfacetype-subtypes.md) | Define Interfaces as abstract BaseInterfaceType subtypes | 4.10.2 | MUST | interfaces |
| [P3-105](part3/P3-105-use-only-mandatory-and-optional-on-interface-declarations.md) | Use only Mandatory and Optional on Interface declarations | 4.10.2 | MUST | interfaces |
| [P3-106](part3/P3-106-do-not-compose-interfaces-with-hasinterface-or-instantiate-them.md) | Do not compose Interfaces with HasInterface or instantiate them | 4.10.2, 7.19 | MUST NOT | interfaces |
| [P3-107](part3/P3-107-make-interfaces-browse-reachable-from-interfacetypes.md) | Make Interfaces browse-reachable from InterfaceTypes | 4.10.2 | MUST | manual |
| [P3-108](part3/P3-108-prefix-interface-names-with-i.md) | Prefix Interface names with I | 4.10.2 | SHOULD | manual |
| [P3-109](part3/P3-109-implement-every-mandatory-interface-path-compatibly.md) | Implement every Mandatory Interface path compatibly | 4.10.2 | MUST | interfaces |
| [P3-110](part3/P3-110-preserve-optional-interface-path-meaning.md) | Preserve optional Interface path meaning | 4.10.2 | MUST | interfaces |
| [P3-111](part3/P3-111-avoid-incompatible-multiple-interface-paths.md) | Avoid incompatible multiple-Interface paths | 4.10.2 | MUST NOT | interfaces |
| [P3-112](part3/P3-112-apply-instance-interfaces-only-when-compatible-with-the-objecttype.md) | Apply instance Interfaces only when compatible with the ObjectType | 4.10.2 | MUST | interfaces |
| [P3-113](part3/P3-113-avoid-redundant-hasinterface-references.md) | Avoid redundant HasInterface References | 4.10.2 | SHOULD NOT | manual |
| [P3-114](part3/P3-114-identify-addins-through-hasaddin-composition.md) | Identify AddIns through HasAddIn composition | 4.10.3, 7.20 | MUST | addins |
| [P3-115](part3/P3-115-define-an-addin-s-default-browsename.md) | Define an AddIn's default BrowseName | 4.10.3, 5.5.2 | MUST | addins |
| [P3-116](part3/P3-116-use-an-addin-default-name-once-per-parent.md) | Use an AddIn default name once per parent | 4.10.3 | MUST | manual |
| [P3-117](part3/P3-117-expose-usable-datatype-descriptions-for-clients.md) | Expose usable DataType descriptions for clients | 5.8.1 | SHOULD | manual |
| [P3-118](part3/P3-118-apply-encoding-rules-according-to-datatype-kind.md) | Apply encoding rules according to DataType kind | 5.8.2, 5.8.3 | MUST | manual |
| [P3-119](part3/P3-119-give-each-datatypeencoding-one-owner-and-distinct-name.md) | Give each DataTypeEncoding one owner and distinct name | 5.8.1, 5.8.3, 5.8.4, 7.14 | MUST | manual |
| [P3-120](part3/P3-120-provide-the-required-datatypedefinition-kind.md) | Provide the required DataTypeDefinition kind | 5.8.3, 8.47, 8.48, 8.50 | MUST | manual |
| [P3-121](part3/P3-121-identify-a-structure-s-base-and-default-encoding-correctly.md) | Identify a Structure's base and default encoding correctly | 8.48 | MUST | manual |
| [P3-122](part3/P3-122-preserve-published-datatype-encodings-and-identities.md) | Preserve published DataType encodings and identities | 5.8.4 | MUST NOT | manual |
| [P3-123](part3/P3-123-provide-suitable-enumeration-labels.md) | Provide suitable enumeration labels | 5.8.2, 5.8.3 | MUST | manual |
| [P3-124](part3/P3-124-restrict-inherited-enumeration-values-without-changing-labels.md) | Restrict inherited Enumeration values without changing labels | 8.14 | MUST | manual |
| [P3-125](part3/P3-125-use-unique-int32-values-for-enumeration-labels.md) | Use unique Int32 values for Enumeration labels | 8.39 | MUST | manual |
| [P3-126](part3/P3-126-provide-optionsetvalues-for-bit-mask-types.md) | Provide OptionSetValues for bit-mask types | 5.8.2, 5.8.3, 8.40 | MUST | manual |
| [P3-127](part3/P3-127-keep-optionsetlength-applicable-and-large-enough.md) | Keep OptionSetLength applicable and large enough | 5.8.3, 8.40 | MUST | manual |
| [P3-128](part3/P3-128-preserve-optionset-layout-and-inherited-bit-meanings.md) | Preserve OptionSet layout and inherited bit meanings | 8.40 | MUST | manual |
| [P3-129](part3/P3-129-derive-custom-union-types-directly-from-union.md) | Derive custom Union types directly from Union | 8.41 | MUST | manual |
| [P3-130](part3/P3-130-reserve-abstract-numeric-root-children-for-namespace-zero.md) | Reserve abstract numeric root children for namespace zero | 8.7, 8.24, 8.30, 8.33 | MUST NOT | subtypes |
| [P3-131](part3/P3-131-give-concrete-structures-at-least-one-field.md) | Give concrete Structures at least one field | 8.32 | MUST | manual |
| [P3-132](part3/P3-132-give-structure-and-enum-fields-distinct-valid-names.md) | Give Structure and Enum fields distinct valid names | 8.51, 8.52 | MUST | manual |
| [P3-133](part3/P3-133-place-inherited-structure-fields-before-new-fields.md) | Place inherited Structure fields before new fields | 8.48 | MUST | manual |
| [P3-134](part3/P3-134-use-fixed-rank-structure-fields.md) | Use fixed-rank Structure fields | 8.51 | MUST | manual |
| [P3-135](part3/P3-135-respect-structurefield-datatype-and-subtyping-rules.md) | Respect StructureField DataType and subtyping rules | 8.51 | MUST | manual |
| [P3-136](part3/P3-136-interpret-isoptional-according-to-structuretype.md) | Interpret IsOptional according to StructureType | 8.49, 8.51 | MUST | manual |
| [P3-137](part3/P3-137-apply-structurefield-maxstringlength-to-compatible-types.md) | Apply StructureField MaxStringLength to compatible types | 8.51 | MUST | manual |
| [P3-138](part3/P3-138-choose-encoding-friendly-type-and-field-names.md) | Choose encoding-friendly type and field names | 5.8.2, 8.51, 8.52 | SHOULD | manual |
| [P3-139](part3/P3-139-bind-each-datatyperefinement-to-one-structured-datatype.md) | Bind each DataTypeRefinement to one Structured DataType | 5.8.5.1, 5.8.5.2, 5.8.5.3, 7.30 | MUST | manual |
| [P3-140](part3/P3-140-map-field-description-variables-to-real-distinct-fields.md) | Map field-description Variables to real distinct fields | 5.8.5.2, 7.25 | MUST | manual |
| [P3-141](part3/P3-141-tighten-field-refinements-without-changing-encoding.md) | Tighten field refinements without changing encoding | 5.8.5.1, 5.8.5.2 | MUST | manual |
| [P3-142](part3/P3-142-restrict-optional-fields-with-valid-description-referencetypes.md) | Restrict optional fields with valid description ReferenceTypes | 5.8.5.2, 7.26, 7.27 | MUST | manual |
| [P3-143](part3/P3-143-apply-datatyperefinements-only-at-concrete-variable-uses.md) | Apply DataTypeRefinements only at concrete Variable uses | 5.8.5.3, 7.24 | MUST | manual |
| [P3-144](part3/P3-144-apply-nested-field-refinements-through-their-concrete-descriptors.md) | Apply nested field refinements through their concrete descriptors | 5.8.5.2, 5.8.6.2 | MAY | manual |
| [P3-145](part3/P3-145-give-each-subtyperestriction-one-datatype-owner.md) | Give each SubtypeRestriction one DataType owner | 5.8.6.1, 7.29, 7.30 | MUST | manual |
| [P3-146](part3/P3-146-use-subtyperestrictions-only-on-compatible-concrete-variables.md) | Use SubtypeRestrictions only on compatible concrete Variables | 5.8.6.1, 7.28 | MUST | manual |
| [P3-147](part3/P3-147-prefer-an-explicit-datatype-over-a-one-choice-subtyperestriction.md) | Prefer an explicit DataType over a one-choice SubtypeRestriction | 5.8.6.1 | SHOULD | manual |
| [P3-148](part3/P3-148-give-allowedsubtype-descriptors-distinct-qualified-names.md) | Give AllowedSubtype descriptors distinct qualified names | 7.29 | MUST | manual |
| [P3-149](part3/P3-149-name-allowedsubtype-descriptors-for-their-actual-domain.md) | Name AllowedSubtype descriptors for their actual domain | 7.29 | SHOULD | manual |
| [P3-150](part3/P3-150-expose-structured-components-with-matching-names-and-shapes.md) | Expose structured components with matching names and shapes | 7.22.1, 7.22.2, 8.51 | MUST | manual |
| [P3-151](part3/P3-151-use-object-endpoints-for-associatedwith.md) | Use Object endpoints for AssociatedWith | 7.23 | MUST | manual |
| [P3-152](part3/P3-152-identify-the-model-version-when-marking-deprecation.md) | Identify the model version when marking deprecation | 7.21 | MUST | manual |
| [P3-153](part3/P3-153-use-the-defined-localeid-forms.md) | Use the defined LocaleId forms | 8.4 | MUST | manual |
| [P3-154](part3/P3-154-keep-values-within-their-declared-built-in-domains.md) | Keep values within their declared built-in domains | 8.8, 8.9, 8.10, 8.11, 8.12, 8.13, 8.15, 8.16, 8.17, 8.18, 8.19, 8.20, 8.21, 8.22, 8.23, 8.25, 8.26, 8.27, 8.28, 8.29, 8.34, 8.35, 8.36, 8.38, 8.53, 8.54 | MUST | manual |
| [P3-155](part3/P3-155-encode-special-localized-text-locales-correctly.md) | Encode special localized-text locales correctly | 8.5.2.1, 8.5.2.2, 8.5.2.3 | MUST | manual |
| [P3-156](part3/P3-156-avoid-inappropriate-control-characters-in-string-values.md) | Avoid inappropriate control characters in String values | 8.31 | SHOULD | manual |
| [P3-157](part3/P3-157-normalize-normalizedstring-values-to-nfc.md) | Normalize NormalizedString values to NFC | 8.45 | MUST | manual |
| [P3-158](part3/P3-158-honor-lexical-contracts-of-typed-string-values.md) | Honor lexical contracts of typed string values | 8.42, 8.43, 8.44, 8.46 | MUST | manual |
| [P3-159](part3/P3-159-convey-time-values-as-utc.md) | Convey time values as UTC | 8.37 | MUST | manual |
| [P3-160](part3/P3-160-prefer-a-known-structured-schema-to-xmlelement.md) | Prefer a known structured schema to XmlElement | 8.38 | SHOULD NOT | manual |
| [P3-161](part3/P3-161-apply-permissiontype-bits-to-their-defined-operations.md) | Apply PermissionType bits to their defined operations | 4.9.3, 8.55 | MUST | manual |
| [P3-162](part3/P3-162-keep-accesslevelex-consistent-with-accesslevel.md) | Keep AccessLevelEx consistent with AccessLevel | 5.6.2, 8.58 | MUST | values |
| [P3-163](part3/P3-163-clear-reserved-eventnotifier-bits.md) | Clear reserved EventNotifier bits | 8.59 | MUST | values |
| [P3-164](part3/P3-164-use-writemask-bits-only-for-supported-attributes.md) | Use WriteMask bits only for supported Attributes | 8.60 | MUST | values |
| [P3-165](part3/P3-165-honor-the-access-restriction-flag-semantics.md) | Honor the access-restriction flag semantics | 5.2.11, 8.56 | MUST | manual |
| [P3-166](part3/P3-166-publish-and-manage-standard-role-metadata-consistently.md) | Publish and manage standard Role metadata consistently | 4.9.1, 4.9.2 | SHOULD | manual |
| [P3-167](part3/P3-167-assign-and-combine-roles-according-to-authentication-and-permissions.md) | Assign and combine Roles according to authentication and permissions | 4.9.1, 4.9.3 | MUST | manual |
| [P3-168](part3/P3-168-use-namespace-permission-defaults-and-overrides-consistently.md) | Use namespace permission defaults and overrides consistently | 5.2.9 | MUST | manual |
| [P3-169](part3/P3-169-keep-userrolepermissions-read-only-and-session-derived.md) | Keep UserRolePermissions read-only and Session-derived | 5.2.10 | MUST | manual |
| [P3-170](part3/P3-170-publish-standard-access-restriction-defaults-only-for-that-model.md) | Publish standard access restriction defaults only for that model | 5.2.11 | MUST | manual |
| [P3-171](part3/P3-171-clear-the-reserved-accesslevel-bit.md) | Clear the reserved AccessLevel bit | 8.57 | MUST | values |
| [P3-172](part3/P3-172-honor-accesslevelex-subtype-and-persistence-promises.md) | Honor AccessLevelEx subtype and persistence promises | 8.58 | MUST | manual |
| [P3-173](part3/P3-173-use-valid-currencyunittype-metadata.md) | Use valid CurrencyUnitType metadata | 5.6.2, 8.61 | MUST | manual |
| [P3-174](part3/P3-174-couple-nodeversion-updates-with-modelchangeevents.md) | Couple NodeVersion updates with ModelChangeEvents | 5.3.1, 5.4, 5.5.1, 5.5.2, 5.6.2, 5.6.5, 5.7.1, 5.8.3, 9.32.1, 9.32.2 | MUST | manual |
| [P3-175](part3/P3-175-report-modelchangeevents-in-their-view-context.md) | Report ModelChangeEvents in their View context | 9.32.3, 9.32.5, 9.32.6 | MUST | manual |
| [P3-176](part3/P3-176-use-complete-non-redundant-modelchange-event-summaries.md) | Use complete non-redundant ModelChange event summaries | 9.32.4, 9.32.7 | SHOULD | manual |
| [P3-177](part3/P3-177-keep-semantic-change-events-distinct-from-structural-versions.md) | Keep semantic change events distinct from structural versions | 9.33.1, 9.33.2, 9.33.3, 9.33.4 | MUST | manual |
| [P3-178](part3/P3-178-preserve-audit-correlation-through-aggregation.md) | Preserve audit correlation through aggregation | 9.5 | MUST | manual |
| [P3-179](part3/P3-179-use-reusable-types-for-reusable-semantic-structures.md) | Use reusable types for reusable semantic structures | A.1, A.2, A.3, A.4.1 | INFORMATIVE | manual |
| [P3-180](part3/P3-180-choose-properties-and-datavariables-by-meaning-and-extensibility.md) | Choose Properties and DataVariables by meaning and extensibility | A.4.2 | INFORMATIVE | manual |
| [P3-181](part3/P3-181-expose-structured-data-to-suit-generic-access-and-transaction-needs.md) | Expose structured data to suit generic access and transaction needs | A.4.3, A.5 | INFORMATIVE | manual |
| [P3-182](part3/P3-182-use-methods-for-operations-with-input-and-results.md) | Use Methods for operations with input and results | A.6 | INFORMATIVE | manual |
| [P3-183](part3/P3-183-reuse-suitable-standard-referencetypes.md) | Reuse suitable standard ReferenceTypes | A.7 | INFORMATIVE | manual |
| [P3-184](part3/P3-184-define-custom-modellingrules-only-for-unsupported-semantics.md) | Define custom ModellingRules only for unsupported semantics | A.8, 6.4.4.1 | INFORMATIVE | manual |
| [P3-185](part3/P3-185-use-the-prescribed-nodeclass-shapes-when-choosing-annex-c-notation.md) | Use the prescribed NodeClass shapes when choosing Annex C notation | C.1, C.2.2 | MUST | manual |
| [P3-186](part3/P3-186-draw-reference-direction-and-shortcuts-consistently.md) | Draw Reference direction and shortcuts consistently | C.2.2 | MUST | manual |
| [P3-187](part3/P3-187-distinguish-inline-attributes-and-properties-in-diagrams.md) | Distinguish inline Attributes and Properties in diagrams | C.2.3 | MUST | manual |
| [P3-188](part3/P3-188-avoid-duplicate-graphical-representations-of-one-relationship.md) | Avoid duplicate graphical representations of one relationship | C.2.3 | MUST NOT | manual |
| [P3-189](part3/P3-189-align-diagram-cardinality-with-the-modellingrule.md) | Align diagram cardinality with the ModellingRule | C.2.3 | MUST | manual |
| [P3-190](part3/P3-190-do-not-encode-formal-meaning-solely-in-diagram-decoration.md) | Do not encode formal meaning solely in diagram decoration | C.2.1 | MUST | manual |
| [P3-191](part3/P3-191-interpret-addressspace-figures-using-their-declared-convention.md) | Interpret AddressSpace figures using their declared convention | 3.3.1 | INFORMATIVE | manual |
| [P3-192](part3/P3-192-use-valid-hasinterface-endpoints.md) | Use valid HasInterface endpoints | 7.19 | MUST | interfaces |
| [P3-193](part3/P3-193-use-supported-outgoing-references-on-datatype-nodes.md) | Use supported outgoing References on DataType Nodes | 5.8.3, 7.30 | MUST | manual |
| [P3-194](part3/P3-194-honor-optionset-value-and-validbits-semantics.md) | Honor OptionSet Value and ValidBits semantics | 8.40 | MUST | manual |
| [P3-195](part3/P3-195-use-concrete-datatypes-for-concrete-values.md) | Use concrete DataTypes for concrete values | 5.8.2, 5.8.3 | MUST | manual |
| [P3-196](part3/P3-196-prefer-bidirectional-event-generation-references.md) | Prefer bidirectional Event generation References | 5.5.2, 5.6.5, 5.7.1 | SHOULD | manual |
| [P3-197](part3/P3-197-report-unknown-underlying-capabilities-without-false-negative-guarantees.md) | Report unknown underlying capabilities without false negative guarantees | 5.2.7, 5.6.2, 5.7.1 | SHOULD | manual |
| [P3-198](part3/P3-198-provide-similar-optional-interface-declarations-when-appropriate.md) | Provide similar optional Interface declarations when appropriate | 4.10.2 | SHOULD | manual |
| [P3-199](part3/P3-199-use-defined-instance-browsename-defaults-where-possible.md) | Use defined instance BrowseName defaults where possible | 4.10.3, 5.5.2 | SHOULD | manual |
| [P3-200](part3/P3-200-limit-displayname-text-to-512-characters.md) | Limit DisplayName text to 512 characters | 5.2.5 | MUST | identity |
| [P3-201](part3/P3-201-respect-the-maximum-transferred-array-element-count.md) | Respect the maximum transferred array element count | 5.6.2, 8.6, 8.51 | MUST | manual |
| [P3-202](part3/P3-202-treat-nodeversion-contents-as-opaque-equality-tokens.md) | Treat NodeVersion contents as opaque equality tokens | 5.8.3 | MUST NOT | manual |
| [P3-203](part3/P3-203-keep-method-invocation-semantics-scoped-and-run-to-completion.md) | Keep Method invocation semantics scoped and run-to-completion | 4.8, 5.7.1 | MUST | manual |
| [P3-204](part3/P3-204-keep-a-type-and-its-instancedeclarations-in-one-server.md) | Keep a type and its InstanceDeclarations in one Server | 4.6.4 | MUST | manual |
| [P3-205](part3/P3-205-expose-and-protect-standard-role-administration.md) | Expose and protect standard Role administration | 4.9.1 | MUST | manual |
| [P3-206](part3/P3-206-make-type-definitions-available-to-generic-clients.md) | Make type definitions available to generic Clients | 4.6.1 | MUST | manual |
| [P3-207](part3/P3-207-honor-standard-property-data-types-and-value-shapes.md) | Honor standard Property data types and value shapes | 3.3.2, 5.3.1, 5.4, 5.5.1, 5.5.2, 5.6.2, 5.6.5, 5.7.1, 5.8.3 | MUST | manual |

## OPC 11030 - Modelling Best Practices

| Rule | Name | Source clauses | Wording | Candidate group |
|---|---|---|---|---|
| [BP-001](best-practices/BP-001-default-a-node-s-browsename-to-its-own-namespace.md) | Default a Node's BrowseName to its own Namespace | 2.1.1 | SHOULD | manual |
| [BP-002](best-practices/BP-002-companion-spec-nodes-use-the-companion-namespace.md) | Companion-spec Nodes use the companion Namespace | 2.1.1 | SHOULD | manual |
| [BP-003](best-practices/BP-003-use-pascalcase-for-browsenames.md) | Use PascalCase for BrowseNames | 2.1.2 | SHOULD | manual |
| [BP-004](best-practices/BP-004-keep-acronyms-abbreviations-in-pascalcase-not-all-caps.md) | Keep acronyms/abbreviations in PascalCase, not all-caps | 2.1.2 | SHOULD | manual |
| [BP-005](best-practices/BP-005-restrict-browsename-characters-for-typedefinitions-and-related-constructs.md) | Restrict BrowseName characters for TypeDefinitions and related constructs | 2.1.2 | SHOULD | manual |
| [BP-006](best-practices/BP-006-define-symbolicname-when-special-characters-are-used.md) | Define SymbolicName when special characters are used | 2.1.2 | SHOULD | manual |
| [BP-007](best-practices/BP-007-prefixes-in-browsenames-are-permitted-not-mandated-or-prohibited.md) | Prefixes in BrowseNames are permitted, not mandated or prohibited | 2.1.2 | MAY | manual |
| [BP-008](best-practices/BP-008-objecttype-browsenames-end-in-type.md) | ObjectType BrowseNames end in "Type" | 2.1.3 | SHOULD | manual |
| [BP-009](best-practices/BP-009-variabletype-browsenames-end-in-type-or-variabletype-if-ambiguous.md) | VariableType BrowseNames end in "Type" (or "VariableType" if ambiguous) | 2.1.3 | SHOULD | manual |
| [BP-010](best-practices/BP-010-structured-datatype-browsenames-end-in-datatype.md) | Structured DataType BrowseNames end in "DataType" | 2.1.3 | SHOULD | manual |
| [BP-011](best-practices/BP-011-enumeration-datatype-browsenames-carry-no-suffix-or-enum-if-any.md) | Enumeration DataType BrowseNames carry no suffix (or "Enum" if any) | 2.1.3 | SHOULD NOT | manual |
| [BP-012](best-practices/BP-012-do-not-define-new-built-in-datatypes-outside-the-base-specification.md) | Do not define new Built-in DataTypes outside the base specification | 2.1.3 | MUST NOT | manual |
| [BP-013](best-practices/BP-013-simple-datatype-browsenames-carry-no-suffix.md) | Simple DataType BrowseNames carry no suffix | 2.1.3 | SHOULD NOT | manual |
| [BP-014](best-practices/BP-014-referencetype-browsenames-are-verb-based-with-no-suffix.md) | ReferenceType BrowseNames are verb-based with no suffix | 2.1.3 | SHOULD | manual |
| [BP-015](best-practices/BP-015-inversename-applies-only-to-asymmetric-referencetypes.md) | InverseName applies only to asymmetric ReferenceTypes | 2.1.3 | SHOULD | manual |
| [BP-016](best-practices/BP-016-inversename-expresses-the-inverse-semantic.md) | InverseName expresses the inverse semantic | 2.1.3 | SHOULD | manual |
| [BP-017](best-practices/BP-017-no-nodeclass-specific-naming-pattern-for-objects-variables-methods-views.md) | No NodeClass-specific naming pattern for Objects, Variables, Methods, Views | 2.1.3 | INFORMATIVE | manual |
| [BP-018](best-practices/BP-018-typedefinitionnode-browsenames-must-be-unique-in-their-namespace.md) | TypeDefinitionNode BrowseNames must be unique in their Namespace | 2.1.4 | MUST | manual |
| [BP-019](best-practices/BP-019-avoid-reusing-browsename-strings-across-namespaces.md) | Avoid reusing BrowseName strings across Namespaces | 2.1.4 | SHOULD | manual |
| [BP-020](best-practices/BP-020-instancedeclaration-browsepaths-must-be-unique.md) | InstanceDeclaration BrowsePaths must be unique | 2.1.4 | MUST | manual |
| [BP-021](best-practices/BP-021-design-browsepaths-to-be-unique-even-ignoring-case.md) | Design BrowsePaths to be unique even ignoring case | 2.1.4 | SHOULD NOT | manual |
| [BP-022](best-practices/BP-022-structure-field-names-must-be-unique.md) | Structure field names must be unique | 2.2 | MUST | manual |
| [BP-023](best-practices/BP-023-structure-field-names-use-pascalcase.md) | Structure field names use PascalCase | 2.2 | SHOULD | manual |
| [BP-024](best-practices/BP-024-enum-value-names-must-be-unique.md) | Enum value names must be unique | 2.3 | MUST | manual |
| [BP-025](best-practices/BP-025-enum-value-names-use-pascalcase.md) | Enum value names use PascalCase | 2.3 | SHOULD | manual |
| [BP-026](best-practices/BP-026-companion-spec-uanodeset-file-name-pattern.md) | Companion-spec UANodeSet file name pattern | 2.4 | SHOULD | manual |
| [BP-027](best-practices/BP-027-vendor-specific-uanodeset-file-name-pattern.md) | Vendor-specific UANodeSet file name pattern | 2.4 | SHOULD | manual |
| [BP-028](best-practices/BP-028-companion-spec-namespaceuri-template-pattern.md) | Companion-spec NamespaceUri template pattern | 2.5 | SHOULD | manual |
| [BP-029](best-practices/BP-029-avoid-escaped-characters-in-namespaceuris.md) | Avoid %-escaped characters in NamespaceUris | 2.5 | SHOULD NOT | manual |
| [BP-030](best-practices/BP-030-method-argument-names-must-be-unique.md) | Method Argument names must be unique | 2.6 | MUST | manual |
| [BP-031](best-practices/BP-031-method-argument-names-use-pascalcase.md) | Method Argument names use PascalCase | 2.6 | SHOULD | manual |
| [BP-032](best-practices/BP-032-do-not-add-new-mandatory-components-to-a-released-objecttype-variabletype.md) | Do not add new mandatory components to a released ObjectType/VariableType | 3.2.1 | MUST NOT | manual |
| [BP-033](best-practices/BP-033-approved-alternatives-for-introducing-new-mandatory-functionality.md) | Approved alternatives for introducing new mandatory functionality | 3.2.1 | MAY | manual |
| [BP-034](best-practices/BP-034-adding-new-optional-components-is-permitted.md) | Adding new optional components is permitted | 3.2.2 | MAY | manual |
| [BP-035](best-practices/BP-035-adding-an-interface-to-an-existing-objecttype-is-permitted-if-no-new-mandatory-elements-result.md) | Adding an Interface to an existing ObjectType is permitted if no new mandatory elements result | 3.2.3 | MAY | manual |
| [BP-036](best-practices/BP-036-do-not-add-or-remove-enumeration-datatype-values.md) | Do not add or remove Enumeration DataType values | 3.2.4 | MUST NOT | manual |
| [BP-037](best-practices/BP-037-restricting-an-enumeration-via-a-value-subset-subtype-is-permitted.md) | Restricting an Enumeration via a value-subset Subtype is permitted | 3.2.4 | MAY | manual |
| [BP-038](best-practices/BP-038-prefer-multistate-variabletypes-over-enumeration-datatypes-when-future-extension-is-foreseeable.md) | Prefer MultiState VariableTypes over Enumeration DataTypes when future extension is foreseeable | 3.2.4 | SHOULD | manual |
| [BP-039](best-practices/BP-039-do-not-add-fields-to-a-released-structure-datatype.md) | Do not add fields to a released Structure DataType | 3.2.5 | MUST NOT | manual |
| [BP-040](best-practices/BP-040-do-not-remove-fields-optional-or-mandatory-from-a-released-structure-datatype.md) | Do not remove fields (optional or mandatory) from a released Structure DataType | 3.2.5 | MUST NOT | manual |
| [BP-041](best-practices/BP-041-do-not-rename-a-field-of-a-released-structure-datatype.md) | Do not rename a field of a released Structure DataType | 3.2.5 | MUST NOT | manual |
| [BP-042](best-practices/BP-042-do-not-change-the-datatype-valuerank-arraydimensions-of-a-structure-datatype-field.md) | Do not change the DataType/ValueRank/ArrayDimensions of a Structure DataType field | 3.2.5 | MUST NOT | manual |
| [BP-043](best-practices/BP-043-do-not-add-or-remove-fields-of-a-released-union-datatype.md) | Do not add or remove fields of a released Union DataType | 3.2.6 | MUST NOT | manual |
| [BP-044](best-practices/BP-044-do-not-change-the-datatype-of-a-union-datatype-field.md) | Do not change the DataType of a Union DataType field | 3.2.6 | MUST NOT | manual |
| [BP-045](best-practices/BP-045-do-not-add-or-remove-entries-of-a-numeric-optionset-s-optionsetvalues.md) | Do not add or remove entries of a numeric-OptionSet's OptionSetValues | 3.2.7 | MUST NOT | manual |
| [BP-046](best-practices/BP-046-editing-optionsetvalues-entry-text-is-permitted-if-semantics-are-unchanged.md) | Editing OptionSetValues entry text is permitted if semantics are unchanged | 3.2.7 | MAY | manual |
| [BP-047](best-practices/BP-047-do-not-add-or-remove-entries-of-an-optionset-datatype-based-optionset-s-optionsetvalues.md) | Do not add or remove entries of an OptionSet-DataType-based OptionSet's OptionSetValues | 3.2.8 | MUST NOT | manual |
| [BP-048](best-practices/BP-048-editing-entry-text-is-permitted-if-semantics-are-unchanged-optionset-datatype-family.md) | Editing entry text is permitted if semantics are unchanged (OptionSet DataType family) | 3.2.8 | MAY | manual |
| [BP-049](best-practices/BP-049-a-bit-may-be-deprecated-by-requiring-it-always-be-false.md) | A bit may be deprecated by requiring it always be false | 3.2.8 | MAY | manual |
| [BP-050](best-practices/BP-050-subtypes-may-add-additional-bits-without-changing-the-defined-length.md) | Subtypes may add additional bits without changing the defined length | 3.2.8 | MAY | manual |
| [BP-051](best-practices/BP-051-subtypes-may-refine-the-semantics-of-existing-entries.md) | Subtypes may refine the semantics of existing entries | 3.2.8 | MAY | manual |
| [BP-052](best-practices/BP-052-the-defined-bit-length-cannot-be-changed-in-any-subtype.md) | The defined bit-length cannot be changed in any subtype | 3.2.8 | MUST NOT | manual |
| [BP-053](best-practices/BP-053-adding-subtypes-into-an-existing-hierarchy-is-permitted.md) | Adding subtypes into an existing hierarchy is permitted | 3.2.9 | MAY | manual |
| [BP-054](best-practices/BP-054-avoid-inserting-a-new-intermediate-type-into-an-existing-hierarchy.md) | Avoid inserting a new intermediate type into an existing hierarchy | 3.2.9 | SHOULD NOT | manual |
| [BP-055](best-practices/BP-055-an-inserted-intermediate-type-must-not-add-mandatory-elements-beyond-what-every-subtype-already-had.md) | An inserted intermediate type must not add mandatory elements beyond what every subtype already had | 3.2.9 | MUST NOT | manual |
| [BP-056](best-practices/BP-056-an-inserted-intermediate-type-must-not-add-new-textual-constraints.md) | An inserted intermediate type must not add new textual constraints | 3.2.9 | MUST NOT | manual |
| [BP-057](best-practices/BP-057-an-inserted-intermediate-type-may-be-abstract-or-concrete.md) | An inserted intermediate type may be abstract or concrete | 3.2.9 | MAY | manual |
| [BP-058](best-practices/BP-058-never-insert-new-types-inside-the-eventtype-hierarchy.md) | Never insert new types inside the EventType hierarchy | 3.2.9 | MUST NOT | manual |
| [BP-059](best-practices/BP-059-new-eventtype-subtypes-may-extend-existing-types-if-they-preserve-the-parent-s-concept.md) | New EventType subtypes may extend existing types if they preserve the parent's concept | 3.2.9 | MAY | manual |
| [BP-060](best-practices/BP-060-creating-new-datatype-subtypes-is-permitted.md) | Creating new DataType subtypes is permitted | 3.2.10 | MAY | manual |
| [BP-061](best-practices/BP-061-avoid-inserting-new-types-inside-a-datatype-hierarchy.md) | Avoid inserting new types inside a DataType hierarchy | 3.2.10 | SHOULD NOT | manual |
| [BP-062](best-practices/BP-062-an-inserted-datatype-supertype-must-not-add-new-textual-constraints.md) | An inserted DataType supertype must not add new textual constraints | 3.2.10 | SHOULD NOT | manual |
| [BP-063](best-practices/BP-063-an-inserted-enumeration-datatype-supertype-s-values-must-be-a-conflict-free-superset-of-its.md) | An inserted Enumeration DataType supertype's values must be a conflict-free superset of its subtypes' values | 3.2.10 | MUST | manual |
| [BP-064](best-practices/BP-064-an-inserted-structured-datatype-supertype-s-fields-must-be-common-to-all-subtypes.md) | An inserted Structured DataType supertype's fields must be common to all subtypes | 3.2.10 | MUST | manual |
| [BP-065](best-practices/BP-065-do-not-change-a-released-method-s-signature.md) | Do not change a released Method's signature | 3.2.11 | MUST NOT | manual |
| [BP-066](best-practices/BP-066-adding-argument-metadata-is-permitted-without-changing-mandatory-optional-status.md) | Adding argument metadata is permitted without changing mandatory/optional status | 3.2.11 | MAY | manual |
| [BP-067](best-practices/BP-067-revising-argument-description-text-is-permitted-if-semantics-are-unchanged.md) | Revising argument description text is permitted if semantics are unchanged | 3.2.11 | MAY | manual |
| [BP-068](best-practices/BP-068-a-changed-signature-requires-a-new-method-with-a-new-browsename.md) | A changed signature requires a new Method with a new BrowseName | 3.2.11 | MUST | manual |
| [BP-069](best-practices/BP-069-do-not-change-a-variable-s-datatype-valuerank-or-arraydimensions-even-to-a-subtype.md) | Do not change a Variable's DataType, ValueRank, or ArrayDimensions, even to a subtype | 3.2.12 | MUST NOT | manual |
| [BP-070](best-practices/BP-070-changing-an-instancedeclaration-s-typedefinition-is-restricted-to-non-constraining-subtypes.md) | Changing an InstanceDeclaration's TypeDefinition is restricted to non-constraining subtypes | 3.2.13 | MUST NOT | manual |
| [BP-071](best-practices/BP-071-avoid-changing-a-released-referencetype-s-usage-restrictions.md) | Avoid changing a released ReferenceType's usage restrictions | 3.2.14 | SHOULD NOT | manual |
| [BP-072](best-practices/BP-072-changing-referencetype-usage-restrictions-is-permitted-if-it-does-not-contradict-the-rest-of-the.md) | Changing ReferenceType usage restrictions is permitted if it does not contradict the rest of the model | 3.2.14 | MAY | manual |
| [BP-073](best-practices/BP-073-adding-referencetype-subtypes-is-permitted.md) | Adding ReferenceType subtypes is permitted | 3.2.15 | MAY | manual |
| [BP-074](best-practices/BP-074-do-not-reclassify-a-released-referencetype-s-hierarchical-symmetric-nature.md) | Do not reclassify a released ReferenceType's hierarchical/symmetric nature | 3.2.15 | MUST NOT | manual |
| [BP-075](best-practices/BP-075-do-not-insert-a-new-referencetype-into-an-existing-hierarchy-chain.md) | Do not insert a new ReferenceType into an existing hierarchy chain | 3.2.15 | MUST NOT | manual |
| [BP-076](best-practices/BP-076-never-remove-a-previously-defined-node-from-a-companion-specification-s-information-model.md) | Never remove a previously-defined Node from a Companion Specification's Information Model | 3.2.16 | MUST NOT | manual |
| [BP-077](best-practices/BP-077-a-server-implementation-may-omit-exposing-optional-unused-nodes.md) | A Server implementation may omit exposing optional/unused Nodes | 3.2.16 | MAY | manual |
| [BP-078](best-practices/BP-078-nodeid-shall-not-change.md) | NodeId shall not change | 3.2.17 | MUST NOT | manual |
| [BP-079](best-practices/BP-079-nodeclass-shall-not-change.md) | NodeClass shall not change | 3.2.17 | MUST NOT | manual |
| [BP-080](best-practices/BP-080-browsename-shall-not-change.md) | BrowseName shall not change | 3.2.17 | MUST NOT | manual |
| [BP-081](best-practices/BP-081-displayname-text-may-change-its-meaning-shall-not-change.md) | DisplayName text may change; its meaning shall not change | 3.2.17 | MAY | manual |
| [BP-082](best-practices/BP-082-description-text-may-change-its-meaning-shall-not-change.md) | Description text may change; its meaning shall not change | 3.2.17 | MAY | manual |
| [BP-083](best-practices/BP-083-writemask-is-typically-unspecified-and-may-be-changed.md) | WriteMask is typically unspecified and may be changed | 3.2.17 | MAY | manual |
| [BP-084](best-practices/BP-084-userwritemask-is-implementation-specific-not-specification-defined.md) | UserWriteMask is implementation-specific (not specification-defined) | 3.2.17 | INFORMATIVE | manual |
| [BP-085](best-practices/BP-085-rolepermissions-is-typically-unspecified-and-may-be-changed.md) | RolePermissions is typically unspecified and may be changed | 3.2.17 | MAY | manual |
| [BP-086](best-practices/BP-086-userrolepermissions-is-implementation-specific.md) | UserRolePermissions is implementation-specific | 3.2.17 | INFORMATIVE | manual |
| [BP-087](best-practices/BP-087-accessrestrictions-is-typically-unspecified-and-may-be-changed.md) | AccessRestrictions is typically unspecified and may be changed | 3.2.17 | MAY | manual |
| [BP-088](best-practices/BP-088-isabstract-may-only-be-relaxed-from-true-to-false-never-the-reverse.md) | IsAbstract may only be relaxed from true to false, never the reverse | 3.2.17 | MAY | manual |
| [BP-089](best-practices/BP-089-symmetric-shall-not-change.md) | Symmetric shall not change | 3.2.17 | MUST NOT | manual |
| [BP-090](best-practices/BP-090-inversename-text-may-change-its-meaning-shall-not-change.md) | InverseName text may change; its meaning shall not change | 3.2.17 | MAY | manual |
| [BP-091](best-practices/BP-091-containsnoloops-is-typically-unspecified-and-may-be-changed.md) | ContainsNoLoops is typically unspecified and may be changed | 3.2.17 | MAY | manual |
| [BP-092](best-practices/BP-092-eventnotifier-is-typically-unspecified-and-may-be-changed.md) | EventNotifier is typically unspecified and may be changed | 3.2.17 | MAY | manual |
| [BP-093](best-practices/BP-093-a-type-level-default-value-is-typically-unspecified-and-may-be-changed.md) | A type-level default Value is typically unspecified and may be changed | 3.2.17 | MAY | manual |
| [BP-094](best-practices/BP-094-a-variable-s-datatype-shall-not-change-at-the-specification-level-a-server-instance-may-narrow-it.md) | A Variable's DataType shall not change at the specification level; a Server instance may narrow it | 3.2.17 | MUST NOT | manual |
| [BP-095](best-practices/BP-095-a-variable-s-valuerank-shall-not-change-at-the-specification-level-a-server-instance-may-narrow-it.md) | A Variable's ValueRank shall not change at the specification level; a Server instance may narrow it | 3.2.17 | MUST NOT | manual |
| [BP-096](best-practices/BP-096-a-variabletype-s-datatype-shall-not-change-no-server-exception.md) | A VariableType's DataType shall not change (no Server exception) | 3.2.17 | MUST NOT | manual |
| [BP-097](best-practices/BP-097-a-variabletype-s-valuerank-shall-not-change-no-server-exception.md) | A VariableType's ValueRank shall not change (no Server exception) | 3.2.17 | MUST NOT | manual |
| [BP-098](best-practices/BP-098-arraydimensions-once-defined-shall-not-change-a-server-may-set-an-otherwise-undefined-dimension.md) | ArrayDimensions, once defined, shall not change; a Server may set an otherwise-undefined dimension | 3.2.17 | MUST NOT | manual |
| [BP-099](best-practices/BP-099-accesslevel-may-be-changed.md) | AccessLevel may be changed | 3.2.17 | MAY | manual |
| [BP-100](best-practices/BP-100-useraccesslevel-is-implementation-specific.md) | UserAccessLevel is implementation-specific | 3.2.17 | INFORMATIVE | manual |
| [BP-101](best-practices/BP-101-minimumsamplinginterval-is-typically-unspecified-and-may-be-changed.md) | MinimumSamplingInterval is typically unspecified and may be changed | 3.2.17 | MAY | manual |
| [BP-102](best-practices/BP-102-historizing-is-typically-unspecified-and-may-be-changed.md) | Historizing is typically unspecified and may be changed | 3.2.17 | MAY | manual |
| [BP-103](best-practices/BP-103-accesslevelex-may-be-changed.md) | AccessLevelEx may be changed | 3.2.17 | MAY | manual |
| [BP-104](best-practices/BP-104-a-method-s-executable-attribute-should-not-be-fixed-by-the-specification.md) | A Method's Executable attribute should not be fixed by the specification | 3.2.17 | SHOULD NOT | manual |
| [BP-105](best-practices/BP-105-userexecutable-is-implementation-specific.md) | UserExecutable is implementation-specific | 3.2.17 | INFORMATIVE | manual |
| [BP-106](best-practices/BP-106-datatypedefinition-shall-not-change.md) | DataTypeDefinition shall not change | 3.2.17 | MUST NOT | manual |
| [BP-107](best-practices/BP-107-symbolicname-changes-are-not-breaking-but-should-be-avoided.md) | SymbolicName changes are not breaking but should be avoided | 3.2.17 | SHOULD NOT | manual |
| [BP-108](best-practices/BP-108-avoid-attribute-changes-without-compelling-justification-even-where-technically-permitted.md) | Avoid attribute changes without compelling justification, even where technically permitted | 3.2.17 | SHOULD | manual |
| [BP-109](best-practices/BP-109-avoid-breaking-changes-in-new-companion-specification-versions.md) | Avoid breaking changes in new Companion Specification versions | 3.3 | SHOULD | manual |
| [BP-110](best-practices/BP-110-strategy-compatible-mandatory-additions-via-subtype-new-conformance-unit-profile.md) | Strategy: compatible mandatory additions via subtype + new Conformance Unit/Profile | 3.3 | MAY | manual |
| [BP-111](best-practices/BP-111-strategy-optional-then-mandatory-via-conformance-unit-profile.md) | Strategy: optional-then-mandatory via Conformance Unit/Profile | 3.3 | MAY | manual |
| [BP-112](best-practices/BP-112-when-a-breaking-change-is-unavoidable-create-a-new-namespaceuri.md) | When a breaking change is unavoidable, create a new NamespaceUri | 3.3 | SHOULD | manual |
| [BP-113](best-practices/BP-113-alternative-when-breaking-change-unavoidable-parallel-numbered-type.md) | Alternative when breaking change unavoidable: parallel numbered type | 3.3 | MAY | manual |
| [BP-114](best-practices/BP-114-do-not-define-additional-statuscodes.md) | Do not define additional StatusCodes | 4 | MUST NOT | manual |
| [BP-115](best-practices/BP-115-the-only-sanctioned-path-for-a-new-statuscode-is-the-base-working-group.md) | The only sanctioned path for a new StatusCode is the base working group | 4 | MUST | manual |
| [BP-116](best-practices/BP-116-use-a-trailing-output-argument-for-an-application-specific-status-code.md) | Use a trailing output Argument for an application-specific status code | 5.1 | SHOULD | manual |
| [BP-117](best-practices/BP-117-the-status-output-argument-s-datatype-should-be-int32.md) | The status output argument's DataType should be Int32 | 5.1 | SHOULD | manual |
| [BP-118](best-practices/BP-118-return-an-uncertain-statuscode-alongside-an-application-specific-error.md) | Return an Uncertain StatusCode alongside an application-specific error | 5.2 | SHOULD | manual |
| [BP-119](best-practices/BP-119-callers-should-rely-only-on-the-status-output-argument-when-the-result-is-uncertain.md) | Callers should rely only on the status output argument when the result is Uncertain | 5.2 | MUST | manual |
| [BP-120](best-practices/BP-120-recommended-concrete-pattern-status-argument-multistatevaluediscretetype-metadata.md) | Recommended concrete pattern: "Status" argument + MultiStateValueDiscreteType metadata | 5.2 | SHOULD | manual |
| [BP-121](best-practices/BP-121-retain-legacy-datatypedictionary-nodes-alongside-datatypedefinition.md) | Retain legacy DataTypeDictionary Nodes alongside DataTypeDefinition | 6.3 | SHOULD | manual |
| [BP-122](best-practices/BP-122-only-define-a-new-objecttype-when-reuse-is-expected.md) | Only define a new ObjectType when reuse is expected | 7.2.1 | SHOULD | manual |
| [BP-123](best-practices/BP-123-derive-from-the-most-appropriate-existing-objecttype.md) | Derive from the most appropriate existing ObjectType | 7.2.2 | SHOULD | manual |
| [BP-124](best-practices/BP-124-a-derived-objecttype-s-optional-substructure-may-be-unused-but-not-its-mandatory-substructure.md) | A derived ObjectType's optional substructure may be unused, but not its mandatory substructure | 7.2.2 | MAY | manual |
| [BP-125](best-practices/BP-125-use-baseobjecttype-when-no-more-appropriate-type-exists.md) | Use BaseObjectType when no more appropriate type exists | 7.2.2 | MUST | manual |
| [BP-126](best-practices/BP-126-make-a-base-type-abstract-when-it-is-an-incomplete-template.md) | Make a base type abstract when it is an incomplete template | 7.2.3 | INFORMATIVE | manual |
| [BP-127](best-practices/BP-127-make-a-base-type-concrete-when-it-is-already-usable-on-its-own.md) | Make a base type concrete when it is already usable on its own | 7.2.3 | INFORMATIVE | manual |
| [BP-128](best-practices/BP-128-prefer-composition-addin-interface-over-the-type-hierarchy-for-independent-aspects.md) | Prefer composition (AddIn/Interface) over the type hierarchy for independent aspects | 7.2.4 | SHOULD | manual |
| [BP-129](best-practices/BP-129-model-co-occurring-independent-capabilities-via-composition-not-re-hierarchy.md) | Model co-occurring independent capabilities via composition, not re-hierarchy | 7.2.4 | SHOULD | manual |
| [BP-130](best-practices/BP-130-grouping-objects-are-a-human-readability-aid-not-a-functional-requirement.md) | Grouping Objects are a human-readability aid, not a functional requirement | 7.2.5 | MAY | manual |
| [BP-131](best-practices/BP-131-rule-of-thumb-group-when-an-objecttype-exceeds-30-direct-subcomponents.md) | Rule of thumb: group when an ObjectType exceeds 30 direct subcomponents | 7.2.5 | SHOULD | manual |
| [BP-132](best-practices/BP-132-group-logically-related-standardized-subcomponents.md) | Group logically-related standardized subcomponents | 7.2.5 | SHOULD | manual |
| [BP-133](best-practices/BP-133-group-subcomponents-attached-via-placeholder-modellingrules.md) | Group subcomponents attached via Placeholder ModellingRules | 7.2.5 | SHOULD | manual |
| [BP-134](best-practices/BP-134-choose-foldertype-for-single-use-grouping-a-dedicated-addin-objecttype-for-reusable-grouping.md) | Choose FolderType for single-use grouping, a dedicated AddIn ObjectType for reusable grouping | 7.2.5 | SHOULD | manual |
| [BP-135](best-practices/BP-135-prefer-an-interface-for-small-directly-deployed-aspects.md) | Prefer an Interface for small, directly-deployed aspects | 7.2.6 | SHOULD | manual |
| [BP-136](best-practices/BP-136-prefer-an-addin-in-all-other-larger-grouped-cases-both-may-coexist.md) | Prefer an AddIn in all other (larger/grouped) cases; both may coexist | 7.2.6 | SHOULD | manual |
| [BP-137](best-practices/BP-137-use-optional-when-a-provider-may-not-support-the-functionality-at-all.md) | Use Optional when a provider may not support the functionality at all | 7.2.7 | SHOULD | manual |
| [BP-138](best-practices/BP-138-use-mandatory-with-a-defined-default-for-writable-variables-a-client-might-populate.md) | Use Mandatory with a defined default for writable Variables a Client might populate | 7.2.7 | SHOULD | manual |
| [BP-139](best-practices/BP-139-do-not-use-mandatory-but-returns-bad-status-as-a-substitute-for-optional.md) | Do not use "Mandatory-but-returns-Bad-status" as a substitute for Optional | 7.2.7 | SHOULD NOT | manual |
| [BP-140](best-practices/BP-140-optional-functionality-may-be-elevated-to-required-via-conformance-units-profiles.md) | Optional functionality may be elevated to required via Conformance Units/Profiles | 7.2.7 | MAY | manual |
| [BP-141](best-practices/BP-141-at-least-one-required-forces-grouping-mandatory-subcomponent-mandatoryplaceholder.md) | "At least one required" forces grouping-Mandatory + subcomponent-MandatoryPlaceholder | 7.2.8 | MUST | manual |
| [BP-142](best-practices/BP-142-option-1-mandatory-grouping-optionalplaceholder-subcomponent-when-the-grouping-object-has-its-own.md) | Option 1: Mandatory grouping + OptionalPlaceholder subcomponent, when the grouping Object has its own functionality | 7.2.8 | SHOULD | manual |
| [BP-143](best-practices/BP-143-option-2-optional-grouping-mandatoryplaceholder-subcomponent-when-the-grouping-object-has-no-own.md) | Option 2: Optional grouping + MandatoryPlaceholder subcomponent, when the grouping Object has no own functionality | 7.2.8 | SHOULD | manual |
| [BP-144](best-practices/BP-144-option-3-optional-grouping-optionalplaceholder-subcomponent-to-preserve-subtype-flexibility.md) | Option 3: Optional grouping + OptionalPlaceholder subcomponent, to preserve subtype flexibility | 7.2.8 | MAY | manual |
| [BP-145](best-practices/BP-145-only-define-a-new-variabletype-when-reuse-is-expected-otherwise-use-base-spec-variabletypes.md) | Only define a new VariableType when reuse is expected; otherwise use base-spec VariableTypes | 7.3.1 | SHOULD | manual |
| [BP-146](best-practices/BP-146-use-a-property-only-for-pure-descriptive-data-with-no-extension-need-otherwise-use-a-datavariable.md) | Use a Property only for pure descriptive data with no extension need; otherwise use a DataVariable | 7.3.2 | SHOULD | manual |
| [BP-147](best-practices/BP-147-a-variable-needing-its-own-properties-must-be-a-datavariable.md) | A Variable needing its own Properties must be a DataVariable | 7.3.2 | MUST | manual |
| [BP-148](best-practices/BP-148-prefer-an-existing-attribute-over-a-new-property-when-one-fits.md) | Prefer an existing Attribute over a new Property when one fits | 7.3.3 | SHOULD | manual |
| [BP-149](best-practices/BP-149-companion-specifications-must-not-invent-new-node-attributes.md) | Companion Specifications must not invent new Node Attributes | 7.3.3 | MUST NOT | manual |
| [BP-150](best-practices/BP-150-define-a-variabletype-mainly-for-reusable-semantics-not-for-objecttype-scoped-variables.md) | Define a VariableType mainly for reusable semantics, not for ObjectType-scoped Variables | 7.3.4 | SHOULD | manual |
| [BP-151](best-practices/BP-151-use-placeholder-modellingrules-on-a-method-only-when-its-signature-cannot-be-standardized.md) | Use Placeholder ModellingRules on a Method only when its signature cannot be standardized | 7.4 | SHOULD | manual |
| [BP-152](best-practices/BP-152-an-objecttype-may-define-class-methods-with-no-modellingrule.md) | An ObjectType may define class Methods with no ModellingRule | 7.4 | MAY | manual |
| [BP-153](best-practices/BP-153-prefer-individual-variables-when-no-transactional-context-is-needed.md) | Prefer individual Variables when no transactional context is needed | 7.5.7, 7.5.2 | SHOULD | manual |
| [BP-154](best-practices/BP-154-prefer-a-structured-datatype-optionally-with-sub-variables-when-atomicity-or-server-limits-require.md) | Prefer a Structured DataType (optionally with sub-variables) when atomicity or server limits require it | 7.5.7, 7.5.3, 7.5.4 | SHOULD | manual |
| [BP-155](best-practices/BP-155-use-a-methods-based-approach-when-extra-context-is-needed-or-the-client-should-trigger-re.md) | Use a Methods-based approach when extra context is needed or the Client should trigger (re)calculation | 7.5.7, 7.5.5 | SHOULD | manual |
| [BP-156](best-practices/BP-156-use-eventing-when-data-creation-is-server-triggered-or-must-carry-incident-specific-context.md) | Use eventing when data creation is server-triggered or must carry incident-specific context | 7.5.7, 7.5.6 | SHOULD | manual |
| [BP-157](best-practices/BP-157-use-a-plain-array-variable-for-the-simplest-list-of-values-case.md) | Use a plain array Variable for the simplest list-of-values case | 7.6 | SHOULD | manual |
| [BP-158](best-practices/BP-158-expose-array-entries-as-sub-variables-when-individual-referencing-or-metadata-is-needed.md) | Expose array entries as sub-variables when individual referencing or metadata is needed | 7.6 | SHOULD | manual |
| [BP-159](best-practices/BP-159-expose-a-dynamic-order-independent-set-of-complex-things-as-referenced-objects.md) | Expose a dynamic, order-independent set of complex things as referenced Objects | 7.6 | SHOULD | manual |
| [BP-160](best-practices/BP-160-use-the-orderedobjecttype-orderedlisttype-pattern-when-order-is-meaningful.md) | Use the OrderedObjectType/OrderedListType pattern when order is meaningful | 7.6 | SHOULD | manual |
| [BP-161](best-practices/BP-161-general-objecttype-design-considerations-extend-to-eventtypes.md) | General ObjectType design considerations extend to EventTypes | 7.7 | INFORMATIVE | manual |
| [BP-162](best-practices/BP-162-prefer-interfaces-as-the-extensibility-mechanism-across-an-eventtype-hierarchy.md) | Prefer Interfaces as the extensibility mechanism across an EventType hierarchy | 7.7 | SHOULD | manual |
| [BP-163](best-practices/BP-163-define-a-new-referencetype-only-for-a-semantic-not-already-covered.md) | Define a new ReferenceType only for a semantic not already covered | 7.8 | SHOULD | manual |
| [BP-164](best-practices/BP-164-represent-a-typedefinition-s-key-structural-aspects-with-hierarchical-references.md) | Represent a TypeDefinition's key structural aspects with hierarchical References | 7.8 | SHOULD | manual |
| [BP-165](best-practices/BP-165-use-an-existing-semantically-appropriate-datatype-rather-than-reinventing-one.md) | Use an existing, semantically-appropriate DataType rather than reinventing one | 7.9 | SHOULD | manual |
| [BP-166](best-practices/BP-166-use-the-least-complex-adequate-datatype.md) | Use the least complex adequate DataType | 7.9 | SHOULD | manual |
| [BP-167](best-practices/BP-167-consider-combining-multiple-related-booleans-into-an-optionset.md) | Consider combining multiple related Booleans into an OptionSet | 7.9 | MAY | manual |
| [BP-168](best-practices/BP-168-explicitly-declare-subtype-permission-when-a-structured-field-s-datatype-must-allow-subtypes.md) | Explicitly declare subtype-permission when a structured field's DataType must allow subtypes | 7.9 | MUST | manual |
| [BP-169](best-practices/BP-169-a-structured-datatype-cannot-combine-allows-subtypes-with-has-optional-fields.md) | A Structured DataType cannot combine "allows subtypes" with "has optional fields" | 7.9 | MUST NOT | manual |
| [BP-170](best-practices/BP-170-four-documented-workarounds-exist-when-both-subtype-flexibility-and-optional-fields-are-needed.md) | Four documented workarounds exist when both subtype-flexibility and optional fields are needed | 7.9 | SHOULD | manual |
| [BP-171](best-practices/BP-171-avoid-structured-datatypes-needing-extension-unless-every-usage-site-allows-it-or-an-extension.md) | Avoid structured DataTypes needing extension unless every usage site allows it or an extension mechanism is built in | 7.9 | SHOULD | manual |
| [BP-172](best-practices/BP-172-a-structure-is-limited-to-32-optional-fields.md) | A Structure is limited to 32 optional fields | 7.9 | MUST NOT | manual |
| [BP-173](best-practices/BP-173-avoid-recursive-structures-when-possible.md) | Avoid recursive structures when possible | 7.10 | SHOULD | manual |
| [BP-174](best-practices/BP-174-a-self-referencing-objecttype-variabletype-member-must-use-optional-optionalplaceholder-never.md) | A self-referencing ObjectType/VariableType member must use Optional/OptionalPlaceholder, never Mandatory | 7.10 | MUST NOT | manual |
| [BP-175](best-practices/BP-175-a-self-containing-structured-datatype-must-provide-a-recursion-termination-mechanism.md) | A self-containing Structured DataType must provide a recursion-termination mechanism | 7.10 | MUST | manual |
| [BP-176](best-practices/BP-176-standardized-server-bound-variables-must-be-marked-non-static-in-namespacemetadata.md) | Standardized server-bound Variables must be marked non-static in NamespaceMetadata | 7.11 | MUST | manual |
| [BP-177](best-practices/BP-177-avoid-a-generic-other-enumeration-value-as-an-extensibility-escape-hatch.md) | Avoid a generic "Other" enumeration value as an extensibility escape hatch | 7.12.2 | SHOULD NOT | manual |
| [BP-178](best-practices/BP-178-use-multistate-variabletypes-when-per-instance-future-value-set-extensibility-is-anticipated.md) | Use MultiState VariableTypes when per-instance/future value-set extensibility is anticipated | 7.12.3 | SHOULD | manual |
| [BP-179](best-practices/BP-179-use-the-nodeid-to-abstract-objecttype-pattern-when-enumeration-values-need-their-own-extensible.md) | Use the NodeId-to-abstract-ObjectType pattern when enumeration values need their own extensible specialization hierarchy | 7.12.4 | SHOULD | manual |
| [BP-180](best-practices/BP-180-use-a-statemachine-only-when-its-additional-semantics-are-genuinely-needed.md) | Use a StateMachine only when its additional semantics are genuinely needed | 7.12.5 | SHOULD | manual |
| [BP-181](best-practices/BP-181-server-implementations-should-avoid-proliferating-namespaces.md) | Server implementations should avoid proliferating Namespaces | 7.13 | SHOULD | manual |
| [BP-182](best-practices/BP-182-let-the-server-assign-nodeids-for-client-created-nodes.md) | Let the Server assign NodeIds for Client-created Nodes | 7.13 | SHOULD | manual |
| [BP-183](best-practices/BP-183-avoid-relying-on-the-generic-nodemanagement-services-for-configuration-driven-addressspace-changes.md) | Avoid relying on the generic NodeManagement Services for configuration-driven AddressSpace changes | 8.2 | SHOULD NOT | manual |
| [BP-184](best-practices/BP-184-avoid-implying-addressspace-changes-via-writing-a-count-number-variable.md) | Avoid implying AddressSpace changes via writing a count/number Variable | 8.3 | SHOULD NOT | manual |
| [BP-185](best-practices/BP-185-exception-writing-an-array-may-create-delete-its-exposed-sub-variable-entries.md) | Exception: writing an array may create/delete its exposed sub-variable entries | 8.3 | MAY | manual |
| [BP-186](best-practices/BP-186-prefer-methods-for-addressspace-configuration-changes-needing-flexibility.md) | Prefer Methods for AddressSpace configuration changes needing flexibility | 8.1, 8.4 | SHOULD | manual |
| [BP-187](best-practices/BP-187-use-a-class-method-on-the-typedefinition-the-0-create-pattern-for-objecttype-instance-construction.md) | Use a class Method on the TypeDefinition (the "0:Create" pattern) for ObjectType instance construction | 8.4.1 | MAY | manual |
| [BP-188](best-practices/BP-188-instance-deletion-may-be-an-instance-method-or-a-class-method-taking-an-identifier.md) | Instance deletion may be an instance Method or a class Method taking an identifier | 8.4.1 | MAY | manual |
| [BP-189](best-practices/BP-189-prefer-methods-on-the-owning-parent-instance-over-purely-type-level-methods.md) | Prefer Methods on the owning parent instance over purely type-level Methods | 8.4.2 | SHOULD | manual |
| [BP-190](best-practices/BP-190-use-filetransfer-for-large-atomic-multi-node-configuration-deployments.md) | Use FileTransfer for large, atomic, multi-Node configuration deployments | 8.4.3 | MAY | manual |
| [BP-191](best-practices/BP-191-package-referenced-dictionary-entries-as-a-separate-flat-uanodeset.md) | Package referenced Dictionary Entries as a separate, flat UANodeSet | 9.2 | SHOULD | manual |
| [BP-192](best-practices/BP-192-implementers-combining-models-must-merge-the-respective-dictionary-entry-uanodesets.md) | Implementers combining models must merge the respective Dictionary-Entry UANodeSets | 9.2 | INFORMATIVE | manual |
| [BP-193](best-practices/BP-193-reuse-existing-companion-specifications-to-maximize-interoperability.md) | Reuse existing Companion Specifications to maximize interoperability | 10.1 | SHOULD | manual |
| [BP-194](best-practices/BP-194-prefer-composition-over-inheritance-when-depending-on-another-companion-specification-s-types.md) | Prefer composition over inheritance when depending on another Companion Specification's types | 10.2 | SHOULD | manual |
| [BP-195](best-practices/BP-195-new-instancedeclarations-may-always-be-added-optionally-anywhere-in-the-structure.md) | New InstanceDeclarations may always be added optionally, anywhere in the structure | 11.2.1 | MAY | manual |
| [BP-196](best-practices/BP-196-mandatory-additions-require-a-subtype-or-an-optional-plus-conformance-unit-pattern.md) | Mandatory additions require a Subtype or an Optional-plus-Conformance-Unit pattern | 11.2.1 | MUST | manual |
| [BP-197](best-practices/BP-197-define-an-interface-addin-first-when-adding-a-related-set-across-multiple-typedefinitions.md) | Define an Interface/AddIn first when adding a related set across multiple TypeDefinitions | 11.2.2 | SHOULD | manual |
| [BP-198](best-practices/BP-198-remediation-for-needing-new-enumeration-values-deprecate-and-replace-ideally-with-an-extensible.md) | Remediation for needing new Enumeration values: deprecate-and-replace (ideally with an extensible pattern instead) | 11.2.3 | SHOULD | manual |
| [BP-199](best-practices/BP-199-remediation-for-needing-new-structure-fields-subtype-conditioned-on-subtype-permission-at-every.md) | Remediation for needing new Structure fields: Subtype, conditioned on subtype-permission at every usage site | 11.2.4 | MUST NOT | manual |
| [BP-200](best-practices/BP-200-remediation-for-a-numeric-optionset-needing-new-bits-new-parallel-or-superseding-datatype.md) | Remediation for a numeric OptionSet needing new bits: new parallel or superseding DataType | 11.2.5 | MUST NOT | manual |
| [BP-201](best-practices/BP-201-remediation-for-an-optionset-datatype-based-optionset-needing-new-bits-subtype-same-length-or-the.md) | Remediation for an OptionSet-DataType-based OptionSet needing new bits: Subtype (same length) or the numeric-style alternatives | 11.2.5 | MUST NOT | manual |
| [BP-202](best-practices/BP-202-a-problematic-typedefinition-may-be-deprecated-and-replaced-in-place-with-usages-updated-and-a.md) | A problematic TypeDefinition may be deprecated and replaced in-place, with usages updated and a numbered successor name | 11.2.6 | MAY | manual |
| [BP-203](best-practices/BP-203-a-required-breaking-change-must-use-a-new-namespaceuri.md) | A required breaking change must use a new NamespaceUri | 11.3 | MUST | manual |
| [BP-204](best-practices/BP-204-construct-the-new-namespaceuri-by-appending-a-major-version-suffix.md) | Construct the new NamespaceUri by appending a major-version suffix | 11.3 | SHOULD | manual |
| [BP-205](best-practices/BP-205-a-new-breaking-change-namespace-requires-new-conformance-units-and-profiles.md) | A new breaking-change Namespace requires new Conformance Units and Profiles | 11.3 | MUST | manual |
| [BP-206](best-practices/BP-206-a-conformance-unit-should-describe-one-individually-testable-unit-of-functionality.md) | A Conformance Unit should describe one individually testable unit of functionality | 12.1 | SHOULD | manual |
| [BP-207](best-practices/BP-207-define-both-content-oriented-and-behavior-oriented-conformance-units.md) | Define both content-oriented and behavior-oriented Conformance Units | 12.1 | SHOULD | manual |
| [BP-208](best-practices/BP-208-give-an-important-optional-feature-its-own-conformance-unit-group-related-ones-fold-the-rest-into-a.md) | Give an important optional feature its own Conformance Unit; group related ones; fold the rest into a broader unit | 12.1 | SHOULD | manual |
| [BP-209](best-practices/BP-209-give-optional-nodes-their-own-conformance-units-to-simplify-testing-and-support-reuse-by-derived.md) | Give optional Nodes their own Conformance Units to simplify testing and support reuse by derived models | 12.1 | SHOULD | manual |
| [BP-210](best-practices/BP-210-state-explicitly-whether-an-instance-level-requirement-means-at-least-one-or-all.md) | State explicitly whether an instance-level requirement means "at least one" or "all" | 12.1 | SHOULD | manual |
| [BP-211](best-practices/BP-211-phrase-instance-related-requirements-in-terms-of-product-configurability.md) | Phrase instance-related requirements in terms of product configurability | 12.1 | SHOULD | manual |
| [BP-212](best-practices/BP-212-domain-specific-companion-specifications-should-define-at-least-one-application-profile.md) | Domain-specific Companion Specifications should define at least one application Profile | 12.2 | SHOULD | manual |
| [BP-213](best-practices/BP-213-generic-reusable-companion-specifications-should-expose-facets-rather-than-only-full-profiles.md) | Generic/reusable Companion Specifications should expose Facets rather than only full Profiles | 12.2 | SHOULD | manual |
| [BP-214](best-practices/BP-214-include-the-namespaceindex-prefix-when-citing-a-browsename-in-companion-specification-only-prose.md) | Include the NamespaceIndex prefix when citing a BrowseName in Companion-Specification-only prose | 13.2 | SHOULD | manual |
| [BP-215](best-practices/BP-215-omit-the-namespaceindex-when-browsename-text-appears-inside-uanodeset-content.md) | Omit the NamespaceIndex when BrowseName text appears inside UANodeSet content | 13.3 | SHOULD | manual |
| [BP-216](best-practices/BP-216-in-rare-foreseeable-collision-cases-reference-the-namespace-by-uri-not-by-index.md) | In rare foreseeable-collision cases, reference the Namespace by URI, not by index | 13.3 | SHOULD | manual |
| [BP-217](best-practices/BP-217-the-isdeprecated-referencetype-marks-a-node-as-deprecated-while-keeping-it-available.md) | The IsDeprecated ReferenceType marks a Node as deprecated while keeping it available | 14.2 | INFORMATIVE | manual |
| [BP-218](best-practices/BP-218-clients-should-default-to-new-nodes-and-use-deprecated-ones-only-as-a-compatibility-fallback.md) | Clients should default to new Nodes and use deprecated ones only as a compatibility fallback | 14.2 | SHOULD NOT | manual |
| [BP-219](best-practices/BP-219-a-released-companion-specification-namespace-must-not-contain-breaking-changes.md) | A released Companion Specification Namespace must not contain breaking changes | 14.3.1 | MUST NOT | manual |
| [BP-220](best-practices/BP-220-prefer-a-new-namespaceuri-over-deprecation-plus-new-mechanism-except-for-small-changes.md) | Prefer a new NamespaceUri over deprecation-plus-new-mechanism, except for small changes | 14.3.1 | SHOULD | manual |
| [BP-221](best-practices/BP-221-a-mandatory-deprecated-node-still-requires-permanent-server-support.md) | A Mandatory deprecated Node still requires permanent Server support | 14.3.1 | MUST | manual |
| [BP-222](best-practices/BP-222-deprecation-may-be-used-deliberately-to-limit-the-number-of-new-namespaces-minted-over-time.md) | Deprecation may be used deliberately to limit the number of new Namespaces minted over time | 14.3.1 | MAY | manual |
| [BP-223](best-practices/BP-223-represent-a-deprecation-marker-as-a-namespacemetadata-child-object-named-by-spec-version.md) | Represent a deprecation marker as a NamespaceMetadata child Object named by spec+version | 14.3.2 | SHOULD | manual |
| [BP-224](best-practices/BP-224-use-or-subtype-the-appropriate-base-auditevent-type-for-auditable-actions.md) | Use (or subtype) the appropriate base AuditEvent type for auditable actions | 15 | SHOULD | manual |
| [BP-225](best-practices/BP-225-subtyping-a-base-auditevent-type-enables-more-precise-categorization-filtering.md) | Subtyping a base AuditEvent type enables more precise categorization/filtering | 15 | MAY | manual |
| [BP-226](best-practices/BP-226-do-not-add-new-fields-to-an-auditevent-subtype.md) | Do not add new fields to an AuditEvent Subtype | 15 | SHOULD NOT | manual |

## Supplement - explicit PropertyType prohibition

| Rule | Name | Source clauses | Wording | Candidate group |
|---|---|---|---|---|
| [P5-001](supplement/P5-001-do-not-subtype-propertytype.md) | Do not subtype PropertyType | 7.3 | MUST NOT | subtypes |
