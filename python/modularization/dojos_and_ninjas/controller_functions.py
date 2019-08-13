from flask import render_template, request, redirect
from config import db
from models import User, Dojo

def index():
    # snag dojos+ninjas
    dojos=Dojo.query.all()
    ninjas=User.query.all()
    print ('*'*80)
    print ('all dojo data:')
    print (dojos)
    # add user+dojo DB responses to the render template below, update index.html with jinja2 iterations
    return render_template("index.html", dojos=dojos, ninjas=ninjas)

def user_create():
    print('*'*80)
    print ('Received new user form with the following data:')
    print ('FORM DATA RECEIVED:\n',request.form)
    ninja = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        dojo_id=request.form['dojo']
        )
    db.session.add(ninja)
    db.session.commit()
    return redirect("/")

def create_dojo():
    print('*'*80)
    print ('Received new dojo form with the following data:')
    print ('FORM DATA RECEIVED:\n',request.form)
    # Adding new dojo to database
    new_dojo=Dojo(name=request.form['dojo_name'],city=request.form['dojo_city'],state=request.form['dojo_state'])
    db.session.add(new_dojo)
    db.session.commit()
    # end db insert
    return redirect("/")
