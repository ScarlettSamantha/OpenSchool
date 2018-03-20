from flask_restful import Resource, marshal
from responses.user import full_fields, index_fields
from models import User
from helpers.security import authentication_required


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
