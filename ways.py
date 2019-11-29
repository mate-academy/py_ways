"""ways search module"""

from typing import Tuple


def way(coord: Tuple[str], city1: str, city2: str) -> bool:
    """
    :param coord: coords map
    :param city1: start city
    :param city2: finish city
    :return: True if can go from city 1 to city 2, else False
    """
    result = city1
    for i in coord:
        if i[0] == result:
            result = i[-1]
        if result == city2:
            break
    else:
        return False
    return True
