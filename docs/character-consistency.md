# Character Consistency

**Character consistency means that a character's behavior remains compatible with their established personality, circumstances, relationships and development. It does not mean identical behavior.**

> **Character consistency ≠ character repetition.**

A consistent character can behave differently from one conversation to the next while remaining recognizable. A repetitive character says and does the same things regardless of context. In AI character systems the two are often confused, and repetition is mistaken for consistency.

## The key question

> **Does the character's behavior still make sense given everything that has happened?**

That question includes the character's personality, the current situation, the relationship with the other person, what has happened before, and how the character has developed.

## What should stay stable

A useful AI character should preserve:

- **core personality:** temperament and characteristic attitudes;
- **recognizable behavioral tendencies:** the patterns that define the archetype;
- **values:** what the character will and won't do;
- **relationship dynamics:** how the character relates to particular people;
- **established boundaries:** limits the character has set.

## What should be allowed to vary

While still allowing:

- **contextual variation:** different situations call for different responses;
- **emotional reactions:** a cheerful character can be sad; a calm character can be shaken;
- **learning:** the character can learn new things about the world and the user;
- **relationship development:** closeness, trust and conflict change behavior;
- **narrative change:** story events can change the character.

## Consistency as a model

```text
Character Consistency
        ↓
Stable underlying tendencies
        +
Context-sensitive behavior
        +
Plausible change over time
```

## Examples

| Situation | Repetitive | Consistent |
|---|---|---|
| A tsundere is thanked sincerely | "Hmph! It's not like I did it for you!" (every time) | Sometimes deflects, sometimes mutters "...you're welcome," depending on how exposed she feels |
| A kuudere hears bad news | "I see." | A brief, calm reply, followed by a concrete offer of help |
| A deredere is told the user is grieving | "Aww, cheer up!" | Gentle, warm, present, without forced positivity |
| A himedere is asked about the weather | "As a princess, I expect sunshine!" | Answers normally; pride shows only if it becomes relevant |

## Why this matters for AI characters

Language models given a short personality description tend to over-express it: the most stereotypical traits appear in every response. Over long conversations, the opposite problem appears: the character slowly loses its distinctive traits and drifts toward a generic assistant voice. Good character design addresses both:

- describe traits as **situational tendencies** to reduce over-expression;
- give the character **values, voice and history** that persist, to reduce drift;
- use **memory** so the character's behavior reflects the relationship, not a reset.

See [Character Development vs. Character Drift](character-development-vs-drift.md) and [Dere Types in AI Character Design](dere-types-in-ai-character-design.md).

---

Related: [README](../README.md#character-consistency-vs-repetition)
