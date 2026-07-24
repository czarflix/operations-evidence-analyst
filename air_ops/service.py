"""Answerable, traceable offline question path for local evaluation."""

from __future__ import annotations

from typing import Any

from .dataset import run_read_only
from .retrieval import retrieve
from .router import route


def _sql_for(question: str) -> str:
    text = question.lower()
    if "cancel" in text:
        return "SELECT COUNT(*) AS cancelled_flights FROM operations WHERE cancellation_flag = 1"
    if "airport" in text or "origin" in text:
        return "SELECT origin, ROUND(AVG(delay_minutes), 2) AS average_delay_minutes FROM operations GROUP BY origin ORDER BY origin"
    return "SELECT ROUND(AVG(delay_minutes), 2) AS average_delay_minutes, COUNT(*) AS flight_records FROM operations"


def answer_question(question: str) -> dict[str, Any]:
    selected_route = route(question)
    trace: list[dict[str, Any]] = [{"step": "route", "route": selected_route}]
    citations: list[dict[str, str]] = []
    sql_rows: list[dict[str, Any]] = []
    evidence = []
    if selected_route in {"sql", "both"}:
        sql = _sql_for(question)
        sql_rows = run_read_only(sql)
        trace.append({"step": "sql", "statement": sql, "row_count": len(sql_rows)})
        citations.append({"source": "operations.csv", "kind": "synthetic_dataset"})
    if selected_route in {"retrieval", "both"}:
        evidence = retrieve(question)
        trace.append({"step": "retrieve", "evidence_ids": [item.evidence_id for item in evidence]})
        citations.extend({"source": item.evidence_id, "kind": "synthetic_document"} for item in evidence[:2])
    if selected_route == "abstain":
        answer = "I cannot answer this from the bounded synthetic evidence set."
    elif sql_rows and evidence:
        answer = f"The bounded query returned {sql_rows}; the glossary/runbook evidence is cited separately."
    elif sql_rows:
        answer = f"The bounded analytics query returned {sql_rows}."
    elif evidence:
        answer = evidence[0].text
    else:
        answer = "No supporting evidence was retrieved."
    return {"answer": answer, "route": selected_route, "trace": trace, "citations": citations, "sql_rows": sql_rows, "evidence": [item.__dict__ for item in evidence]}
