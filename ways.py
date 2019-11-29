"""
module ways
"""
from itertools import product
from typing import Tuple, Union


def way(routes: Tuple[str], city1: str, city2: str) -> Union[str, bool]:
    """
    The presence of a path between cities A and B is defined as "A-B".
    Determine whether it is possible to get from city X to city Y.
    :param routes: Tuple[str]
    :param city1: str
    :param city2: str
    :return: bool
    """
    result_route = []
    cities = (city1, city2)

    for route in routes:
        localities = route.split('-')
        for local in localities:
            result_route.append(local)

    route_combinations = list(product(result_route, repeat=2))
    return cities in route_combinations
