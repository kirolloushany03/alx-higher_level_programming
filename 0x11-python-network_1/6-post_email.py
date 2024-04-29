#!/usr/bin/python3
"""
python script that takes in a url and email and sends a post request
and passed url with the email and displays the body of the response
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)

    print(response.text)
