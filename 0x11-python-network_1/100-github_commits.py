#!/usr/bin/python3
"""
A Python script that fetches the 10 most recent
commits of a repository using the GitHub API
"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)
    commits = response.json()[:10]

    for commit in commits:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")
