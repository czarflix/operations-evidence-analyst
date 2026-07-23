"""Read-only analytics over the bundled synthetic operations fixture."""

from __future__ import annotations

import csv
import re
import sqlite3
from pathlib import Path
from typing import Any

DATA_PATH = Path(__file__).parent / "data" / "operations.csv"

_MUTATION = re.compile(
    r"\b(?:ALTER|ATTACH|CREATE|DELETE|DETACH|DROP|INSERT|PRAGMA|REINDEX|REPLACE|UPDATE|VACUUM)\b",
    re.IGNORECASE,
)


def load_rows() -> list[dict[str, str]]:
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _connection() -> sqlite3.Connection:
    connection = sqlite3.connect(":memory:")
    connection.row_factory = sqlite3.Row
    connection.execute(
        """CREATE TABLE operations (
            flight_id TEXT, flight_date TEXT, origin TEXT, destination TEXT,
            delay_minutes INTEGER, cancellation_flag INTEGER, aircraft_type TEXT,
            weather_flag INTEGER, maintenance_flag INTEGER, passengers INTEGER,
            turnaround_minutes INTEGER, gate_changes INTEGER
        )"""
    )
    columns = list(load_rows()[0])
    values = [[int(row[c]) if c not in {"flight_id", "flight_date", "origin", "destination", "aircraft_type"} else row[c] for c in columns] for row in load_rows()]
    connection.executemany(f"INSERT INTO operations ({','.join(columns)}) VALUES ({','.join('?' for _ in columns)})", values)
    connection.commit()
    return connection


def run_read_only(sql: str) -> list[dict[str, Any]]:
    """Execute one bounded read-only statement and return JSON-safe rows."""
    normalized = sql.strip()
    if not normalized or not re.match(r"^(?:SELECT|WITH|EXPLAIN)\b", normalized, re.IGNORECASE):
        raise ValueError("only SELECT, WITH, and EXPLAIN statements are allowed")
    if ";" in normalized.rstrip(";") or _MUTATION.search(normalized):
        raise ValueError("statement is outside the read-only analytics boundary")
    with _connection() as connection:
        return [dict(row) for row in connection.execute(normalized).fetchmany(100)]
