# project/db_create_Alchemy.py

from views import db
from models import User

# create the database and db table
db.create_all()
db.session.commit()
