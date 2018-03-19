from uuid import uuid4
from entitys.gender import Gender
from OpenSchool import db
from datetime import datetime
from helpers.uuid import UuidField
from models import Authentication, Organisation
from .userOrganisation import UserOrganisation
from dateutil.relativedelta import relativedelta
from sqlalchemy.orm import relationship


class User(db.Model):
    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4().hex, primary_key=True)

    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=True)
    password = db.Column(db.String(255), unique=False, nullable=True)

    first_name = db.Column(db.String(255), unique=False, nullable=True)
    last_name = db.Column(db.String(255), unique=False, nullable=True)

    gender = db.Column(db.Enum(Gender), unique=False, default=Gender.unknown)

    is_bot = db.Column(db.Boolean(), default=False)
    is_blocked = db.Column(db.Boolean(), default=False)
    is_visible = db.Column(db.Boolean(), default=True)

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    api_keys = relationship('Authentication', backref='user', lazy=True)

    @classmethod
    def attach_access_key(cls, user: 'User', key: Authentication):
        key.user_id = user
        db.session.add(key)
        db.session.commit()

    def generate(self):
        self.id = uuid4().hex

    def set_organisation(self, organisation: Organisation):
        link = UserOrganisation(user_id=self.id, organisation_id=organisation.id)
        db.session.add(link)

    def generate_access_key(self, expires: relativedelta = None, note: str=None):
        auth_key = Authentication(note=note)
        if expires is None:
            auth_key.never_expire()
        else:
            auth_key.expires_in(expires)
        self.attach_access_key(self, auth_key)

    def enable_bot(self):
        self.is_bot = True
        self.gender = Gender.unknown
