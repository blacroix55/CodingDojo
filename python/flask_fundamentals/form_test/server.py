from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

# our index route will handle rendering our form:
@app.route('/')
def index():
    return render_template("index.html")

# Capture form data after user performs "POST" function:
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    print ("showing the user into from the form")
    print (request.form)
    return render_template("show.html")

if __name__ == "__main__":
    app.run(debug=True)