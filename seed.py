from datetime import datetime
from app import app
from models import db, User, Post, Tag, PostTag

db.drop_all()
db.create_all()

new_user = User(first_name='alex', last_name='reyes')

new_post1 = Post(
    title="New Post Title",
    content="This is the content of the new post.",
    created_at=datetime.utcnow(), 
    user_id=1  
)
new_post2 = Post(
    title="New Post Title2",
    content="This is the content of the new post.",
    created_at=datetime.utcnow(), 
    user_id=1  
)

new_tag1 = Tag(
    name= 'funny'
)

new_tag2 = Tag(
    name= 'SAD'
)

new_post_tag1 = PostTag(
    post_id=1,
    tag_id=1)

new_post_tag2 = PostTag(
    post_id=1,
    tag_id=2)

new_post_tag3 = PostTag(
    post_id=2,
    tag_id=1)


db.session.add(new_user)
db.session.add_all([new_post1,new_post2])
db.session.add_all([new_tag1, new_tag2])
db.session.commit()
db.session.add_all([new_post_tag1, new_post_tag2, new_post_tag3])
db.session.commit()

