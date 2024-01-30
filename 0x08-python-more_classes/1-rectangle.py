#!/usr/bin/python3
"""
Define a Regtangle class with H and W
"""


class Rectangle:
    """Representation of Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes the width rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for priv instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter fot height priv inst"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
