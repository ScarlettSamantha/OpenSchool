from datetime import datetime
from .user import User
from .branch import Branch
from OpenSchool import db
from uuid import uuid4
from sqlalchemy.orm import relationship, backref
from helpers.uuid import UuidField


class UserBranch(db.Model):
    __tablename__ = 'user_has_branch'

    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4, primary_key=True)

    user_id = db.Column(UuidField, db.ForeignKey('user.id'))
    branch_id = db.Column(UuidField, db.ForeignKey('branch.id'))

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship(User, backref=backref("branches", cascade="all, delete-orphan"))
    branch = relationship(Branch, backref=backref("users", cascade="all, delete-orphan"))