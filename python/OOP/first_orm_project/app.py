from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy			# instead of mysqlconnection
from sqlalchemy.sql import func
from flask_migrate import Migrate			# this is new
app = Flask(__name__)
# configurations to tell our app about the database we'll be connecting to
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///first_orm_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# an instance of the ORM
db = SQLAlchemy(app)
# a tool for allowing migrations/creation of tables
migrate = Migrate(app, db)

#### ADDING THIS CLASS ####
# the db.Model in parentheses tells SQLAlchemy that this class represents a table in our database
class User(db.Model):	
    # __tablename__ = "users"    # optional	- if not specified, will user class name as table name.
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    age = db.Column(db.String(4))
    created_at = db.Column(db.DateTime, server_default=func.now())    # notice the extra import statement above
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

# routes go here...

print ('at routes')
@app.route('/')
def index():
    users = User.query.all()
    print ('*'*80)
    print ('all user data:')
    for user in users:
        print (user.first_name,user.last_name,user.email)
    return render_template("index.html", users=users)

@app.route("/users/create", methods=["POST"])
def user_create():
    print('*'*80)
    print ('Received add_new_user form with the following data:')
    print ('FORM DATA RECEIVED:\n',request.form)
    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        email=request.form['email'],
        age=request.form['age']
        )
    db.session.add(new_user)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
