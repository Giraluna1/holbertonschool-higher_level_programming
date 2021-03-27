#!/usr/bin/python3
""" First state """
import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
# import the layout of the table instead of Base class
from model_state import State, Base

mysql_username = sys.argv[1]
database_name = sys.argv[2]

# Accesing the MetaData
engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'.
    format(mysql_username, "", database_name), pool_pre_ping=True)
Base.metadata.create_all(engine)

# create the session
session = Session(engine)

# The query: lists all State objects that
# contain the letter a from the database hbtn_0e_6_usa
for state in session.query(State).filter(State.name.like('%a%')):
    print("{}: {}".format(state.id, state.name))

session.close()
