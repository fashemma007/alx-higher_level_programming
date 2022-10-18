#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Class representation of a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): instance width. Defaults to 0.
            height (int): instance height. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter function for the width of the rectangle.
        Returns: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter function for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for the height of the rectangle.

        Args:
            value: The newly given height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes and returns the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
