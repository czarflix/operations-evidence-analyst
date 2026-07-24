# AirOps Evidence Analyst: Interview Boundary Guide

Use this project as a compact example of making a prototype's evidence boundaries inspectable. Do not present it as a production RAG platform, a general text-to-SQL system, or an accuracy benchmark.

## Defensible one-sentence description

AirOps is a deterministic reference fixture that routes a small set of synthetic operations questions to bounded SQLite templates, a checked-in retrieval corpus, both tools, or abstention, while returning citations and a tool trace.

## What I can demonstrate from the repository

- A read-only SQL boundary rejects mutations and multiple statements.
- A transparent keyword policy selects `sql`, `retrieval`, `both`, or `abstain`.
- Three hard-coded SQL templates query a 20-row synthetic CSV loaded into in-memory SQLite.
- A six-item synthetic corpus is ranked with token overlap and a 64-bin hashed bag-of-words vector.
- Returned JSON exposes the selected route, tool calls, result rows, evidence IDs, and citations.
- A prompt-injection fixture is treated as untrusted data and excluded from answer evidence.
- Twenty-one checked-in cases provide an offline fixture-regression check.

## What I must not claim

- The 21-case pass is not model accuracy or benchmark performance.
- The router is not learned, agentic, or LLM-based.
- The SQL path is not general natural-language SQL generation.
- The retrieval path is not validated against an independently judged relevance set.
- The answer layer does not synthesize a narrative or verify citation entailment.
- The fixture is not live airline data, and the project is not an operational airline system.
- The retained FastAPI/React prototype and optional provider integrations are not part of the measured deterministic path.

## Useful technical discussion

### Why deterministic rules here?

They make the control flow, failure modes, and test expectations easy to inspect. That is useful for a safety/reference slice, but it trades away generalization and should not be confused with a learned analytics agent.

### What does the SQL boundary prove?

It proves that this local path accepts one bounded read-only statement and rejects obvious mutation keywords and multiple statements. It does not prove complete SQL sandboxing for an untrusted multi-tenant service.

### What does the retrieval score mean?

It is a deterministic blend of token overlap and cosine similarity over hashed token counts. It is only a ranking heuristic for the small checked-in corpus; no retrieval-quality metric is claimed.

### What would make this a stronger benchmark?

A separate synthetic-data generator and data dictionary, independently authored cases, broader query families, validated structured query plans, category-level metrics, exact numeric checks, evidence-entailment labels, adversarial cases, and failure analysis.

## Reproduce the checked-in proof

```bash
python3 -m pytest -q tests
PYTHONPATH=. python3 evaluation/run_evaluation.py
```

The expected evaluator label is `fixture_regression_pass`. Report the case count and limitations with the result; never restate it as accuracy.
