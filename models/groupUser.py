from datetime import datetime
from .user import User
from .userGroup import UserGroup
from OpenSchool import db
from uuid import uuid4
from sqlalchemy.orm import relationship, backref
from helpers.uuid import UuidField


class GroupUser(db.Model):
    __tablename__ = 'group_has_user'

    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4, primary_key=True)

    user_id = db.Column(UuidField, db.ForeignKey('user.id'))
    userGroup_id = db.Column(UuidField, db.ForeignKey('user_group.id'))

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship(User, backref=backref("group", cascade="all, delete-orphan"))
    group = relationship(UserGroup, backref=backref("user", cascade="all, delete-orphan"))