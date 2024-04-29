#!/usr/bin/python3
"""
python script that takes a letter, sends a post request to url
with the letter as parameter , displays respns based on json format and content
"""

import requests
import sys
import json

if __name__ == "__main__":
    # Default value for q if no argument is given
    q = ""

    # Check if an argument is given
    if len(sys.argv) > 1:
        q = sys.argv[1]

    # URL to send the POST request to
    url = "http://0.0.0.0:5000/search_user"

    # Prepare the data to be sent in the POST request
    data = {'q': q}

    # Send the POST request
    response = requests.post(url, data=data)

    # Try to parse the response body as JSON
    try:
        response_json = response.json()

        # Check if the JSON is not empty
        if response_json:
            # Display the id and name for each user in the JSON
            for user in response_json:
                print(f"[{user['id']}] {user['name']}")
        else:
            print("No result")
    except json.JSONDecodeError:
        print("Not a valid JSON")
