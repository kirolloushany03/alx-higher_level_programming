#!/usr/bin/python3
"""
python script that fetches website using the requests package
"""

if __name__ == "__main__":
    import requests

    response = requests.get("https://alx-intranet.hbtn.io/status")

    content = response.text
    print("Body response:")
    print(f"\ttype: {type(content)}")
    print(f"\tcontent: {content}")
