from msiapp import db


# Create a data model for the database to be setup for the app
class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False, nullable=False)
    artist = db.Column(db.String(100), unique=False, nullable=False)
    album = db.Column(db.String(100), unique=False, nullable=True)

    def __repr__(self):
        return '<Track %r>' % self.title


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    timestamp = db.Column(db.Integer, unique=False, nullable=False)
    name = db.Column(db.String(100), unique=False, nullable=False)
    country = db.Column(db.String(100), unique=False, nullable=False)
    temperature = db.Column(db.Float, unique=False, nullable=False)
    max_temp = db.Column(db.Float, unique=False, nullable=False)
    min_temp = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return '<City %r>' % self.name
