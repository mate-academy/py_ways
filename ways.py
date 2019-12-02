"""module"""
from typing import Tuple, Any


def way(map_: Tuple[str], city1: str, city2: str) -> bool:
    """return is it possible to get from city X to city Y with given road"""
    #  fill dictionary with pairs city : list of possible roads
    road_map = {el[0]: [] for el in map_}  # type: Any
    for city in map_:
        road_map[city[0]].append(city[2])

    key_cities = road_map.keys()
    if city1 not in key_cities:
        return False
    #  list to storage all possible roads from city1
    resulting_road = road_map[city1]
    i = 0

    while resulting_road[i] in key_cities and i < len(resulting_road):
        for road in road_map[city1]:
            if road in road_map.keys():
                resulting_road.extend(road_map[road])
        i += 1

    if city2 in resulting_road:
        return True
    return False





#way(("A-B", "C-D", "B-X", "C-W", "A-Q", "Q-R", "D-T"), "A", "T")
