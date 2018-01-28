from wtforms import validators


class Uuid():
    LENGTH_WITH_DASHES = 36
    LENGTH_WITHOUT_DASHES = 32
    LENGTH_HEX = 16

    @classmethod
    def length(cls):
        return cls.LENGTH_WITH_DASHES

    @classmethod
    def validator(cls):
        return validators.UUID()
