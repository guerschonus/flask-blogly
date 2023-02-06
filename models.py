"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime

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

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")
    
    
    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.firstname} {self.lastname}"

class Post(db.Model):
    """Post"""
    __tablename__="posts"
    id = db.Column(db.Integer, 
                primary_key=True,
                autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @property
    def friendly_date(self):
        """Return nicely-formatted date."""

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")

