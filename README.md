# Dere Types

**An open reference guide to Japanese-inspired dere character archetypes, their personality traits, behavioral patterns, and use in AI character design and roleplay.**

[![Validate data](https://github.com/garretewilliams/dere-types/actions/workflows/validate.yml/badge.svg)](https://github.com/garretewilliams/dere-types/actions/workflows/validate.yml)
![Version: 1.0.0](https://img.shields.io/badge/version-1.0.0-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-blue)

## What Is a Dere Type?

**A dere type is a character archetype used to describe recurring patterns of personality, affection, social behavior, and emotional expression.** The "dere" naming convention is commonly used for Japanese-inspired fictional characters, particularly characters whose outward behavior and relationships follow recognizable patterns.

The suffix *dere* comes from the Japanese ideophone *dere dere* (デレデレ), meaning lovey-dovey or infatuated. A dere type name pairs it with a word for the character's distinctive way of being: *tsun tsun* (aloof) gives **tsundere**, *kūru* (cool) gives **kuudere**, *hime* (princess) gives **himedere**, and so on. The terms began in Japanese anime, manga, game and visual novel fandom and are now widely used as shorthand for character personality in fiction, fan communities, character design and roleplay.

**Dere types are not rigid psychological diagnoses or scientifically validated personality categories.** They are fictional character archetypes used in storytelling, fandom, character design and roleplay. See [Dere types are not psychological diagnoses](#dere-types-are-not-psychological-diagnoses).

Some terms, such as tsundere and yandere, are well documented. Others are newer, fan-coined and used less consistently. Each page states how certain the origin of its name is.

## Core Dere Types

| Type | Quick definition | Usage |
|---|---|---|
| [Tsundere](types/tsundere.md) | Cold, irritable or dismissive toward someone they care about, while gradually or intermittently revealing warmth and affection. | core |
| [Yandere](types/yandere.md) | Intense affection that can become possessive or obsessive, in fiction sometimes escalating to extreme or dangerous behavior. | core |
| [Kuudere](types/kuudere.md) | Calm, composed and emotionally reserved; affection is expressed in understated ways. | core |
| [Dandere](types/dandere.md) | Quiet and socially reserved, often shy; becomes more talkative and expressive with people they feel comfortable with. | core |
| [Deredere](types/deredere.md) | Openly warm, cheerful and affectionate, expressing care directly. | common |
| [Himedere](types/himedere.md) | Princess-like expectations, pride, authority, and a desire for admiration or special treatment. | common |
| [Kamidere](types/kamidere.md) | God-like self-regard: superiority, a desire for authority, and an expectation of recognition. | common |
| [Oujidere](types/oujidere.md) | Prince-like expectations: confidence, regal or chivalrous self-presentation, and expected respect. | niche |
| [Sadodere](types/sadodere.md) | Expresses interest through teasing, provocation or playful control. | niche |
| [Mayadere](types/mayadere.md) | Begins as an antagonist or rival and becomes an ally or love interest after a turning point. | niche |
| [Bakadere](types/bakadere.md) | Naive, scatterbrained or clumsy; expresses affection with unfiltered enthusiasm. | niche |

*Usage* is an editorial label: **core** terms are widely recognized and documented in reference works; **common** terms are widely used in fandom; **niche** terms are fan-coined and less consistently used.

Every page follows the same structure: definition, quick definition, meaning of the name, defining traits, typical behavior, relationship behavior, common misconceptions, use in AI character design, character consistency, and related types.

## Dere Types at a Glance

| Dere Type | Core Pattern | Typical Exterior | Relationship Pattern |
|---|---|---|---|
| Tsundere | Defensive affection | Cold, irritated, embarrassed | Affection emerges through conflict or vulnerability |
| Yandere | Intense attachment | Loving, intense, potentially possessive | Attachment can become obsessive |
| Kuudere | Emotional restraint | Calm, cool, reserved | Affection tends to be understated |
| Dandere | Shyness/reserve | Quiet, withdrawn | Opens up through comfort and trust |
| Deredere | Open affection | Cheerful, warm | Affection is expressed openly |
| Himedere | Royal/princess expectations | Proud, demanding | Expects admiration and special treatment |
| Oujidere | Prince-like expectations | Regal, confident | Expects respect and elevated treatment |
| Kamidere | God-like superiority | Dominant, self-important | Expects authority or submission |
| Sadodere | Pleasure in teasing/control | Playful, provocative, dominant | Affection may involve teasing or control |
| Mayadere | Formerly antagonistic | Hostile or dangerous initially | Relationship changes after a turning point |
| Bakadere | Naive/airheaded behavior | Energetic, silly, innocent | Affection expressed without much subtlety |

These are concise reference descriptions, not universal definitions. Individual characters combine and bend archetypes.

## Dere Types in AI Characters

A dere type is best understood as a **behavioral tendency**, not a script. A character labeled "tsundere" should not insult the user in every message, and a "himedere" should not announce she is a princess every turn.

- A tsundere should not be hostile in every interaction.
- A himedere should not constantly announce that she is a princess.
- A kuudere should not be emotionless.
- A dandere should not be incapable of speaking.
- A yandere should not automatically be violent.
- A deredere should not be cheerful regardless of context.

The archetype influences **how** the character responds. The current situation, the relationship, previous interactions and the character's development determine **what** the response is.

```text
Dere Type
    +
Current Situation
    +
Relationship
    +
Previous Interactions
    ↓
Contextual Behavior
```

For example, a himedere's expectation of admiration matters when it is relevant: receiving praise may produce visible satisfaction; being ignored may produce irritation; being treated respectfully may reinforce trust; being publicly embarrassed may trigger defensiveness; becoming emotionally attached may gradually soften her behavior.

**The goal is consistent behavioral expression, not repetitive output.** A dere type is a starting point, not a complete character specification. See [Dere Types in AI Character Design](docs/dere-types-in-ai-character-design.md) for how to turn a label into a usable character definition, including a full example.

## Character Consistency vs. Repetition

> **Character consistency ≠ character repetition.**

**Character consistency means that a character's behavior remains compatible with their established personality, circumstances, relationships and development.** A consistent character can behave differently from one conversation to the next and still be recognizable. A character who says the same catchphrases in every message is repetitive, not well realized.

The key question is: **does the character's behavior still make sense given everything that has happened?** See [Character Consistency](docs/character-consistency.md).

## Dere Types and Character Development

Characters change. The important question is why.

> **Character development has a cause; character drift often doesn't.**

A himedere who gradually becomes more vulnerable with someone she trusts is developing. A himedere who suddenly loses all pride for no reason has drifted. This distinction matters most in long-running AI roleplay, where characters may change over hundreds of conversations. See [Character Development vs. Character Drift](docs/character-development-vs-drift.md).

## Dere Types and AI Memory

**Dere types describe how a character tends to behave. Memory determines how previous interactions can influence how that character behaves later.**

These are separate dimensions, so an AI character can have:

1. strong character consistency but poor memory;
2. strong memory but poor character consistency;
3. both;
4. neither.

A character may correctly remember the user's favorite book while responding in a way that is completely out of character. Another may be a convincing himedere in every message while forgetting what happened yesterday.

| Question | Dimension |
|---|---|
| Does the character continue to behave like the character it was designed to be? | **Character consistency** |
| Do previous interactions meaningfully influence later conversations and behavior? | **Memory continuity** |

```text
Character Archetype
        +
Character Traits
        +
Relationship History
        +
Relevant Memory
        +
Current Context
        ↓
Character Response
```

This is one reason long-running AI roleplay is more complex than giving an AI a personality prompt. Memory continuity is measured by the companion project, the [AI Character Memory Benchmark](https://github.com/garretewilliams/ai-character-memory-benchmark). Neither repository depends on the other.

```text
AI Character
     │
     ├── Personality / Archetype  →  Dere Types (this repository)
     │
     └── Memory / Continuity      →  AI Character Memory Benchmark
```

## Dere Types Are Not Psychological Diagnoses

**Dere types are fictional character archetypes and fandom terminology, not clinically validated psychological categories or personality diagnoses.**

- A dere type does not diagnose anyone's personality.
- A dere type does not predict real-world behavior.
- A dere type is not equivalent to any clinical condition.
- Fictional archetypes do not map onto psychological disorders. Words like "sick" in *yandere* or "sadist" in *sadodere* are fictional framing, not clinical terms.

This repository is about fictional character design.

## Machine-Readable Data

Each type has a YAML file in [`data/`](data/) that follows [`schema/dere-type.schema.json`](schema/dere-type.schema.json) (JSON Schema draft 2020-12). The data is intended for developers, AI character creators, researchers, dataset builders, character-card authors and roleplay systems.

```yaml
name: Himedere
category: dere-type
definition: >-
  A character archetype characterized by princess-like expectations, pride,
  authority, and a desire for admiration or special treatment, who may reveal
  a softer side toward people they trust.
core_traits: [pride, authority, high standards, desire for admiration, ...]
behavioral_patterns: [expects respect and courtesy, ...]
relationship_patterns: [values sincere admiration and loyalty, ...]
related_types: [oujidere, kamidere, tsundere]
common_misconceptions: ["A himedere is simply a dominant character.", ...]
term_origin: { components: [...], confidence: commonly-cited }
usage: common
```

Required fields: `name`, `category`, `definition`, `core_traits`, `behavioral_patterns`, `relationship_patterns`, `related_types`, `common_misconceptions`. Optional: `japanese`, `term_origin` (with a `confidence` of `established`, `commonly-cited` or `uncertain`), and `usage`.

Validate locally:

```bash
pip install pyyaml jsonschema
python tools/validate.py
```

The validator checks every file against the schema, checks that related types exist, and checks that each YAML definition matches the Quick Definition on its page.

## Repository Structure

```text
dere-types/
├── README.md
├── types/            one canonical page per dere type
├── data/             machine-readable YAML for each type
├── schema/           JSON Schema for the data
├── docs/
│   ├── dere-types-in-ai-character-design.md
│   ├── character-consistency.md
│   ├── character-development-vs-drift.md
│   └── references.md
├── tools/validate.py
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CITATION.cff
├── CHANGELOG.md
└── LICENSE
```

## Contributing

Corrections, better definitions, references, data improvements and proposals for additional types are welcome. Please distinguish established terminology from fandom usage and from your own interpretation. See [CONTRIBUTING.md](CONTRIBUTING.md).

## References

Terminology sources, Japanese language references, AI character research and clearly labeled background essays are listed in [docs/references.md](docs/references.md).

## Maintainer

Maintained by Garret E. Williams ([@garretewilliams](https://github.com/garretewilliams)). This repository is maintained by [ChatBrat](https://chatbrat.ai/) as an open reference for AI character design, roleplay, and conversational character systems. The taxonomy is intended to be useful across platforms and implementations. ChatBrat did not invent these terms and does not claim authority over Japanese language or culture.

## License

[MIT](LICENSE). The license covers all content in this repository: written reference pages, machine-readable data, schema and code. You may reuse the definitions and data, including commercially, with attribution as described in the license.

## Readable PDF and archived versions

A [PDF companion](23195714-documentation.pdf) is available for the archived v1.0.0 documentation. See [archive and version notes](ZENODO.md) and the [published Zenodo version](https://zenodo.org/records/23555520). This documentation update adds no benchmark results or new software-release claim.
