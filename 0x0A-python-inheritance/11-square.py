#!/usr/bin/python3
"""
This module contain Square class
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
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """return the rectangle area"""
        return self.__size*self.__size

    def __str__(self):
        """object string representation"""
        return f"[Square] {self.__size}/{self.__size}"
