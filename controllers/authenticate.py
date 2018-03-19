from flask_restful import Resource
from helpers import client_secret
from validation.authentication import get_session_key_validator
from models import User


class Authenticate(Resource):
    def get(self):
        r = ''
        u = User.query.all()
        print(u)
        for user in u:
            r += str(user.id.hex)
            for key in user.api_keys:
                r += "     " + str(key.key)
        return r

    def post(self):
        args = get_session_key_validator().parse_args()
        print(args)
        return client_secret.ClientSecret.generate()
