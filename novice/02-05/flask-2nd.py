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