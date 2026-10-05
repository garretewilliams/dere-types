# Contributing

Thank you for helping make this a better reference. Contributions are welcome from writers, developers, researchers, translators and fans.

## Ways to contribute

- **Correct factual errors** in definitions, etymologies or references.
- **Improve definitions** so they are clearer, more accurate or more useful.
- **Clarify terminology:** romanization, Japanese spelling, common usage.
- **Improve the machine-readable data** in `data/`.
- **Improve the schema** in `schema/` (please open a *Schema improvement* issue first).
- **Add references,** especially reference works and primary sources.
- **Propose additional dere types** (please open a *New dere type proposal* issue first).

## Standards

### Distinguish what kind of claim you are making

Label claims as one of:

- **established terminology:** documented in reference works;
- **common fandom usage:** widely used, but not formally documented;
- **interpretation:** a reasonable reading of how the term is used;
- **original analysis:** your own framework or guidance (for example, AI design advice).

Do not present uncertain historical or linguistic claims as established fact. If the origin of a term is unclear, say so and set `term_origin.confidence` to `uncertain`.

### New terminology

New dere types should be used with a reasonably consistent meaning across multiple independent sources. Include those sources in your proposal. The project prefers a smaller set of well-defined types over a long list of obscure ones.

### Keep definitions and data in sync

Each type has a page in `types/` and data in `data/`. The YAML `definition` must match the **Quick Definition** on the page exactly. The validator checks this.

```bash
pip install pyyaml jsonschema
python tools/validate.py
```

### Page structure

Every type page uses the same sections, in this order: What Is a …?, Quick Definition, Meaning, Defining Traits, Typical Behavior, Relationship Behavior, Common Misconceptions, … in AI Character Design, Character Consistency, Related Dere Types, Further Reading.

### Content rules

- **No copyrighted material.** Do not copy text from wikis, articles, books or other guides. Write in your own words and cite sources.
- **No psychological diagnoses.** Dere types are fictional archetypes. Do not link them to clinical conditions or use them to describe real people.
- **Platform-neutral.** Do not add promotional content, competitor comparisons or links added for search ranking.
- **Further Reading links** must be contextual and useful to readers of that page.

## License

By contributing, you agree that your contributions are licensed under the [MIT License](LICENSE), which covers all content, data and code in this repository.

## Conduct

Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).
