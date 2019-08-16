from flask import Flask, render_template, request, redirect, flash, session
import re
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL      # import the function that will return an instance of a connection

app = Flask(__name__)

#   App-wide items to be used throughout the program:
app.secret_key = 'shh, this is a secret.  no one should know.' # set a secret key for security purposes
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
bcrypt = Bcrypt(app)

#   MAIN LANDING PAGE - REGISTRATION AND LOGIN
@app.route("/")
def index():
    print ('*'*20)
    print ('Rendering index.html')
    return render_template("index.html")

#   CREATE NEW USER
@app.route("/user/create", methods=["POST"])
def create():
    print ('*'*20)
    print ('Got registration request')
    print (request.form)

    # Data validation
    is_valid = True

    if len(request.form['first_name']) < 2:
    	is_valid = False
    	flash("Please enter a first name",'first_name')
    elif request.form['first_name'].isalpha() == False:
        is_valid= False
        flash("First name must be alphabetic only", "first_name")

    if len(request.form['last_name']) < 2:
    	is_valid = False
    	flash("Please enter a last name", "last_name")
    elif request.form['last_name'].isalpha() == False:
        is_valid= False
        flash("Last name must be alphabetic only", "last_name")

    if len(request.form['password']) < 8:
    	is_valid = False
    	flash("Password should be at least 8 characters", "password")
    if request.form['password']!=request.form['password_conf']:
        is_valid = False
        flash("Passwords do not match!", "password_conf")

    if len(request.form['email']) < 1:
        is_valid=False
        flash("Email cannot be left blank", "email")
    elif not EMAIL_REGEX.match(request.form['email']):    # test whether a field matches the pattern
        is_valid=False
        flash("Invalid email address!","email")
    else:
        # If that email already exists, complain, as this is your login ID #
        mysql = connectToMySQL('deep_thoughts')
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
        mysql = connectToMySQL('deep_thoughts')
        query = 'INSERT INTO users (first_name, last_name, password, email) VALUES (%(fn)s, %(ln)s, %(pw)s, %(eml)s)'
        print (query)
        data = {
            'fn': request.form['first_name'],
            'ln': request.form['last_name'],
            'pw': hashed_pw,
            'eml': request.form['email']
        }
        user_id = mysql.query_db(query,data)
        print('user_id =',user_id)
        flash("Successfullly added!","success")
        session['id']=user_id
        session['auth'] = True
        session['first_name']=request.form['first_name']
        session['last_name']=request.form['last_name']
        session['email']=request.form['email']
        print ("session data =",session)
        return redirect('/thoughts')
    else:
        print ("BAD DATA, DID NOT COMMIT")
    return redirect("/")

#   USER LOGIN SEQUENCE
@app.route("/user/login", methods=["POST"])
def login():
    print ('*'*20)
    print ('Attempting to log user in')
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
    
    if len(request.form['password']) < 8:
    	is_valid = False
    	flash("Invalid email or password!", "auth")
    
    if is_valid:
        mysql = connectToMySQL('deep_thoughts')
        query = 'SELECT id,first_name, last_name, password FROM users WHERE email = %(email)s'
        data = {
            'email': request.form['email']
        }
        user_id = mysql.query_db(query,data)

        print ("user_id = ",user_id)
        print ("length of user_id =",len(user_id))

        if len(user_id)==0:
            is_valid = False
            flash("Invalid email or password!", "auth")
            print ('email did not exist in database')
            return redirect('/')

        # login verification sequence here  
        result=bcrypt.check_password_hash( user_id[0]['password'], request.form['password'] )
        print ("auth result response:",result)

        if result:
            # passwords match, set up session data accordingly, then rediret to /home
            print ('password and stored hash match, logging user in')
            session['id']=user_id[0]['id']
            session['auth'] = True
            session['first_name']=user_id[0]['first_name']
            session['last_name']=user_id[0]['last_name']
            session['email']=request.form['email']
            print ("session data =",session)
            return redirect('/thoughts')
        else:
            print ('password did not match')
            flash("Password is incorrect", "login-password")
    
    # If user/pwd is wrong, punt back to /
    return redirect('/')

#   USER HOME PAGE
@app.route("/thoughts")
def home(): 
    print ('*'*20)
    print ('Moving to user home page, post auth')

    # If user not logged in, punt back to /
    if (session['auth']==False):
        return redirect('/')

    # snag all thoughts
    mysql = connectToMySQL('deep_thoughts')
    query = 'SELECT users.first_name, users.last_name, thoughts.description, thoughts.id, thoughts.owner_id FROM thoughts JOIN deep_thoughts.users ON users.id = thoughts.owner_id'
    data = {}
    thoughts = mysql.query_db(query,data)
    print ("thoughts =",thoughts)

    # Render page back to user
    return render_template('home.html',session=session,thoughts=thoughts)
    
