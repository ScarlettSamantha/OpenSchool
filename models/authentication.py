from uuid import uuid4
from OpenSchool import db
from datetime import datetime
from helpers.uuid import UuidField

class Authentication(db.Model):
    key = db.Column(UuidField, unique=True, nullable=False, default=uuid4().hex, primary_key=True)
    expiration = db.Column(db.DateTime, unique=False, nullable=True)

    note = db.Column(db.Text, unique=False, nullable=True)
    is_blocked = db.Column(db.Boolean, default=False, nullable=False, unique=False)

    user_id = db.Column(UuidField, db.ForeignKey('user.id'), nullable=False)

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)