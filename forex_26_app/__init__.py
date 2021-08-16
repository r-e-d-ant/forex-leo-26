
# ======= IS THERE =======

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import json

app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

with open('etc/config.json') as config_file:
    config = json.load(config_file)

app.config['SECRET_KEY'] = config.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app)

from forex_26_app import routes
from forex_26_app.forms import PostForm, AdminForm, LoginForm
from forex_26_app.models import Admin, Post
