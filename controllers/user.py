from sqlalchemy.exc import IntegrityError
from flask_restful import Resource, marshal
from responses.user import full_fields, index_fields
from models import User
from helpers.security import authentication_required
from validation.user import create_user
from helpers.responses import ErrorResponses
from helpers.errors import get_voilating_field_from_sql_exception


class Index(Resource):
    @authentication_required
    def get(self):
        users = User.query.all()
        return marshal(users, index_fields)


class Entity(Resource):
    @authentication_required
    def get(self, user_id):
        user = User.from_id(user_id)
        return marshal(user, full_fields)

    @authentication_required
    def post(self):
        args = create_user().parse_args()
        user = User(username=args.username, email=args.email)
        user.generate_access_key()
        if 'firstname' in args:
            user.first_name = args.firstname
        if 'lastname' in args:
            user.last_name = args.lastname
        if 'password' in args:
            user.password = args.password
        try:
            user.save()
        except IntegrityError as e:
            return ErrorResponses.entity_not_unique(User.__name__.lower(), get_voilating_field_from_sql_exception(e))
        return marshal(user, full_fields)