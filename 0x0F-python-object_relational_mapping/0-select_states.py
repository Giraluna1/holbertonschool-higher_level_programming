#!/usr/bin/python3
""" Module  Get all states """

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localHost", port=3306,
                           user=sys.argv[1], passwd='',
                           db=sys.argv[2], charset="utf8")
    cur = conn.cursor()
    # HERE I have to know SQL to grab all states in my database
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
