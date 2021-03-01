from flask_sqlalchemy import SQLAlchemy
import datetime
"""Models for Blogly."""

DEFAULT_IMG_URL = "https://th.bing.com/th/id/R75faf4f409563b6bae8d6dfc331bba8f?rik=6sPDoHS7E64M%2fw&riu=http%3a%2f%2fprofiledps.com%2fimages%2fdps%2ffull%2fitm_2012-12-22_22-46-40_3.jpg&ehk=fAdHW2putEk%2f5%2bCmhClzA%2b28uiGPMLnq9ISi0qHGW2I%3d&risl=&pid=ImgRaw"

db=SQLAlchemy()

def connect_db(app):
    db.app = app 
    db.init_app(app)


class User(db.Model):
    """ User/users Model for Blogly blogging application """
    __tablename__ = 'users'

    def full_name(self):
        """Return user's full name"""
        return f"{self.first_name} {self.last_name}"
        
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

    img_url = db.Column(db.String(255),
    nullable = True, default = DEFAULT_IMG_URL)
    

class Post(db.Model):
    __tablename__='posts'

    id = db.Column(db.Integer,
    primary_key = True,
    autoincrement = True)

    title = db.Column(db.Text,
    nullable = False)

    content = db.Column(db.Text, 
    nullable = False)

    created_at = db.Column(db.DateTime,
    nullable=False,
    default=datetime.datetime.now)
    
    user_id = db.Column(db.Integer, 
    db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', backref='posts')

    @property
    def friendly_date(self):
        """Return nicely-formatted date - from teacher's example."""
        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")
