#!/usr/bin/python3
# -*- coding: utf-8 -*-
from math import sqrt


# Say Greeting(waypoint1)
def hello(name):
    name = name.strip()
    print('hello ' + name)


# Pythagorean Theorem(waypoint2)
def calculate_hypotenuse(a, b):
    print(sqrt(a ** 2 + b ** 2))


# Waypoint 3: Test whether all Conditions are True
def are_all_conditions_true(a):
    if a == []:
        print(None)
    elif False in a:
        print(False)
    else:
        print(True)


# Waypoint 4: Test whether at least one Condition is True
def is_a_condition_true(a):
    if a == []:
        print(None)
    elif True in a:
        print(True)
    else:
        False


# Waypoint 5: Filter List of Integers
def filter_integers_greater_than(l, n):
    result = []
    for i in l:
        if i > n:
            result.append(i)
    return result


# Waypoint 6: Find Cheapest Hotels

def find_cheapest_hotels(hotels, bid):
    sorted_cheap = sorted(hotels, key=lambda hotel: hotel[1])
    list = []
    for hotel in hotels:
        if hotel[1] < bid:
            list.append(hotel[0])
    return (list)

# Waypoint 7: Calculate Distance between two 2D Points

def calculate_euclidean_distance_between_2_points(p1, p2):
    (a, b) = p1

    (c, d) = p2
    d = sqrt((c - a) ** 2 + (d - b) ** 2)

    return d


# Waypoint 8: Calculate Distance between several 2D Points

def calculate_euclidean_distance_between_2_points(p1, p2):
    (a, b) = p1

    (c, d) = p2
    d = sqrt((c - a) ** 2 + (d - b) ** 2)

    return d


def calculate_euclidean_distance_between_points(point):
    tong = 0
    if point == [] or len(point) < 2:
        raise ValueError('The list MUST contain at least 2 point')
    for i in range(0, len(point) - 1):
        tong = tong + calculate_euclidean_distance_between_2_points(point[i], point[i + 1])
    return tong


# Waypoint 9: Capitalize the Words of a String

def capitalize_words(c):
    if c == []:
        print(None)
    elif isinstance(c, str) == False:
        raise TypeError(' Not a string')
    else:
        return " ".join((c.title().strip()).split())
