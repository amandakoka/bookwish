from flask import render_template
from bookwish import app, db
from bookwish.models import User, Book


@app.route("/")
def home():
    return render_template("base.html")