#!/usr/bin/python3
"""
    this a python script that fetches https://alx-intranet.hbtn.io/status
    and get a response from it
"""
if __name__ == "__main__":
    import urllib.request
    # with urllib.request.urlopen("https://alx-intranet.hbtn.io/status"):
    response = urllib.request.urlopen("https://alx-intranet.hbtn.io/status")
    read_data = response.read()
    print("Body response:")
    print(f"\t- type: {type(read_data)}")
    print(f"\t- content: {read_data}")
    print(f"\t- utf8 content: {read_data.decode('utf-8')}")
