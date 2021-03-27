#!/usr/bin/python3
"""
First state With ORM
"""
import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # import the layout of the table instead of Base class
    from model_state import State, Base

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

    for state in session.query(State).order_by(State.id).filter(State.id == 1):
        if state is not None:
            print("{}: {}".format(state.id, state.name))
        else:
            print("Nothing")
    session.close()
