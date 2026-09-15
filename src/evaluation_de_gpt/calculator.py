"""Core logic for the four-operation calculator."""

from __future__ import annotations

from decimal import Decimal, DivisionByZero, InvalidOperation


class CalculatorError(ValueError):
    """Raised when a calculator operation cannot be completed."""


def calculate(left: str, operator: str, right: str) -> str:
    """Calculate one binary operation and return a display-friendly result."""
    try:
        a = Decimal(left)
        b = Decimal(right)
    except InvalidOperation as exc:
        raise CalculatorError("Invalid number") from exc

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "×":
        result = a * b
    elif operator == "÷":
        if b == 0:
            raise CalculatorError("Division by zero")
        try:
            result = a / b
        except DivisionByZero as exc:
            raise CalculatorError("Division by zero") from exc
    else:
        raise CalculatorError("Unknown operator")

    return format_decimal(result)


def format_decimal(value: Decimal) -> str:
    """Format a Decimal without unnecessary trailing zeroes."""
    if value == value.to_integral_value():
        return str(value.quantize(Decimal("1")))
    text = format(value.normalize(), "f")
    return text.rstrip("0").rstrip(".")
