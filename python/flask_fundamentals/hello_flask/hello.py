from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/hello/<name>')
def hello(name):
    print ("*"*40)
    print ("responding to call to /hello/<name>")
    return f"Hello, {name}"

@app.route('/success')
def success():
    return "success"

@app.route('/user/<username>/<id>')
def show_user_profile(username,id):
    return f"Username: {username}  ID: {id}"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.