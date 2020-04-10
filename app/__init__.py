from flask import Flask
from flask_wtf.csrf import CsrfProtect
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI ='sqlite:///'+ os.path.join(basedir,'app.db') #path del db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.secret_key = "123456789"
db = SQLAlchemy(app)
CsrfProtect(app)

from app import views