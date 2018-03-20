from uuid import uuid4
from OpenSchool import db
from datetime import datetime
from helpers.uuid import UuidField

class AttendanceReason(db.Model):
    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)

    allowed = db.Column(db.Boolean, unique=False, default=True, nullable=False)

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)