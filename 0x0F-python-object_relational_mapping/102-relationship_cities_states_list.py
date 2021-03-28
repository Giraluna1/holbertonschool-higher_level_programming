#!/usr/bin/python3
"""
prints all City objects
"""

import sys
# import the layout of the table instead of Base class
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    # Take the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Accesing the MetaData
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (mysql_username, mysql_password, database_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create the session
    session = Session(engine)

    # The query: all City object

    all_city = session.query(City).order_by(City.id).all()

    for cities in all_city:
        print("{}: {} -> {}".
              format(cities.id, cities.name, cities.state.name))

    session.close()
