from flask_restful import fields

fields = {
    'key': fields.String,
    'is_blocked': fields.Boolean,
    'note': fields.String
}
