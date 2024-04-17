from bookwish import db 


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(250), nullable=False)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(255), nullable=False)
    book_author = db.Column(db.String(255), nullable=False)
    book_genre = db.Column(db.String(100), nullable=True)
    book_link = db.Column(db.String(255), nullable=True)
    has_read = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('books',cascade='all, delete', lazy=True))

