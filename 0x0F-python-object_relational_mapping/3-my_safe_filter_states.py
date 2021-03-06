#!/usr/bin/python3
"""
Filter states by user input
"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    # HERE I have to know SQL to grab all states in my database
    cur.execute(
        "SELECT * FROM states WHERE \
         states.name=%s ORDER BY id ASC", (sys.argv[4], ))
    full_states = cur.fetchall()
    for row in full_states:
        print(row)
    cur.close()
    conn.close()
