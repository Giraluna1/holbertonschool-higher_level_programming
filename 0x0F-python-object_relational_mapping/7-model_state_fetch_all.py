#!/usr/bin/python3
"""
All satates via SQLAlchemy
"""
import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
# import the layout of the table instead of Base class
from model_state import State, Base

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

# Accesing the MetaData
engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'.format(mysql_username, mysql_password, database_name), pool_pre_ping=True)
Base.metadata.create_all(engine)

# create the session
session = Session(engine)

for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
