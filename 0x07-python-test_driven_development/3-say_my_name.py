#!/usr/bin/python3
"""this is module that will print full name with using 2 str(names) given"""


def say_my_name(first_name, last_name=""):
    """
    function that prints the name with 2 parameters

    Args:
        first_name: refer the first name to print
        last_name: refer the last name to print

    Raises:
        TypeError: If either of first_name or last_name are not strings.
    Return:
        full name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
