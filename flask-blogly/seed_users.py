from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add pets
bilbo = User(first_name='Bilbo', last_name="Baggins", img_url="https://github.com/Larry-Volz/Blogly/blob/master/flask-blogly/static/images/Bilbo_baggins.jpeg?raw=true")
frodo = User(first_name='Frodo', last_name="Baggins", img_url="https://github.com/Larry-Volz/Blogly/blob/master/flask-blogly/static/images/frodo_baggins.jpeg?raw=true")
dr_who = User(first_name='Doctor', last_name="Who", img_url="https://github.com/Larry-Volz/Blogly/blob/master/flask-blogly/static/images/Doctor-Who.jpg?raw=true")


# Add new objects to session, so they'll persist
db.session.add(dr_who)
db.session.add(bilbo)
db.session.add(frodo)

# Commit--otherwise, this never gets saved!
db.session.commit()