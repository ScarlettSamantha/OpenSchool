from uuid import uuid4
from OpenSchool import db
from datetime import datetime
from helpers.uuid import UuidField

class Room(db.Model):
    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4().hex, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)

    floor = db.Column(db.String(255), unique=False, nullable=True)
    number = db.Column(db.String(255), unique=False, nullable=True)

    note = db.Column(db.Text, unique=False, nullable=True)

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)