from flask import jsonify
from entitys.error_codes import ResponseErrorIdentifiers
from entitys.http_codes import HttpResponseCodes


class ErrorResponses:

    DEFAULT_ACCESS_DENIED_ERROR = 'Access Denied'
    REQUIRED_FIELD_ERROR_PATTERN = "%s is missing from the form data \r\n"
    RESOURCE_NOT_FOUND_ERROR_PATTERN = '%s requested resource could not be found'
    ERROR_ID_DEFAULT = 'None'

    @classmethod
    def access_denied(cls, reason=None, err_id=None):
        return cls.json_err(reason if reason else cls.DEFAULT_ACCESS_DENIED_ERROR,
                            HttpResponseCodes.ACCESS_DENIED, err_id)

    @classmethod
    def four_o_four(cls, resource_name):
        if not isinstance(resource_name, str):
            resource_name = resource_name.__class__
        error_response = cls.json_err(cls.RESOURCE_NOT_FOUND_ERROR_PATTERN % resource_name, HttpResponseCodes.RESOURCE_NOT_FOUND,
                            ResponseErrorIdentifiers.COULD_NOT_FIND_RESOURCE)
        return error_response

    # We use code 413 here as code 412 does not return a response body.
    # @todo https://github.com/pallets/werkzeug/issues/1231
    @classmethod
    def required_fields_missing(cls, err_or_fields: list, code=HttpResponseCodes.ENTITY_TO_LARGE):
        err_str = ''
        if type(err_or_fields) is list:
            for f in err_or_fields:
                err_str += cls.REQUIRED_FIELD_ERROR_PATTERN % f
        elif type(err_or_fields) is str:
            err_str = err_or_fields
        else:
            raise TypeError('err_or_fields can be ether a string or a list is a %s' % type(err_or_fields))
        return cls.json_err(err_str, code, ResponseErrorIdentifiers.POST_REQUIRED_FIELD_MISSING)

    @classmethod
    def json_err(cls, err_msg, err_code, err_id=None):
        response = jsonify({
            "error_msg": err_msg,
            "error_code": err_code,
            "error_id": err_id if err_id else cls.ERROR_ID_DEFAULT
        })
        response.status_code = err_code
        return response


