from flask_restful import Resource
from helpers import client_secret
from validation.authentication import get_session_key_validator


class Authenticate(Resource):
    def get(self):
        return 'test'

    def post(self):
        args = get_session_key_validator().parse_args()
        print(args)
        return client_secret.ClientSecret.generate()
