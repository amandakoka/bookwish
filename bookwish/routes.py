from flask import render_template
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
    return render_template("wishlist.html")


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    return render_template("add_book.html")


