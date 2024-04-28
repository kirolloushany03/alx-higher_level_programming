#!/usr/bin/python3
"""
python script will take url and send request to url and display the value
of the x request variable
"""
import urllib.request


if __name__ == "__main__":
    import urllib
    from sys import argv

    url = argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.headers

        if "X-Request-Id" in headers:
            print(headers["X-Request-Id"])
        else:
            print("X-Request-Id header not found")
