from app import db, login_manager
from flask import render_template, url_for, session
import sqlite3
import datetime
from flask_login import UserMixin, current_user

@login_manager.user_loader
def load_user(user_id):
    return users.query.get(int(user_id))
#this shows the layout of the table users to flask
class users(db.Model ,UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)
    regdate = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"user('{self.username}', '{self.email}')"
#shows the layout of the table posts to flask
# class posts(db.Model ,UserMixin):
#     postid = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     image = db.Column(db.String(100), unique=True, nullable=False)
#     text = db.Column(db.String(100), unique=True, nullable=False)
#     postusers = db.Column(db.Integer(100), ForeignKey("userid"), nullable=False)
