"""Run the reproducible offline evaluation and print a compact summary."""

from __future__ import annotations

import json
from pathlib import Path

from air_ops import answer_question


def main() -> None:
    cases = [json.loads(line) for line in (Path(__file__).parent / "cases.jsonl").read_text().splitlines() if line.strip()]
    passed = 0
    for case in cases:
        result = answer_question(case["question"])
        ok = result["route"] == case["expected_route"] and case["must_contain"].lower() in result["answer"].lower()
        passed += int(ok)
        if not ok:
            print(json.dumps({"question": case["question"], "expected": case, "actual": result}, sort_keys=True))
    all_passed = passed == len(cases)
    print(
        json.dumps(
            {
                "cases": len(cases),
                "passed": passed,
                "fixture_pass_rate": round(passed / len(cases), 4),
                "result": "fixture_regression_pass" if all_passed else "fixture_regression_fail",
            },
            sort_keys=True,
        )
    )
    raise SystemExit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
