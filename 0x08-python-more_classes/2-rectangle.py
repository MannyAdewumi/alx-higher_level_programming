#!/usr/bin/python3
""" The rectangle class module """


class Rectangle:
    """ Class to create rectangle """

    def __init__(self, width=0, height=0):
        """ instantation of class """
        self.width = width
        self.height = height

    @property
    def width(self):
        """The getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The getter for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ The setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that returns area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Public instance method that returns rectangle perimeter"""
        if self.__height == 0 or self.__width == int(0):
            return (0)
        return ((self.__width * 2) + (self.__height * 2))