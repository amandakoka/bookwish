import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Check if the "env.py" file exists and import environment variables if it does
if os.path.exists("env.py"):
    import env  # noqa

# Create a Flask application instance
app = Flask(__name__)

# Configure the secret key for the application
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# Configure the URI for the SQLAlchemy database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# Initialize a SQLAlchemy database instance with the Flask application
db = SQLAlchemy(app)

# Import routes from the "bookwish" package
from bookwish import routes  # noqa

