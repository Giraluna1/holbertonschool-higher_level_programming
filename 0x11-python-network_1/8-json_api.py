#!/usr/bin/python3
""" SEARCH API """

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    # Create the object to load
    myobj = {'q': q}
    r = requests.post('http://0.0.0.0:5000/search_user', data=myobj)
    # convert to Json
    try:
        Obj_Json = r.json()
        # case if Json is empty
        if len(Obj_Json) == 0:
            print('No result')
        # case if Json is load succesfull
        else:
            print('[{}] {}'.format(Obj_Json.get('id'), Obj_Json.get('name')))
    # case if pased a invalid json
    except:
        print('Not a valid JSON')
