from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlite3 import Connection as SQLite3Connection

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finalbackend.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True

db=SQLAlchemy(app)
migrate=Migrate(app,db)
# app.test_client()
