from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()


class Station(db.Model): 

    __tablename__ = "stations"

    station_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    capacity = db.Column(db.Integer(50), nullable=False)
    current_capacity = db.Column(db.Integer(50), nullable=False)
    # sponsors = db.Column(db.String(100), nullable=False)
  

    def __repr__(self):

        return f"<Station station_id={self.station_id}>"

class Bike(db.Model):

    __tablename__ = "bikes"

    bike_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    home_station = db.Column(db.String(50), nullable=False)
    current_station = db.Column(db.String(50), nullable=False)
    checked_in = db.Column(db.Boolean, nullable=False)
    trips = db.Column(db.Integer(50), nullable=False)

 
    def __repr__(self):

        return f"<Bike bike_id={self.bike_id}>"

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///bike'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")