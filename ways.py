"""ways search module"""

from typing import Tuple, List


def way(coord_map: Tuple[str], city_1: str, city_2: str) -> bool:
    """
    :param coord: coords map
    :param city1: start city
    :param city2: finish city
    :return: True if can go from city 1 to city 2, else False
    """
    result = []  # type: List[str]
    checker = city_1
    index = 0
    while True:
        for coord in coord_map:
            if coord[0] == checker and coord[-1] not in result:
                result.append(coord[-1])
            elif coord[-1] == checker and coord[0] not in result:
                result.append(coord[0])
            if city_2 in result:
                return True
        try:
            checker = result[index]
            index += 1
        except IndexError:
            return False
