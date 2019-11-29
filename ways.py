"""
module ways
"""
from typing import Tuple, Union


def way(map_route: Tuple[str], city1: str, city2: str) -> Union[str, bool]:
    """
    The presence of a path between cities A and B is defined as "A-B".
    Determine whether it is possible to get from city X to city Y.
    :param map_route: Tuple[str]
    :param city1: str
    :param city2: str
    :return: bool
    """
    result_route = ""
    for locality in map_route:
        result_route += "".join(locality).replace('-', '')
    return city1 and city2 in result_route
