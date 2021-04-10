#!/usr/bin/python3
""" This is the module What's my status? """

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    # Obtain the headers directory
    headers = r.headers
    # Obtain the X_request_id from directory
    X_Request_Id = headers.get('X-Request-Id')
    print(X_Request_Id)
