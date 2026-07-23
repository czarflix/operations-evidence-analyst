# Architecture and evidence contract

The public reference path is intentionally smaller than the original provider-backed prototype:

1. `air_ops.router` selects SQL, retrieval, both, or abstain using an explicit policy.
2. `air_ops.dataset` loads a bundled synthetic CSV into an in-memory SQLite database and permits one read-only statement.
3. `air_ops.retrieval` combines token overlap with a deterministic hashed-vector similarity baseline.
4. `air_ops.service` returns the answer, route, tool trace, evidence IDs, and citations.

The provider-backed FastAPI path is retained for comparison, but its optional external services are not silently represented as measured capabilities of this offline slice.
