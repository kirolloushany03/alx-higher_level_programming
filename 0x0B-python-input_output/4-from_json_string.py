#!/usr/bin/python3
'''import JSON module'''
import json


def from_json_string(my_str):
    '''
    funtion that return str to normal
    Args: my_str

    Return: string from Json
    '''
    string_returned = json.loads(my_str)
    return string_returned
