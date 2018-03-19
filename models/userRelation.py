from datetime import datetime
from .user import User
from .relationType import RelationType
from OpenSchool import db
from uuid import uuid4
from sqlalchemy.orm import relationship, backref
from helpers.uuid import UuidField


class UserRelation(db.Model):
    __tablename__ = 'user_has_relation'

    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4().hex, primary_key=True)

    student_id = db.Column(UuidField, db.ForeignKey('user.id'))
    relation_id = db.Column(UuidField, db.ForeignKey('user.id'))
    relationType_id = db.Column(UuidField, db.ForeignKey('relation_type.id'))

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    student = relationship(User, foreign_keys=[student_id], backref=backref("relation", cascade="all, delete-orphan"))
    relation = relationship(User, foreign_keys=[relation_id], backref=backref("student", cascade="all, delete-orphan"))
    relationType = relationship(RelationType)
