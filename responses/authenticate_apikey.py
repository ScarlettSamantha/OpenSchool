from flask_restful import fields

index_fields = {
    'key': fields.String
}

full_fields = {
    'key': fields.String,
    'belongs_to': fields.String(attribute='user_id'),
    'is_blocked': fields.Boolean,
    'note': fields.String,
    'note_blocked': fields.String,
    'date_created': fields.DateTime(dt_format='rfc822')
}
