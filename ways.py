'''
Module
'''
from typing import Tuple


def delete_dub(strng, this_city):
    '''
    Видаляємо дублікати міст і саме місто з якого ми вирушаємо
    :param strng:
    :param this_city:
    :return:
    '''
    result = ''
    for letter in strng:
        if (letter not in result) and (letter != this_city):
            result += letter
    return result


def way(mapp: Tuple[str], city_from: str, city_in: str) -> bool:
    '''

    :param mapp:
    :param city_from:
    :param city_in:
    :return:
    '''
    dictionary = {city_from: '', city_in: ''}
    for i in mapp:
        name_city_from, name_city_in = i.split('-')[0], i.split('-')[1]
        if name_city_from not in dictionary:
            dictionary[name_city_from] = name_city_in
        else:
            dictionary[name_city_from] += name_city_in
        if name_city_in not in dictionary:
            dictionary[name_city_in] = name_city_from
        else:
            dictionary[name_city_in] += name_city_from
    list_keys = dictionary.keys()
    for _ in range(len(mapp)):
        for value in list_keys:
            for i in dictionary[value]:
                dictionary[value] += dictionary[i]
                dictionary[value] = delete_dub(dictionary[value], value)
    return city_in in dictionary[city_from]
