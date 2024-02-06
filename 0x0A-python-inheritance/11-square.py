#!/usr/bin/python3
"""
Module for class that inherits from REctangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Basic class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size must be private. No getter or setter, must be a positive
            integer, validated by integer_validator
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
