#!/usr/bin/python3
""" This is the module that you know the status """

import urllib.request

url = 'https://intranet.hbtn.io/status'
# opean and read
with urllib.request.urlopen(url) as response:
    html = response.read()
print("Body response:")
print("\t- type: {}".format(type(html)))
print("\t- type: {}".format(html))
print("\t- utf8 content: {}".format(html.decode('utf-8')))
