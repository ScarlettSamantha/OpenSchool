from functools import wraps
from flask import request
from models.authentication import Authentication
from models.user import User
from helpers.responses import ErrorResponses
from entitys.error_codes import ResponseErrorIdentifiers


def validate_bearer(token: str):
    return Authentication.validate(token)


def validate_password(token: str):
    user_result = User.from_password(token)
    return user_result is not None


def validate_and_fetch(token: str, type: str='bearer'):
    user = User.from_token(token) if type == 'bearer' else User.from_password(token)
    return user if user is not None else False


def access_denied():
    return ErrorResponses.access_denied('Invalid token', ResponseErrorIdentifiers.ACCESS_DENIED_ON_TOKEN)


def authenticate_return_user(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'Authorization' in request.headers:
            try:
                auth_type, token = request.headers['Authorization'].split(
                    None, 1)
                # This means its a authentication record in the database.
                if auth_type == 'Bearer':
                    user_obj = validate_and_fetch(token)
                    if not user_obj:
                        return access_denied()
            except ValueError:
                print('Error 1')
                return access_denied()
        else:
            return access_denied()
        return f(*args, **kwargs, api_user=user_obj)
    return decorated


def authentication_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'Authorization' in request.headers:
            try:
                auth_type, token = request.headers['Authorization'].split(
                    None, 1)
                # This means its a authentication record in the database.
                if auth_type == 'Bearer':
                    if not validate_bearer(token):
                        return access_denied()
                # This means the user password is directly used.
                elif auth_type is 'Password':
                    if not validate_password(token):
                        return access_denied()
            except ValueError:
                print('Error 1')
                return access_denied()
        else:
            return access_denied()
        return f(*args, **kwargs)
    return decorated
