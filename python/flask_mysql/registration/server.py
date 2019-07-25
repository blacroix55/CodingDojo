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
        flash("Passwords do not match!", "password_conf")

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
        print('user_id =',user_id)
        flash("Successfullly added!")
        session['id']=user_id
        session['auth'] = True
        session['first_name']=request.form['first_name']
        session['last_name']=request.form['last_name']
        session['email']=request.form['email']
        print ("session data =",session)
        return redirect('/user/'+str(user_id))
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
    
    
    if len(request.form['password']) < 5:
    	is_valid = False
    	flash("Invalid email or password!", "auth")
    
    if is_valid:
        mysql = connectToMySQL('registration')
        query = 'SELECT id,first_name, last_name, password FROM users WHERE email = %(email)s'
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
            session['id']=user_id[0]['id']
            session['auth'] = True
            session['first_name']=user_id[0]['first_name']
            session['last_name']=user_id[0]['last_name']
            session['email']=request.form['email']
            print ("session data =",session)
            return redirect('/user/'+str(session['id']))
        else:
            print ('password did not match')
            flash("Password is incorrect", "login-password")
    
    # If user/pwd is wrong, punt back to /
    return redirect('/')

#   USER HOME PAGE  (aka dashboard) 
@app.route("/user/<int:user_id>")
def home(user_id): 
    print ('*'*20)
    print ('Moving to user home page, post auth')

    # If user not logged in or landing at right place, punt back to /
    if (session['auth']==False)  or (user_id != session['id']):
        return redirect('/')

    # Grab who we are following to pass into render_template
    mysql = connectToMySQL('registration')
    query = 'SELECT following_id FROM follows WHERE follower_id=%(follower_id)s'
    data = {
        'follower_id': user_id
    }
    following = mysql.query_db(query,data)
    print ("following =",following)

    # Convert following's dictionary into a string to pass into tweet query
    following_ids="("
    for id in following:
        following_ids= following_ids + str(id['following_id'])+","
    following_ids=following_ids+str(user_id)+")"
    print (following_ids)

    # Grab tweets to pass into render_template
    mysql = connectToMySQL('registration')
    query = 'SELECT CONCAT(users.first_name," ",users.last_name) as creator, tweets.creator_id, tweets.id, tweets.message,tweets.created_at '
    query = query + 'FROM registration.tweets JOIN registration.users ON users.id = tweets.creator_id WHERE creator_id IN '+following_ids
    query = query + ' ORDER BY tweets.created_at DESC'
    data = {
        'following_ids': following_ids
    }
    tweets = mysql.query_db(query,data)
    print ("tweets =",tweets)


#[{'following_id': 17}, {'following_id': 17}, {'following_id': 17}, {'following_id': 17}, {'following_id': 16}, {'following_id': 6}]




    # Render page back to user
    return render_template('home.html',session=session,tweets=tweets)
    
#   CREATE TWEETS 
@app.route("/tweets/create", methods=["POST"])
def create_tweets():

    print ('*'*20)
    print ('Got request to create a tweet')
    print (request.form)

    # If user not logged in, punt back to /
    if (session['auth']==False):
        return redirect('/')
    
    # form validation
    is_valid=True
    if len(request.form['message'])<1:
        flash ("Tweet must contain at least one character","tweet")
        is_valid=False
    elif len(request.form['message'])>255:
        flash ("Tweet must be 255 chars or less","tweet")
        is_valid=False
    
    if is_valid==False:
        print ("******** tweet validation failed ********")
        return redirect('/user/'+str(session['id']))

    # Commit tweet to database
    mysql = connectToMySQL('registration')
    query = 'INSERT INTO tweets (creator_id, message) VALUES ( %(creator_id)s, %(message)s )'
    print (query)
    data = {
        'creator_id': session['id'],
        'message': request.form['message']
    }
    tweet_id = mysql.query_db(query,data)
    print('tweet_id =',tweet_id)
    flash("Successfully added!")

    return redirect('/user/'+str(session['id']))

