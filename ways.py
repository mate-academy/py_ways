"""
The presence of a path between cities A and B is defined as "A-B".
It is necessary to determine whether it is possible to get from
city X to city Y.
"""


from typing import Tuple
import string


def way(map_cities: Tuple[str], city1: str, city2: str) -> bool:
    """checking the map with cities"""
    alp = string.ascii_uppercase
    roads = ''
    for road in map_cities:
        roads += alp[alp.find(road[0]):alp.find(road[-1])]
    new_road = alp[alp.find(city1[0]):alp.find(city2[-1])]
    return set(new_road) <= set(roads)
