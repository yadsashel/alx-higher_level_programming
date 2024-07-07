#!/usr/bin/python3
"""
A Python script that uses the GitHub API
to display your id using requests package
"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=HTTPBasicAuth(username, token))

    print(response.json().get('id'))
