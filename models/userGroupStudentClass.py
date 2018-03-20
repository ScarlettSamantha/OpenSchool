from datetime import datetime
from .userGroup import UserGroup
from .studentClass import StudentClass
from OpenSchool import db
from uuid import uuid4
from sqlalchemy.orm import relationship, backref
from helpers.uuid import UuidField


class UserGroupStudentClass(db.Model):
    __tablename__ = 'user_group_has_class'

    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4, primary_key=True)

    userGroup_id = db.Column(UuidField, db.ForeignKey('user_group.id'))
    studentClass_id = db.Column(UuidField, db.ForeignKey('student_class.id'))

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    userGroup = relationship(UserGroup, backref=backref("classes", cascade="all, delete-orphan"))
    studentClass = relationship(StudentClass, backref=backref("groups", cascade="all, delete-orphan"))