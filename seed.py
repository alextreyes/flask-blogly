from datetime import datetime
from app import app
from models import db, User, Post  # Import the User and Post models

db.drop_all()
db.create_all()

new_user = User(first_name='alex', last_name='reyes')
# Create a new post
new_post = Post(
    title="New Post Title",
    content="This is the content of the new post.",
    created_at=datetime.utcnow(),  # You can customize the creation date if needed
    user_id=1  # Set the user_id foreign key for the post
)


# Commit the changes to the database
db.session.add(new_user)
db.session.add(new_post)
db.session.commit()

