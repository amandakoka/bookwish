from flask import render_template, request, redirect, url_for
from bookwish import app, db
from bookwish.models import User, Book


@app.route("/")
def home():
    return render_template("welcome.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/wishlist")
def wishlist():
    books = Book.query.all()
    return render_template("wishlist.html", books=books)


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book = Book(
            book_title=request.form.get("book_title"),
            book_author=request.form.get("book_author"),
            book_genre=request.form.get("book_genre"),
            book_link=request.form.get("book_link"),
            has_read=bool(True if request.form.get("has_read") else False),
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("wishlist"))
    return render_template("add_book.html")


@app.route("/edit_book/<int:book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)

    if request.method == "POST":
        book.book_title = request.form.get("book_title")
        book.book_author = request.form.get("book_author")
        book.book_genre = request.form.get("book_genre")
        book.book_link = request.form.get("book_link")
        book.has_read = bool(request.form.get("has_read"))

        db.session.commit()
        return redirect(url_for('wishlist'))
    return render_template("edit_book.html", book=book, book_id=book_id)


@app.route("/delete_book/<int:book_id>", methods=["GET", "POST"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == "POST":
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('wishlist'))
    return render_template("wishlist.html", book=book)

