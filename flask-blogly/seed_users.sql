from models import User, db
from app import app

-- # Create all tables
db.drop_all()
db.create_all()

-- # If table isn't empty, empty it
User.query.delete()

-- # Add pets
larry = User(first_name='Larry', last_name="Volz")
zach = User(first_name='Zachary', last_name="Volz")
faniel = User(first_name='Nathaniel', last_name="Volz")


-- # Add new objects to session, so they'll persist
db.session.add(larry)
db.session.add(zach)
db.session.add(faniel)

-- # Commit--otherwise, this never gets saved!
db.session.commit()