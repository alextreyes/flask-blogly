"""Models for Blogly."""

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
    




