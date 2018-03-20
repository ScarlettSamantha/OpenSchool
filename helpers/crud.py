from OpenSchool import db
from sqlalchemy.exc import IntegrityError
from helpers.errors import get_voilating_field_from_sql_exception

class Crud(object):

    __ID_FIELD__ = 'id'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def from_id(cls, id: str):
        return cls.query.filter(cls.id == id).first()