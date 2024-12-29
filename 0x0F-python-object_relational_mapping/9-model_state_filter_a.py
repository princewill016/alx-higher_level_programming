#!/usr/bin/python3
"""
Script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                         .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create session factory
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query State objects containing letter 'a'
    states = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()

    # Print results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
