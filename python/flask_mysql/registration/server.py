from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import connectToMySQL      # import the function that will return an instance of a connection
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
@app.route("/")
def index():
    # mysql = connectToMySQL('registration')       # call the function, passing in the name of our db
    # friends = mysql.query_db('SELECT * FROM users;')  # call the query_db function, pass in the query as a string
    # print(friends)
    return render_template("index.html")

@app.route("/create", methods=["POST"])
def create():
    print ('Got add request')
    print (request.form)

    # Data validation
    is_valid = True
    if len(request.form['first_name']) < 1:
    	is_valid = False
    	flash("Please enter a first name")
    if request.form['first_name'].isalpha() == False:
        is_valid= False
        flash("First name must be alphabetic only")
    if len(request.form['last_name']) < 1:
    	is_valid = False
    	flash("Please enter a last name")
    if request.form['last_name'].isalpha() == False:
        is_valid= False
        flash("Last name must be alphabetic only")
    if len(request.form['password']) < 5:
    	is_valid = False
    	flash("Password should be at least 5 characters")
    if request.form['password']!=request.form['password_conf']:
        is_valid = False
        flash("Password confirmation does not match!")
    if is_valid:
        mysql = connectToMySQL('registration')
        query = 'INSERT INTO users (first_name, last_name, password) VALUES (%(fn)s, %(ln)s, %(pwd)s)'
        data = {
            'fn': request.form['first_name'],
            'ln': request.form['last_name'],
            'pwd': request.form['password']
        }
        user_id = mysql.query_db(query,data)
        flash("Successfullly added!")
    else:
        print ("BAD DATA, DID NOT COMMIT")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)