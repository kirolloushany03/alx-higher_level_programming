#!/usr/bin/python3
"""
python script that takes a letter, sends a post request to url
with the letter as parameter , displays respns based on json format and content
"""

import requests
import sys
import json

if __name__ == "__main__":
    q = ""

    if len(sys.argv) > 1:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"

    response = requests.post(url, data={"q": q})

    try:
        response_json = response.json()

        if response.json():
            for user in response_json:
                print(f"[{response.get('id')}] {response.get('name')}")
        else:
            print("No result")
            
    except json.JSONDecodeError:
        print("Not a valid JSON")
