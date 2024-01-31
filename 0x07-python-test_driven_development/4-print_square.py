#!/usr/bin/python3
"""defining a function to print squares using only on parameter"""


def print_square(size):
    """
    Printing  a square with the # character.

    Args:
        size (int): and it will be the height and width.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
        TypeError: if size is float and -ve
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
