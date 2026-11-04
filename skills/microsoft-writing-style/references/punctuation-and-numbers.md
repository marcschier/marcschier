# Punctuation and numbers

Heavy punctuation signals a complex sentence. When a sentence needs a
semicolon, several commas, or nested dashes, first try splitting it.

## Punctuation

**Periods.** End every sentence with a period, even a two-word sentence. Use one
space after a period, question mark, exclamation point, or colon.

**Commas.**

- Use the serial (Oxford) comma before the conjunction in a list of three or
  more: *keys, certificates, and tokens*.
- Use a comma after an introductory phrase: *After the handshake, the client
  sends the request.*
- Use a comma before a conjunction joining two independent clauses: *Open the
  file, and then read the header.*
- Omit the comma between the two verbs of a compound predicate: *The parser
  reads the header and then validates the body.*
- Use a comma between two adjectives only when their order could be reversed or
  joined with *and*: *a small, fast parser*.
- Surround the year in a full date within a sentence: *On May 4, 2026, the API
  changed.*

**Colons.** Within a sentence, prefer rephrasing, a comma, or an em dash over a
colon. When a colon is the clearest choice, lowercase the next word unless it's
a proper noun or starts a quotation. When a complete sentence introduces an
example, table, or code block, end it with a period.

**Semicolons.** Rewrite a sentence with a semicolon into two sentences or a
list. Keep a semicolon only between closely contrasting clauses or to separate
list items that already contain commas.

**Dashes, hyphens, and minus signs.** These four marks aren't interchangeable.

| Mark | Use for | Spacing |
|---|---|---|
| Em dash (—) | A break in thought or an inserted clarification. Use sparingly. | No spaces |
| En dash (–) | Ranges of numbers, pages, or dates (*2024–2026*); compound modifiers containing an open compound (*message queue–based design*) | No spaces |
| Hyphen (-) | Compound modifiers and some prefixes | No spaces |
| Minus sign (−) | Negative numbers and subtraction (*−12*, *12 − 3*) | Spaces around the operator |

**Hyphens.**

- Hyphenate a compound modifier before a noun when it would otherwise be
  ambiguous, when it includes a participle, or when it starts with a number or
  single letter: *built-in parser*, *well-defined schema*, *read-only property*,
  *64-bit value*, *y-axis label*.
- Leave a compound modifier unhyphenated after the noun: *The schema is well
  defined.*
- Leave *very* and *-ly* adverbs unhyphenated: *highly available service*.
- Spell out suspended compounds: *upper-left or lower-left corner* rather than
  *upper- or lower-left corner*.
- Write prefixes closed by default: *reenter*, *nonzero*, *preconfigure*,
  *subnet*, *multithreaded*. Add a hyphen when the closed form misleads
  (*re-create* vs. *recreate*, *re-sign*), when the stem is capitalized
  (*non-XML*), or when the closed form is hard to read (*non-native*).
- Apply a prefix to a word, not a phrase: *unrelated to security*, not
  *non-security related*.
- Hyphenate a compound noun when one part is abbreviated (*e-book*), except
  *email*.

**Apostrophes.** Form the possessive with *'s*, even after *s*: *the class's
members*. Plural nouns ending in *s* take only the apostrophe: *users'
passwords*. Use *its* for the possessive and *it's* only for *it is*. Avoid
possessives of acronyms and product names: *the IDE features* rather than *the
IDE's features*.

**Quotation marks.** Use double quotation marks, with single quotation marks for
a quotation inside a quotation. Place commas and periods inside the closing
mark; place other punctuation outside unless it belongs to the quoted text.
When a literal value appears in quotation marks and trailing punctuation would
change it, move the value out of the sentence or rephrase.

**Slashes.** Use *or* instead of a slash: *read or write*, not *read/write*.
Keep a slash only for established combinations (*client/server*, *TCP/IP*),
paths, and fractions inside equations. When the reader must type one, name it
first: *Enter two backslashes (\\\\).*

**Ellipses.** Use only to show omitted text in a quotation or omitted code.

**Exclamation points and question marks.** Use rarely. Readers come for
answers, so answer rather than ask.

**Parentheses.** Prefer a separate sentence over a parenthetical aside. Keep
parentheses for introducing an acronym and for short clarifications.

**Special characters.** Spell out *and*, *plus*, *about*, and *at* in prose.
Screen readers can skip or misread *&*, *+*, *~*, and *@*.

## Numbers

When a number comes from an interface, a log, or code, reproduce it exactly.
Otherwise:

**Words or numerals.**

- Spell out zero through nine; use numerals for 10 and higher.
- Use numerals for all items in a category when any one needs a numeral:
  *3 shards, 12 replicas, and 9 regions*.
- When two numbers refer to different things side by side, spell out one:
  *four 16-bit registers*.
- Always use numerals for measurements, sizes, data quantities, percentages,
  versions, time of day, coordinates, numbered sections, and any value the
  reader enters: *3 ms*, *5 percent*, *8 bits*, *step 4*, *Enter 5*.
- Don't start a sentence with a numeral. Add a modifier (*More than 10 nodes
  failed*) or spell the number out (*Twelve nodes failed*).
- Use numerals for round numbers of a million or more: *7 million requests*.
- Spell out *thousand*, *million*, and *billion* in prose rather than using
  *K*, *M*, or *B*.

**Formatting values.**

- Use commas in numbers of four or more digits: *1,024 entries*. Exceptions:
  years, pixel dimensions, and baud take commas only at five or more digits;
  page numbers, addresses, and decimal places take none.
- Add a leading zero before a decimal point: *0.5*, unless the reader types the
  value.
- Hyphenate spelled-out compound numbers and fractions: *twenty-five*,
  *one-third*.
- Express a fraction in words or decimals, not with a slash, except within an
  equation.
- With a spelled-out unit, use the plural for anything except exactly one:
  *0.5 seconds*, *1 second*, *0 seconds*.
- Spell out *by* for dimensions, except screen resolutions and similar
  dimensions that use the multiplication sign: *1920 × 1080*.
- Write negative numbers with a minus sign, not a hyphen or en dash.

**Ordinals.** Spell out ordinals: *the first entry*, *the twenty-first
release*. Avoid *firstly* and *secondly*. Avoid ordinals in dates: *June 1*,
not *June first*.

**Ranges.** Write *from 9 through 17* in prose. Use an en dash only in tight
spaces such as tables, and never with *from*: *9–17*. For times, use *to*:
*10:00 AM to 2:00 PM*.

**Dates and times.** Write *month day, year* with the month spelled out:
*January 5, 2026*. Avoid all-numeric dates, which readers in different regions
parse differently. Use *AM* and *PM*, *noon*, and *midnight*. Include the time
zone whenever readers in other zones could misread the time. Name months or
quarters instead of seasons.
