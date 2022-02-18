from ast import Return
from flask import Blueprint, render_template,request,flash, jsonify,redirect,url_for
import psycopg2

auth = Blueprint('auth',__name__)
conn = psycopg2.connect(
        database='postgres', 
        user='john', 
        host='localhost',
        password='1234',)
conn.autocommit = True
cur = conn.cursor()

@auth.route('/login',methods=['GET','POST'] )
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password1')
        #print(email)
        #print(password)
        try:
            sql_email = f"SELECT * FROM all_users WHERE email='{email}' AND password_1='{password}'"
        
            cur.execute(sql_email)
            data = cur.fetchone()
 
            conn.commit()
            conn.close()
            flash('berhasil login',category='success')
            return redirect(url_for('views.home'))
        except Exception as e:
            return jsonify({"error": f"{e}"})
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        print(first_name)


        if password1 != password2:
            flash('password anda tidak sama', category='error')
        elif len(password1) < 4 :
            flash('password anda telalu pendek', category='error')
        else:
            try:
                # email = user_data['email']
                # first_name = user_data['first_name']
                # password1 = user_data['password_1']

                query = f"INSERT INTO all_users(first_name,email,password_1) VALUES('{first_name}','{email}','{password1}')"

                cur.execute(query)
                conn.commit()
                conn.close()
                jsonify({"success": True,"response":"user added successfully"})
                flash('akun anda sudah masuk', category='success')
                return redirect(url_for('views.home'))
            except Exception as e:
                return jsonify({"error": f"{e}"})    
    return render_template('signup.html')

