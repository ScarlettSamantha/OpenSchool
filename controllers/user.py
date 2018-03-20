from flask_restful import Resource, marshal
from helpers.responses import ErrorResponses
from validation.authentication import generate_session_key_validator
from responses.user import full_fields
from models import User, Authentication
from helpers.security import authentication_required

class Index(Resource):
    def get(self, user_id):
        result = User.search_user_secure(id=user_id, secret=user_secret)
        # We check here if we dont have a empty user.
        if result is None or not isinstance(result, User):
            return ErrorResponses.four_o_four(User.__name__)
        api_keys = result.api_keys()
        if not api_keys or api_keys.__len__ == 0:
            return ErrorResponses.four_o_four(Authentication.__name__)
        keys = api_keys
        #return marshal(keys, full_key_fields)


class Entity(Resource):

    @authentication_required
    def get(self, user_id):
        user = User.from_id(user_id)
        return marshal(user, full_fields)
