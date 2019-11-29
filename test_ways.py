import ways


def test_unlinked():
    assert ways.way(
        ("A-B", "C-D", "E-F"),
        "X", "Y"
    ) == False


def test_direct():
    assert ways.way(
        ("A-B", "C-D", "E-F"),
        "A", "B"
    ) == True


def test_linked():
    assert ways.way(
        ("A-B", "B-C", "C-D"),
        "A", "D"
    ) == True


def test_also_linked():
    assert ways.way(
        ("A-B", "C-D", "B-X", "C-W", "A-Q", "Q-R", "D-T"),
        "C", "T"
    ) == True