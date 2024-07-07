#!/usr/bin/python3
"""
A Python script that sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter using requests package
"""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post(url, data={'q': q})

    try:
        json_response = response.json()
        if json_response:
            print(
                "[{}] {}".format(
                    json_response.get('id'),
                    json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
