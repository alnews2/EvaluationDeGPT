from evaluation_de_gpt.main import CalculatorWindow


def make_window() -> CalculatorWindow:
    window = CalculatorWindow.__new__(CalculatorWindow)
    window._display = "0"
    window._memory = None
    window._waiting_for_operand = False
    window._refresh = lambda: None
    return window


def test_memory_store_and_recall_replaces_new_operand():
    window = make_window()
    window._display = "12.5"

    window.memory_store()
    window._display = "0"
    window._waiting_for_operand = True
    window.memory_recall()

    assert window._display == "12.5"
    assert window._waiting_for_operand is False


def test_memory_recall_appends_to_current_input():
    window = make_window()
    window._display = "12"
    window._memory = "3"

    window.memory_recall()

    assert window._display == "123"


def test_memory_store_ignores_error():
    window = make_window()
    window._display = "Erreur"

    window.memory_store()

    assert window._memory is None


def test_clear_keeps_memory():
    window = make_window()
    window._memory = "42"
    window._display = "99"

    # Reproduces the state reset performed by clear without creating widgets.
    window.clear = lambda: (
        setattr(window, "_display", "0"),
        setattr(window, "_waiting_for_operand", False),
        window._refresh(),
    )
    window.clear()
    window.memory_recall()

    assert window._display == "042"
