#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
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
    cities = session.query(City).order_by(City.id).all()
    for City in cities:
        print("{}: ({}) {}".format(City.id, City.state_id, City.name))
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
