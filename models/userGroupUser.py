from datetime import datetime
from .user import User
from .userGroup import UserGroup
from OpenSchool import db
from uuid import uuid4
from sqlalchemy.orm import relationship, backref
from helpers.uuid import UuidField


class UserGroupUser(db.Model):
    __tablename__ = 'group_has_user_group'

    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4, primary_key=True)

    user_id = db.Column(UuidField, db.ForeignKey('user.id'))
    userGroup_id = db.Column(UuidField, db.ForeignKey('user_group.id'))

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship(User, backref=backref("groups", cascade="all, delete-orphan"))
    group = relationship(UserGroup, backref=backref("users", cascade="all, delete-orphan"))