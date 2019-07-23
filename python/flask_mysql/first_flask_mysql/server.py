from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import connectToMySQL      # import the function that will return an instance of a connection
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
@app.route("/")
def index():
    mysql = connectToMySQL('first_flask')       # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM friends;')  # call the query_db function, pass in the query as a string
    print(friends)
    return render_template("index.html", all_friends=friends)

@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
    print ('Got add user request')
    print (request.form)
    is_valid = True
    if len(request.form['fname']) < 1:
    	is_valid = False
    	flash("Please enter a first name")
    if len(request.form['lname']) < 1:
    	is_valid = False
    	flash("Please enter a last name")
    if len(request.form['occ']) < 2:
    	is_valid = False
    	flash("Occupation should be at least 2 characters")
    if is_valid:
        mysql = connectToMySQL('first_flask')
        query = 'INSERT INTO friends (first_name, last_name, occupation) VALUES (%(fn)s, %(ln)s, %(occup)s)'
        data = {
            'fn': request.form['fname'],
            'ln': request.form['fname'],
            'occup': request.form['occ']
        }
        new_friend_id = mysql.query_db(query,data)
        flash("Successfullly added!")

    else:
        print ("BAD DATA, DID NOT COMMIT")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)