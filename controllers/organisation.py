from flask_restful import Resource, marshal
from responses.organisation import full_fields, index_fields
from responses.user import index_fields as user_index_fields
from helpers.responses import Responses, ErrorResponses

from models import Organisation, UserOrganisation, User
from helpers.security import authentication_required


class Index(Resource):
    @authentication_required
    def get(self):
        users = Organisation.query.all()
        return marshal(users, index_fields)


class Entity(Resource):
    @authentication_required
    def get(self, organisation_id):
        user = Organisation.from_id(organisation_id)
        return marshal(user, full_fields)


class Users(Resource):
    @authentication_required
    def get(self, organisation_id):
        users = User.query.join(UserOrganisation).filter(UserOrganisation.organisation_id == organisation_id).all()
        return marshal(users, user_index_fields)


class Link(Resource):
    @authentication_required
    def post(self, organisation_id, user_id):
        num = UserOrganisation.find(user_id, organisation_id)
        if num is None:
            link_obj = UserOrganisation.link(user_id, organisation_id)
            link_obj.save()
        else:
            return ErrorResponses.entity_already_exists('User-organisation link')
        return Responses.operation_completed()

    @authentication_required
    def delete(self, organisation_id: str, user_id: str):
        if False == UserOrganisation.unlink(user_id, organisation_id):
            return ErrorResponses.four_o_four('User-organisation link')
        return Responses.operation_completed()