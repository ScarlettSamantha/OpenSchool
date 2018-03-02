from uuid import uuid4
from entitys.gender import Gender
from OpenSchool import db
from datetime import datetime
from helpers.uuid import UuidField


class User(db.Model):
    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4().hex, primary_key=True)

    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=True)

    first_name = db.Column(db.String(255), unique=False, nullable=False)
    last_name = db.Column(db.String(255), unique=False, nullable=False)

    gender = db.Column(db.Enum(Gender), unique=False, default=Gender.unknown)

    is_bot = db.Column(db.Boolean(), default=False)
    is_blocked = db.Column(db.Boolean(), default=False)

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)