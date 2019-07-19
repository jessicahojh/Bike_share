import datetime

from sqlalchemy import func

from model import *

from server import app


def load_stations():
    """Load stations into database."""

    s1 = Station(10, 0)
    s2 = Station(5, 0)
    s3 = Station(3, 0)
    s4 = Station(10, 0)

    db.session.add(s1)
    db.session.add(s2)
    db.session.add(s3)
    db.session.add(s4)
    

    db.session.commit()


def load_bike():
    """Load bikes into database."""

    b1 = Bike(s1, s1, True, 0)
    b2 = Bike(s2, s2, True, 0)
    b3 = Bike(s4, s4, True, 0)

    db.session.add(b1)
    db.session.add(b2)
    db.session.add(b3)

    db.session.commit()

    
if __name__ == "__main__":
    connect_to_db(app)
    db.drop_all() #prevents dupe seeding
    db.create_all()


    load_users()
    load_bike()
