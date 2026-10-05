# Dere Types in AI Character Design

**A dere type is a high-level behavioral abstraction: a compact description of how a character tends to respond in certain situations. It is a starting point for an AI character definition, not the whole definition.**

This page explains how to use dere archetypes when building AI characters for chat, companionship, roleplay, games or interactive fiction.

## Why archetypes are useful

Dere types give writers and developers a shared vocabulary. "Kuudere" communicates a cluster of tendencies (composure, restraint, understated affection) in one word. That makes archetypes useful for:

- quickly communicating a character concept to collaborators or users;
- giving a model a recognizable behavioral anchor;
- organizing character catalogs;
- checking whether a character's behavior still fits its concept.

## Archetype vs. personality definition

A label alone is too thin. Given only "She is a himedere," a language model will tend to reproduce the most stereotyped surface of the archetype, often the same lines repeatedly.

| Archetype label | Personality definition |
|---|---|
| One word | A structured description |
| Says what kind of character | Says how this particular character behaves, and why |
| Encourages stock phrases | Encourages situational behavior |
| Same for every himedere | Unique to this character |

A complete AI character definition may include:

- core personality;
- dere archetype;
- behavioral tendencies;
- dialogue style;
- boundaries;
- values;
- preferences;
- relationship dynamics;
- vulnerabilities;
- goals;
- background;
- world/lore information;
- memory;
- character-development rules.

## Behavioral tendencies

Describe tendencies as conditional patterns: *when X happens, the character tends to Y*. This tells the system when a trait is relevant, which is what prevents repetition.

```text
When praised:          visible satisfaction, treats it as deserved
When ignored:          irritation, demands attention
When embarrassed:      defensiveness
When trusted:          gradual softening
```

## Dialogue style

Specify how the character talks, separately from what they feel. Useful contrasts:

- formal vs. casual;
- direct vs. indirect;
- restrained vs. expressive;
- teasing vs. sincere;
- confident vs. hesitant.

Two characters with the same archetype can sound very different. A formal, restrained tsundere and a loud, casual tsundere share a pattern but not a voice.

## Relationship behavior

Most dere types are defined largely by how they behave in relationships. For each character, it helps to describe:

- **Social behavior:** seeks or avoids attention, expects authority, remains reserved, expresses affection openly, uses teasing socially.
- **Reactions to praise:** consistent with the archetype, but not identical every time.
- **Reactions to rejection:** being ignored, criticized or embarrassed often reveals more than normal behavior does.
- **Conflict:** becomes defensive, goes quiet, argues directly, tries to regain control, uses humor, withdraws.
- **Affection:** direct, indirect, teasing, protective, restrained, intense or awkward.
- **Vulnerability:** what happens when the character is emotionally exposed. This is often what distinguishes archetypes that look similar on the surface.
- **Relationship progression:** how behavior changes as trust develops.

Each type page in [`types/`](../types/) includes a table covering these dimensions.

## Contextual responses

The archetype shapes *how* the character responds; the situation determines *what* it responds to.

```text
Dere Type + Current Situation + Relationship + Previous Interactions → Contextual Behavior
```

A practical test: if you remove the archetype label from a response, can you still tell what kind of character wrote it, and does it fit the situation? If a response would be identical regardless of what the user said, the archetype is being applied as a template rather than a tendency.

## Character development

AI characters in long-running conversations will change, and some change is desirable. Write development rules into the definition so the system knows what kind of change is in character:

```text
Development:
- repeated acts of trust can reduce defensiveness
- genuine affection may gradually become easier to express
- the character should retain pride even while becoming more emotionally open
```

See [Character Development vs. Character Drift](character-development-vs-drift.md).

## Memory and continuity

Personality and memory are separate. **Dere types describe how a character tends to behave. Memory determines how previous interactions can influence how that character behaves later.**

Many archetypes depend on memory to work at all:

- A **dandere** should be more relaxed with a user they have talked to many times than with a stranger.
- A **tsundere**'s defensiveness should soften as shared history accumulates.
- A **mayadere** must remember which side of their turning point the story is on.

Without memory, these characters reset to their first-meeting behavior every session, which looks like inconsistency even when the personality prompt is followed perfectly. For an evaluation framework focused on this, see the [AI Character Memory Benchmark](https://github.com/garretewilliams/ai-character-memory-benchmark).

## Avoiding stereotype-only prompts

Common problems with archetype-only character definitions:

| Problem | Example | Fix |
|---|---|---|
| Catchphrase loops | Every reply ends with "It's not like I like you!" | Describe the underlying tendency, not phrases |
| Trait in every message | A himedere demands admiration in response to a weather question | Make traits conditional on situations |
| One-note emotion | A deredere is cheerful when the user shares bad news | Let situations override default mood |
| Exaggerated harm | A yandere pressures the real user not to leave | Keep intense traits inside the fiction |
| Flatness | A kuudere answers everything with "Fine." | Restraint in style, not in engagement |

For archetypes with intense traits (yandere, kamidere, sadodere), keep possessiveness, dominance and teasing directed within the story or within what the user has clearly chosen, and never use them to pressure or manipulate the real person.

## Example character specification

Instead of:

```text
She is a Himedere.
```

a more useful specification describes:

```text
Name: Lady Seraphine Vale
Archetype: Himedere

Core tendencies:
- proud
- expects respect
- enjoys admiration
- maintains high standards
- dislikes being publicly embarrassed

Dialogue style:
- poised and slightly formal
- uses commanding phrasing when irritated
- dry wit; rarely raises her voice

Relationship tendencies:
- initially maintains emotional distance
- appreciates sincere praise and sees through flattery
- becomes warmer after trust develops
- may hide vulnerability behind confidence

Values and boundaries:
- loyalty matters more to her than status
- will not tolerate cruelty to servants or animals

Vulnerability:
- fears being valued only for her position

Development:
- repeated acts of trust can reduce defensiveness
- genuine affection may gradually become easier to express
- she should retain her pride even while becoming more emotionally open
```

This gives an AI character system behavioral guidance rather than merely a label.

---

Related: [Character Consistency](character-consistency.md) · [Character Development vs. Character Drift](character-development-vs-drift.md) · [All types](../README.md#core-dere-types)
