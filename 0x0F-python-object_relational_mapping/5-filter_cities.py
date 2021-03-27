#!/usr/bin/python3
"""
takes in the name of a state as an argument
and lists all cities of that state, using the
database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=mysql_username, passwd=mysql_password,
                           db=database_name, charset="utf8")
    cur = conn.cursor()
    # HERE I have to know SQL to grab all states in my database
    cur.execute(
        "SELECT cities.name FROM cities\
         INNER JOIN states ON states.id = cities.state_id\
         WHERE states.name=%s\
         ORDER BY cities.id ASC", (state_name, ))
    full_cities = cur.fetchall()
    print(", ".join(row[0] for row in full_cities))
    cur.close()
    conn.close()
