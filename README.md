# AirOps Evidence Analyst

An interview-ready, evidence-first analytics vertical slice built from the existing FinSync prototype. It demonstrates deterministic SQL, hybrid retrieval, explicit routing, citations, and an inspectable tool trace over a small synthetic operations dataset.

```mermaid
flowchart LR
  Q[Question] --> R[Explicit router]
  R --> SQL[Read-only SQLite analytics]
  R --> RET[Lexical + hashed-vector retrieval]
  SQL --> T[Trace + citation]
  RET --> T
  T --> A[Answer or abstain]
```

## Run locally

```bash
python3 -m pytest -q tests
PYTHONPATH=. python3 evaluation/run_evaluation.py
```

The evaluation is offline and reproducible. It uses 20 synthetic cases and a 20-row fixture in `air_ops/data/operations.csv`; the data is not an airline feed and the result is not a production quality claim.

## What is demonstrated

- SQL is restricted to one bounded `SELECT`, `WITH`, or `EXPLAIN` statement against an in-memory copy of the fixture.
- Retrieval returns evidence IDs and citations; retrieved text is treated as untrusted data, including the prompt-injection fixture.
- The route and each tool call are returned in a JSON trace.
- Unsupported, live, or instruction-bypassing requests abstain.

The original FastAPI/React application remains in `backend/` and `frontend/` as the prototype surface. Its optional LLM, web-search, and PDF ingestion integrations require separately configured providers and are not used by the deterministic evaluation.

## Limitations

This is a portfolio reference slice, not a financial adviser, airline operations system, or hosted production service. The hashed-vector baseline is deterministic rather than a quality-validated embedding model; the fixture is synthetic; no current-data, privacy, latency, or provider-isolation guarantee is implied.
