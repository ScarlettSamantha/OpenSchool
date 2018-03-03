from datetime import datetime
from .user import User
from .address import Address
from OpenSchool import db
from uuid import uuid4
from sqlalchemy.orm import relationship, backref
from helpers.uuid import UuidField


class UserAddress(db.Model):
    __tablename__ = 'user_has_address'

    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4().hex, primary_key=True)

    user_id = db.Column(UuidField, db.ForeignKey('user.id'))
    address_id = db.Column(UuidField, db.ForeignKey('address.id'))

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship(User, backref=backref("orders", cascade="all, delete-orphan"))
    address = relationship(Address, backref=backref("orders", cascade="all, delete-orphan"))