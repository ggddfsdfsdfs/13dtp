from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bruh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databasev2.db'
#this links the app to the database
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'regform'
bcrypt = Bcrypt(app)

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
#adds a new commands

from app import routes
