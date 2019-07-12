from python_basics import *

# Say Greeting(waypoint1)
hello('     Jack Carver')
hello('Jack Carver   ')
hello('   Jack Carver       ')

# Pythagorean Theorem(waypoint2)
calculate_hypotenuse(1, 2)

# Waypoint 3: Test whether all Conditions are True
are_all_conditions_true([True, True, False, True, False, False, True])
are_all_conditions_true([True, True, True])
are_all_conditions_true([])

# Waypoint 4: Test whether at least one Condition is True
is_a_condition_true([True, True, False, True, False, False, True])
is_a_condition_true([True, True, True])
is_a_condition_true([])

# Waypoint 5: Filter List of Integers
l = [0, 3, 5, -2, 9, 8]

print(filter_integers_greater_than(l, 4))

##Waypoint 6: Find Cheapest Hotels by another way

hotel_daily_rates = [
    ('Majestic Saigon Hotel', 93),
    ('Hotel Grand Saigon', 80),
    ('Sofitel Saigon Plaza', 123),
    ('Hotel Continental', 62),
    ('Caravelle Hotel', 180),
    ('Sheraton Saigon Hotel', 216),
    ('Park Hyatt Saigon', 209)
]
find_cheapest_hotels(hotel_daily_rates, 150)

# Waypoint 7: Calculate Distance between two 2D Points
# import math
print(calculate_euclidean_distance_between_2_points((1, 2), (1, 2)))
print(calculate_euclidean_distance_between_2_points((0, 0), (3, 4)))
print(calculate_euclidean_distance_between_2_points((1, 1), (2, 2)))

# Waypoint 8: Calculate Distance between several 2D Points
print(calculate_euclidean_distance_between_points([(0, 0), (3, 4)]))
print(calculate_euclidean_distance_between_points([(0, 0), (3, 4), (-1, -1), (9, 8)]))
print(calculate_euclidean_distance_between_points([]))

# Waypoint 9: Capitalize the Words of a String
print(capitalize_words('    '))
print(capitalize_words('JACK CARVER'))
print(capitalize_words('Không  có gì    quý hơn  độc lập      tự do'))
