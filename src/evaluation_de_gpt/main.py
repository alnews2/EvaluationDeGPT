"""Application entry point."""

from __future__ import annotations

import sys
from decimal import Decimal, InvalidOperation

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QPushButton, QWidget

from .calculator import CalculatorError, calculate


class CalculatorWindow(QMainWindow):
    """Simple desktop calculator for the four basic operations."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Calculatrice")
        self.setFixedSize(320, 440)

        self._display = "0"
        self._left: str | None = None
        self._operator: str | None = None
        self._waiting_for_operand = False

        self._display_label = QLabel(self._display)
        self._display_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self._display_label.setMinimumHeight(70)
        self._display_label.setObjectName("display")

        central = QWidget()
        layout = QGridLayout(central)
        layout.setSpacing(8)
        layout.addWidget(self._display_label, 0, 0, 1, 4)

        buttons = [
            ("C", 1, 0, self.clear), ("⌫", 1, 1, self.backspace),
            ("÷", 1, 3, lambda: self.set_operator("÷")),
            ("7", 2, 0, lambda: self.input_digit("7")),
            ("8", 2, 1, lambda: self.input_digit("8")),
            ("9", 2, 2, lambda: self.input_digit("9")),
            ("×", 2, 3, lambda: self.set_operator("×")),
            ("4", 3, 0, lambda: self.input_digit("4")),
            ("5", 3, 1, lambda: self.input_digit("5")),
            ("6", 3, 2, lambda: self.input_digit("6")),
            ("-", 3, 3, lambda: self.set_operator("-")),
            ("1", 4, 0, lambda: self.input_digit("1")),
            ("2", 4, 1, lambda: self.input_digit("2")),
            ("3", 4, 2, lambda: self.input_digit("3")),
            ("+", 4, 3, lambda: self.set_operator("+")),
            ("0", 5, 0, lambda: self.input_digit("0")),
            (",", 5, 1, self.input_decimal),
            ("=", 5, 2, self.equals),
            ("±", 5, 3, self.toggle_sign),
        ]

        for text, row, column, callback in buttons:
            button = QPushButton(text)
            button.setMinimumHeight(55)
            button.clicked.connect(callback)
            layout.addWidget(button, row, column)

        self.setCentralWidget(central)
        self.setStyleSheet(
            "QLabel#display { font-size: 30px; padding: 8px; border: 1px solid #999; }"
            "QPushButton { font-size: 18px; }"
        )

    def _refresh(self) -> None:
        self._display_label.setText(self._display)

    def input_digit(self, digit: str) -> None:
        if self._waiting_for_operand or self._display == "0":
            self._display = digit
            self._waiting_for_operand = False
        else:
            self._display += digit
        self._refresh()

    def input_decimal(self) -> None:
        if self._waiting_for_operand:
            self._display = "0"
            self._waiting_for_operand = False
        if "." not in self._display:
            self._display += "."
        self._refresh()

    def set_operator(self, operator: str) -> None:
        if self._operator and not self._waiting_for_operand:
            self._calculate_pending()
        self._left = self._display
        self._operator = operator
        self._waiting_for_operand = True

    def _calculate_pending(self) -> None:
        if self._left is None or self._operator is None:
            return
        self._display = calculate(self._left, self._operator, self._display)
        self._left = None
        self._operator = None
        self._waiting_for_operand = True
        self._refresh()

    def equals(self) -> None:
        if self._operator is None:
            return
        try:
            self._calculate_pending()
        except CalculatorError as exc:
            self._display = "Erreur"
            self._left = None
            self._operator = None
            self._waiting_for_operand = True
            self._refresh()
            return

    def clear(self) -> None:
        self._display = "0"
        self._left = None
        self._operator = None
        self._waiting_for_operand = False
        self._refresh()

    def backspace(self) -> None:
        if self._waiting_for_operand or self._display == "Erreur":
            return
        self._display = self._display[:-1] or "0"
        self._refresh()

    def toggle_sign(self) -> None:
        if self._display == "0" or self._display == "Erreur":
            return
        self._display = self._display[1:] if self._display.startswith("-") else "-" + self._display
        self._refresh()


def main() -> int:
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
