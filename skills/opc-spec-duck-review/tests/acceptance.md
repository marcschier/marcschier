# Comprehension review acceptance scenarios

Use synthetic specifications and authorized scratch output. Record actual
agent transcripts, per-unit ledgers, tool use, and diffs when executing these
scenarios; this list alone is not evidence that they passed.

| Scenario | Expected behavior |
|---|---|
| Informative subsection decision | Connecting technology context would be removed by concision rules; the editor offers the user an informative subsection with examples and diagrams, preserves the original pending the choice, and keeps normative facts normative |
| Informative reader flow | An approved informative subsection supplies context for a later requirement; the specification reader reads it forward for the unchanged specification audience without guide knowledge, flags missing transitions and checks examples and diagrams |
| Informative publisher conflict | The supported authoring contract cannot mark the selected subsection informative; report the conflict and seek a decision rather than deleting the explanation or inventing markup |
| Companion guide | Useful implementation rationale is removed during revision; the editor reads the shared guide workflow and retains it in implementer-guide.md beside spec.md with exact ledger destinations, while normative facts remain in normative homes |
| Guide reader isolation | A guide explains something absent from the specification; the specification reader does not receive it, while a separate fresh developer reader reviews the guide, examples, diagrams and referenced clauses without earlier findings |
| Guide branch blocked | Guide writing permission, the shared guide reference, or a guide writing companion is missing; report the blocked branch and proposed retention destinations without edits or claiming guide acceptance, and continue only independent work |
| Guide final audit | Normative content is intact but a useful removed example has only a proposed guide destination; leave guide retention incomplete until the final guide contains it and a fresh complete developer reading accepts the unchanged edition |
| Final audit after agreement | Fresh reader and editor agree and validation passes, but the baseline contains an omitted mapping exception; editor and coordinator audit against the complete fixed inventory and withhold acceptance until it is accounted for |
| Final audit isolation and correction | Editor and coordinator keep baseline and audit history from the fresh reader; an authorized restoration triggers applicable validation, a new fresh full pass and another final audit |
| Missing final audit evidence | The resolved review package lacks the final audit section or baseline evidence is unavailable; report the dependency or audit gap and withhold completion rather than substituting reader acceptance |
| Findings-only final audit | Proposed wording drops an error condition; compare the proposal against its baseline, record the loss and intended home without edits or writing regeneration, and do not claim publication evidence |
| Shared authority and fresh reader | Both roles independently read the integrated prose guidance, per-rule examples, safeguards and concise structure from the resolved review package; give the fresh reader no prior findings or editor history or domain knowledge from examples |
| Editor style opt-in | The coordinator asks once before authorized prose edits and routes the user's opt-in to the editor only; the editor uses the additional skill across passes without changing the reader's instructions or dropping an existing cleanup pass |
| Optional style unselected | Findings-only review, declined or unanswered opt-in, or an older review package without the option does not block the review; continue with the integrated guidance and report when the optional pass requires an updated review package |
| Missing authority or safeguards | An integrated prose reference or the resolved review package is unavailable to either role; stop before style review, proposal or writing, report the missing path and do not substitute another style skill |
| Conflicting example | An example strengthens descriptive text into a requirement or contradicts the guidance; rules and preservation safeguards take precedence and the editor requests a technical decision |
| Generated region | A reader requests relocating a requirement to a kept table inside an outer generated region; the editor proposes a persistent authored home and performs no writing regeneration without authorization |
| Semantic preservation | A rewrite would lose a role distinction, negative error contract, mapping omission or provisional release disclosure; both roles flag the loss and require equivalent published treatment |
| Cross-part and tables | A moved table has inbound references from a sibling spec and contains ReferenceType attributes and encoding facts; inventory references and all table facts, report out-of-scope dependencies and never treat a green build as semantic proof |
| Proposals and retirement | An unnamed result code is proposed and one upstream safeguard is later corrected; keep the proposal outside normative text, persist its flag and require a matching regression before retiring only that safeguard |
| Ambiguous selection | Discover two manifests, ask which specs and then source-only or source plus HTML; obtain edit permission independently |
| Non-OPC prerequisite | A first sentence relies on an unexplained non-OPC domain concept; the reader flags it rather than researching the domain to fill the gap |
| Prior OPC UA part | Part 2 relies on the agreed Part 1 definition; the reader uses that prerequisite without demanding a duplicate introduction |
| First dependent use | Run the paired synthetic fixture below in fresh contexts; report the missing premises in the link-only edition and accept the same requirement with the orientation in place |
| First use outside prose | Move the fixture requirement to a table cell or an example tied to a figure label, and repeat in generated HTML; judge each in its actual reading order and locate the first dependent-use obstacle even if source or another representation explains it |
| Ordered batches | Split the link-only fixture before its exact definition; the reader logs the obstacle in the first batch and later records where it was clarified without erasing it. In the passing version, split just after the introduction; the same reader carries that introduction into the next batch without relearning it |
| Knowledge learned later | A later paragraph explains an earlier unexplained operation; the ledger retains the earlier obstacle and the editor considers moving the explanation |
| Full paragraph resolves sentence | An initially unclear sentence becomes clear in its paragraph; record both judgments and avoid a spurious rewrite for ordinary sentence-level ambiguity, but a later sentence still cannot supply a premise at first dependent use |
| Stable terms | A paragraph switches names for one concept; request a correction that preserves meaning and follows the integrated prose guidance |
| Redundant teaching | Repeated explanations add no condition or audience benefit; propose consolidation while preserving distinct normative obligations |
| Example or diagram | One concept needs an example, another has a distracting figure; record specific reader needs rather than demanding more figures everywhere |
| Coverage gap | A tool truncates a page or a figure cannot be opened; resume unread ranges or report incomplete coverage, never approve the whole batch |
| HTML loses content | Source is clear but generated HTML omits a field description; reader reports the HTML gap even after learning the concept from source |
| First pass dissatisfaction | Reader remains confused after a rewrite; editor revises again rather than vetoing the request, while preserving established requirements |
| Unsafe requested rewrite | Reader suggests replacing Optional with Mandatory; editor offers a faithful explanation or asks for a decision instead of changing the model requirement |
| Later challenge | A fresh reader demands an unnecessary repetition; editor requests located reasoning and can reject with evidence, but closes only with reader agreement or a user decision |
| Persistent dispute | Both roles maintain incompatible interpretations; user receives the wording, both arguments, evidence, and concrete choices for a tie-break |
| Fresh pass isolation | Every full pass starts with a new first-time reader that receives the agreed inputs, never prior findings or private explanations; the editor retains the finding history across passes |
| Final revision | A local re-review accepts the last edit; log it as local, not independent first-time acceptance, and require a complete fresh pass of the unchanged current edition |
| Read-only request | Editor returns recommendations without edits, composition, or a claim that unapplied fixes passed re-review |
| Missing tools or agents | Knowledge-base access, reference-site access, a writing companion, or independent contexts are unavailable; affected work stops with an explicit dependency |
| Limits or repeated cycle | Resource limit or repeated disagreement interrupts convergence; report incomplete work and ask for continuation or decision |
| Successful closure | Every current unit is covered, no unresolved issue remains, and both roles accept the same hashes; report comprehension acceptance only, not conformance certification |

## Synthetic fixture: first dependent use

The fixture uses `RunStamp`, a name outside the agreed prerequisites. Its
first mention in the contents list is incidental. At the first requirement,
show this version to the reader:

> The server shall set `RunStamp` when it starts a measurement run. See
> [RunStamp definition](#runstamp-definition).

**Expected:** Flag the requirement, not the contents entry. The requirement
does not establish that `RunStamp` is a timestamp field in the run record or
explain that clients use the recorded start time to align readings.
Even though the link works, record the missing premises at the requirement.
When the reader reaches the definition, record that location and that it
resolved the questions, without erasing the original obstacle.

In a fresh context, insert this immediately before the requirement or in an
earlier introduction. Leave the requirement and its link unchanged:

> Each measurement run has a run record. Its `RunStamp` field records the
> start time so clients can align readings to the start of the run.

**Expected:** Pass the first-use test. The reader can explain the field, its
place in the record, and its purpose before needing the detailed definition.

### RunStamp definition

Place this after the requirement in both editions:

> `RunStamp` is a field in the run record. It contains the UTC start time of
> the measurement run so clients can align readings to that time. The value
> has the OPC UA `DateTime` data type.
