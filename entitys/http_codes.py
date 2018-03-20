class HttpResponseCodes:

    OK = 200

    ACCESS_DENIED = 403
    RESOURCE_NOT_FOUND = 404
    # Should be used then resource already exists.
    CONFLICT = 409
    PRECONDITION_FAILED = 412
    ENTITY_TO_LARGE = 413

    SERVER_ERROR = 500
