from flask_restful import Resource, marshal
from helpers.responses import ErrorResponses
from validation.authentication import generate_session_key_validator
from responses.api_key import fields
from models import User

class Authenticate(Resource):
    def get(self, user_id, user_secret):
        result = User.search_user_secure(id=user_id, secret=user_secret)
        print(result)
        # We check here if we dont have a empty user.
        if result is None or not isinstance(result, User):
            return ErrorResponses.four_o_four(User.__name__)
        api_keys = result.api_keys()
        if not api_keys or api_keys.__len__ == 0:
            return ErrorResponses.four_o_four(Authenticate.__name__)
        keys = api_keys
        return marshal(keys, fields)

    def post(self, user_id, user_secret):
        args = generate_session_key_validator().parse_args()
        result = User.search_user_secure(id=user_id, secret=user_secret)
        # We check here if we dont have a empty user.
        if not result or not isinstance(result, User):
            return ErrorResponses.four_o_four(User.__name__)
        key = result.generate_access_key(note=None if not args.note else args.note)
        return marshal(key, fields)





