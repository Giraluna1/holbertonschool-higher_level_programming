#!/usr/bin/python3
""" list 10 first commits of the specific github acount  """

import requests
from requests import auth
import sys

if __name__ == "__main__":

    # Making request with HTTP Basic Auth
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    r = requests.get(
        'https://api.github.com/repos/{}/{}/commits'.format(
            owner_name, repository_name),
        auth=(repository_name, owner_name))
    # Obtein the content of json
    list_of_directories = r.json()
    # Obtain the first 10 elements
    # Obtain only the sha and author name
    for directories in list_of_directories[:10]:
        sha = directories.get('sha')
        name = directories.get('commit').get('author').get('name')
        print('{}: {}'.format(sha, name))
