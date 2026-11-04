# Developer content

Use this route for tutorials, quickstarts, how-to guides, conceptual
overviews, architecture explanations, samples, and any prose that teaches a
technical reader to do something. The core references still apply. This file
adds what changes in wording for a developer audience. Which sections an
article has, their order, and how procedures and code are laid out come from
other context.

## Audience assumptions

- Assume programming fundamentals. Skip general concepts (what a variable,
  loop, or HTTP request is) and spend the words on what's specific to this
  technology.
- Keep the same voice: warm, crisp, and helpful. Technical readers want
  directness, not formality.
- Define every term specific to the product, protocol, or domain on first use.
  Don't define widely known industry terms for a professional audience.
- Use industry terms the way the field uses them. Verify usage against
  standards, specifications, and technical journals rather than inventing
  vocabulary.
- State prerequisites (knowledge, tools, versions, permissions) before the
  reader needs them.

## Language about code

- Lowercase generic programming concepts: *class*, *interface*, *method*,
  *namespace*, *callback*, *thread pool*.
- Keep identifiers exactly as declared, including case, wherever prose names
  them. Don't pluralize or possess an identifier. Write *the `Retry` objects*
  or *instances of `Retry`*, not *`Retry`s* or *`Retry`'s*.
- Don't use an identifier as an English verb: *call `Dispose`*, not
  *`Dispose` the object*.
- Use a noun after an identifier when the kind of element isn't obvious: *the
  `timeout` parameter*, *the `Connect` method*.
- Use precise verbs for code actions: *call* a method or function, *return* a
  value, *throw* or *raise* an exception, *set* a property, *pass* an
  argument, *declare* a variable, *implement* an interface, *instantiate* or
  *create* an object, *invoke* a delegate.
- Distinguish *parameter* (in the declaration) from *argument* (in the call).
- Prefer *run* for programs, scripts, and commands, and *start* for services.
  Avoid *execute* in prose except in fixed technical phrases.
- Passive voice is acceptable when the actor is irrelevant or the receiver
  matters more: *The connection is closed when the scope exits.*

## Code examples

**What to show.**

- Show real tasks.
- Prioritize frequently used elements and those that are tricky to get right.
- Don't show the obvious, and don't contrive an example just to demonstrate
  syntax.
- Show the expected output or result.

**How to introduce it.**

- Before the code, state the scenario, the requirements, and any dependencies
  in a sentence or two.
- Make the code easy to copy and run, or to adapt.
- Point out the parts the reader must change, and use placeholder names that
  clearly read as placeholders.

**Quality bar.**

- Compile and test every example.
- Write secure code: validate input, never hard-code passwords, keys, or
  secrets, and follow the security practices you'd expect in production.
- Show exception handling only when it's intrinsic to the example. Don't catch
  exceptions caused by invalid arguments.
- Consider accessibility in any example that builds a user interface.
- Write comments that explain intent or a non-obvious step. Don't comment the
  obvious.
- Design for reuse: the reader should be able to lift the code into a real
  program.

## Procedures

- Use the imperative mood. Write each step as a complete sentence.
- Give one action per step. Combine short actions only when they happen in the
  same place.
- Say where before saying what: *In the configuration file, set `retries` to
  3.*
- Include the action that completes the step, such as *and then select OK* or
  *and then save the file*.
- Write an introductory sentence only when it adds information that the
  title doesn't.
- State the result of a step when the reader needs it to confirm success.
- Put optional steps and conditions at the start of the step: *Optional: ...*
  or *If you use a proxy, ...*.

**Input-neutral verbs.** Describe what the reader does, not which device they
use.

| Verb | Use for |
|---|---|
| open | apps, files, folders, panes, menus |
| close | apps, files, windows, panes |
| go to | a page, a location, a section |
| select | a command, option, item, or link |
| select and hold | a long press or right-click equivalent |
| clear | a checkbox |
| choose | an option among preferences, especially when *select* is already in the text |
| turn on, turn off | a toggle or setting |
| enter | text or a value the reader types |
| move, drag | an item to a new position |

Avoid *click*, *tap*, *press*, *right-click*, *swipe*, and *hit* unless the
instruction is specific to one device. Name a key only when the key itself
matters.

## Command-line and configuration instructions

- Name what the reader runs before showing it: *Run the following command to
  create the certificate.*
- Describe each placeholder the reader must replace, with an example value.
- Say what success looks like, or show the expected output.
- Spell out options and flags in prose once, then refer to them consistently.
