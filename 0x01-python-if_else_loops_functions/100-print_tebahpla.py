#!/usr/bin/python3
for char in chr(ord('z') + 1)[::-1]:
    if char.isupper():
        char.lower()
    else:
         char
    print("{:s}".format(char), end='')
