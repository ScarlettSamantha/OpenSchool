from flask_restful import reqparse


def get_session_key_validator():
    parser = reqparse.RequestParser()
    parser.add_argument('client_id', required=True, help='Cannot be empty or a invalid uuid.', location='form')
    parser.add_argument('client_secret', required=True, help='Cannot be empty or a invalid uuid.', location='form')
    parser.add_argument('organisation_id', required=True, help='Cannon be empty or a invalid uuid.', location='form')
    return parser
