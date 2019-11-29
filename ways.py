"""module"""
from typing import Tuple


def way(road: Tuple[str], city1: str, city2: str) -> bool:
    """return is it possible to get from city X to city Y with given road"""
    try:
        return "".join(road).index(city1) < "".join(road).index(city2)
    except ValueError:
        return False
