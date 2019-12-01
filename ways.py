"""
The presence of a path between cities A and B is defined as "A-B".
It is necessary to determine whether it is possible to get from
city X to city Y.
"""


from typing import Tuple
import string


def way(map_roads: Tuple[str], city1: str, city2: str) -> bool:
    """checking the map with cities"""

    alphabets = string.ascii_uppercase
    str_roads = ''

    for road in map_roads:
        str_roads += alphabets[alphabets.find(road[0]):
                               alphabets.find(road[-1])]

    check_road = alphabets[alphabets.find(city1[0]):
                           alphabets.find(city2[-1])]

    return set(check_road) <= set(str_roads)
