#!/usr/bin/env python3
"""Validate dere-types data.

Checks:
  * every data/*.yaml file validates against schema/dere-type.schema.json;
  * the file name equals the lowercased `name`;
  * every related type exists in data/ and is not the type itself;
  * every data file has a page in types/, and every page has a data file;
  * each page's Quick Definition matches the YAML `definition` exactly.

Requires: pip install pyyaml jsonschema
"""
import json
import re
import sys
from pathlib import Path

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    schema = json.loads((ROOT / "schema" / "dere-type.schema.json").read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    data_files = sorted((ROOT / "data").glob("*.yaml"))
    slugs = {p.stem for p in data_files}
    pages = {p.stem for p in (ROOT / "types").glob("*.md")}
    errors = []

    for path in data_files:
        rel = path.relative_to(ROOT)
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        for err in validator.iter_errors(doc):
            loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
            errors.append(f"{rel}: {loc}: {err.message}")
        if not isinstance(doc, dict) or "name" not in doc:
            continue
        if doc["name"].lower() != path.stem:
            errors.append(f"{rel}: file name must be '{doc['name'].lower()}.yaml'")
        for rt in doc.get("related_types", []):
            if rt == path.stem:
                errors.append(f"{rel}: lists itself as a related type")
            elif rt not in slugs:
                errors.append(f"{rel}: related type '{rt}' has no data file")
        page = ROOT / "types" / f"{path.stem}.md"
        if not page.exists():
            errors.append(f"{rel}: no page at types/{path.stem}.md")
            continue
        m = re.search(r"^\*\*" + re.escape(doc["name"]) + r":\*\* (.+)$", page.read_text(encoding="utf-8"), re.M)
        if not m:
            errors.append(f"types/{path.stem}.md: Quick Definition line not found")
        elif m.group(1).strip() != " ".join(doc["definition"].split()):
            errors.append(f"types/{path.stem}.md: Quick Definition does not match {rel} definition")

    for p in sorted(pages - slugs):
        errors.append(f"types/{p}.md: no data file at data/{p}.yaml")

    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} problem(s).")
        return 1
    print(f"OK: {len(data_files)} dere types valid; pages and data are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
