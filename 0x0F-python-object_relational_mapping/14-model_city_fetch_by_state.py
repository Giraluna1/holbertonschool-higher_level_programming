#!/usr/bin/python3
"""
prints all City objects
from the database hbtn_0e_14_usa
"""

import sys
# import the layout of the table instead of Base class
from model_state import State, Base
from model_city import City

import sqlalchemy
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    # Take the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Accesing the MetaData
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(mysql_username, mysql_password, database_name),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create the session
    session = Session(engine)

    # The query: all city objects
    full_cities = session.query(City).join(State).order_by(City.id)

    for city in full_cities:
        print(f'{city.state.name}: ({city.id}) {city.name}')

    session.close()
