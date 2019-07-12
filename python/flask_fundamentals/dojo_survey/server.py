from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# our index route will handle rendering our form:
@app.route('/')
def index():
    return render_template("index.html")

# Capture form data after user performs "POST" function:
@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    results=request.form
    return render_template("result.html", results=results)

@app.route('/return', methods=['POST'])
def go_back_to_form():
    print("Got request to go back to form")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)