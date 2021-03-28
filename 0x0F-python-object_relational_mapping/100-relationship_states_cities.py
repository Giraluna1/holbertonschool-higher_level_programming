#!/usr/bin/python3
"""
create the State "California with the City "San Francisco"
from the data base hbtn_0e_100_usa
"""

import sys
# import the layout of the table instead of Base class
from model_state import Base, State
from model_city import City
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

    # The query: create the state and the city
    California = State()
    California.id = 1
    California.name = "California"
    San_Francisco = City()
    San_Francisco.id = 1
    San_Francisco.state_id = 1
    San_Francisco.name = "San Francisco"

    # persists data
    session.add(California)
    session.add(San_Francisco)

    # commit and close session

    session.commit()

    session.close()
