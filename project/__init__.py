# project/__init__.py

from flask import Flask, jsonify
from flask_restx import Resource, Api

# instantiate the app
app = Flask(__name__)
api = Api(app)

import os
# set config
app_settings = os.getenv('APP_SETTINGS')  # new
app.config.from_object(app_settings)      # ne

# see log using docker-compose logs
import sys
print(app.config, file=sys.stderr)


class Ping (Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong !!!!',
        }


api.add_resource(Ping, '/ping')