#   CREATE THOUGHTS 
@app.route("/thought/create", methods=["POST"])
def create_thought():

    print ('*'*20)
    print ('Got request to create a thought')
    print (request.form)

    # If user not logged in, punt back to /
    if (session['auth']==False):
        return redirect('/')
    
    # form validation
    is_valid=True
    if len(request.form['description'])<5:
        flash ("Thought must contain at least 5 character","thought")
        is_valid=False
    elif len(request.form['description'])>255:
        flash ("Thought must be 255 chars or less","thought")
        is_valid=False
    
    if is_valid==False:
        print ("******** thought validation failed ********")
        return redirect('/thoughts')

    # Commit thought to database
    mysql = connectToMySQL('deep_thoughts')
    query = 'INSERT INTO thoughts (owner_id, description) VALUES ( %(owner_id)s, %(description)s )'
    print (query)
    data = {
        'owner_id': session['id'],
        'description': request.form['description']
    }
    thought_id = mysql.query_db(query,data)
    print('thought_id =',thought_id)
    flash("Successfully added!","success")

    return redirect('/thoughts')

#   DELETE THOUGHT 
@app.route("/thought/<id>/delete", methods=["POST"])
def delete_thought(id):
    print ('*'*20)
    print ('Got request to delete a thought')
    if (session['auth']==False):
        return redirect('/')

    # Must delete any likes pointing to thought prior to deleting thoughts first
    mysql = connectToMySQL('deep_thoughts')
    query = 'DELETE FROM deep_thoughts.likes WHERE likes.thought_id=%(id)s'
    data = {
        'id': id
    }
    delete_likes = mysql.query_db(query,data)
    print ("Likes deleted:",delete_likes)

    # Delete the thought from the thoughts table now
    mysql = connectToMySQL('deep_thoughts')
    query = 'DELETE FROM deep_thoughts.thoughts WHERE thoughts.id=%(id)s'
    data = {
        'id': id
    }
    delete_id = mysql.query_db(query,data)
    print ("Thought ID deleted:",delete_id)
    return redirect('/thoughts')
    
#   THOUGHT DETAIL PAGE 
@app.route("/thoughts/<thought_id>")
def thought_detail(thought_id):
    print ('*'*20)
    print ('Going to thought detail page')
    if (session['auth']==False):
        return redirect('/')

    # Grab thought from DB
    mysql = connectToMySQL('deep_thoughts')
    query = 'SELECT users.first_name, users.last_name, thoughts.description, thoughts.id, thoughts.owner_id FROM thoughts JOIN deep_thoughts.users ON users.id = thoughts.owner_id WHERE thoughts.id=%(thought_id)s'
    data = {
        'thought_id': thought_id
    }
    thought = mysql.query_db(query,data)
    print ("thought:",thought)

    # Grab users that like this thought
    mysql = connectToMySQL('deep_thoughts')
    query = 'SELECT users.id, users.first_name, users.last_name FROM deep_thoughts.likes JOIN users ON users.id = likes.user_id WHERE thought_id=%(thought_id)s'
    data={
        'thought_id': thought_id
    }
    likes = mysql.query_db(query,data)
    print ('liked by:',likes)

    liked_by_me=False
    if likes:
        for like in likes:
            if like['id']==session['id']:
                liked_by_me=True
                print ('Found that I like this post...')
        if liked_by_me==False:
            print ('I do not like this post, but did find likes')
    else:
        print ('No one likes this post... so sad!')

    return render_template('thoughts.html', thought=thought[0],likes=likes,liked_by_me=liked_by_me)
    

#   LIKE A THOUGHT  
@app.route("/thought/<thought_id>/like", methods=['POST'])
def like_a_thought(thought_id):
    print ('*'*20)
    print ('Got request to like a thought')
    if (session['auth']==False):
        return redirect('/')

    mysql = connectToMySQL('deep_thoughts')
    query = 'INSERT INTO likes (thought_id, user_id) VALUES (%(thought_id)s, %(user_id)s)'
    data = {
        'thought_id': thought_id,
        'user_id': session['id']
    }
    like = mysql.query_db(query,data)
    print ("like:",like)

    return redirect('/thoughts/'+str(thought_id))

#   UNLIKE A THOUGHT  
@app.route("/thought/<thought_id>/unlike", methods=['POST'])
def unlike_a_thought(thought_id):
    print ('*'*20)
    print ('Got request to unlike a thought')
    if (session['auth']==False):
        return redirect('/')
    mysql = connectToMySQL('deep_thoughts')
    query = 'DELETE FROM deep_thoughts.likes WHERE thought_id=%(thought_id)s AND user_id=%(user_id)s'
    data = {
        'user_id': session['id'],
        'thought_id': thought_id
    }
    unlike = mysql.query_db(query,data)
    print ("unlike:",unlike)

    return redirect('/thoughts/'+str(thought_id))

#   LOGOUT SEQUENCE
@app.route("/logout")
def logout():
    session.clear()
    session['auth'] = False
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)