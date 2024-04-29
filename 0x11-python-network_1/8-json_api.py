#!/usr/bin/python3
"""
python script that takes a letter, sends a post request to url
with the letter as parameter , displays respns based on json format and content
"""

if __name__ == "__main__":
    import requests
    import sys
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"

    res = requests.post(url, data={"q": q})
    try:
        resp = res.json()
        if resp:
            print(f"[{resp.get('id')}] {resp.get('name')}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
