import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY,"
# #                "title varchar(250) NOT NULL UNIQUE,"
# #                "author varchar(250) NOT NULL,"
# #                "rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()

# new_book2 = Book(id=2, title="The Kite Runner", author="Khaled Hosseini", rating=9.5)
# db.session.add(new_book2)
# db.session.commit()

all_books = db.session.query(Book).all()