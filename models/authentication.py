from uuid import uuid4
from OpenSchool import db
from helpers.crud import Crud
from datetime import datetime
from dateutil.relativedelta import relativedelta
from helpers.uuid import UuidField

class Authentication(db.Model, Crud):
    key = db.Column(UuidField, unique=True, nullable=False, default=uuid4, primary_key=True)
    expiration = db.Column(db.DateTime, unique=False, nullable=True)

    note = db.Column(db.Text, unique=False, nullable=True)
    note_blocked = db.Column(db.Text, unique=False, nullable=True)

    is_blocked = db.Column(db.Boolean, default=False, nullable=False, unique=False)

    user_id = db.Column(UuidField, db.ForeignKey('user.id'), nullable=False)

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def expires_in(self, delta: relativedelta):
        self.expiration = datetime.now() + delta

    def never_expire(self):
        self.expires_in(relativedelta(years=100))
