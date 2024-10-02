#!/usr/bin/python3

"""Define a square class"""


class Square:
    """Representation of square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with size for object initialization"""
        self.size = size
        self.__position = position

        """setter and getter for position"""
    @property
    def position(self):
        """getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""

        if (not isinstance(value, tuple) or len(value) != 2 or not
                all(isinstance(num, int) for num in value)
                or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            return
        [print() for j in range(0, self.__position[1])]
        for j in range(self.__size):
            [print(" ", end="") for item in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
