from models import User, Post, db, Tag, PostTag
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()
Post.query.delete()
Tag.query.delete()
PostTag.query.delete()

# Add users
bilbo = User(first_name='Bilbo', last_name="Baggins", img_url="https://github.com/Larry-Volz/Blogly/blob/master/flask-blogly/static/images/Bilbo_baggins.jpeg?raw=true")
frodo = User(first_name='Frodo', last_name="Baggins", img_url="https://github.com/Larry-Volz/Blogly/blob/master/flask-blogly/static/images/frodo_baggins.jpeg?raw=true")
dr_who = User(first_name='Doctor', last_name="Who", img_url="https://github.com/Larry-Volz/Blogly/blob/master/flask-blogly/static/images/Doctor-Who.jpg?raw=true")


# Add new users to session, so they'll persist
db.session.add(bilbo)
db.session.add(frodo)
db.session.add(dr_who)

# Commit--otherwise, this never gets saved!
db.session.commit()

# Add new posts
post1 = Post(title='Why is there air?', content='The dictionary defines air as blahdy blah blah', user_id="2")
post2 = Post(title='So a horse walks into a bar', content='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nulla, quas placeat. Hic perspiciatis quisquam vel, voluptatem debitis odit dicta? Consectetur totam rem praesentium pariatur quia rerum dolor. Cumque, optio modi.', user_id="1")
post3 = Post(title='Don''t eat asphalt', content='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nulla, quas placeat. Hic perspiciatis quisquam vel, voluptatem debitis odit dicta? Consectetur totam rem praesentium pariatur quia rerum dolor. Cumque, optio modi.', user_id="2")
post4 = Post(title='Wibbly-Wobbly Timey-wimey', content='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nulla, quas placeat. Hic perspiciatis quisquam vel, voluptatem debitis odit dicta? Consectetur totam rem praesentium pariatur quia rerum dolor. Cumque, optio modi.', user_id="3")
post5 = Post(title='4 breakfasts is enough', content='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nulla, quas placeat. Hic perspiciatis quisquam vel, voluptatem debitis odit dicta? Consectetur totam rem praesentium pariatur quia rerum dolor. Cumque, optio modi.', user_id="1")

# Add new posts to session, so they'll persist
db.session.add(post1)
db.session.add(post2)
db.session.add(post3)
db.session.add(post4)
db.session.add(post5)

# Commit--otherwise, this never gets saved!
db.session.commit()

#Add new tags
tag1 = Tag(name="family")
tag2 = Tag(name="business")
tag3 = Tag(name="fun")
tag4 = Tag(name="magic")

#Add tags to session, so they'll persist
db.session.add(tag1)
db.session.add(tag2)
db.session.add(tag3)
db.session.add(tag4)

# Commit--otherwise, this never gets saved!
db.session.commit()

#add new post-tag connection
pt1 = PostTag(post_id=1, tag_id=3)
pt2 = PostTag(post_id=2, tag_id=3)
pt3 = PostTag(post_id=2, tag_id=4)
pt4 = PostTag(post_id=3, tag_id=3)
pt5 = PostTag(post_id=3, tag_id=2)
pt6 = PostTag(post_id=3, tag_id=1)
pt7 = PostTag(post_id=4, tag_id=1)
pt8 = PostTag(post_id=4, tag_id=2)
pt9 = PostTag(post_id=4, tag_id=3)
pt10 = PostTag(post_id=4, tag_id=4)
pt11 = PostTag(post_id=5, tag_id=3)
pt12 = PostTag(post_id=5, tag_id=4)

#add post-tags to session
db.session.add(pt1)
db.session.add(pt2)
db.session.add(pt3)
db.session.add(pt4)
db.session.add(pt5)
db.session.add(pt6)
db.session.add(pt7)
db.session.add(pt8)
db.session.add(pt9)
db.session.add(pt10)
db.session.add(pt11)
db.session.add(pt12)

# Commit--otherwise, this never gets saved!
db.session.commit()