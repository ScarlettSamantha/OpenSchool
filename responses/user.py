from flask_restful import fields


class GenderCode(fields.Raw):
    def format(self, value):
        return str(value.value)


class GenderNames(fields.Raw):
    def format(self, value):
        return str(value.name.lower())


full_fields = {
    'id': fields.String,
    'username': fields.String,

    'firstname': fields.String,
    'lastname': fields.String,
    'gender': GenderNames(),

    'is_bot': fields.Boolean,
    'is_blocked': fields.Boolean,
    'is_visible': fields.Boolean,

    'date_created': fields.DateTime(dt_format='rfc822'),
    'date_updated': fields.DateTime(dt_format='rfc822')
}

index_fields = {
    'id': fields.String,
    'username': fields.String,
    'firstname': fields.String,
    'lastname': fields.String
}