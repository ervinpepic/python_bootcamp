
from flask import Flask, render_template, request, redirect, url_for
# import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app=app)
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=False, nullable=False)
    author = db.Column(db.String(120), unique=False, nullable=False)
    rating = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self) -> str:
        return self.title

@app.route('/')
def home():
    book_list = Book.query.all()
    # book_id = request.args.get('id')
    return render_template('index.html', book_list=book_list)


@app.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title = request.form["title"], 
            author = request.form["author"],
            rating =  request.form["rating"]
        )
        db.session.add(instance=new_book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_update = Book.query.get(book_id)
        book_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get("id")
    book = Book.query.get(book_id)
    print(book)
    return render_template("edit.html", book=book)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    delete_book = Book.query.get(book_id)
    db.session.delete(delete_book)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

