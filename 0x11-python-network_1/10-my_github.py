#!/usr/bin/python3
"""Script that uses GitHub API to display user id"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    headers = {
        'Authorization': 'token ' + token,
        'Accept': 'application/vnd.github.v3+json',
    }
    r = requests.get(url, headers=headers)
    print(r.json().get('id'))
