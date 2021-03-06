# project/api/models.py

import os  # new

from sqlalchemy.sql import func
from flask_admin.contrib.sqla import ModelView  # new

from project import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

# new
if os.getenv("FLASK_ENV") == "development":
    from project import admin
    admin.add_view(ModelView(User, db.session))