#   LIKE TWEETS 
@app.route("/tweets/<tweet_id>/add_like", methods=["POST"])
def like_tweet(tweet_id):
    print ('*'*20)
    print ('Got request to like a tweet')
    if (session['auth']==False):
        return redirect('/')
    
    # CHECK TO SEE IF UER ALREADY LIKES POST #
    mysql = connectToMySQL('registration')
    query = 'SELECT id FROM likes WHERE tweet_id=%(tweet_id)s AND user_id=%(user_id)s'
    data = {
    'user_id': session['id'],
    'tweet_id': tweet_id
    }
    like = mysql.query_db(query,data)
    
    # if like exists, skip; otherwise, add the like to the DB
    if like:
        print ("User already likes this tweet!")
    else: 
        print ("Adding like")
        mysql = connectToMySQL('registration')
        query = 'INSERT INTO likes (user_id, tweet_id) VALUES ( %(user_id)s, %(tweet_id)s )'
        data = {
            'user_id': session['id'],
            'tweet_id': tweet_id
        }
        like = mysql.query_db(query,data)
        print ("Like response =",like)

    return redirect('/user/'+str(session['id']))

#   EDIT TWEETS 
@app.route("/tweets/<tweet_id>/edit")
def edit_tweet(tweet_id):
    print ('*'*20)
    print ('Got request to edit a tweet')
    if (session['auth']==False):
        return redirect('/')
    
    # SNAG TWEET TO POPULATE FORM FOR EDITING #
    mysql = connectToMySQL('registration')
    query = 'SELECT id, message, creator_id FROM tweets WHERE id=%(tweet_id)s'
    data = {
    'tweet_id': tweet_id
    }
    tweet = mysql.query_db(query,data)
    print ("tweet=",tweet)
    print ("session=",session)
    return render_template('edit.html',session=session,tweet=tweet)

#   UPDATE TWEETS 
@app.route("/tweets/<tweet_id>/update", methods=["POST"])
def update_tweet(tweet_id):
    print ('*'*20)
    print ('Got request to update a tweet')
    print ("form data=",request.form)

    # form validation
    is_valid=True
    if len(request.form['message'])<1:
        flash ("Tweet must contain at least one character","tweet")
        is_valid=False
    elif len(request.form['message'])>255:
        flash ("Tweet must be 255 chars or less","tweet")
        is_valid=False
    
    if is_valid==False:
        print ("******** tweet validation failed ********")
        return redirect('/tweets/'+tweet_id+"/edit")

    if 'cancel' in request.form:
        print ('user clicked cancel, redirecting to user home')
        
    elif 'update' in request.form:
        print ('user clicked update, updating tweet in database')
        mysql = connectToMySQL('registration')
        query = 'UPDATE tweets SET message="%(message)s" where id=%(tweet_id)s'
        data = {
            'message': request.form['message'],
            'tweet_id': tweet_id
        }
        update = mysql.query_db(query,data)
        print ("Update response =",update)
    
    return redirect('/user/'+str(session['id']))

#   DELETE TWEETS 
@app.route("/tweets/<id>/delete")
def delete_tweet(id):
    print ('*'*20)
    print ('Got request to delete a tweet')
    if (session['auth']==False):
        return redirect('/')
    mysql = connectToMySQL('registration')
    query = 'DELETE FROM registration.tweets WHERE tweets.id=%(id)s'
    data = {
        'id': id
    }
    delete_id = mysql.query_db(query,data)
    print ("Tweet ID deleted:",delete_id)
    return redirect('/user/'+str(session['id']))

#   USERS PAGE 
@app.route("/users")
def user_follows():
    print ('*'*20)
    print ('Going to users page to follow people')
    if (session['auth']==False):
        return redirect('/')

    # Get full userlist
    mysql = connectToMySQL('registration')
    query = 'SELECT id,first_name,last_name,email FROM users ORDER BY last_name'
    data = {}
    users = mysql.query_db(query,data)
    print ("users:",users)

    return render_template('users.html',users=users,my_id=session['id'])

#   FOLLOW SOMEONE 
@app.route("/user/<follower_id>/follow/<following_id>")
def add_follow(follower_id,following_id):
    print ('*'*20)
    print ('Got request to follow someone')
    if (session['auth']==False):
        return redirect('/')

    mysql = connectToMySQL('registration')
    query = 'INSERT INTO follows (follower_id, following_id) VALUES (%(follower_id)s, %(following_id)s)'
    data = {
        'follower_id': follower_id,
        'following_id': following_id
    }
    users = mysql.query_db(query,data)
    print ("users:",users)

    return redirect('/users')

#   LOGOUT SEQUENCE
@app.route("/logout")
def logout():
    session.clear()
    session['auth'] = False
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)