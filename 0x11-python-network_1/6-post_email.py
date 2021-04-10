#!/usr/bin/python3
""" POST an email """

import requests
import sys

if __name__ == "__main__":
    myobj = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=myobj)
    print(r.text)
