#!/usr/bin/python3
"""
python script will take url and send request to url and display the value
of the x request variable
"""
import urllib.request


if __name__ == "__main__":
    import urllib
    import sys

    url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
