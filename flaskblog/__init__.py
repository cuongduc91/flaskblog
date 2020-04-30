from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
# Set a secret key
app.config['SECRET_KEY'] = '8f588d8897247ff20ddd004bc3563425'
# /// current directory creates the site.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager=LoginManager(app)
#the same as route login
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from flaskblog import routes