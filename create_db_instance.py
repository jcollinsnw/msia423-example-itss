from msiapp import db
from msiapp.models import Track

import os
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
db.create_engine(SQLALCHEMY_DATABASE_URI)
