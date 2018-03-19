from uuid import uuid4
from uuid import UUID
from entitys.gender import Gender
from OpenSchool import db
from datetime import datetime
from helpers.uuid import UuidField
from helpers.crud import Crud
from models import Authentication, Organisation
from .userOrganisation import UserOrganisation
from dateutil.relativedelta import relativedelta
from sqlalchemy import or_
from sqlalchemy.orm import relationship


class User(db.Model, Crud):
    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4, primary_key=True)

    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=True)

    # This is allowed for key based authentication aswell. When in bot mode its node allowed
    # When not in bot mode this is also allowed as user secret.
    password = db.Column(db.String(255), unique=False, nullable=True)
    secret = db.Column(UuidField, unique=True, nullable=False, default=uuid4)

    first_name = db.Column(db.String(255), unique=False, nullable=True)
    last_name = db.Column(db.String(255), unique=False, nullable=True)

    gender = db.Column(db.Enum(Gender), unique=False, default=Gender.unknown)

    is_bot = db.Column(db.Boolean(), default=False)
    is_blocked = db.Column(db.Boolean(), default=False)
    is_visible = db.Column(db.Boolean(), default=True)

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.id = uuid4().hex
        self.secret = uuid4().hex

    def link_organisation(self, organisation: Organisation):
        link = UserOrganisation.link_obj(user_obj=self, organisation_obj=organisation)
        link.save()

    def check_secret(self, secret):
        # We check here as it can also be a str as the password is also a valid secret.
        if isinstance(secret, UUID):
            secret = str(secret.hex)
        if self.is_bot:
            return secret == str(self.secret.hex)
        else:
            return secret in [str(self.secret.hex), self.password]

    def api_keys(self, also_blocked=False):
        results = Authentication.query.filter(Authentication.user_id == self.id)
        if not also_blocked:
            results = results.filter(Authentication.is_blocked == False)
        return results.all()

    def generate_access_key(self, expires: relativedelta = None, note: str=None, save:bool=False) -> Authentication:
        auth_key = Authentication(note=note)
        if expires is None:
            auth_key.never_expire()
        else:
            auth_key.expires_in(expires)
        self.attach_access_key(self, auth_key)
        if save:
            auth_key.save()
        return auth_key

    def enable_bot(self):
        self.is_bot = True
        self.gender = Gender.unknown

    @classmethod
    def attach_access_key(cls, user: 'User', key: Authentication, auto_save:bool=True):
        key.user_id = user.id
        if auto_save:
            key.save()

    @classmethod
    def search_user_secure(cls, id, secret) -> 'User':
        result = User.query\
            .filter(User.id == id)\
            .filter(or_(User.password == secret, User.secret == secret))\
            .first()
        return result
