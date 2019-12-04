"""
docstring
"""
from typing import Tuple


def way(map_: Tuple[str], city1: str, city2: str) -> bool:
    """

    :param map:
    :param city1:
    :param city2:
    :return:
    """
    mid = []
    c_map = [''.join(line.split('-')) for line in map_]

    if city1 + city2 in c_map:
        return True

    for item in c_map:
        if item[0] == city1:
            mid.append(item[1])
        if item[1] == city2:
            mid.append(item[0])

    if len(mid) == 2:
        if mid[0] + mid[1] in c_map:
            return True

    for item in mid:
        if mid.count(item) > 1:
            return True

    return False
