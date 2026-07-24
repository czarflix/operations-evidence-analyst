# AirOps Positioning Fix Verification

Date: 2026-07-23

## Fix Contract

- Expectation: present AirOps as a small deterministic safety/reference fixture and make its proof limits explicit.
- Broken contract: recruiter-facing copy overstated readiness, documented 20 cases when 21 exist, emitted an `accuracy` field, and retained a long production-RAG/financial-advice interview guide unrelated to the measured path.
- In scope: `README.md`, `EVALUATION.md`, evaluator result labels, the evaluator-label regression test, and the stale interview guide.
- Out of scope: router, SQL templates, retrieval algorithm, synthetic data, legacy provider-backed prototype, deployments, providers, and remotes.
- Preserved behavior: all 21 existing cases, read-only SQL checks, citations, trace output, abstention, and prompt-injection handling.

## Pass 1 Candidate Shape

The first candidate corrected the case count, replaced benchmark-like language with fixture-regression language, documented the exact router/SQL/retrieval/evaluation boundaries, renamed the result fields, added a focused regression check, and replaced the stale 868-line interview guide with a concise boundary guide.

## New Evidence Learned After Pass 1

- The fixture contains 21 cases and the CSV contains 20 data rows plus one header row.
- The implementation has three hard-coded SQL templates and six checked-in retrieval documents.
- The existing regression suite remained green after the labeling change.
- No evidence required changing the deterministic implementation.

## Pass 2 Clean Fix Shape

Starting fresh, the clean fix is the same: change only claims, evaluator labels, their focused proof, and the directly contradictory interview document. Expanding the benchmark or refactoring the implementation would exceed the fast-safe repair contract.

## Decision

Kept. The pass-1 structure matches the independently restated pass-2 design.

## Why The Final Implementation Is Not A Patched-Forward Compromise

The final diff has one owner for each problem: recruiter copy defines the boundary, the evaluator reports a fixture label, and one regression test locks that label. The stale interview guide was replaced rather than accumulating disclaimers around contradictory production claims.

## Red-Green Proof

- Before: `PYTHONPATH=. python3 evaluation/run_evaluation.py` emitted `accuracy: 1.0` for 21 cases while the README and evaluation guide said 20.
- After: the command emits `result: fixture_regression_pass`, `cases: 21`, `passed: 21`, and `fixture_pass_rate: 1.0`.
- The new regression test would fail against the prior `accuracy`-labeled output.

## Minimality Proof

- Changed: three recruiter/proof documents, the evaluator’s summary label, and one focused test file.
- Untouched: router, SQL, retrieval, service behavior, data, frontend/backend prototype code, secrets, provider configuration, and remote state.

## Validation Results

- `python3 -m pytest -q tests`: 4 passed.
- `PYTHONPATH=. python3 evaluation/run_evaluation.py`: 21/21 checked-in cases, labeled `fixture_regression_pass`.
- `git diff --check`: passed.
- Determinism: all changed tests use checked-in files and local subprocess execution; no network, time, randomness, or provider dependency.

## Failure Classification

- Branch-caused failures: none.
- Unrelated/pre-existing failures: none observed in the executed scope.
- Inconclusive: no claim is made about the retained provider-backed prototype or any deployment because those surfaces were not exercised.
