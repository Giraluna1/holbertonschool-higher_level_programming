#!/usr/bin/python3
""" Filter states by user input """

import MySQLdb
import sys

mysql_username = sys.argv[1]
database_name = sys.argv[2]
state_name = sys.argv[3]


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localHost", port=3306,
                           user=mysql_username, passwd='',
                           db=database_name, charset="utf8")
    cur = conn.cursor()
    # HERE I have to know SQL to grab all states in my database
    cur.execute(
        "SELECT cities.name FROM cities \
         INNER JOIN states ON states.id = cities.state_id \
         WHERE states.name=%s \
         ORDER BY cities.id ASC", (state_name, ))
    full_cities = cur.fetchall()
    print(", ".join(row[0] for row in full_cities))
    cur.close()
    conn.close()
