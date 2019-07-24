from flask import Flask, render_template, request, redirect, flash, session
import re
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL      # import the function that will return an instance of a connection

app = Flask(__name__)

# App-wide items to be used throughout the program:
app.secret_key = 'shh, this is a secret.  no one should know.' # set a secret key for security purposes
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create", methods=["POST"])
def create():
    print ('Got registration request')
    print (request.form)

    # Data validation
    is_valid = True

    if len(request.form['first_name']) < 1:
    	is_valid = False
    	flash("Please enter a first name",'first_name')
    elif request.form['first_name'].isalpha() == False:
        is_valid= False
        flash("First name must be alphabetic only", "first_name")

    if len(request.form['last_name']) < 1:
    	is_valid = False
    	flash("Please enter a last name", "last_name")
    elif request.form['last_name'].isalpha() == False:
        is_valid= False
        flash("Last name must be alphabetic only", "last_name")

    if len(request.form['password']) < 5:
    	is_valid = False
    	flash("Password should be at least 5 characters", "password")
    if request.form['password']!=request.form['password_conf']:
        is_valid = False
        flash("Password confirmation does not match!", "password")

    if len(request.form['email']) < 1:
        is_valid=False
        flash("Email cannot be left blank", "email")
    elif not EMAIL_REGEX.match(request.form['email']):    # test whether a field matches the pattern
        is_valid=False
        flash("Invalid email address!","email")
    else:
        # If that email already exists, complain, as this is your login ID #
        mysql = connectToMySQL('registration')
        query = 'SELECT id FROM users WHERE email = %(email)s'
        data = {
            'email': request.form['email']
        }
        user_id = mysql.query_db(query,data)
        print ("Verifying email existance: \n user_id =",user_id)
        if user_id:
            print ("email exists, erroring out")
            flash("That email address already exists, try something different","email")
            is_valid=False

    if is_valid:
        hashed_pw = bcrypt.generate_password_hash(request.form['password'])
        print (hashed_pw)  
        mysql = connectToMySQL('registration')
        query = 'INSERT INTO users (first_name, last_name, password, email) VALUES (%(fn)s, %(ln)s, %(pw)s, %(eml)s)'
        print (query)
        data = {
            'fn': request.form['first_name'],
            'ln': request.form['last_name'],
            'pw': hashed_pw,
            'eml': request.form['email']
        }
        user_id = mysql.query_db(query,data)
        flash("Successfullly added!")
    else:
        print ("BAD DATA, DID NOT COMMIT")
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    # Set up session data for auth = False
    if 'auth' not in session:
        session['auth'] = False

    print ('Got login request')
    print (request.form)

    # Data validation
    is_valid = True

    if len(request.form['email']) < 1:
        is_valid=False
        flash("Invalid email or password!", "auth")
    elif not EMAIL_REGEX.match(request.form['email']):    # test whether a field matches the pattern
        is_valid=False
        flash("Invalid email or password!", "auth")
    
    
    if len(request.form['password']) < 5:
    	is_valid = False
    	flash("Invalid email or password!", "auth")
    
    if is_valid:
        mysql = connectToMySQL('registration')
        query = 'SELECT first_name, last_name, password FROM users WHERE email = %(email)s'
        data = {
            'email': request.form['email']
        }
        user_id = mysql.query_db(query,data)

        print ("user_id = ",user_id)

        # login verification sequence here  
        result=bcrypt.check_password_hash( user_id[0]['password'], request.form['password'] )
        print ("auth result response:",result)

        if result:
            # passwords match, set up session data accordingly, then rediret to /home
            print ('password and stored hash match, logging user in')
            session['auth'] = True
            session['first_name']=user_id[0]['first_name']
            session['last_name']=user_id[0]['last_name']
            session['email']=request.form['email']
            print ("session data =",session)
            return redirect('/home')
        else:
            print ('password did not match')
            flash("Password is incorrect", "login-password")
    
    # If user/pwd is wrong, punt back to /
    return redirect('/')

@app.route("/home")
def home(): 
    print ('entering /home (post auth)')
    print (session)
    if session['auth']==True:
        print ('session auth is true, going to render home.html next')
        return render_template('home.html',session=session)
    else:
        return redirect('/')

@app.route("/logout")
def logout():
    session.clear()
    session['auth'] = False
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)