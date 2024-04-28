#!/usr/bin/python3
"""
python script that takes url, email and sends post request and display body
"""

import urllib.parse
import urllib.request


if __name__ == "__main__":
    import urllib
    import sys
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data2 = data.encode('utf-8')
    with urllib.request.urlopen(url, data2) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)
