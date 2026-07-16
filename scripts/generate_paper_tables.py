#!/usr/bin/env python3
"""Generate task-specific Markdown tables from verified paper records."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKER = """<!--
This file is generated automatically.
Do not edit it manually.
Update the corresponding CSV file and rerun the generation script.
-->"""
COLUMNS = [
    ("title", "Paper"), ("year", "Year"), ("task", "Task"),
    ("world_model_scope", "Scope"), ("representation_space", "Representation"),
    ("transition_type", "Transition"), ("learning_objective", "Objective"),
    ("datasets", "Dataset"), ("code_url", "Code"), ("verified", "Verified"),
]


def slug(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")
    return cleaned or "uncategorized"


def escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def link(label: str, url: str) -> str:
    if url.startswith(("http://", "https://")):
        return f"[{escape(label)}]({url})"
    return escape(label)


def render_table(title: str, rows: list[dict[str, str]]) -> str:
    lines = [MARKER, f"# {title}", "", "Only manually verified records are included.", ""]
    lines.append("| " + " | ".join(label for _, label in COLUMNS) + " |")
    lines.append("| " + " | ".join("---:" if key == "year" else "---" for key, _ in COLUMNS) + " |")
    if not rows:
        lines.append("| _No verified records available._ |  |  |  |  |  |  |  |  |  |")
    else:
        for row in sorted(
            rows,
            key=lambda item: (
                -int(item["year"]),
                item["title"].casefold(),
                item["title"],
                item["id"],
            ),
        ):
            values: list[str] = []
            for key, _ in COLUMNS:
                value = row[key]
                if key == "title":
                    value = link(value, row["paper_url"])
                elif key == "code_url":
                    value = link("code", value) if value.startswith(("http://", "https://")) else escape(value)
                else:
                    value = escape(value)
                values.append(value)
            lines.append("| " + " | ".join(values) + " |")
    lines.append("")
    return "\n".join(lines)


def render_index(grouped: dict[str, list[dict[str, str]]]) -> str:
    paper_count = sum(len(rows) for rows in grouped.values())
    task_names = sorted(grouped, key=lambda value: (value.casefold(), value))
    lines = [
        MARKER,
        "# Verified Paper Index",
        "",
        "The structured source of truth is [`../../data/papers.csv`](../../data/papers.csv).",
        "Only records with `verified=true` are included in generated pages.",
        "",
        "## Summary",
        "",
        f"- Verified papers: **{paper_count}**",
        f"- Tasks represented: **{len(task_names)}**",
        "",
    ]
    if not task_names:
        lines.extend([
            "## Current State",
            "",
            "No manually verified paper records are available yet. This page reports an empty state and does not imply literature coverage or research findings.",
            "",
        ])
    else:
        lines.extend(["## Task Pages", ""])
        for task in task_names:
            title = task.replace("_", " ").title()
            lines.append(f"- [{title}]({slug(task)}.md) — {len(grouped[task])} verified paper(s)")
        lines.append("")
    return "\n".join(lines)


def safe_write(path: Path, content: str) -> None:
    if path.exists() and MARKER not in path.read_text(encoding="utf-8"):
        raise RuntimeError(f"refusing to overwrite manually maintained file: {path}")
    path.write_text(content, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=ROOT / "data" / "papers.csv")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "papers" / "generated")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        with args.input.open("r", encoding="utf-8", newline="") as handle:
            rows = [row for row in csv.DictReader(handle) if row.get("verified") == "true"]
        args.output_dir.mkdir(parents=True, exist_ok=True)
        grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in rows:
            grouped[row.get("task", "uncategorized")].append(row)
        expected_files = {args.output_dir / "index.md"}
        expected_files.update(args.output_dir / f"{slug(task)}.md" for task in grouped)
        for path in sorted(args.output_dir.glob("*.md")):
            if path not in expected_files:
                if MARKER not in path.read_text(encoding="utf-8"):
                    raise RuntimeError(f"refusing to remove manually maintained file: {path}")
                path.unlink()
        safe_write(args.output_dir / "index.md", render_index(grouped))
        for task in sorted(grouped, key=lambda value: (value.casefold(), value)):
            task_rows = grouped[task]
            safe_write(
                args.output_dir / f"{slug(task)}.md",
                render_table(task.replace("_", " ").title(), task_rows),
            )
    except (OSError, csv.Error, KeyError, ValueError, RuntimeError) as exc:
        print(f"Paper table generation failed: {exc}", file=sys.stderr)
        return 1
    print(f"Generated paper tables for {len(rows)} verified record(s) across {len(grouped)} task(s) in {args.output_dir}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
