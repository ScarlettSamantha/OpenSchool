from uuid import uuid4
from OpenSchool import db
from datetime import datetime
from helpers.uuid import UuidField

class Assignment(db.Model):
    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4().hex, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)

    tax = db.Column(db.String(255), unique=False, nullable=True)
    coc = db.Column(db.String(255), unique=False, nullable=True)

    turned_in = db.Column(db.Boolean, default=False, nullable=False)

    is_group_assignment = db.Column(db.Boolean, default=False, nullable=False)
    is_graded = db.Column(db.Boolean, default=True, nullable=False)

    note = db.Column(db.Text, nullable=True)

    assignmentGroup_id = db.Column(UuidField, db.ForeignKey('assignment_group.id'), nullable=False)
    classStart_id = db.Column(UuidField, db.ForeignKey('student_class.id'), nullable=False)
    classDue_id = db.Column(UuidField, db.ForeignKey('student_class.id'), nullable=False)

    date_started = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    date_due = db.Column(db.DateTime, nullable=True)

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)