#!/usr/bin/python3
"""
python script that takes in a url and sends reuest to the url
and display the body of the resonse
"""
import urllib.error
import urllib.request


if __name__ == "__main__":
    import urllib
    import sys

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            response_body = response.read().decode("utf-8")
            print(response_body)
    except urllib.error.HTTPError as exception:
        print(f"Error code: {exception.code}")
