#!/usr/bin/python3
"""
First state
"""
import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # import the layout of the table instead of Base class
    from model_state import State, Base

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

    # The query: changes the name of a State
    # (where id = 2 to New Mexico) object from
    # the database hbtn_0e_6_usa

    query = session.query(State).filter(State.id == 2).first()
    query.name = "New Mexico"
    session.commit()

    session.close()
