from flask import Flask, render_template, request, request, redirect
from mysqlconnection import connectToMySQL      # import the function that will return an instance of a connection
app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('cr_pets')       # call the function, passing in the name of our db
    pets = mysql.query_db('SELECT * FROM pets;')  # call the query_db function, pass in the query as a string
    print(pets)
    return render_template("index.html", pets=pets)

@app.route("/create_pet", methods=["POST"])
def add_pet_to_db():
    print ('Got add pet request')
    print (request.form)
    mysql = connectToMySQL('cr_pets')
    query = 'INSERT INTO pets (name, type) VALUES (%(name)s, %(type)s)'
    data = {
        'name': request.form['name'],
        'type': request.form['type']
    }
    new_pet_id = mysql.query_db(query,data)
    print (new_pet_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)