from flask import Flask
from markupsafe import escape
from flask import url_for


app = Flask(__name__)


'''variable rules'''

@app.route('/user/<username>')
def show_user_profile(username):
    #show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show the post with given id, the id is interger
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'