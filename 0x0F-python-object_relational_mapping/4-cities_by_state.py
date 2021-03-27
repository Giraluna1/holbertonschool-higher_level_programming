#!/usr/bin/python3
"""
Filter states by user input
"""

import MySQLdb
import sys


if __name__ == "__main__":

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

conn = MySQLdb.connect(host="localhost", port=3306,
                       user=mysql_username, passwd=mysql_password,
                       db=database_name, charset="utf8")
cur = conn.cursor()
 # HERE I have to know SQL to grab all states in my database
 cur.execute(
      "SELECT cities.id, cities.name, states.name FROM states \
         INNER JOIN cities ON states.id = cities.state_id \
         ORDER BY cities.id ASC")
  full_cities = cur.fetchall()
   for row in full_cities:
        print(row)
    cur.close()
    conn.close()
