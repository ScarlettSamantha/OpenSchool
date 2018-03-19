from OpenSchool import db

class Crud(object):
    def save(self):
        db.session.add(self)
        db.session.commit()