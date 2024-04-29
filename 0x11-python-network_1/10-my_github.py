#!/usr/bin/python3
"""
python scrpt that takes github credntail and uses gitup ap to dispay you id
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    headers = {
        "Authorization": f"Basic {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_info = response.json()
        print(f"Your GitHub ID is: {user_info['id']}")
    else:
        print(f"Error: {response.status_code}")
