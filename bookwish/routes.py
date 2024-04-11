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