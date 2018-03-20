from datetime import datetime
from OpenSchool import db
from helpers.crud import Crud
from uuid import uuid4
from sqlalchemy.orm import relationship, backref
from helpers.uuid import UuidField


class UserOrganisation(db.Model, Crud):
    __tablename__ = 'user_has_organisation'

    id = db.Column(UuidField, unique=True, nullable=False, default=uuid4, primary_key=True)

    user_id = db.Column(UuidField, db.ForeignKey('user.id'))
    organisation_id = db.Column(UuidField, db.ForeignKey('organisation.id'))

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship('User', backref=backref("organisations", cascade="all, delete-orphan"))
    organisation = relationship('Organisation', backref=backref("users", cascade="all, delete-orphan"))

    @classmethod
    def find(cls, user_id, organisation_id) -> 'UserOrganisation':
        return cls.query\
            .filter(UserOrganisation.user_id == user_id)\
            .filter(UserOrganisation.organisation_id == organisation_id)\
            .first()

    @classmethod
    def link_obj(cls, user_obj:'User', organisation_obj:'Organisation') -> 'UserOrganisation':
        return cls.link(user_id=user_obj.id, organisation_id=organisation_obj.id)

    @classmethod
    def link(cls, user_id:str, organisation_id:str) -> 'UserOrganisation':
        return cls(user_id=user_id, organisation_id=organisation_id)

    @classmethod
    def unlink(cls, user_id: str, organisation_id: str):
        obj = cls.find(user_id, organisation_id=organisation_id)
        if obj is None:
            return False
        return obj.delete()