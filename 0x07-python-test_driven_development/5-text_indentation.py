#!/usr/bin/python3
"""define function to print 2 new lines after . ? ; with one parameter """


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    while start < len(text) and text[start] == ' ':
        start += 1

    while start < len(text):
        print(text[start], end="")
        if text[start] == "\n" or text[start] in ".?:":
            if text[start] in ".?:":
                print("\n")
            start += 1
            while start < len(text) and text[start] == ' ':
                start += 1
            continue
        start += 1
