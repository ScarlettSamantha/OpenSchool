from uuid import uuid4
from OpenSchool import db
from datetime import datetime
from helpers.uuid import UuidField

class StudentClass(db.Model):
    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)

    tax = db.Column(db.String(255), unique=False, nullable=True)
    coc = db.Column(db.String(255), unique=False, nullable=True)

    default_time = db.Column(db.DateTime)
    current_time = db.Column(db.DateTime)

    is_cancelt = db.Column(db.Boolean, default=False)
    is_attendance_required = db.Column(db.Boolean, default=True)

    defaultRoom_id = db.Column(UuidField, db.ForeignKey('room.id'), nullable=False)
    currentRoom_id = db.Column(UuidField, db.ForeignKey('room.id'), nullable=True)

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)