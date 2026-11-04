# Grammar

## Verbs

**Tense.** Use present tense. Describe what the system does, not what it will
do: *The service retries the request* rather than *The service will retry the
request*. Use past or future tense only when time actually matters.

**Mood.** Keep one mood per sentence.

| Mood | Use for | Example |
|---|---|---|
| Indicative | Facts, explanations, descriptions (most content) | The cache holds up to 512 entries. |
| Imperative | Instructions, procedures, required actions | Set the timeout, and then restart the service. |
| Subjunctive | Wishes and hypotheses. Rewrite into indicative or imperative | ~~We suggest that the value be set~~ → Set the value. |

**Voice.** Prefer active voice: the subject performs the action. Use passive
voice deliberately to:

- Keep blame off the reader (*The connection was closed*).
- Avoid an awkward construction.
- Emphasize the receiver of the action, which is common in technical
  descriptions: *When the caller commits, the transaction is persisted.*

**Agreement.**

| Subject | Verb | Example |
|---|---|---|
| A group of things (*a set of*, *a variety of*) | Singular | A set of handlers is registered at startup. |
| Two subjects joined by *and* | Plural | The client and the server negotiate a version. |
| Two singular subjects joined by *or* | Singular | The key or the certificate is required. |
| A singular and a plural joined by *or* | Agrees with the nearer subject | The tokens or the key is required. |

**Recommendations and requirements.** Prefer the imperative for required
actions and *we recommend* for optional ones. Use *must* only for a required
action and *should* only for a recommended, optional action. Use *might* or
*can* for possibility, never *should*. Avoid *it is recommended*. When a
document follows a normative-keyword convention (for example, uppercase
requirement keywords in a specification), that convention governs those words.

## Person

- Address the reader as *you*, stated or implied. Second person keeps the text
  direct and reduces passive voice.
- Use *we* sparingly. *We recommend* is acceptable when it avoids *it is
  recommended*, but rewriting around it is better. Keep the focus on the reader,
  not the author or vendor.
- Use first-person singular (*I*, *my*) only for labels where the reader speaks,
  such as *Remember my choice*.
- For content generated or decided by software on the reader's behalf, say so
  plainly (*suggested for you*) and use wording that signals the result may be
  imperfect.

## Nouns and pronouns

**Proper vs. common nouns.** Capitalize unique names: people, organizations,
products, published works, and managed standards. Lowercase technology
concepts, categories, devices, and features: *cloud computing*, *message
broker*, *open source*. Capitalize a technology term only when the industry
consistently does or when it distinguishes a named product from the generic
concept. When unsure, lowercase.

**Plurals.**

- Abbreviation: add *s*, even if it ends in *s*: *APIs*, *DBMSs*.
- Abbreviation that already stands for a plural: no *s*.
- Single letter: apostrophe plus *s*: *x's*.
- Numbers: add *s*: *the 1990s*.
- Use the plural instead of *(s)*: *Wait for the jobs to finish*, not *job(s)*.

**Gender.** Don't use gendered pronouns for a generic person. Rewrite with
*you*, a plural, an article (*the document*), or the person's role (*the
administrator*). If none works, use singular *they*. Avoid *he/she* and *s/he*.
For a real person, use the pronouns that person uses.

**Collective nouns.** A collective noun takes a singular pronoun: *The
committee published its report.* Use a plural pronoun only when the emphasis is
on the individual members.

## Modifiers

- Place a modifier next to what it modifies. *Only* is the most common
  offender: *Only the selected entries are deleted* differs from *The selected
  entries are only deleted*.
- Avoid dangling modifiers. *After installing the package, the service starts*
  implies the service installed the package. Rewrite: *After you install the
  package, the service starts.*
- Short, active sentences prevent most modifier problems.

## Words ending in *-ing* and *-ed*

An *-ing* word can be a verb, noun, or adjective, and an *-ed* word can be a
modifier or part of a verb. Make the role obvious.

- Ambiguous: *Meeting requirements*. Clear: *Requirements for the meeting* or
  *How to meet the requirements*.
- Add an article, a form of *be*, or *that* to resolve an *-ed* word: *Configure
  limits that are based on available storage.*
- Or split the sentence: *Configure limits for the backup. Base them on
  available storage.*

## Prepositions

- Avoid chaining more than two prepositional phrases. *The value of the field
  of the header of the message* becomes *the message header's field value* or a
  rewritten sentence.
- Ending a sentence with a preposition is fine when it reads naturally: *Choose
  the queue that you want to send to.*

## Sentence structure

- Use standard subject-verb-object order.
- Keep sentences short. If a sentence has more than two commas, rewrite it.
- Link at most two clauses with *and*, *or*, or *but*. Split longer chains.
- Use a complete sentence where meaning depends on it. Limit fragments to
  headings, labels, and quick asides.
- Keep parallel items parallel: same grammatical form, same starting part of
  speech.
