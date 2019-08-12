from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy			# instead of mysqlconnection
from sqlalchemy.sql import func
from flask_migrate import Migrate			# this is new
app = Flask(__name__)
# configurations to tell our app about the database we'll be connecting to
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books_and_authors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# an instance of the ORM
db = SQLAlchemy(app)
# a tool for allowing migrations/creation of tables
migrate = Migrate(app, db)

# ### ADDING THIS CLASS ####
# the db.Model in parentheses tells SQLAlchemy that this class represents a table in our database

book_to_author_table = db.Table('book_to_author',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True))

class Book(db.Model):	
    id = db.Column(db.Integer, primary_key=True)
    authors_of_book = db.relationship('Author', secondary=book_to_author_table)
    title = db.Column(db.String(45))
    description = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, server_default=func.now())    
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class Author(db.Model):	
    id = db.Column(db.Integer, primary_key=True)
    books_by_author = db.relationship('Book', secondary=book_to_author_table)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    notes = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, server_default=func.now())   
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

#
# TESTING
#
# single_author=Author.query.get(2)
# print (single_author.first_name, single_author.last_name)
# print (single_author.books_by_author)
# print ( "\nauthor dir = ",dir(single_author) )
# print ( "\nauthor.books_by_author dir = ",dir(single_author.books_by_author) )
# single_author.books_by_author.all()
# exit()

# routes go here...



print ('at routes')
@app.route('/')
def book_index():
    # snag books
    books=Book.query.all()
    print ('*'*80)
    print ('rendering book index page')
    return render_template("book_index.html", books=books)

@app.route('/books/<int:book_id>')
def books(book_id):
    # snag book
    book=Book.query.get(book_id)
    authors=Author.query.all()
    print ('*'*80)
    print ('rendering individual book page')
    print (book)
    return render_template("books.html", book=book, authors=authors)

@app.route("/books/create", methods=["POST"])
def create_book():
    print('*'*80)
    print ('Received new book form with the following data:')
    print ('FORM DATA RECEIVED:\n',request.form)
    new_book = Book(
        title=request.form['title'],
        description=request.form['description'],
        )
    db.session.add(new_book)
    db.session.commit()
    return redirect("/")

@app.route("/book/<int:book_id>/add", methods=["POST"])
def add_book_to_author(book_id):
    print('*'*80)
    print ('Received request to book to author with the following form data:')
    print ('FORM DATA RECEIVED:\n',request.form)
    print ('book id: ',book_id)
    existing_book=Book.query.get(book_id)
    existing_author=Author.query.get(request.form['author_id'])
    existing_book.authors_of_book.append(existing_author)
    db.session.commit()
    return redirect("/")

@app.route('/authors')
def author_index():
    # snag authors
    authors=Author.query.all()
    print ('*'*80)
    print ('rendering author index page')
    return render_template("author_index.html", authors=authors)

@app.route('/authors/<int:author_id>')
def authors(author_id):
    # snag book
    author=Author.query.get(author_id)
    books=Book.query.all()
    print ('*'*80)
    print ('rendering individual author page')
    return render_template("authors.html", author=author, books=books)

@app.route("/authors/create", methods=["POST"])
def create_author():
    print('*'*80)
    print ('Received new author form with the following data:')
    print ('FORM DATA RECEIVED:\n',request.form)
    new_author = Author(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        notes=request.form['notes'],
        )
    db.session.add(new_author)
    db.session.commit()
    return redirect("/authors")

@app.route("/author/<int:author_id>/add", methods=["POST"])
def add_author_to_book(author_id):
    print('*'*80)
    print ('Received request to add author to book with the following form data:')
    print ('FORM DATA RECEIVED:\n',request.form)
    print ('Author id: ',author_id)
    existing_book=Book.query.get(request.form['book_id'])
    existing_author=Author.query.get(author_id)
    existing_author.books_by_author.append(existing_book)
    db.session.commit()
    return redirect("/authors")

if __name__ == "__main__":
    app.run(debug=True)
