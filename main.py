

import os

from flask import Flask, flash, render_template, request, session
from qwe import *
from sqlalchemy.orm import sessionmaker


engine = create_engine('mssql+pyodbc://TOR-PC\SQLEXPRESS/log?driver=ODBC+Driver+11+for+SQL+Server',echo=True )


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('landing_page.html')



@app.route('/login', methods=['GET','POST'])
def do_admin_login():
    if request.method == 'GET':

        return render_template('login.html')


    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()

    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    result = query.first()
    if result:
        session['logged_in'] = True
        return home()
    else:
        flash('wrong password!')
        return render_template('login.html')


@app.route('/signup', methods=['GET','POST'])
def do_admin_signup():
    if request.method == 'GET':

        return render_template('signup.html')


    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])



    Session = sessionmaker(bind=engine)
    s = Session()
    user = User(POST_USERNAME, POST_PASSWORD)
    s.add(user)
    s.commit()



    return home()



@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()





if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='127.0.0.1', port=4000)

