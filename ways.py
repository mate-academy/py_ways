"""The presence of a path between cities A and B is defined as "A-B".
It is necessary to determine whether it is possible
to get from city X to city Y.
"""


def way(paths, city1, city2):
    """
    Func return if it possible to get from city to city
    :param paths: tuple of paths
    :param city1: start
    :param city2: finish
    :return: if road exist
    """
    graph = {}
    cities = [city1]
    for i in paths:
        try:
            graph[i[0]].append(i[2])
        except KeyError:
            graph[i[0]] = list(i[2])
    while cities:
        city = cities.pop(0)
        try:
            if city2 in graph[city]:
                return True
            cities += graph[city]
        except KeyError:
            return False
