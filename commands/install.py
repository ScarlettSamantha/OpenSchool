from OpenSchool import app, db
from helpers import installing

@app.cli.command()
def install():
    organisation = installing.generate_base_organisation('test')
    installing.generate_root_api_user(organisation=organisation, name='root')
