from wtforms import validators
from hashlib import sha512
from uuid import uuid4


class ClientSecret:
    __LENGTH = 64
    __ALGORITME = sha512

    @classmethod
    def length(cls):
        return cls.__LENGTH

    @classmethod
    def validator(cls):
        return validators.length(min=cls.length(), max=cls.length())

    @classmethod
    def generate(cls):
        m = cls.__ALGORITME()
        m.update(str(uuid4()).encode())
        m.update(str(uuid4()).encode())
        return m.hexdigest()
