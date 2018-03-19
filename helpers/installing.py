from OpenSchool import db
from models import Organisation, User


def generate_base_organisation(name: str) -> Organisation:
    org = Organisation(name=name)
    db.session.add(org)
    db.session.commit()
    return org


def generate_root_api_user(organisation: Organisation, name: str='api_root') -> User:
    user = User(username=name)
    user.generate()
    user.enable_bot()
    user.set_organisation(organisation)
    user.generate_access_key(note='Root Api User - Generated by install command')
    db.session.add(user)
    db.session.commit()
    return user
