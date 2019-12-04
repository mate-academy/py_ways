"""
docstring
"""
import ways


def test_unlinked():
    """

    :return:
    """
    assert ways.way(
        ("A-B", "C-D", "E-F"),
        "X", "Y"
    ) == False


def test_direct():
    """

    :return:
    """
    assert ways.way(
        ("A-B", "C-D", "E-F"),
        "A", "B"
    ) == True


def test_linked():
    """

    :return:
    """
    assert ways.way(
        ("A-B", "B-C", "C-D"),
        "A", "D"
    ) == True


def test_also_linked():
    """

    :return:
    """
    assert ways.way(
        ("A-B", "C-D", "B-X", "C-W", "A-Q", "Q-R", "D-T"),
        "C", "T"
    ) == True
