"""Calculation history model."""

from __future__ import annotations


class CalculationHistory:
    """Store the calculations performed during the current application session."""

    def __init__(self) -> None:
        self._entries: list[str] = []

    def add(self, expression: str, result: str) -> None:
        """Add a calculation to the history."""
        self._entries.append(f"{expression} = {result}")

    def entries(self) -> list[str]:
        """Return the history from oldest to newest."""
        return list(self._entries)

    def clear(self) -> None:
        """Remove all calculations from the history."""
        self._entries.clear()
