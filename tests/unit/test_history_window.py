import pytest
from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QApplication

from evaluation_de_gpt.main import CalculatorWindow


@pytest.fixture
def app():
    application = QApplication.instance() or QApplication([])
    yield application


def test_history_window_is_attached_to_main_window(app):
    window = CalculatorWindow()

    window.show_history()
    app.processEvents()

    assert window._history_window is not None
    assert window._history_window.parentWidget() is window

    window.close()


def test_history_window_is_aligned_with_main_window(app):
    window = CalculatorWindow()
    window.move(200, 150)

    window.show_history()
    app.processEvents()

    assert window._history_window is not None
    assert window._history_window.frameGeometry().topRight() == window.frameGeometry().topLeft()

    window.close()


def test_history_window_follows_main_window(app):
    window = CalculatorWindow()
    window.move(200, 150)
    window.show_history()

    window.move(400, 250)
    app.processEvents()

    assert window._history_window is not None
    assert window._history_window.frameGeometry().topRight() == window.frameGeometry().topLeft()

    window.close()


def test_history_window_closes_with_main_window(app):
    window = CalculatorWindow()
    window.show_history()

    history_window = window._history_window
    assert history_window is not None
    assert history_window.isVisible()

    window.close()

    assert not history_window.isVisible()
    assert window._history_window is None
