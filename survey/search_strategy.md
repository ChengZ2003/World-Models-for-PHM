# Search Strategy

> **Status: Draft.** This protocol describes the intended review process. It does not claim that any database search, screening round, or snowballing pass has been completed.

## Review Type

The planned study is a structured survey with systematic search, auditable screening, mechanism-based classification, and transparent limitations. It is not currently registered as a formal systematic review. Any later protocol registration must be recorded explicitly.

## Research Questions

The search and extraction process is organized around the nine questions in [`research_questions.md`](research_questions.md), covering definitions, state representations, temporal dynamics, rollouts, uncertainty, boundaries with related predictive models, evaluation resources, reproducibility, and research gaps.

## Target Databases

Draft target candidates are:

- IEEE Xplore
- Scopus
- Web of Science Core Collection
- ACM Digital Library
- ScienceDirect
- SpringerLink
- arXiv

Google Scholar may be considered as a supplementary snowballing aid rather than a primary reproducible export source. The final database list, subscriptions, export capabilities, and access dates are pending maintainer review. Each executed search must be recorded in [`../data/search_runs.csv`](../data/search_runs.csv); a database must not be described as searched until a verified run exists.

## Search Concepts

The draft concept groups are:

1. **Dynamics concepts:** world model, latent dynamics, state transition, state-space model, system identification, trajectory generation, rollout, predictive state.
2. **PHM concepts:** prognostics and health management, condition monitoring, fault prognosis, health assessment, remaining useful life, predictive maintenance.
3. **Anomaly concepts:** anomaly detection, anomaly prediction, early warning, fault detection, multivariate sensor anomaly.
4. **Industrial context:** industrial system, cyber-physical system, machinery, manufacturing, process system, asset degradation.

Terms within a block may be joined with `OR`; concept blocks may be joined with `AND`. Database-specific syntax must be preserved in the recorded query.

## Draft Query Blocks

The following is a conceptual draft, not evidence of an executed search:

```text
("world model" OR "latent dynamics" OR "state transition" OR rollout OR "predictive state")
AND
("prognostics and health management" OR anomaly OR "early warning" OR prognosis
 OR "remaining useful life" OR "predictive maintenance")
AND
(industrial OR machinery OR manufacturing OR "cyber-physical" OR degradation)
```

Broader and narrower variants should be piloted and documented without silently replacing earlier queries.

## Date Range

Draft policy: no lower or upper publication-year boundary has been finalized. Every search run must record `date_start`, `date_end`, and `search_date`. `TODO` may be used before execution, but a verified search run requires a concrete search date and result count.

## Language Policy

Draft policy: English-language full text is expected to be required for detailed extraction. Non-English records with an English abstract may be retained during title/abstract screening and documented as a limitation if full-text assessment is not feasible. The final policy is pending review.

## Deduplication

Exports should retain a stable search-run identifier. Deduplication should use identifiers such as DOI or database accession when available, followed by normalized title, year, and author checks. Merges and ambiguous duplicates must be traceable; raw export files should not be overwritten.

## Title and Abstract Screening

Two reviewers independently record decisions in [`../data/screening.csv`](../data/screening.csv). Allowed decisions come from `data/vocabularies.json`. Candidates advance only after a consensus decision; uncertainty should be retained rather than forced into inclusion or exclusion.

## Full-Text Screening

Full text is assessed against the operational definition and seven inclusion questions. Reviewers should identify evidence locations for state representation, transitions, future prediction, PHM use, dynamics centrality, rollout or uncertainty, and terminology-independent classification.

## Inclusion and Exclusion

Include work when it materially informs world-model or dynamics-model mechanisms for anomaly detection, early warning, diagnosis, health assessment, prognosis, RUL, or maintenance decisions. Related predictive models may be retained for explicit comparison.

Exclude general generation unrelated to PHM, static classifiers without temporal dynamics, maintenance text generation without system dynamics, generic reinforcement-learning world models unrelated to reliability, and forecasting with no PHM methodological relevance. Exclusion reasons must be recorded at full-text screening.

## Backward and Forward Snowballing

Backward reference checks and forward citation checks are planned for included seed papers. Each supplementary search must be recorded as a search run or otherwise linked to its source paper and date. No snowballing has yet been claimed as complete.

## Dual-Review Procedure

1. Record the database query and export as a search run.
2. Perform independent title/abstract screening.
3. Perform independent full-text screening for retained candidates.
4. Add candidate metadata to `papers.csv` with `verified=false`.
5. Two reviewers independently complete all seven classification questions in `paper_reviews.csv`.
6. Resolve scope disagreements and document consensus.
7. Set `verified=true` only after metadata, rationale, evidence locations, and two approved reviews agree.

`verified=true` does not mean that experimental claims or results have been independently reproduced.

## Disagreement Resolution

Reviewers first compare evidence locations and the mechanism-based criteria. Unresolved cases remain `uncertain` with low confidence. A third reviewer may adjudicate, but the original reviews must remain visible. Classification must not be forced merely to simplify counts.

## Update Schedule

Draft policy: search updates should be performed before major survey releases and may be scheduled periodically after the first complete search. No fixed cadence has been approved. Every update is a new versioned search run rather than an undocumented overwrite.

## Limitations

Expected limitations include terminology drift, incomplete indexing across disciplines, database-access constraints, English-language bias, inconsistent reporting of dynamics mechanisms, unavailable full text or code, and subjective boundary decisions. Search coverage and reviewer agreement must be reported from recorded evidence rather than assumed.
