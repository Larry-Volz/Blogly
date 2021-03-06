from flask_sqlalchemy import SQLAlchemy
import datetime
"""Models for Blogly."""

db=SQLAlchemy()


DEFAULT_IMG_URL = "https://th.bing.com/th/id/R75faf4f409563b6bae8d6dfc331bba8f?rik=6sPDoHS7E64M%2fw&riu=http%3a%2f%2fprofiledps.com%2fimages%2fdps%2ffull%2fitm_2012-12-22_22-46-40_3.jpg&ehk=fAdHW2putEk%2f5%2bCmhClzA%2b28uiGPMLnq9ISi0qHGW2I%3d&risl=&pid=ImgRaw"



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

    posts = db.relationship('Post', backref='user', cascade="all, delete-orphan")   


class Post(db.Model):
    """blog posts"""

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

    # usrs = db.relationship('User', backref='psts')

    @property
    def friendly_date(self):
        """Return nicely-formatted date - from teacher's example."""
        return self.created_at.strftime("%a %b %d,  %Y at %I:%M %p")


class PostTag(db.Model):
    """Mapping table m2m for posts and tags"""

    __tablename__='posts_tags'

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)


class Tag(db.Model):
    """tags users attach to posts"""

    __tablename__ = 'tags'

    id = db.Column(db.Integer,
    primary_key = True,
    autoincrement = True)

    name = db.Column(db.Text,
    nullable=False, unique=True)

    posts = db.relationship('Post', secondary='posts_tags', backref='tags')




def connect_db(app):
    db.app = app 
    db.init_app(app)



