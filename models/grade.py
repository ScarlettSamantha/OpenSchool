from uuid import uuid4
from OpenSchool import db
from datetime import datetime
from helpers.uuid import UuidField

class Grade(db.Model):
    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4, primary_key=True)

    is_group_grade = db.Column(db.Boolean, unique=False, default=False)

    percentage = db.Column(db.Integer, unique=False)
    weight = db.Column(db.Numeric(precision=5, asdecimal=True))

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)