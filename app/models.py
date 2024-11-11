"""
Database Models
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Like(db.Model):
    """
    Table for content likes
    """
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    email = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    origin = db.Column(db.String(120), nullable=False)
    page_slug = db.Column(db.String(120), nullable=False)

class Comment(db.Model):
    """
    Table for comments
    """
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    email = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    origin = db.Column(db.String(120), nullable=False)
    page_slug = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
