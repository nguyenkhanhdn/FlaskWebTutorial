"""
Routes and views for the flask application.
"""
from markupsafe import escape
from datetime import datetime
from flask import render_template
from Lesson2 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )
@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/admin/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'admin/{escape(subpath)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/urlex')
def urlex():
    """Renders the about page."""
    return render_template('urlbuilding.html')

@app.route('/create/<first_name>/<last_name>')
def create(first_name=None, last_name=None):
    return 'Hello ' + first_name + ',' + last_name

@app.route('/sales/<int:id>')
def sales(id=0):
    return "The transaction is "+str(id)

@app.route('/product/<name>')
def product(name):
    return "The product is " + str(name)
