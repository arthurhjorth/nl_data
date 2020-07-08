from sqlalchemy.types import JSON
from nl_data import db


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))


