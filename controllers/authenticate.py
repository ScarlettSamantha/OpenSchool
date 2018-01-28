from OpenSchool import app
from helpers import client_secret
from helpers.errors import ValidationErrors
from forms import authentication
from helpers.responses import ErrorResponses


@app.route('/authenticate/get_session_key', methods=['post'])
def get_session_key():
    _input = authentication.GetSessionForm()
    if not _input.validate():
        return ErrorResponses.required_fields_missing(ValidationErrors.field_errors(_input))

    return client_secret.ClientSecret.generate()
