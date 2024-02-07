#!/usr/bin/python3
'''define a function to write text'''


def write_file(filename="", text=""):
    '''
    function to write text

    Args:
    filename: str file name
    text: text to write in
    Return: number of chars

    '''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
