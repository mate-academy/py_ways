"""The presence of a path between cities A and B is defined as "A-B".
It is necessary to determine whether it is possible to get from city X to city Y."""
from typing import Tuple


def way(route_map: Tuple[str], city1: str, city2: str) -> bool:
    """Method checks if the both cities are in the list"""
    list_of_routes = [route.split('-') for route in route_map]
    list_of_cities = [x for xs in list_of_routes for x in xs]
    if city1 in list_of_cities[0::2] and city2 in list_of_cities[1::2]:
        return True
    return False
