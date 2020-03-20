# project/__init__.py

from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# instantiate the app
app = Flask(__name__)
api = Api(app)

import os
# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# see log using docker-compose logs
import sys
print(app.config, file=sys.stderr)

# setup database
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


class Ping (Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong pong',
        }


api.add_resource(Ping, '/ping')
