#!/usr/bin/python3
"""Square Module"""

class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size: Length of a side of a sqaure.
            position (int, int): The position of the new square.
        """
         self.__size = size
         self.position = position

    @property
    def size(self):
        """ Property for the length of a side of a sqaure."""
        return (self.__size)
    
    @size.setter
    def size(self, value):
        if not isinstance(size, int):@property
def position(self, value):
    """Get position of square."""
    return (self.__position)

@position.setter
def position(self, value):
    if (not isinstance(value, tuple) or
            len(value) != 2 or 
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
        raise TypeError("position must be a tuple of 2 positive integers")
    self.__position = value
     
def area(self):
    """Return area of the square"""
    return (self.__size * self.__size)

def my_print(self):
    """print sqaure with the #character"""
    if self.__size == 0:
        print("")
        return

    [print("") for i in range(0, self .__position[1])]
    for i in range(0, self.__size):
        [print("") for i in range(0, self .__position[0])]
        [print("#") for i in range(0, self .__size)]
        print("")
            raise TypeError('size must be an integer')
            if size < 0:
            raise ValueError('size must be >= 0')
            self.__size = value

def __str__(self)
"""print sqaure with the square"""
    if self.__size == 0:
 [print("") for i in range(0, self .__position[1])]
    for i in range(0, self.__size):
        [print("") for i in range(0, self .__position[0])]
        [print("#") for i in range(0, self .__size)]
        if i != self.__size - 1:
            print("")
        return ("")


