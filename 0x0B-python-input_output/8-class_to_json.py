#!/usr/bin/python3
'''function that return to jsn'''


def class_to_json(obj):
    """
    Returns a dictionary description

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary representing the obj

    """
    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            '''Simple data types can be directly included'''
            result[key] = value
        else:
            '''Skip non-serializable values'''
            pass
    return result
