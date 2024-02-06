#!/usr/bin/python3
"""
This module contain a function adds attrbute to an object
"""


def add_attribute(object, key, value):
    """add attribute to an object"""
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, key, value)
