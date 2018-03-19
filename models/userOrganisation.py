from datetime import datetime
from OpenSchool import db
from uuid import uuid4
from sqlalchemy.orm import relationship, backref
from helpers.uuid import UuidField


class UserOrganisation(db.Model):
    __tablename__ = 'user_has_organisation'

    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4().hex, primary_key=True)

    user_id = db.Column(UuidField, db.ForeignKey('user.id'))
    organisation_id = db.Column(UuidField, db.ForeignKey('organisation.id'))

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship('User', backref=backref("organisations", cascade="all, delete-orphan"))
    organisation = relationship('Organisation', backref=backref("users", cascade="all, delete-orphan"))