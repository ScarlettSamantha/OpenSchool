from wtforms import Form, StringField
from helpers.uuid import Uuid


class GetSessionFromLoginForm(Form):
    pass


class GetSessionForm(Form):
    organisation_id = StringField('organisation_id', validators=[Uuid.validator()])
    client_id = StringField('client_id', validators=[Uuid.validator()])
    client_secret = StringField('client_secret', validators=[Uuid.validator()])
