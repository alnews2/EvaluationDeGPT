import pytest

from evaluation_de_gpt.calculator import CalculatorError, calculate


@pytest.mark.parametrize(
    ("left", "operator", "right", "expected"),
    [
        ("2", "+", "3", "5"),
        ("7.5", "-", "2.5", "5"),
        ("6", "×", "4", "24"),
        ("10", "÷", "4", "2.5"),
        ("0.1", "+", "0.2", "0.3"),
    ],
)
def test_calculate_basic_operations(left, operator, right, expected):
    assert calculate(left, operator, right) == expected


def test_division_by_zero_is_rejected():
    with pytest.raises(CalculatorError, match="Division by zero"):
        calculate("10", "÷", "0")


def test_unknown_operator_is_rejected():
    with pytest.raises(CalculatorError, match="Unknown operator"):
        calculate("10", "%", "2")


def test_invalid_number_is_rejected():
    with pytest.raises(CalculatorError, match="Invalid number"):
        calculate("abc", "+", "2")
