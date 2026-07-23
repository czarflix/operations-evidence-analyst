"""Small, inspectable routing policy used by the offline reference service."""

from __future__ import annotations

import re


def route(question: str) -> str:
    text = question.lower()
    if any(word in text for word in ("ignore", "bypass", "perfect score", "secret")):
        return "abstain"
    asks_sql = bool(re.search(r"\b(average|mean|count|how many|airport|origin|destination)\b", text))
    asks_docs = bool(re.search(r"\b(define|definition|meaning|glossary|runbook|why|what does|synthetic|flag|live|explain)\b", text))
    if "what does" in text and not re.search(r"\b(average|count|how many)\b", text):
        return "retrieval"
    if asks_docs and not asks_sql:
        return "retrieval"
    if asks_sql and asks_docs:
        return "both"
    if asks_sql:
        return "sql"
    if asks_docs:
        return "retrieval"
    return "abstain"
