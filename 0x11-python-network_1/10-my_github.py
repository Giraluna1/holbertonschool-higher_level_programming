#!/usr/bin/python3
""" Takes your github credentials """

import requests
from requests import auth
import sys

if __name__ == "__main__":

    # Making request with HTTP Basic Auth
    user = sys.argv[1]
    password = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(user, password))
    # Obtein the content like directory
    dic_of_content = r.json()
    # Show only id number
    print(dic_of_content.get('id'))
