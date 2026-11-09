#!/usr/bin/env python3
"""Export the auditable TSV catalog without inventing citation metadata."""
from __future__ import annotations
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "references" / "catalog.tsv"

def main() -> None:
    with SOURCE.open(encoding="utf-8", newline="") as stream:
        records = list(csv.DictReader(stream, delimiter="\t"))
    ids = [row["id"] for row in records]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate reference IDs")
    for row in records:
        if None in row or any(value is None for value in row.values()):
            raise ValueError(f"Invalid TSV row: {row}")
        if not row["url"] and row["status"] != "needs-resolution":
            raise ValueError(f"Missing URL without explicit unresolved status: {row['id']}")
    target = ROOT / "references" / "catalog.json"
    target.write_text(json.dumps({"as_of": "2026-11-09", "scope": "discussion archive; status is verification depth, not efficacy", "records": records}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    def esc(text: str) -> str:
        return text.replace("\\", "\\textbackslash{}").replace("&", "\\&").replace("%", "\\%").replace("_", "\\_")
    entries = []
    for row in records:
        note = f"{row['date_note']}; {row['status']}; {row['note']}"
        lines = [f"@misc{{{row['id']},", "  title = {{" + esc(row["title"]) + "}},", "  note = {" + esc(note) + "},"]
        if row["url"]:
            lines.append("  url = {" + row["url"] + "},")
        lines.append("}")
        entries.append("\n".join(lines))
    (ROOT / "references" / "references.bib").write_text("% Generated draft: check canonical publication metadata before submission.\n\n" + "\n\n".join(entries) + "\n", encoding="utf-8")
    print(f"Exported {len(records)} records to catalog.json and references.bib")

if __name__ == "__main__":
    main()
