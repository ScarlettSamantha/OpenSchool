class ValidationErrors:
    @staticmethod
    def field_errors(form):
        err_text = ''
        for field, err in form.errors.items():
            err_text += '%s Error: %s \r\n' % (field, ', '.join(err))
        return err_text
