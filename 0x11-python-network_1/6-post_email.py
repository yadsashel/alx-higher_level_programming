#!/usr/bin/python3
"""
A Python script that sends a POST request to a URL with an email as
a parameter and displays the response using requests package
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    response = requests.post(url, data=email)
    print(response.text)
