#!/usr/bin/env python3
"""Validate CSV schemas, controlled vocabularies, and review consensus."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS: dict[str, list[str]] = {
    "papers.csv": "id,title,year,authors,venue,paper_url,code_url,tasks,world_model_scope,scope_confidence,consensus_reached,consensus_date,consensus_rationale,classification_rationale,evidence_locations,representation_space,transition_type,learning_objective,rollout_capability,action_conditioned,physics_informed,uncertainty_modeling,datasets,metrics,application_domain,open_source,paper_note_path,notes,verified,last_checked".split(","),
    "datasets.csv": "name,task,domain,multivariate,run_to_failure,contains_actions,contains_operating_conditions,labels,official_url,license,redistribution_allowed,download_instructions,notes,verified,last_checked".split(","),
    "methods.csv": "method,reference_id,task,world_model_scope,representation_space,transition_type,learning_objective,rollout_capability,probabilistic,action_conditioned,physics_informed,open_source,reproduction_status,notes".split(","),
    "repositories.csv": "id,name,category,url,description,main_scope,relationship,last_checked,verified,notes".split(","),
    "paper_reviews.csv": "paper_id,reviewer,review_date,q1,q2,q3,q4,q5,q6,q7,proposed_scope,scope_confidence,classification_rationale,evidence_locations,approved,notes".split(","),
    "search_runs.csv": "search_id,database,query,search_date,date_start,date_end,result_count,export_file,notes,verified".split(","),
    "screening.csv": "screening_id,candidate_id,title,doi,source_url,external_id,source_search_ids,stage,reviewer_1,decision_1,reviewer_2,decision_2,consensus_decision,exclusion_reason,notes,last_checked".split(","),
}
REQUIRED_VOCABULARIES = {
    "tasks",
    "world_model_scopes",
    "scope_confidences",
    "representation_spaces",
    "transition_types",
    "learning_objectives",
    "rollout_capabilities",
    "uncertainty_types",
    "application_domains",
    "repository_categories",
    "screening_decisions",
    "screening_stages",
    "review_answers",
}
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
STRICT_BOOLEAN = {"true", "false"}
TRI_STATE_BOOLEAN = {"true", "false", "unknown"}
SNAKE_CASE = re.compile(r"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$")


@dataclass
class FileSummary:
    records: int = 0
    verified_or_approved: int = 0
    unverified_or_example: int = 0
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


def is_todo(value: str) -> bool:
    return not value.strip() or value.strip().upper() == "TODO"


def is_example(value: str) -> bool:
    return "EXAMPLE" in value.upper()


def is_unresolved(value: str, *, allow_unknown: bool = False) -> bool:
    normalized = value.strip().upper()
    return is_todo(value) or is_example(value) or (normalized == "UNKNOWN" and not allow_unknown)


def valid_url(value: str) -> bool:
    if is_todo(value):
        return True
    parsed = urlparse(value.strip())
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def valid_doi(value: str) -> bool:
    """Accept an empty/TODO DOI or a canonical bare DOI value."""
    if is_todo(value):
        return True
    return bool(re.fullmatch(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", value.strip(), re.IGNORECASE))


def valid_date(value: str) -> bool:
    if is_todo(value) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        return False
    return True


class MetadataValidator:
    def __init__(self, data_dir: Path) -> None:
        self.data_dir = data_dir
        self.summaries = {name: FileSummary() for name in ["vocabularies.json", *SCHEMAS]}
        self.vocabularies: dict[str, set[str]] = {}
        self.rows: dict[str, list[dict[str, str]]] = {}

    def error(self, filename: str, line: int | None, message: str) -> None:
        location = str(self.data_dir / filename)
        if line is not None:
            location = f"{location}:{line}"
        self.summaries[filename].errors.append(f"{location}: {message}")

    def warning(self, filename: str, line: int | None, message: str) -> None:
        location = str(self.data_dir / filename)
        if line is not None:
            location = f"{location}:{line}"
        self.summaries[filename].warnings.append(f"{location}: {message}")

    def load_vocabularies(self) -> None:
        filename = "vocabularies.json"
        path = self.data_dir / filename
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            self.error(filename, None, f"could not read controlled vocabularies: {exc}")
            return
        if not isinstance(raw, dict):
            self.error(filename, None, "top-level JSON value must be an object")
            return
        self.summaries[filename].records = len(raw)
        for required in sorted(REQUIRED_VOCABULARIES):
            if required not in raw:
                self.error(filename, None, f"missing required vocabulary {required!r}")
        for name, values in raw.items():
            if not isinstance(values, list) or not values:
                self.error(filename, None, f"vocabulary {name!r} must be a non-empty array")
                continue
            if any(not isinstance(value, str) for value in values):
                self.error(filename, None, f"vocabulary {name!r} must contain only strings")
                continue
            if len(values) != len(set(values)):
                self.error(filename, None, f"vocabulary {name!r} contains duplicate values")
            for value in values:
                if not SNAKE_CASE.fullmatch(value):
                    self.error(filename, None, f"vocabulary value {value!r} is not lowercase snake_case")
            self.vocabularies[name] = set(values)

    def load_csv_files(self) -> None:
        for filename, expected in SCHEMAS.items():
            path = self.data_dir / filename
            try:
                with path.open("r", encoding="utf-8", newline="") as handle:
                    reader = csv.DictReader(handle)
                    actual = reader.fieldnames or []
                    if actual != expected:
                        self.error(
                            filename,
                            None,
                            "header mismatch\n"
                            f"  expected: {','.join(expected)}\n"
                            f"  actual:   {','.join(actual)}",
                        )
                        self.rows[filename] = []
                        continue
                    raw_rows = list(reader)
            except (OSError, csv.Error) as exc:
                self.error(filename, None, f"could not read CSV: {exc}")
                self.rows[filename] = []
                continue
            rows: list[dict[str, str]] = []
            self.summaries[filename].records = len(raw_rows)
            for line, row in enumerate(raw_rows, start=2):
                if None in row:
                    self.error(filename, line, "row contains more columns than the schema")
                rows.append({key: row.get(key) or "" for key in expected})
            self.rows[filename] = rows

    def controlled(
        self,
        filename: str,
        line: int,
        field_name: str,
        value: str,
        vocabulary_name: str,
        *,
        multiple: bool = False,
        allow_todo: bool = True,
    ) -> list[str]:
        if is_todo(value):
            if not allow_todo:
                self.error(filename, line, f"{field_name} cannot be empty or TODO")
            return []
        if multiple:
            if "," in value:
                self.error(filename, line, f"{field_name} must use semicolons, not commas, between values")
            values = [item.strip() for item in value.split(";")]
            if any(not item for item in values):
                self.error(filename, line, f"{field_name} contains an empty semicolon-delimited value")
            if len(values) != len(set(values)):
                self.error(filename, line, f"{field_name} contains duplicate values")
        else:
            values = [value.strip()]
            if ";" in value:
                self.error(filename, line, f"{field_name} is a single-value field")
        allowed = self.vocabularies.get(vocabulary_name, set())
        for item in values:
            if item and item not in allowed:
                self.error(filename, line, f"invalid {field_name} {item!r}; expected a value from {vocabulary_name}")
        return [item for item in values if item]

    def check_unique(self, filename: str, field_name: str) -> None:
        seen: dict[str, int] = {}
        for line, row in enumerate(self.rows.get(filename, []), start=2):
            value = row[field_name].strip()
            if not value:
                self.error(filename, line, f"missing {field_name}")
            elif value in seen:
                self.error(filename, line, f"duplicate {field_name} {value!r}; first seen on line {seen[value]}")
            else:
                seen[value] = line

    def validate_papers(self) -> None:
        filename = "papers.csv"
        self.check_unique(filename, "id")
        required_verified = (
            "id", "title", "year", "authors", "venue", "paper_url", "tasks",
            "world_model_scope", "scope_confidence", "consensus_date",
            "consensus_rationale", "classification_rationale", "evidence_locations",
            "representation_space", "transition_type", "learning_objective",
            "rollout_capability", "notes", "last_checked",
        )
        for line, row in enumerate(self.rows.get(filename, []), start=2):
            verified = row["verified"] == "true"
            example = any(is_example(value) for value in row.values())
            if row["verified"] not in STRICT_BOOLEAN:
                self.error(filename, line, "verified must be true or false")
            if row["consensus_reached"] not in STRICT_BOOLEAN:
                self.error(filename, line, "consensus_reached must be true or false")
            if verified:
                self.summaries[filename].verified_or_approved += 1
            else:
                self.summaries[filename].unverified_or_example += 1
            if example and verified:
                self.error(filename, line, "example records cannot be verified")

            year = row["year"].strip()
            if is_todo(year):
                if verified:
                    self.error(filename, line, "verified paper year must be a valid four-digit year")
            elif not re.fullmatch(r"\d{4}", year) or not 1900 <= int(year) <= date.today().year + 1:
                self.error(filename, line, "year must be TODO for an unverified paper or a valid four-digit year")

            self.controlled(filename, line, "tasks", row["tasks"], "tasks", multiple=True, allow_todo=not verified)
            self.controlled(filename, line, "world_model_scope", row["world_model_scope"], "world_model_scopes", allow_todo=not verified)
            self.controlled(filename, line, "scope_confidence", row["scope_confidence"], "scope_confidences", allow_todo=not verified)
            self.controlled(filename, line, "representation_space", row["representation_space"], "representation_spaces", allow_todo=not verified)
            self.controlled(filename, line, "transition_type", row["transition_type"], "transition_types", multiple=True, allow_todo=not verified)
            self.controlled(filename, line, "learning_objective", row["learning_objective"], "learning_objectives", multiple=True, allow_todo=not verified)
            self.controlled(filename, line, "rollout_capability", row["rollout_capability"], "rollout_capabilities", allow_todo=not verified)
            self.controlled(filename, line, "uncertainty_modeling", row["uncertainty_modeling"], "uncertainty_types", multiple=True)
            self.controlled(filename, line, "application_domain", row["application_domain"], "application_domains", multiple=True)

            for field_name in ("action_conditioned", "physics_informed", "open_source"):
                if row[field_name] not in TRI_STATE_BOOLEAN:
                    self.error(filename, line, f"{field_name} must be true, false, or unknown")
            for field_name in ("paper_url", "code_url"):
                if not valid_url(row[field_name]):
                    self.error(filename, line, f"{field_name} must be empty, TODO, or an HTTP(S) URL")
            if not is_todo(row["last_checked"]) and not valid_date(row["last_checked"]):
                self.error(filename, line, "last_checked must be TODO or YYYY-MM-DD")
            if not is_todo(row["consensus_date"]) and not valid_date(row["consensus_date"]):
                self.error(filename, line, "consensus_date must be TODO or YYYY-MM-DD")
            if row["world_model_scope"] == "uncertain" and row["scope_confidence"] == "high":
                self.error(filename, line, "uncertain scope cannot have high confidence")

            if verified:
                if row["consensus_reached"] != "true":
                    self.error(filename, line, "verified paper requires consensus_reached=true")
                for field_name in required_verified:
                    if is_unresolved(row[field_name]):
                        self.error(filename, line, f"verified paper has unresolved required field {field_name}")
                if not valid_url(row["paper_url"]) or is_todo(row["paper_url"]):
                    self.error(filename, line, "verified paper must have a valid HTTP(S) paper_url")
                if is_todo(row["code_url"]):
                    self.warning(filename, line, "verified paper has no confirmed code URL")

    def validate_datasets(self) -> None:
        filename = "datasets.csv"
        self.check_unique(filename, "name")
        for line, row in enumerate(self.rows.get(filename, []), start=2):
            verified = row["verified"] == "true"
            self.summaries[filename].verified_or_approved += int(verified)
            self.summaries[filename].unverified_or_example += int(not verified)
            if row["verified"] not in STRICT_BOOLEAN:
                self.error(filename, line, "verified must be true or false")
            self.controlled(filename, line, "task", row["task"], "tasks")
            self.controlled(filename, line, "domain", row["domain"], "application_domains")
            for field_name in ("multivariate", "run_to_failure", "contains_actions", "contains_operating_conditions", "redistribution_allowed"):
                if row[field_name] not in TRI_STATE_BOOLEAN:
                    self.error(filename, line, f"{field_name} must be true, false, or unknown")
            if not valid_url(row["official_url"]):
                self.error(filename, line, "official_url must be empty, TODO, or an HTTP(S) URL")
            if not is_todo(row["last_checked"]) and not valid_date(row["last_checked"]):
                self.error(filename, line, "last_checked must be TODO or YYYY-MM-DD")
            if verified and any(is_example(value) for value in row.values()):
                self.error(filename, line, "example records cannot be verified")

    def validate_methods(self) -> None:
        filename = "methods.csv"
        self.check_unique(filename, "method")
        for line, row in enumerate(self.rows.get(filename, []), start=2):
            self.summaries[filename].unverified_or_example += 1
            self.controlled(filename, line, "task", row["task"], "tasks")
            self.controlled(filename, line, "world_model_scope", row["world_model_scope"], "world_model_scopes")
            self.controlled(filename, line, "representation_space", row["representation_space"], "representation_spaces")
            self.controlled(filename, line, "transition_type", row["transition_type"], "transition_types", multiple=True)
            self.controlled(filename, line, "learning_objective", row["learning_objective"], "learning_objectives", multiple=True)
            self.controlled(filename, line, "rollout_capability", row["rollout_capability"], "rollout_capabilities")
            for field_name in ("probabilistic", "action_conditioned", "physics_informed", "open_source"):
                if row[field_name] not in TRI_STATE_BOOLEAN:
                    self.error(filename, line, f"{field_name} must be true, false, or unknown")
            if row["reproduction_status"] not in REPRODUCTION_STATUSES:
                self.error(filename, line, f"invalid reproduction_status {row['reproduction_status']!r}")

    def validate_repositories(self) -> None:
        filename = "repositories.csv"
        self.check_unique(filename, "id")
        required = ("id", "name", "category", "url", "description", "relationship", "last_checked")
        for line, row in enumerate(self.rows.get(filename, []), start=2):
            verified = row["verified"] == "true"
            self.summaries[filename].verified_or_approved += int(verified)
            self.summaries[filename].unverified_or_example += int(not verified)
            if row["verified"] not in STRICT_BOOLEAN:
                self.error(filename, line, "verified must be true or false")
            self.controlled(filename, line, "category", row["category"], "repository_categories")
            if not valid_url(row["url"]):
                self.error(filename, line, "url must be empty, TODO, or an HTTP(S) URL")
            if not is_todo(row["last_checked"]) and not valid_date(row["last_checked"]):
                self.error(filename, line, "last_checked must be TODO or YYYY-MM-DD")
            if verified:
                if any(is_example(value) for value in row.values()):
                    self.error(filename, line, "example records cannot be verified")
                for field_name in required:
                    if is_unresolved(row[field_name]):
                        self.error(filename, line, f"verified repository has unresolved field {field_name}")
                if is_todo(row["url"]):
                    self.error(filename, line, "verified repository must have a valid HTTP(S) URL")

    def validate_reviews(self) -> None:
        filename = "paper_reviews.csv"
        paper_ids = {row["id"] for row in self.rows.get("papers.csv", [])}
        seen: dict[tuple[str, str], int] = {}
        for line, row in enumerate(self.rows.get(filename, []), start=2):
            approved = row["approved"] == "true"
            example = any(is_example(value) for value in row.values())
            self.summaries[filename].verified_or_approved += int(approved)
            self.summaries[filename].unverified_or_example += int(not approved)
            if row["approved"] not in STRICT_BOOLEAN:
                self.error(filename, line, "approved must be true or false")
            if example and approved:
                self.error(filename, line, "example reviews cannot be approved")
            if row["paper_id"] not in paper_ids:
                self.error(filename, line, f"paper_id {row['paper_id']!r} does not reference papers.csv")
            if is_todo(row["reviewer"]):
                self.error(filename, line, "reviewer cannot be empty or TODO")
            if not valid_date(row["review_date"]):
                self.error(filename, line, "review_date must be YYYY-MM-DD")
            pair = (row["paper_id"], row["reviewer"].strip().casefold())
            if pair in seen:
                self.error(filename, line, f"duplicate paper/reviewer pair; first seen on line {seen[pair]}")
            else:
                seen[pair] = line
            for number in range(1, 8):
                self.controlled(filename, line, f"q{number}", row[f"q{number}"], "review_answers", allow_todo=False)
            self.controlled(filename, line, "proposed_scope", row["proposed_scope"], "world_model_scopes", allow_todo=False)
            self.controlled(filename, line, "scope_confidence", row["scope_confidence"], "scope_confidences", allow_todo=False)
            if row["proposed_scope"] == "uncertain" and row["scope_confidence"] == "high":
                self.error(filename, line, "uncertain proposed_scope cannot have high confidence")
            for field_name in ("classification_rationale", "evidence_locations"):
                if is_todo(row[field_name]):
                    self.error(filename, line, f"{field_name} cannot be empty or TODO")

    def validate_search_runs(self) -> None:
        filename = "search_runs.csv"
        self.check_unique(filename, "search_id")
        for line, row in enumerate(self.rows.get(filename, []), start=2):
            verified = row["verified"] == "true"
            self.summaries[filename].verified_or_approved += int(verified)
            self.summaries[filename].unverified_or_example += int(not verified)
            if row["verified"] not in STRICT_BOOLEAN:
                self.error(filename, line, "verified must be true or false")
            for field_name in ("search_date", "date_start", "date_end"):
                if not is_todo(row[field_name]) and not valid_date(row[field_name]):
                    self.error(filename, line, f"{field_name} must be TODO or YYYY-MM-DD")
            if not is_todo(row["result_count"]):
                try:
                    if int(row["result_count"]) < 0:
                        raise ValueError
                except ValueError:
                    self.error(filename, line, "result_count must be TODO or a non-negative integer")
            if verified:
                if any(is_example(value) for value in row.values()):
                    self.error(filename, line, "example search runs cannot be verified")
                for field_name in ("search_id", "database", "query", "search_date", "result_count"):
                    if is_unresolved(row[field_name]):
                        self.error(filename, line, f"verified search run has unresolved field {field_name}")

    def validate_screening(self) -> None:
        filename = "screening.csv"
        self.check_unique(filename, "screening_id")
        search_ids = {row["search_id"] for row in self.rows.get("search_runs.csv", [])}
        candidate_stages: dict[tuple[str, str], int] = {}
        for line, row in enumerate(self.rows.get(filename, []), start=2):
            self.summaries[filename].unverified_or_example += 1
            for field_name in ("candidate_id", "title"):
                if is_todo(row[field_name]):
                    self.error(filename, line, f"{field_name} cannot be empty or TODO")
            self.controlled(filename, line, "stage", row["stage"], "screening_stages", allow_todo=False)
            pair = (row["candidate_id"].strip(), row["stage"].strip())
            if pair in candidate_stages:
                self.error(
                    filename,
                    line,
                    f"duplicate candidate_id/stage pair; first seen on line {candidate_stages[pair]}",
                )
            else:
                candidate_stages[pair] = line
            if not valid_doi(row["doi"]):
                self.error(filename, line, "doi must be empty, TODO, or a canonical bare DOI")
            if not valid_url(row["source_url"]):
                self.error(filename, line, "source_url must be empty, TODO, or an HTTP(S) URL")
            source_ids = []
            if not is_todo(row["source_search_ids"]):
                if "," in row["source_search_ids"]:
                    self.error(filename, line, "source_search_ids must use semicolons, not commas")
                source_ids = [value.strip() for value in row["source_search_ids"].split(";")]
                if any(not value for value in source_ids):
                    self.error(filename, line, "source_search_ids contains an empty value")
                if len(source_ids) != len(set(source_ids)):
                    self.error(filename, line, "source_search_ids contains duplicate values")
            for search_id in source_ids:
                if search_id not in search_ids:
                    self.error(filename, line, f"source_search_id {search_id!r} does not reference search_runs.csv")
            for field_name in ("decision_1", "decision_2", "consensus_decision"):
                self.controlled(filename, line, field_name, row[field_name], "screening_decisions")
            for reviewer_field, decision_field in (("reviewer_1", "decision_1"), ("reviewer_2", "decision_2")):
                if is_todo(row[reviewer_field]) != is_todo(row[decision_field]):
                    self.error(filename, line, f"{reviewer_field} and {decision_field} must be completed together")
            reviewers_complete = not is_todo(row["reviewer_1"]) and not is_todo(row["reviewer_2"])
            if reviewers_complete and row["reviewer_1"].strip().casefold() == row["reviewer_2"].strip().casefold():
                self.error(filename, line, "reviewer_1 and reviewer_2 must be different people")
            consensus = row["consensus_decision"].strip()
            if not is_todo(consensus) and consensus != "pending":
                if not reviewers_complete:
                    self.error(filename, line, "completed consensus requires both reviewers")
                for decision_field in ("decision_1", "decision_2"):
                    if is_todo(row[decision_field]) or row[decision_field] == "pending":
                        self.error(filename, line, f"completed consensus requires a non-pending {decision_field}")
            if consensus == "exclude" and is_unresolved(row["exclusion_reason"]):
                self.error(filename, line, "exclude consensus requires a non-placeholder exclusion_reason")
            if not is_todo(row["last_checked"]) and not valid_date(row["last_checked"]):
                self.error(filename, line, "last_checked must be TODO or YYYY-MM-DD")

    def validate_paper_consensus(self) -> None:
        reviews_by_paper: dict[str, list[dict[str, str]]] = {}
        for review in self.rows.get("paper_reviews.csv", []):
            if review["approved"] == "true" and not any(is_example(value) for value in review.values()):
                reviews_by_paper.setdefault(review["paper_id"], []).append(review)
        for line, paper in enumerate(self.rows.get("papers.csv", []), start=2):
            if paper["verified"] != "true":
                continue
            reviews = reviews_by_paper.get(paper["id"], [])
            reviewers = {review["reviewer"].strip().casefold() for review in reviews}
            if len(reviewers) < 2:
                self.error("papers.csv", line, "verified paper requires approved reviews from at least two different reviewers")
                continue
            scopes = {review["proposed_scope"] for review in reviews}
            confidences = {review["scope_confidence"] for review in reviews}
            if len(scopes) > 1 or len(confidences) > 1:
                rationale = paper["consensus_rationale"].strip().casefold()
                missing_values = sorted(
                    value for value in scopes | confidences if value.casefold() not in rationale
                )
                if missing_values or not any(token in rationale for token in ("resolv", "consensus", "adjudicat")):
                    self.error(
                        "papers.csv",
                        line,
                        "review disagreement requires consensus_rationale to name the differing values and explain resolution",
                    )

    def run(self) -> int:
        self.load_vocabularies()
        self.load_csv_files()
        if not self.summaries["vocabularies.json"].errors:
            self.validate_papers()
            self.validate_datasets()
            self.validate_methods()
            self.validate_repositories()
            self.validate_reviews()
            self.validate_search_runs()
            self.validate_screening()
            self.validate_paper_consensus()

        all_warnings = [item for summary in self.summaries.values() for item in summary.warnings]
        all_errors = [item for summary in self.summaries.values() for item in summary.errors]
        for warning in all_warnings:
            print(f"WARNING: {warning}", file=sys.stderr)

        print("Metadata validation summary by file:")
        for filename, summary in self.summaries.items():
            print(
                f"- {filename}: records={summary.records}, "
                f"verified/approved={summary.verified_or_approved}, "
                f"unverified/example={summary.unverified_or_example}, "
                f"warnings={len(summary.warnings)}, errors={len(summary.errors)}"
            )
        print(
            f"Totals: records={sum(item.records for item in self.summaries.values())}, "
            f"verified/approved={sum(item.verified_or_approved for item in self.summaries.values())}, "
            f"unverified/example={sum(item.unverified_or_example for item in self.summaries.values())}, "
            f"warnings={len(all_warnings)}, errors={len(all_errors)}"
        )
        if all_errors:
            print(f"Metadata validation failed with {len(all_errors)} error(s):", file=sys.stderr)
            for error in all_errors:
                print(f"- {error}", file=sys.stderr)
            return 1
        print("Metadata validation passed.")
        return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=ROOT / "data")
    return parser.parse_args()


def main() -> int:
    return MetadataValidator(parse_args().data_dir).run()


if __name__ == "__main__":
    raise SystemExit(main())
