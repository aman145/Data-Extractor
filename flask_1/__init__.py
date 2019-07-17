from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
UPLOAD_FOLDER = '/'

app=Flask(__name__)

app.config['SECRET_KEY']='c72cee28c22645558773db6d22f62803'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
db =SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

from flask_1 import routes
