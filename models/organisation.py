from uuid import uuid4
from OpenSchool import db
from models.userOrganisation import UserOrganisation
from datetime import datetime
from helpers.uuid import UuidField
from helpers.crud import Crud

class Organisation(db.Model, Crud):
    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)

    tax = db.Column(db.String(255), unique=False, nullable=True)
    coc = db.Column(db.String(255), unique=False, nullable=True)

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def add_user(self, user: 'User') -> UserOrganisation:
        link_obj = UserOrganisation.link_obj(user_obj=user, organisation_obj=self)
        link_obj.save()
        return link_obj

