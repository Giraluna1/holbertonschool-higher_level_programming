#!/usr/bin/python3
""" Use POST an email """

import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    myobj = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(myobj)
    data = data.encode('ascii')
    r = urllib.request.Request(url, data)
    with urllib.request.urlopen(r) as response:
        html = response.read().decode('utf-8')
        print(html)
