from evaluation_de_gpt.history import CalculationHistory


def test_history_is_empty_when_created():
    history = CalculationHistory()

    assert history.entries() == []


def test_history_keeps_calculations_in_order():
    history = CalculationHistory()

    history.add("2 + 3", "5")
    history.add("10 × 4", "40")

    assert history.entries() == ["2 + 3 = 5", "10 × 4 = 40"]


def test_entries_returns_a_copy():
    history = CalculationHistory()
    history.add("2 + 3", "5")

    entries = history.entries()
    entries.clear()

    assert history.entries() == ["2 + 3 = 5"]


def test_history_can_be_cleared():
    history = CalculationHistory()
    history.add("2 + 3", "5")

    history.clear()

    assert history.entries() == []
