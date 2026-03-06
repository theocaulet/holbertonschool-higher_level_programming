#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


def main():
    """Define the main function"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}'
                           '@localhost:3306/{}'.format(username, password,
                                                       database))
    session = sessionmaker(bind=engine)
    session = session()
    cities = session.query(State, City).filter(State.id == City.state_id).\
        order_by(City.id).all()
    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
