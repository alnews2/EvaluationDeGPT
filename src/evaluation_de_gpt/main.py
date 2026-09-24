"""Application entry point."""

from __future__ import annotations

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QCloseEvent, QMoveEvent
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QWidget,
)

from .calculator import CalculatorError, calculate
from .history import CalculationHistory
from .history_window import HistoryWindow


class CalculatorWindow(QMainWindow):
    """Simple desktop calculator for the four basic operations."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Calculatrice")
        self.setFixedSize(320, 575)

        self._display = "0"
        self._left: str | None = None
        self._operator: str | None = None
        self._waiting_for_operand = False
        self._memory: str | None = None
        self._history = CalculationHistory()
        self._history_window: HistoryWindow | None = None

        self._display_label = QLabel(self._display)
        self._display_label.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        self._display_label.setMinimumHeight(70)
        self._display_label.setObjectName("display")

        self._memory_label = QLabel(self._memory_text())
        self._memory_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )
        self._memory_label.setObjectName("memory")

        central = QWidget()
        layout = QGridLayout(central)
        layout.setSpacing(8)
        layout.addWidget(self._display_label, 0, 0, 1, 4)
        layout.addWidget(self._memory_label, 1, 0, 1, 4)

        buttons = [
            ("C", 2, 0, self.clear, 1),
            ("⌫", 2, 1, self.backspace, 1),
            ("÷", 2, 3, lambda: self.set_operator("÷"), 1),
            ("7", 3, 0, lambda: self.input_digit("7"), 1),
            ("8", 3, 1, lambda: self.input_digit("8"), 1),
            ("9", 3, 2, lambda: self.input_digit("9"), 1),
            ("×", 3, 3, lambda: self.set_operator("×"), 1),
            ("4", 4, 0, lambda: self.input_digit("4"), 1),
            ("5", 4, 1, lambda: self.input_digit("5"), 1),
            ("6", 4, 2, lambda: self.input_digit("6"), 1),
            ("-", 4, 3, lambda: self.set_operator("-"), 1),
            ("1", 5, 0, lambda: self.input_digit("1"), 1),
            ("2", 5, 1, lambda: self.input_digit("2"), 1),
            ("3", 5, 2, lambda: self.input_digit("3"), 1),
            ("+", 5, 3, lambda: self.set_operator("+"), 1),
            ("0", 6, 0, lambda: self.input_digit("0"), 1),
            (",", 6, 1, self.input_decimal, 1),
            ("=", 6, 2, self.equals, 1),
            ("±", 6, 3, self.toggle_sign, 1),
            ("M", 7, 0, self.memory_store, 1),
            ("MR", 7, 1, self.memory_recall, 1),
            ("Historique", 8, 0, self.show_history, 2),
        ]

        for text, row, column, callback, column_span in buttons:
            button = QPushButton(text)
            button.setMinimumHeight(55)
            button.clicked.connect(callback)
            layout.addWidget(button, row, column, 1, column_span)

        self._credit_label = QLabel(
            "« Application générée par l'intelligence artificielle GPT de la société OpenAI »."
        )
        self._credit_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._credit_label.setWordWrap(True)
        self._credit_label.setObjectName("credit")
        layout.addWidget(self._credit_label, 9, 0, 1, 4)

        self.setCentralWidget(central)
        self.setStyleSheet(
            "QLabel#display { font-size: 30px; padding: 8px; color: white; "
            "background-color: black; border: 1px solid #999; }"
            "QLabel#memory { font-size: 13px; padding: 3px 8px; }"
            "QPushButton { font-size: 18px; }"
            "QLabel#credit { font-size: 10px; padding: 6px; }"
        )

    def _memory_text(self) -> str:
        return f"Mémoire : {self._memory if self._memory is not None else '—'}"

    def _refresh(self) -> None:
        self._display_label.setText(self._display)
        self._memory_label.setText(self._memory_text())

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
        expression = f"{self._left} {self._operator} {self._display}"
        self._display = calculate(self._left, self._operator, self._display)
        self._history.add(expression, self._display)
        self._left = None
        self._operator = None
        self._waiting_for_operand = True
        self._refresh()
        if self._history_window is not None:
            self._history_window.refresh()

    def equals(self) -> None:
        if self._operator is None:
            return
        try:
            self._calculate_pending()
        except CalculatorError:
            self._display = "Erreur"
            self._left = None
            self._operator = None
            self._waiting_for_operand = True
            self._refresh()

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
        self._display = (
            self._display[1:]
            if self._display.startswith("-")
            else "-" + self._display
        )
        self._refresh()

    def memory_store(self) -> None:
        """Store the displayed number in the calculator memory."""
        if self._display != "Erreur":
            self._memory = self._display
            self._refresh()

    def memory_recall(self) -> None:
        """Insert the stored number as if it had been typed on the keyboard."""
        if self._memory is None:
            return
        if self._waiting_for_operand or self._display in {"0", "Erreur"}:
            self._display = self._memory
            self._waiting_for_operand = False
        else:
            self._display += self._memory
        self._refresh()

    def _position_history_window(self) -> None:
        if self._history_window is None:
            return
        main_top_left = self.frameGeometry().topLeft()
        history_width = self._history_window.frameGeometry().width()
        history_top_left = main_top_left
        history_top_left.setX(main_top_left.x() - history_width + 1)
        self._history_window.move(history_top_left)

    def show_history(self) -> None:
        """Show the calculation history window."""
        if self._history_window is None:
            self._history_window = HistoryWindow(self._history, self)
        self._history_window.refresh()
        self._history_window.show()
        self._position_history_window()
        self._history_window.raise_()
        self._history_window.activateWindow()

    def moveEvent(self, event: QMoveEvent) -> None:
        """Keep the history window attached to the main window."""
        super().moveEvent(event)
        if self._history_window is not None and self._history_window.isVisible():
            self._position_history_window()

    def closeEvent(self, event: QCloseEvent) -> None:
        """Close the history window when the main window closes."""
        if self._history_window is not None:
            self._history_window.close()
            self._history_window = None
        super().closeEvent(event)


def main() -> int:
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
