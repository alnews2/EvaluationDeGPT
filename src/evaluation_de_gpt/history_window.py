"""History window for the calculator."""

from __future__ import annotations

from PySide6.QtWidgets import QListWidget, QMainWindow, QPushButton, QVBoxLayout, QWidget

from .history import CalculationHistory


class HistoryWindow(QMainWindow):
    """Display the calculations performed during the current session."""

    def __init__(self, history: CalculationHistory) -> None:
        super().__init__()
        self._history = history
        self.setWindowTitle("Historique des calculs")
        self.resize(360, 300)

        self._list = QListWidget()

        clear_button = QPushButton("Effacer l'historique")
        clear_button.clicked.connect(self.clear_history)

        central = QWidget()
        layout = QVBoxLayout(central)
        layout.addWidget(self._list)
        layout.addWidget(clear_button)
        self.setCentralWidget(central)

        self.refresh()

    def refresh(self) -> None:
        """Refresh the list from the history model."""
        self._list.clear()
        self._list.addItems(self._history.entries())

    def clear_history(self) -> None:
        """Clear the history and update the display."""
        self._history.clear()
        self.refresh()
