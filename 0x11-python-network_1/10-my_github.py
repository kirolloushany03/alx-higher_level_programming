#!/usr/bin/python3
"""
python scrpt that takes github credntail and uses gitup ap to dispay you id
"""
import requests
import sys

if __name__ == "__main__":
    with requests.get("https://api.github.com/user",
                    auth=(sys.argv[1], sys.argv[2])) as response:
        print(response.json().get("id"))
