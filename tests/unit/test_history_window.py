import pytest
from PySide6.QtCore import Qt
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


def test_result_display_has_copy_context_menu(app):
    window = CalculatorWindow()

    assert (
        window._display_label.contextMenuPolicy()
        == Qt.ContextMenuPolicy.CustomContextMenu
    )

    menu = window._create_display_context_menu()
    assert [action.text() for action in menu.actions()] == ["Copier", "Coller"]

    window._display = "123.45"
    window._copy_display()
    assert app.clipboard().text() == "123.45"

    menu.deleteLater()
    window.close()


def test_paste_number_from_clipboard(app):
    window = CalculatorWindow()

    app.clipboard().setText("123,45")
    window._paste_number()
    assert window._display == "123.45"

    app.clipboard().setText("-6.5")
    window._paste_number()
    assert window._display == "-6.5"

    window.close()


def test_paste_invalid_text_is_ignored(app):
    window = CalculatorWindow()
    window._display = "12"

    app.clipboard().setText("12 + 3")
    window._paste_number()

    assert window._display == "12"
    window.close()
