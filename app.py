"""Blogly application."""

from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, User, Post, PostTag, Tag    

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  =  False
app.config['SQLALCHEMY_ECHO'] =  True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def redirect_to_list():
    """Redirects to users."""
    return redirect("/users")

@app.route("/users")
def list_users():
    """Returns list of users."""
    users = User.query.all()
    return render_template("list.html", users=users)

@app.route("/users/new")
def view_create_users():
    """Shows form to create a new user."""
    return render_template("newUser.html")

@app.route("/users/new", methods=["POST"])
def create_user():
    """Creates a new user."""
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()
    return redirect("/users")

@app.route("/users/<int:user_id>")
def view_user(user_id):
    """shows user profile"""
    user = User.query.get_or_404(user_id)
    return render_template("details.html", user=user)

@app.route('/users/<int:user_id>/edit')
def users_edit(user_id):
    """Show a form to edit an existing user"""

    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=["POST"])
def users_update(user_id):
    """Handle form submission for updating an existing user"""

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/users")


@app.route('/users/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):
    """Handle form submission for deleting an existing user"""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")

@app.route('/users/<int:user_id>/posts/new', methods=['GET'])
def view_create_post(user_id):
    """Shows form to add a post for a specific user."""
    user = User.query.get_or_404(user_id)
    return render_template('new_post.html', user=user)

@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def create_post(user_id):
    """Handles add form; add post and redirect to the user detail page."""
    user = User.query.get_or_404(user_id)
    title = request.form['title']
    content = request.form['content']

    new_post = Post(title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    return redirect(f"/users/{user_id}")

@app.route('/posts/<int:post_id>', methods=['GET'])
def view_post(post_id):
    """Shows a post with edit and delete buttons."""
    post = Post.query.get_or_404(post_id)

    return render_template('post_details.html', post=post)

@app.route('/posts/<int:post_id>/edit', methods=['GET'])
def view_edit_post(post_id):
    """Shows form to edit a post."""
    post = Post.query.get_or_404(post_id)
    tags = Tag.query.all()
    return render_template('edit_post.html', post=post, tags=tags)

@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def edit_post(post_id):
    """Handles editing of a post. Redirect back to the post view."""
    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']
    selected_tags = request.form.getlist('tags')

    for tag_id in selected_tags:
        new_post_tag = PostTag(post_id=post_id, tag_id=tag_id)
        db.session.add(new_post_tag)


    db.session.commit()
    return redirect(f"/posts/{post_id}")

@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    """Delete the post."""
    post = Post.query.get_or_404(post_id)
    user_id = post.user_id

    db.session.delete(post)
    db.session.commit()
    return redirect(f"/users/{user_id}")


@app.route('/tags')
def show_tags():
    """shows all tags"""
    tags = Tag.query.all()
    return render_template("tag_list.html", tags=tags) 

@app.route("/tags/<int:tag_id>")
def tag_details(tag_id):
    """shows tag details"""

    tag = Tag.query.get_or_404(tag_id)
    return render_template("tag_details.html", tag=tag)

@app.route("/tags/<int:tag_id>/edit", methods=['GET'])
def edit_tag(tag_id):
    """shows edit form"""
    tag = Tag.query.get_or_404(tag_id)
    return render_template('edit_tag.html', tag=tag)


@app.route("/tags/<int:tag_id>/edit", methods=['POST'])
def tag_edit(tag_id):
    """edit tags"""
    tag = Tag.query.get_or_404(tag_id)
    tag.name = request.form['name']

    db.session.commit()
    return redirect(f"/tags/{tag_id}")

@app.route('/tags/<int:tags_id>/delete', methods=["POST"])
def tags_destroy(tags_id):
    """Handle form submission for deleting an existing tag"""

    tag = Tag.query.get_or_404(tags_id)
    db.session.delete(tag)
    db.session.commit()

    return redirect("/tags")

@app.route('/tags/new', methods=['GET'])
def new_tag_form():
    """creates a new tag"""
    return render_template('new_tag.html')

@app.route("/tags/new", methods=["POST"])
def create_tag():
    """Creates a new tag."""
    name = request.form["name"]

    new_tag = Tag(name=name)
    db.session.add(new_tag)
    db.session.commit()
    return redirect("/tags")











