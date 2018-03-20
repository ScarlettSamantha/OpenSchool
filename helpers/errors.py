import re
from sqlalchemy.exc import IntegrityError

class ValidationErrors:
    @staticmethod
    def field_errors(form):
        err_text = ''
        for field, err in form.errors.items():
            err_text += '%s Error: %s \r\n' % (field, ', '.join(err))
        return err_text


def get_voilating_field_from_sql_exception(obj: IntegrityError):
    r = re.compile(r"UNIQUE constraint failed: (\S+)")
    matches = r.findall(str(obj))
    return matches[0]