#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
import sys

if __name__ == '__main__':
    response = requests.get('https://api.github.com/user',
                            auth=requests.auth.HTTPBasicAuth
                            (sys.argv[1], sys.argv[2]))
    json = response.json()
    print('{}'.format(json.get('id')))
