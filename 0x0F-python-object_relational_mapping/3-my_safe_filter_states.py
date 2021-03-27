#!/usr/bin/python3
""" Filter states by user input """

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_to_search = sys.argv[4]

    conn = MySQLdb.connect(host="localHost", port=3306,
                           user=mysql_username, passwd=mysql_password,
                           db=database_name, charset="utf8")
    cur = conn.cursor()
    # HERE I have to know SQL to grab all states in my database
    cur.execute(
        "SELECT * FROM states WHERE \
         name=%s ORDER BY id ASC", (state_to_search, ))
    full_states = cur.fetchall()
    for row in full_states:
        print(row)
    cur.close()
    conn.close()
