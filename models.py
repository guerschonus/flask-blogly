"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    """User."""

    __tablename__="users"
    id = db.Column(db.Integer,
                primary_key=True, 
                autoincrement=True)
    firstname = db.Column(db.TEXT,
                nullable=False)
    lastname = db.Column(db.TEXT,
                nullable=False)
    url = db.Column(db.TEXT,
                nullable=True)
    
    
    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.firstname} {self.lastname}"
