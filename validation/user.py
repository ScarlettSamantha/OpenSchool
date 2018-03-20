from flask_restful import reqparse


def create_user():
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True)
    parser.add_argument('email', required=True)
    parser.add_argument('firstname', required=False)
    parser.add_argument('lastname', required=False)
    parser.add_argument('password', required=False)
    return parser

