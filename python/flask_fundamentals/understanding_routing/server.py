from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    print ("*"*40)
    print ("executing hello_world function")
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def dojo():
    print ("*"*40)
    print ("executing dojo function")
    return 'Dojo!'  # Return the string 'Hello World!' as a response

@app.route('/say/<string:name>')
def say(name):
    print ("*"*40)
    print ("executing say function")
    if type(name) != str :
        return f"{name} is not a string and string is required.  Try again!"
    return f"Hello, {name}"

@app.route('/<int:repeat>/<string:word>')
def repeat_word(repeat,word):
    print ("*"*40)
    print ("executing repeat_word function")
    ans=f""
    for x in range(repeat):
       ans += f"{word} "
    return ans

@app.route("/<path:u_path>")
def you_suck(u_path):
    print ("*"*40)
    print ("executing you_suck function")
    return "You suck - and put in an invalid path!  Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.