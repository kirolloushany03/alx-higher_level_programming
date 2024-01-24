#!/usr/bin/python3

"""Define a class"""


class Square:
    """Represent a class"""

    def __init__(self, size=0):
        """Initialize a new sqaure

        Args:
            size (int): The size of the new.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
