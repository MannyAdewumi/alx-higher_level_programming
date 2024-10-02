#!/usr/bin/python3

"""Define a square class"""


class Square:
    """Representation of square class"""

    def __init__(self, size=0):
        """Instantiation with size for object initialization"""
        self.__size = size

        """Getter for the private sttr size"""
    @property
    def size(self):
        """property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Function that defines current area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print representation of self with #"""
        if self.__size == 0:
            print()
        for item in range(self.__size):
            [print("#", end="") for j in range(self.size)]
            print()
