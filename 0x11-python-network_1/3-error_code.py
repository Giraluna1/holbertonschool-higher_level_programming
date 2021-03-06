#!/usr/bin/python3
""" Error code """

from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = Request(url)
    try:
        with urlopen(r) as response:
            html = response.read().decode('utf-8')
            print(html)
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
