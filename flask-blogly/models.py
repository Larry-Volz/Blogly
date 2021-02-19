from flask_sqlalchemy import SQLAlchemy
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
    
