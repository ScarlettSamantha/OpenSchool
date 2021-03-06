from uuid import uuid4
from OpenSchool import db
from datetime import datetime
from helpers.uuid import UuidField
from sqlalchemy.orm import relationship

class Branch(db.Model):
    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)

    is_main = db.Column(db.Boolean, unique=False, default=False)

    website = db.Column(db.String(255), unique=False, nullable=True)
    phone = db.Column(db.String(255), unique=False, nullable=True)
    email = db.Column(db.String(255), unique=False, nullable=True)

    organisation_id = db.Column(UuidField, db.ForeignKey('organisation.id'), nullable=False)

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    rooms = relationship('Room', backref="Branch", lazy=True)