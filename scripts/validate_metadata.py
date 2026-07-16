#!/usr/bin/env python3
"""Validate the repository's CSV schemas and core metadata invariants."""

from __future__ import annotations

import csv
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]

SCHEMAS: dict[str, list[str]] = {
    "papers.csv": "id,title,year,authors,venue,paper_url,code_url,task,world_model_scope,scope_confidence,representation_space,transition_type,learning_objective,rollout_capability,action_conditioned,physics_informed,uncertainty_modeling,datasets,metrics,application_domain,open_source,notes,verified,last_checked".split(","),
    "datasets.csv": "name,task,domain,multivariate,run_to_failure,contains_actions,contains_operating_conditions,labels,official_url,license,redistribution_allowed,download_instructions,notes,verified,last_checked".split(","),
    "methods.csv": "method,reference_id,task,world_model_scope,representation_space,transition_type,learning_objective,rollout_capability,probabilistic,action_conditioned,physics_informed,open_source,reproduction_status,notes".split(","),
    "repositories.csv": "id,name,category,url,description,main_scope,relationship,last_checked,verified,notes".split(","),
}

WORLD_MODEL_SCOPES = {
    "strict_world_model",
    "world_model_like",
    "related_predictive_model",
    "uncertain",
}
SCOPE_CONFIDENCES = {"high", "medium", "low", "unknown"}
REPRODUCTION_STATUSES = {
    "not_evaluated",
    "code_available",
    "environment_built",
    "partial_reproduction",
    "reproduced",
    "failed_reproduction",
    "blocked_data",
    "blocked_details",
}
STRICT_BOOLEAN_FIELDS: dict[str, set[str]] = {
    "papers.csv": {"action_conditioned", "physics_informed", "verified"},
    "datasets.csv": {
        "multivariate",
        "run_to_failure",
        "contains_actions",
        "contains_operating_conditions",
        "redistribution_allowed",
        "verified",
    },
    "methods.csv": {"probabilistic", "action_conditioned", "physics_informed"},
    "repositories.csv": {"verified"},
}
BOOLEAN_OR_UNKNOWN_FIELDS: dict[str, set[str]] = {
    "papers.csv": {"open_source"},
    "methods.csv": {"open_source"},
}
URL_FIELDS: dict[str, set[str]] = {
    "papers.csv": {"paper_url", "code_url"},
    "datasets.csv": {"official_url"},
    "repositories.csv": {"url"},
}
KEY_FIELDS: dict[str, tuple[str, ...]] = {
    "papers.csv": (
        "title", "year", "authors", "venue", "paper_url", "task",
        "world_model_scope", "representation_space", "transition_type",
        "learning_objective", "datasets", "verified", "last_checked",
    ),
    "datasets.csv": ("name", "task", "domain", "official_url", "license", "last_checked"),
    "repositories.csv": ("id", "name", "category", "url", "description", "relationship", "last_checked"),
}


@dataclass
class ValidationResult:
    errors: list[str]
    row_count: int = 0


def is_todo(value: str) -> bool:
    return not value.strip() or value.strip().upper() == "TODO"


def valid_url(value: str) -> bool:
    if is_todo(value):
        return True
    parsed = urlparse(value.strip())
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def valid_date(value: str) -> bool:
    if is_todo(value):
        return True
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        return False
    return True


def read_csv(path: Path, expected_header: list[str]) -> tuple[list[dict[str, str]], list[str]]:
    errors: list[str] = []
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            actual = reader.fieldnames or []
            if actual != expected_header:
                errors.append(f"{path}: header mismatch\n  expected: {','.join(expected_header)}\n  actual:   {','.join(actual)}")
                return [], errors
            rows = list(reader)
    except (OSError, csv.Error) as exc:
        errors.append(f"{path}: could not read CSV: {exc}")
        return [], errors
    return rows, errors


def validate_file(path: Path, expected_header: list[str]) -> ValidationResult:
    rows, errors = read_csv(path, expected_header)
    filename = path.name
    seen: dict[str, int] = {}
    identifier = "id" if "id" in expected_header else ("name" if "name" in expected_header else "method")

    for line_number, row in enumerate(rows, start=2):
        prefix = f"{path}:{line_number}"
        record_id = row.get(identifier, "").strip()
        if not record_id:
            errors.append(f"{prefix}: missing {identifier}")
        elif record_id in seen:
            errors.append(f"{prefix}: duplicate {identifier} {record_id!r} (first seen on line {seen[record_id]})")
        else:
            seen[record_id] = line_number

        if filename == "papers.csv":
            year = row["year"].strip()
            if not re.fullmatch(r"\d{4}", year):
                errors.append(f"{prefix}: year must be four digits")
            elif not 1900 <= int(year) <= date.today().year + 1:
                errors.append(f"{prefix}: year {year} is outside the accepted range")
            if row["world_model_scope"] not in WORLD_MODEL_SCOPES:
                errors.append(f"{prefix}: invalid world_model_scope {row['world_model_scope']!r}")
            if row["scope_confidence"] not in SCOPE_CONFIDENCES:
                errors.append(f"{prefix}: invalid scope_confidence {row['scope_confidence']!r}")

        if filename == "methods.csv":
            if row["world_model_scope"] not in WORLD_MODEL_SCOPES:
                errors.append(f"{prefix}: invalid world_model_scope {row['world_model_scope']!r}")
            if row["reproduction_status"] not in REPRODUCTION_STATUSES:
                errors.append(f"{prefix}: invalid reproduction_status {row['reproduction_status']!r}")

        for field in STRICT_BOOLEAN_FIELDS.get(filename, set()):
            if row[field] not in {"true", "false"}:
                errors.append(f"{prefix}: {field} must be true or false")
        for field in BOOLEAN_OR_UNKNOWN_FIELDS.get(filename, set()):
            if row[field] not in {"true", "false", "unknown"}:
                errors.append(f"{prefix}: {field} must be true, false, or unknown")
        for field in URL_FIELDS.get(filename, set()):
            if not valid_url(row[field]):
                errors.append(f"{prefix}: {field} must be TODO or an HTTP(S) URL")
        if "last_checked" in row and not valid_date(row["last_checked"]):
            errors.append(f"{prefix}: last_checked must be TODO or YYYY-MM-DD")

        if row.get("verified") == "true":
            for field in KEY_FIELDS.get(filename, ()):
                if is_todo(row[field]):
                    errors.append(f"{prefix}: verified record has unresolved key field {field}")

    return ValidationResult(errors=errors, row_count=len(rows))


def main() -> int:
    all_errors: list[str] = []
    total_rows = 0
    for filename, header in SCHEMAS.items():
        path = ROOT / "data" / filename
        if not path.is_file():
            all_errors.append(f"{path}: file not found")
            continue
        result = validate_file(path, header)
        all_errors.extend(result.errors)
        total_rows += result.row_count

    if all_errors:
        print(f"Metadata validation failed with {len(all_errors)} error(s):", file=sys.stderr)
        for error in all_errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Metadata validation passed: {len(SCHEMAS)} files, {total_rows} records, 0 errors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
