# Changelog

All notable changes to this project are documented here. Versions follow [semantic versioning](https://semver.org/): breaking schema changes are major, new types or fields are minor, wording fixes are patch.

## [1.0.0] - 2026-10-05

Initial release.

### Added

- Canonical pages for 11 dere types: tsundere, yandere, kuudere, dandere, deredere, himedere, oujidere, kamidere, sadodere, mayadere, bakadere.
- YAML data for each type and a JSON Schema (draft 2020-12), with optional fields for Japanese spelling, term origin with a confidence level, and usage level.
- Documentation: dere types in AI character design, character consistency, character development vs. drift, references.
- `tools/validate.py` and a CI workflow that validates data against the schema and checks that pages and data agree.
