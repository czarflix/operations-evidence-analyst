# Evaluation

`evaluation/cases.jsonl` contains 21 deterministic fixture cases covering the bounded SQL templates, glossary retrieval, combined evidence, unsupported questions, and one prompt-injection regression. Run:

```bash
PYTHONPATH=. python3 evaluation/run_evaluation.py
```

The command reports `fixture_regression_pass` only when every checked-in case passes. A case passes when the rule-based router selects the expected route and the formatted answer contains one required substring.

This is a same-repository regression check, not an independently authored benchmark. It does not measure model accuracy, SQL-generation correctness beyond the three templates, retrieval relevance, evidence entailment, numeric generalization, or live-data behavior. The synthetic cases and implementation are intentionally small and deterministic.
