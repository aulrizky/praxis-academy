from flask import Flask, flash, request, redirect, url_for,render_template, send_from_directory,make_response,abort,jsonify,session
from markupsafe import escape
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '/home/aul/Documents/Praxi/praxis-academy/novice/02-04/upload'
ALLOWED_EXTENTIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'HGFYTCHDYT8587HGFHHDJFJ'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

'''Hello-world '''
# @app.route('/')
# def hello_world():
#     return 'Hello, world!'


''' Routing'''
# @app.route('/')
# def index():
#     return 'Index page'

# @app.route('/hello/')
# def hello():
#     return 'Hello, world!'

'''variable rules'''

# @app.route('/user/<username>')
# def show_user_profile(username):
#     #show the user profile for that user
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     #show the post with given id, the id is interger
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

'''Unique URL/'''

# @app.route('/projects/')
# def projects():
#     return 'the project page'

# @app.route('/about')
# def about():
#     return 'the about page'

'''URL Building '''

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f"{username}\'s profile"

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username = 'John Doe'))

# ''''randering template'''
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)
# ''''HTTP methods'''
# @app.route('/login', methods = ['GET','POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()
# def do_the_login():
#     return 'test'
# def show_the_login_form():
#     return 'test2'
'''accessing req data'''

with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'
    
with app.request_context(environ):
    assert request.method == 'POST'

# '''req object'''

# @app.route('/login', methods=['POST','GET'])
# def login():
#     username = request.cookies.get('username')
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         if username == 'admin' and password == 'admin':
#             flash('success login','success')
#             resp = make_response(redirect('/'))
#             resp.set_cookie('username',username)
#             return resp
#         else:
#             flash('wrong username or password')
#     return render_template('login.html')


# def valid_login(username,password):
#     pass 

# def log_the_user_in(v):
#     return 'berhasil login'



# def allowed_file(filename):
#     return '.' in filename and \
#             filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENTIONS

# @app.route('/', methods=['GET','POST'])
# def upload_file():
#     if request.method == 'POST':
#         # if 'file' not in request.files:
#         #     flash('no file part')
#         #     return redirect(request.url)
#         file = request.files['file']


#         # if file.filename =='': 
#         #     flash('no select file')
#         #     return redirect(request.url)

#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
#             print(filename)
#             # return redirect(url_for('download_file', name=filename))
#             return 'berhasil upload file'
#     return render_template('upload.html')     

# @app.route('/upload/<name>')
# def download_file(name):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],name)


# '''redirect and error'''
# @app.route('/')
# def index():
#     return redirect(url_for('login'))

# @app.route('/login')
# def login():
#     abort(401)
#     return "hahahahaha"

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'),404

# @app.errorhandler(404)
# def not_found(error):
#     return render_template('error.html'), 404

# @app.errorhandler(404)
# def not_found(error):
#     resp = make_response(render_template('error.html'), 404)
#     resp.headers['X-Something'] = 'A value'
#     return resp

# @app.route("/users")
# def users_api():
#     users = get_all_users()
#     return jsonify([user.to_json() for user in users])

# @app.route('/me')
# def me_api():
#     #user = get_current_user()
#     return {
#         "username" : 'test',
#         "theme" : 'ubuntu',
#         "image" : 'image.img',
#     }

@app.route('/')
def index():
    if 'username' in session:
        return f'logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))