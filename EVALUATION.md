# Evaluation

`evaluation/cases.jsonl` contains 20 deterministic cases covering SQL aggregation, glossary retrieval, combined evidence, unsupported questions, and prompt-injection resistance. Run:

```bash
PYTHONPATH=. python3 evaluation/run_evaluation.py
```

The command reports the measured pass count. It is a fixture-level regression check, not a benchmark, production accuracy estimate, or live-data validation.
