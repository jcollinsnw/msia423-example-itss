from msiapp import db
from msiapp.models import Track


# Creates a table in the database provided as the 'SQLALCHEMY_DATABASE_URI'
# configuration parameter in __init__.py with the schema defined by models.Track()
def create_db():
    db.create_all()
    track1 = Track(artist='Britney Spears', album='Circus', title='Radar')
    track2 = Track(artist='Emancipator', album='Dusk to Dawn', title='Minor Cause')
    db.session.add(track1)
    db.session.add(track2)
    db.session.commit()


if __name__ == "__main__":
    create_db()
