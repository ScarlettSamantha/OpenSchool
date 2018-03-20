from flask_restful import fields

full_fields = {
    'id': fields.String,
    'name': fields.String,

    'tax': fields.String,
    'coc': fields.String,

    'date_created': fields.DateTime(dt_format='rfc822'),
    'date_updated': fields.DateTime(dt_format='rfc822')
}

index_fields = {
    'id': fields.String,
    'name': fields.String
}