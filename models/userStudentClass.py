from datetime import datetime
from .user import User
from .studentClass import StudentClass
from OpenSchool import db
from uuid import uuid4
from sqlalchemy.orm import relationship, backref
from helpers.uuid import UuidField


class UserStudentClass(db.Model):
    __tablename__ = 'user_has_class'

    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4().hex, primary_key=True)

    user_id = db.Column(UuidField, db.ForeignKey('user.id'))
    studentClass_id = db.Column(UuidField, db.ForeignKey('student_class.id'))

    attendance_reasons_id = db.Column(UuidField, db.ForeignKey('attendance_reason.id'), nullable=False)

    note = db.Column(db.Text, nullable=True, unique=False)

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship(User, backref=backref("classes", cascade="all, delete-orphan"))
    studentClass = relationship(StudentClass, backref=backref("users", cascade="all, delete-orphan"))