"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def connect_db(app):
    db.app = app 
    db.init_app(app)

class User(db.Model):
    """ User/users Model for Blogly blogging application """
    __tablename__ = 'users'

    @classmethod
    def get_all_users(cls):
        return cls.query.all()

    # TODO THIS
    # def __repr__(self):
    #     p=self
    #     return f"<Pet id={p.id} name={p.name} species={p.species} hunger = {p.hunger}>"
    
    id = db.Column(db.Integer,
    primary_key = True,
    autoincrement = True)

    first_name = db.Column(db.String(30),
    nullable = False)

    last_name = db.Column(db.String(50),
    nullable = False)

    img_url = db.Column(db.String(100),
    nullable = True)
    
