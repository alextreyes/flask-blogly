"""Models for Blogly."""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    """User Model"""

    __tablename__ = "users"

    id = db.Column(db.Integer, 
                   primary_key= True, 
                   autoincrement = True )

    first_name = db.Column(db.String(20), 
                     nullable = False, 
                     unique= True)
    last_name = db.Column(db.String(20),
                          nullable = False,
                          unique = True)
    image_url = db.Column(db.String,
                          nullable = True,
                          default = 'https://static.vecteezy.com/system/resources/previews/020/765/399/non_2x/default-profile-account-unknown-icon-black-silhouette-free-vector.jpg')
    
    posts = db.relationship("Post", backref="user")
                          

                          

    
class Post(db.Model):
    """Post Model"""
    
    __tablename__ = "posts"

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)
    title = db.Column(db.String(100), 
                      nullable=False)
    content = db.Column(db.String, 
                        nullable=False)
    created_at = db.Column(db.DateTime, 
                           nullable=False, 
                           default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                         nullable=False)


    post_tags = db.relationship("PostTag", backref='post',cascade='all, delete-orphan')

class Tag(db.Model):
    """Tag Model"""

    __tablename__ = "tags"
        
    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)
    name = db.Column(db.String, 
                     nullable=False, 
                     unique=True)
    post_tags = db.relationship("PostTag", backref='tag', cascade='all, delete-orphan')

class PostTag(db.Model):
    """PostTag Model"""

    __tablename__ = 'post_tags'

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True, nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True, nullable=False)




