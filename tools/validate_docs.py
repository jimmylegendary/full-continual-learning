#!/usr/bin/env python3
"""Offline integrity checks. Not a literature audit or model efficacy test."""
from __future__ import annotations
import ast
import csv
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git", ".venv", "__pycache__", ".local-validation"}

def files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*") if p.is_file() and not any(part in IGNORED for part in p.relative_to(ROOT).parts))

def main() -> None:
    all_files = files()
    errors: list[str] = []
    link_count = 0
    for path in all_files:
        relative = str(path.relative_to(ROOT))
        if path.suffix == ".md":
            text = path.read_text(encoding="utf-8")
            text = re.sub(r"```.*?```", "", text, flags=re.S)
            for raw in re.findall(r"\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", text):
                target = urlsplit(raw)
                if target.scheme or target.netloc or not target.path:
                    continue
                link_count += 1
                resolved = (path.parent / unquote(target.path)).resolve()
                if not resolved.is_relative_to(ROOT) or not resolved.exists():
                    errors.append(f"{relative}: unresolved local link {raw}")
        elif path.suffix == ".py":
            try:
                ast.parse(path.read_text(encoding="utf-8"), filename=relative)
            except SyntaxError as exc:
                errors.append(f"{relative}: {exc}")
        elif path.suffix == ".json":
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except (ValueError, UnicodeDecodeError) as exc:
                errors.append(f"{relative}: invalid JSON: {exc}")
    with (ROOT / "references" / "catalog.tsv").open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    ids = [row["id"] for row in rows]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate reference IDs")
    for row in rows:
        if None in row or any(value is None for value in row.values()):
            errors.append(f"Malformed TSV row: {row}")
        if not row["url"] and row["status"] != "needs-resolution":
            errors.append(f"Missing URL without needs-resolution: {row['id']}")
    report = {"files_scanned": len(all_files), "markdown_files": sum(p.suffix == ".md" for p in all_files), "local_links_checked": link_count, "reference_records": len(rows), "unresolved_reference_ids": [r["id"] for r in rows if r["status"] == "needs-resolution"], "errors": errors, "scope": "Offline local links, reference format, JSON and Python syntax only; no full URL, scientific or efficacy validation."}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
