# OPC UA companion prose: corpus analysis

## Coverage

The corpus is the [OPC UA Online Reference index](https://reference.opcfoundation.org/)
as retrieved on 20 November 2026. Each of its 151 direct specification links
resolved to a current edition with a Markdown export. All 151 exports were
downloaded and processed (17,419,563 bytes). Older editions linked from the
landing pages' version histories were not included. Neither were NodeSets,
separately linked files, or external standards cited by the specifications.

The analysis uses 114 documents outside `OPC-10000-*` as the companion-led
group and 37 documents in that series as the comparison group. This split
follows document numbers, not a claim about a document's function. It puts
Devices (Part 100), the UAFX parts and other foundational models in the
comparison group, and includes the modelling best-practices document
(OPC 11030) in the companion-led group.

Corpus-wide counts were computed from the downloads. Close reading of
selected sections explains the counts; the whole corpus was not individually
annotated. The observations below describe a shared register, not a single
author or a set of mandatory OPC Foundation editorial rules.

## What the counts show

| Prose group | Blocks | Median words per block | 25th to 75th percentile | One sentence | Two sentences |
| --- | ---: | ---: | ---: | ---: | ---: |
| Outside the 10000 series | 22,449 | 21 | 14-37 | 53% | 27% |
| Outside the 10000 series, Scope text | 336 | 43 | 25-58 | 38% | 25% |
| Outside the 10000 series, text containing `shall`, `should` or `may` | 4,012 | 38 | 24-61 | 26% | 32% |
| 10000 series | 12,783 | 26 | 15-46 | 45% | 27% |

Outside the 10000 series, the median sentence was 14 words, with the middle
half at 10-20 words. The median of each document's median block length was
23 words. Removing the Mining and Plastics and Rubber Machinery families
left 71 documents: the median block went from 21 to 22 words and the
one-sentence share remained 53% when rounded. The terse reference cadence is
not just an artifact of those two multipart families.

In the broad companion-led group there were about 25 commas and 7 opening
parentheses per 1,000 words, compared with about 1.5 colons and 0.4 semicolons
in the selected prose. Em dashes and direct address were rare. `Shall` occurred
about 4.5 times per 1,000 words outside the 10000 series, versus about 7.9 in the
comparison group. These are counts of words and marks, not of grammatical
functions or requirements. The greater length of blocks containing one of
the selected modals does not imply that obligations should be padded: those
blocks often need related conditions, alternative cases or explanations.

**Method.** The publisher describes the [Markdown format](https://reference.opcfoundation.org/ai-help)
as a plain-prose export with cross-references reduced to display text. A
heuristic used blank lines to identify blocks, tracked numbered sections,
and kept single-line blocks that looked like complete prose sentences.
It excluded recognized reference and terminology sections, metadata, notes,
headings, numbered or bulleted items, captions, and multiline blocks such
as CSV tables. It found eligible prose in every export. Sentence boundaries
were estimated from terminal punctuation, with common abbreviations,
decimals and URLs protected. The filter can miss real prose, colons
introducing lists, or export-specific boundaries; shared boilerplate can
remain. The measurements describe this filtered text, not all sentences in
the specifications. Use them as calibration, not editing limits.

## Close reading by prose function

| Function | What to carry into new prose | Primary sources |
| --- | --- | --- |
| Scope and overview | Lead with what the model represents. Expand on the purpose, context or scope boundary only as far as the distinction needs. A multi-sentence paragraph works for a single explanation, such as why distinct systems need separate configurations or how two aspects of a drive model relate. | [Machine Vision, Scope](https://reference.opcfoundation.org/specs/OPC-40100-1/1); [Machine Vision, ConfigurationManagementType overview](https://reference.opcfoundation.org/specs/OPC-40100-1/7.2.1); [PROFINET Drives, model overview](https://reference.opcfoundation.org/specs/OPC-30145/6.1) |
| Type and member descriptions | Lead with the exact entity and its function. Repeat the defined name if the next sentence changes which type, instance, or property is in view. A sentence locating an inherited definition can sit beside a short sentence on its local use. | [PA-DIM, IAdministrationType](https://reference.opcfoundation.org/specs/OPC-30081/7.1.1); [Extrusion Line, ConfigurationParameters](https://reference.opcfoundation.org/specs/OPC-40084-2/6.7); [Extrusion Line, MaterialList](https://reference.opcfoundation.org/specs/OPC-40084-2/6.8) |
| Condition and exception | Put the limitation next to its effect. A single paragraph can carry a main rule and its dependent cases; a new paragraph marks a separate rule or change of subject. Keep a recommendation visibly distinct from a requirement. | [PA-DIM, General rules](https://reference.opcfoundation.org/specs/OPC-30081/6.3); [Extrusion Line, Components](https://reference.opcfoundation.org/specs/OPC-40084-2/6.3) |
| Explanation of a sequence | Develop the behavior over several sentences when cause, progression and observable result belong together. Break at the change of phase, not after every action automatically. | [LADS, Program and result lifetime](https://reference.opcfoundation.org/specs/OPC-30500-1/4.1.4) |
| Core contrast | The third-person, actor-led voice carries over. Compound service behavior can require several adjacent cases and repeated Client and Server names. Do not copy the core's greater density into a simple domain member description. | [OPC UA Part 4, Call description](https://reference.opcfoundation.org/specs/OPC-10000-4/5.12.2.1) |

The examples are evidence for the prose choices, not clauses to reuse.
Keep deliberate capitalization of defined terms and identifiers. Correct
local mechanical errors such as a missing article, a colon separating the
subject from its verb, an erroneous plural, or a repeated note label. Do not
imitate marketing copy or the quirks of the export.

## Calibration for longer passages

These are original examples. They do not define OPC UA behavior.

**Overview.** Keep the purpose and the relation between the two views together.
Start a new paragraph when the subject changes to retention.

> The inspection model provides access to the current inspection and to
> completed results. The current inspection exposes the active step and the
> elapsed time. Completed results remain available independently of the
> current inspection.
>
> The Server sets the retention period for completed results. A Client can
> read the retention period before requesting an older result.

**Behavior.** Keep the specific exception with the permission it limits.
Start a new paragraph for the effect on another request.

> A Client may cancel an inspection before it starts. If the inspection is
> in progress, the Server shall reject the cancellation and leave the
> inspection running.
>
> If a Client requests a result during the inspection, the Server shall
> return the most recent completed result. If no completed result is
> available, the Server shall return Bad_NoData.
