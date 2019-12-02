"""
The presence of a path between cities A and B is defined as "A-B".
It is necessary to determine whether it is possible to get from
city X to city Y.
"""


from typing import Tuple


def way(map_roads: Tuple[str], city1: str, city2: str) -> bool:
    """checking the map with cities"""
    str_roads = ''

    for road in map_roads:
        str_roads += road[0] + road[-1]

    return set(city1[0] + city2[-1]) <= set(str_roads)
