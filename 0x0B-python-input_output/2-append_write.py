#!/usr/bin/python3
'''define a function to append text'''


def append_write(filename="", text=""):
    '''
    function to write text

    Args:
    filename: str file name
    text: text to append to
    Return: number of chars

    '''
    with open(filename, "a", encoding="utf-8") as filee:
        return filee.write(text)
