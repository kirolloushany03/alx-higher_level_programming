#!/usr/bin/python3
"""
python script that takes a letter, sends a post request to url
with the letter as parameter , displays respns based on json format and content
"""

import requests
import sys

if __name__ == "__main__":

    q = sys.argv[1] if len(sys.argv) > 1 else ""
    # if len(sys.argv) > 1:
    #     q = sys.argv[1]
    # else:
    #     q = ""

    url = "http://0.0.0.0:5000/search_user"

    response = requests.post(url, data={"q": q})

    try:
        response_json = response.json()

        if response_json:
            print(f"[{response_json.get('id')}] {response_json.get('name')}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
