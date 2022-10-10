#!/usr/bin/python3
""" a script that deletes all State objects from the database hbtn_0e_6_usa
    that has a charater of 'a'
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(State.name.like('%a%')) \
            .order_by(State.id).all():
        session.delete(state)
    session.commit()
    session.close()
