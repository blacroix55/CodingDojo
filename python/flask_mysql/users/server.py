from flask import Flask, render_template, request, request, redirect
from mysqlconnection import connectToMySQL      # import the function that will return an instance of a connection
app = Flask(__name__)
@app.route("/users")
def index():
    print('*'*80)
    print ('entered index route')
    mysql = connectToMySQL('users_db')       # call the function, passing in the name of our db
    users = mysql.query_db('SELECT * FROM users_db.users;')  # call the query_db function, pass in the query as a string
    print ("ALL USERS =",users)
    return render_template("index.html", users=users)

@app.route("/users/<id>")
def show_user_details(id):
    print('*'*80)
    print ('entered show_user_details route')
    mysql = connectToMySQL('users_db')  
    user = mysql.query_db(f'SELECT * FROM users_db.users WHERE id={id};')  
    print (user)
    return render_template("show.html", user=user)

@app.route("/users/new")
def new():
    print('*'*80)
    print ('entered create new user route')
    return render_template("create.html")

@app.route("/users/create", methods=["POST"])
def create():
    print('*'*80)
    print ('Received add_new_user form with the following data:')
    print ('FORM DATA RECEIVED:\n',request.form)
    mysql = connectToMySQL('users_db')
    query = 'INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)'
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    new_user_id = mysql.query_db(query,data)
    return redirect("/users")

@app.route("/users/<id>/edit")
def edit(id):
    print('*'*80)
    print ('entered edit user route')
    mysql = connectToMySQL('users_db')  
    user = mysql.query_db(f'SELECT * FROM users_db.users WHERE id={id};')
    return render_template("edit.html",user=user)

@app.route("/users/<id>/update", methods=["POST"])
def update(id):
    print('*'*80)
    print ('Received update user form with the following data:')
    print ('FORM DATA RECEIVED:\n',request.form)
    print ('ID resolves to',id)
    mysql = connectToMySQL('users_db')
    query = 'UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s'
    data = {
        'id': {id},
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    new_user_id = mysql.query_db(query,data)
    return redirect(f"/users/{id}")

@app.route("/users/<id>/destroy")
def destroy(id):
    print('*'*80)
    print ('entered delete user route')
    mysql = connectToMySQL('users_db')  
    user = mysql.query_db(f'DELETE FROM users_db.users WHERE id={id};')
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)