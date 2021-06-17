from app import app, db, bcrypt
from flask import render_template, url_for, request, logging, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_login import login_user, current_user, logout_user, login_required
from app.databasestuff import users
from datetime import datetime
#imported librarys

@app.route('/')
@app.route('/index')
def index():
    return render_template('mainpage.html')
#this the flask route the home page
@app.route('/loginform')
def loginform():
    return render_template('form2.html')
#register page
@app.route('/regform')
def regform():
    return render_template('login.html')
#login page
@app.route('/badreg')
def badreg():
    return render_template('badreg.html')
#if bad register
@app.route('/goodreg')
def goodreg():
    return render_template('goodreg.html')
#if good register
@app.route('/basetest')
def basetest():
    return render_template('basetest.html')
#test html
@app.route('/goodlog')
def goodlog():
    return render_template('goodlog.html')
#if good login

#if incorrect passwrod or email
@app.route('/badlog')
def badlog():
    return render_template('badlog.html')

@app.errorhandler(404)
def page_not_found(e):
    # note that i set the 404 status explicitly
    return render_template('404.html'), 404
#this flask route is to replace the stock 404 (page not found) page

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pass']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        #hash the password in bycrpt
        email = request.form['email']
        time = str(datetime.now())
        #get time now
        year, month, day, hour, minute, seconds = time[:4:], time[5:7:], time[8:10], time[11:13:], time[14:16], time[17:19]
        regdate = (f"year:{year} month:{month} day:{day} hour:{hour} seconds:{seconds}")
        usernew = users.query.filter_by(username=username).first()
        emailnew = users.query.filter_by(email=email).first()
        if emailnew: return render_template("badregemail.html")
        if usernew: return render_template("badreg.html")
        # username or username already in database try again
        user = users(username=username,email=email,password=hashed_password,regdate=regdate)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        session["username"] = user.username
            # adds to the database and adds the user to the session

    return render_template("goodreg.html")
    #then redirect to this html

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
         email = request.form['email']
         password = request.form['pass']

    emaillog = users.query.filter_by(email=email).first()
    if emaillog:
        if bcrypt.check_password_hash(emaillog.password, password):
            flash('successfully logged in')
            session["username"] = emaillog.username
            #sets the users name to whatever there username in the database is
            login_user(emaillog)
            return redirect(url_for('index'))
        else:
           return redirect(url_for('badlog'))
    else:
        return redirect(url_for('badlog'))
        #then redirect to wrong password html

@app.route('/logout')
@login_required
def logout():
    logout_user()
    print(f"{session['username']}, {url_for('logout')}")
    session["username"] = ""
    flash('successfully logged out')
    return redirect(url_for('index'))
#logout route set session to nothing and redirect to homepage

if __name__ == '__main__':
   app.run(debug = True)
#enable debugging
