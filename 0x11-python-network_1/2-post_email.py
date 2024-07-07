#!/usr/bin/python3
"""
A Python script that sends a POST request to a URL
with an email as a parameter and displays the response
"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
