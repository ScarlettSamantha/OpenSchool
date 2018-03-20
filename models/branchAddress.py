from datetime import datetime
from .branch import Branch
from .address import Address
from OpenSchool import db
from uuid import uuid4
from sqlalchemy.orm import relationship, backref
from helpers.uuid import UuidField


class BranchAddress(db.Model):
    __tablename__ = 'branch_has_address'

    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4, primary_key=True)

    branch_id = db.Column(UuidField, db.ForeignKey('branch.id'))
    address_id = db.Column(UuidField, db.ForeignKey('address.id'))

    is_current_address = db.Column(db.Boolean, unique=False, nullable=False, default=False)

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    branch = relationship(Branch, backref=backref("addresses", cascade="all, delete-orphan"))
    address = relationship(Address, backref=backref("branches", cascade="all, delete-orphan"))