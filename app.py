from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Hello from Flask with Database!"
