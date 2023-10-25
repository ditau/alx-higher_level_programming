#!/usr/bin/python3
"""Square Module"""

class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Length of a side of a sqaure.
        """
         self.__size = size

     @property
    def size(self):
        """ Property for the length of a side of a sqaure.
        
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of square

        Returns:
            The size squared
        """
        return self.__size ** 2
    
    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() == other.area()

    def __ge__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() == other.area()
