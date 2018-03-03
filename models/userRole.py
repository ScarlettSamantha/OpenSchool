from datetime import datetime
from .user import User
from .role import Role
from OpenSchool import db
from uuid import uuid4
from sqlalchemy.orm import relationship, backref
from helpers.uuid import UuidField


class UserRole(db.Model):
    __tablename__ = 'user_has_role'

    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4().hex, primary_key=True)

    user_id = db.Column(UuidField, db.ForeignKey('user.id'))
    role_id = db.Column(UuidField, db.ForeignKey('role.id'))

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship(User, backref=backref("roles", cascade="all, delete-orphan"))
    role = relationship(Role, backref=backref("users", cascade="all, delete-orphan"))