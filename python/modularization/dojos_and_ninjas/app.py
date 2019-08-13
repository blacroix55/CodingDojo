from flask import render_template, request, redirect
from config import app, db
from models import User, Dojo

# from sqlalchemy.sql import func

# from flask_sqlalchemy import SQLAlchemy			# instead of mysqlconnection
# from sqlalchemy.sql import func
# from flask_migrate import Migrate			# this is new
# app = Flask(__name__)
# # configurations to tell our app about the database we'll be connecting to
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_and_dojos.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # an instance of the ORM
# db = SQLAlchemy(app)
# # a tool for allowing migrations/creation of tables
# migrate = Migrate(app, db)

#### ADDING THIS CLASS ####
# the db.Model in parentheses tells SQLAlchemy that this class represents a table in our database
# class User(db.Model):	
#     # __tablename__ = "users"    # optional	- if not specified, will user class name as table name.
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(45))
#     last_name = db.Column(db.String(45))
#     #dojo_id is the FK, pointing to Dojo.id; one dojo may have many users (one-to-many)
#     dojo_id = db.Column(db.Integer, db.ForeignKey('dojo.id'), nullable=False)
#     created_at = db.Column(db.DateTime, server_default=func.now())    # notice the extra import statement above
#     updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

# class Dojo(db.Model):	
#     # __tablename__ = "users"    # optional	- if not specified, will user class name as table name.
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(45))
#     city = db.Column(db.String(45))
#     state = db.Column(db.String(45))
#     created_at = db.Column(db.DateTime, server_default=func.now())    # notice the extra import statement above
#     updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

# routes go here...

print ('at routes')
@app.route('/')
def index():
    # snag dojos+ninjas
    dojos=Dojo.query.all()
    ninjas=User.query.all()
    print ('*'*80)
    print ('all dojo data:')
    print (dojos)
    # add user+dojo DB responses to the render template below, update index.html with jinja2 iterations
    return render_template("index.html", dojos=dojos, ninjas=ninjas)

@app.route("/users/create", methods=["POST"])
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

@app.route("/dojos/create", methods=["POST"])
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

if __name__ == "__main__":
    app.run(debug=True)
