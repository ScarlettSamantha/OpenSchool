from OpenSchool import db

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