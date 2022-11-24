"""
Nathan loves cycling.

Beacuse Nathan knows it is important to stay hydrated, he drinks 0.5 liters
of water per hour of cycling.

You get given the time in hours and you need to return the number of liters
Natahn will drink, rounded to the smallest value.

For example:

    time = 3 ---> liters = 1
    time = 6.7 ---> liters = 3
    time = 11.8 ---> liters = 5
"""

import math
def litres(time):
    water = math.floor(time*0.5)
    return water