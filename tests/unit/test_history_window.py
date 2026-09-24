import pytest
from PySide6.QtWidgets import QApplication

from evaluation_de_gpt.main import CalculatorWindow


@pytest.fixture
def app():
    application = QApplication.instance() or QApplication([])
    yield application


def test_history_window_is_attached_to_main_window(app):
    window = CalculatorWindow()

    window.toggle_history()
    app.processEvents()

    assert window._history_window is not None
    assert window._history_window.parentWidget() is window

    window.close()


def test_history_window_is_aligned_with_main_window(app):
    window = CalculatorWindow()
    window.move(200, 150)

    window.toggle_history()
    app.processEvents()

    assert window._history_window is not None
    assert window._history_window.frameGeometry().topRight() == window.frameGeometry().topLeft()

    window.close()


def test_history_window_follows_main_window(app):
    window = CalculatorWindow()
    window.move(200, 150)
    window.show()
    app.processEvents()
    window.toggle_history()

    window.move(400, 250)
    app.processEvents()

    assert window._history_window is not None
    assert window._history_window.frameGeometry().topRight() == window.frameGeometry().topLeft()

    window.close()


def test_history_window_closes_with_main_window(app):
    window = CalculatorWindow()
    window.toggle_history()

    history_window = window._history_window
    assert history_window is not None
    assert history_window.isVisible()

    window.close()

    assert not history_window.isVisible()
    assert window._history_window is None


def test_history_button_toggles_window_and_label(app):
    window = CalculatorWindow()

    assert window._history_button is not None
    assert window._history_button.text() == "Historique"

    window.toggle_history()
    app.processEvents()

    assert window._history_window is not None
    assert window._history_window.isVisible()
    assert window._history_button.text() == "Fermer Historique"

    window.toggle_history()
    app.processEvents()

    assert window._history_window is None
    assert window._history_button.text() == "Historique"

    window.close()


def test_history_button_resets_when_history_window_is_closed_directly(app):
    window = CalculatorWindow()

    window.toggle_history()
    app.processEvents()

    history_window = window._history_window
    assert history_window is not None
    assert window._history_button is not None
    assert window._history_button.text() == "Fermer Historique"

    history_window.close()
    app.processEvents()

    assert window._history_window is None
    assert window._history_button.text() == "Historique"

    window.close()
