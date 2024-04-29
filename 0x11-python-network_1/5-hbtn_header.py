#!/usr/bin/python3
"""
python script takes url and send request and desplay value
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    respnse = requests.get(url)

    request_id = respnse.headers.get("X-Request-Id")

    print(request_id)
