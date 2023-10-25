#!/usr/bin/python3
"""Define a MagicClass Matching bytecode"""

import Math

class MagicClass:

    def __init__(self, radius=0):
        """Initialize MagicClass.
        Args
        radius (float or int): radius of new MagicClass
        """
        self.__radius = 0
        if type (radius) is not int and type(radius) is not float:
            raise TypeError("radius must be number")
        self.__radius = radius

    def area(self):
        """Return area of the MagicClass."""
        return (self._radius ** 2 * math.pi)

    def circumference(self):
        """Return the circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
