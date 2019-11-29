"""
ways module provides function
way(map, city1, city2),  that return
True if it is possible to get from city1
to city2 using map, otherwise return False
"""
from typing import Tuple


def way(map_: Tuple[str], city1: str, city2: str) -> bool:
    """
    Return True if using given map possible to travel from
    city1 to city2 and return False if it is not possible.
    :param map: Tuple[str]
    :param city1: str
    :param city2: str
    :return: bool
    """
    city_map = [(region.split('-')) for region in map_]
    transits = []
    for town1, town2 in city_map:
        if (town1, town2) == (city1, city2):
            return True
        if town1 == city1:
            transits.append(town2)

    for transit in transits:
        for town1, town2 in city_map:
            if town1 == transit:
                if town2 == city2:
                    return True
                transits.append(town2)
    return False
