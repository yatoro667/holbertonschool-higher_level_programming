#!/usr/bin/python3
"""
cript that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1],
                                                             argv[2],
                                                             argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=argv[4]).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)
    session.close()
