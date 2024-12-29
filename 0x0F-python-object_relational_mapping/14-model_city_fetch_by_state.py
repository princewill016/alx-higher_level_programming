#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
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

    # Query all cities and their states
    cities = session.query(State, City).filter(State.id == City.state_id)\
        .order_by(City.id).all()

    # Print results
    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session
    session.close()
