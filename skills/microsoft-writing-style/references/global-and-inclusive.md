# Global, inclusive, and accessible writing

Write so a reader in another country, reading in a second language, through
machine translation, or with a screen reader, gets the same meaning as a
native speaker reading the original.

## Global English

**Sentences.**

- Keep sentences short and in subject-verb-object order.
- If a sentence needs more than a few commas, split it into shorter
  sentences.
- Link at most two clauses. Three is the absolute limit.
- Keep a modifier next to the word it modifies.
- Write complete sentences. Limit fragments to labels and headings.

**Small words that carry meaning.** Keep words that native speakers drop but
translators need:

- *that* and *who* introducing a clause: *Verify that the key is valid.*
- Articles: *Select the file* rather than *Select file*.
- A verb in a short label or message: *Access is denied* rather than *Access
  denied*.

**Modifier stacks.** Break up chains of nouns used as adjectives. *Server
certificate revocation list update interval* becomes *how often the server
updates its certificate revocation list*.

**Idioms and culture.** Remove idioms, metaphors, slang, sports and pop-culture
references, humor that depends on wordplay, and region-specific examples.

| Instead of | Use |
|---|---|
| out of the box | by default, built in |
| hit the ground running | start quickly |
| ballpark figure | estimate |
| a slam dunk | certain |
| on the fly | while running, dynamically |
| under the hood | internally |

**Dates, times, and places.**

- Write dates as *month day, year* with the month spelled out.
- Name months or quarters, not seasons. If a season is unavoidable, name the
  hemisphere.
- State the time zone whenever it matters.
- Give the country or region with a place name.

**Examples.** Use names, places, currencies, phone numbers, and addresses from
a mix of regions, or use clearly fictitious ones. Avoid region-specific
standards, holidays, and measurement systems as defaults; when units matter,
give both metric and imperial.

## Bias-free language

**Gender.**

- Don't use gendered pronouns for a generic person. Rewrite with *you*, a
  plural, an article, or a role; use singular *they* as a fallback.
- Use gender-neutral terms: *chair*, *humanity*, *staff* (verb), *sales
  representative*, *synthetic* or *artificial*, *workforce*.

**Loaded technical terms.** Use neutral terms.

| Instead of | Use |
|---|---|
| master/slave | primary/secondary, primary/replica, primary/subordinate, leader/follower |
| whitelist/blacklist | allow list/block list (verb: allow/block) |
| DMZ, demilitarized zone | perimeter network |
| hang | stop responding |
| abort (outside an API name) | end (connections), close (apps), stop (hardware), cancel (requests, processes) |
| black hat hacker | malicious hacker, unauthorized user |
| white hat hacker | security expert |
| native language (for computers) | machine language, host language |

**People and cultures.**

- Use diverse names, roles, and situations in examples. Avoid stereotypes and
  assumptions about wealth, culture, or location.
- Avoid generalizations about any group, including positive ones.
- Don't use culturally appropriative slang such as *spirit animal*.
- Capitalize names of racial, ethnic, and Indigenous groups (*Black*,
  *Hispanic*, *Indigenous Peoples*); lowercase *white* and *multiracial*.
- Don't use profanity or derogatory terms.
- Use neutral, parallel geography. Don't take sides on disputed regions, and
  use the same kind of label (country, region, city) for every place in a list.

**Disability.**

- Mention a disability only when it's relevant.
- Default to people-first language: *person who is blind*, *person with limited
  mobility*. Use identity-first language (*blind person*, *autistic person*)
  when the community or individual prefers it.
- Avoid words that imply pity or limitation: *suffers from*, *afflicted with*,
  *victim of*, *confined to a wheelchair*, *handicapped*.
- Avoid using disability terms as metaphors: *blind to*, *lame*, *crippled*,
  *crazy*, *insane*, *dumb*.

## Militaristic and violent language

Avoid terms of violence and military action unless the text is about physical
combat. This matters most in security writing.

| Instead of | Use |
|---|---|
| combat, fight, eliminate | address, protect against, respond to |
| kill chain, cyber kill chain | cyberattack chain |
| adversary, unqualified attacker | threat actor, cyberattacker, bad actor |
| blast radius | impact |
| defense-in-depth approach | multilayered approach, defense-in-depth security |
| guard, ward | protect, safeguard, defend |
| locked down | secured |
| fortifications, first line of defense, frontlines | security, protection, defense |
| frontline analysts | security teams, security analysts, defenders |
| external attack surface (for a reader's exposure) | vulnerabilities, points of access, external exposure |

- Qualify *attack* and *threat* with the kind: *malware attack*, *identity
  threat*. Without a qualifier, write *cyberattack* or *cyberthreat* as one
  word.
- Use *defend* and *defenses* only when the same sentence makes the security
  context clear.
- Write *threat intelligence* in full, never *threat intel*.
- Never use *air cover*, *bomb* (including *email bomb* and *time bomb*),
  *enemy* or *enemy lines*, *go on the offensive*, *invade* or *invasion*,
  *missile*, *torpedo*, *nuke* or *go nuclear*, *strike*, or *troops*.

## Accessible wording

These rules are about words, not layout.

- Use one main idea and, in procedures, one verb per sentence.
- Keep list items and steps grammatically parallel.
- Spell out *and*, *plus*, *about*, and *at* rather than using symbols.
- Write link text that says where the link goes. Avoid *click here*, *more*,
  and *this link*.
- Don't rely on position, color, shape, or sound alone: avoid *the button on
  the left*, *the red value*, *above*, and *below*. Name the item or say
  *preceding* and *following*.
- Introduce a table or figure with a sentence that says what it shows.
- Describe actions in input-neutral terms (*select*, *open*, *enter*) rather
  than device-specific ones (*click*, *tap*, *press*). See
  [developer-content.md](developer-content.md#procedures).
- Write meaningful alternative text for images: what the image conveys, not
  what it looks like.
