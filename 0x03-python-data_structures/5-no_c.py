#!/usr/bin/python3
def no_c(my_string):
    replace = "cC"
    new = ""
    for i in my_string:
        if i not in replace:
            new += i
    return new
