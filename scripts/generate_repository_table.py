#!/usr/bin/env python3
"""Generate a categorized Markdown table of verified related repositories."""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKER = """<!--
This file is generated automatically.
Do not edit it manually.
Update the corresponding CSV file and rerun the generation script.
-->"""


def escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def render(rows: list[dict[str, str]]) -> str:
    lines = [
        MARKER,
        "# Verified Related Repositories",
        "",
        "Only manually verified records from [`../data/repositories.csv`](../data/repositories.csv) are included.",
        f"Verified repositories: **{len(rows)}**",
        "",
    ]
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["category"]].append(row)
    if not grouped:
        lines.extend([
            "| Repository | Category | Focus | Main Scope | Relationship | Last Checked |",
            "| --- | --- | --- | --- | --- | --- |",
            "| _No verified records available._ |  |  |  |  |  |",
            "",
        ])
    else:
        for category in sorted(grouped, key=lambda value: (value.casefold(), value)):
            lines.extend([
                f"## {escape(category)}",
                "",
                "| Repository | Focus | Main Scope | Relationship | Last Checked |",
                "| --- | --- | --- | --- | --- |",
            ])
            for row in sorted(
                grouped[category],
                key=lambda item: (item["name"].casefold(), item["name"], item["id"]),
            ):
                name = f"[{escape(row['name'])}]({row['url']})"
                lines.append("| " + " | ".join([
                    name, escape(row["description"]), escape(row["main_scope"]),
                    escape(row["relationship"]), escape(row["last_checked"]),
                ]) + " |")
            lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=ROOT / "data" / "repositories.csv")
    parser.add_argument("--output", type=Path, default=ROOT / "resources" / "generated_related_repositories.md")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        with args.input.open("r", encoding="utf-8", newline="") as handle:
            rows = [row for row in csv.DictReader(handle) if row.get("verified") == "true"]
        if args.output.exists() and MARKER not in args.output.read_text(encoding="utf-8"):
            raise RuntimeError(f"refusing to overwrite manually maintained file: {args.output}")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(render(rows), encoding="utf-8")
    except (OSError, csv.Error, KeyError, RuntimeError) as exc:
        print(f"Repository table generation failed: {exc}", file=sys.stderr)
        return 1
    print(f"Generated repository table for {len(rows)} verified record(s) at {args.output}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
