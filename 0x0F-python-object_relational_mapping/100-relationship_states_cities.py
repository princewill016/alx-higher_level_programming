#!/usr/bin/python3
"""
Script that creates the State "California" with the City "San Francisco"
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                         .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create all tables
    Base.metadata.create_all(engine)

    # Create session factory
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Create new State "California" with City "San Francisco"
    new_state = State(name="California")
    new_state.cities = [City(name="San Francisco")]

    # Add and commit
    session.add(new_state)
    session.commit()

    # Close session
    session.close()
