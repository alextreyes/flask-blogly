from datetime import datetime
from app import app
from models import db, User, Post  

db.drop_all()
db.create_all()

new_user = User(first_name='alex', last_name='reyes')

new_post = Post(
    title="New Post Title",
    content="This is the content of the new post.",
    created_at=datetime.utcnow(), 
    user_id=1  
)



db.session.add(new_user)
db.session.add(new_post)
db.session.commit()

