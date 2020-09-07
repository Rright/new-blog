#
#   Created by Voronov Vadim
#


from os import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import basedir


UPLOAD_FOLDER = path.join(basedir, "app", "static", "images")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = path.join("sqlite:///" + basedir, 'app.db')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)


from app import routes
