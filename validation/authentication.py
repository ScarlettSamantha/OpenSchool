from flask_restful import reqparse


def generate_session_key_validator():
    parser = reqparse.RequestParser()
    parser.add_argument('note')
    return parser

