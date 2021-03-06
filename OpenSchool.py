from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

import config

api = Api(app)
db = SQLAlchemy(app)
engine = create_engine(config.db_path, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

from models import *
from commands import *
from controllers import *

api.add_resource(authenticate.List, '/api/v1.0/user/<user_id>/authenticate/<user_secret>/keys/', endpoint='list_keys')
api.add_resource(authenticate.Generate, '/api/v1.0/user/<user_id>/authenticate/<user_secret>/key/', endpoint='create_key')

api.add_resource(user.Index, '/api/v1.0/users/', endpoint='list_users')
api.add_resource(user.Entity, '/api/v1.0/user/<user_id>/', endpoint='get_user')
api.add_resource(user.Entity, '/api/v1.0/user/', endpoint='create_user')

api.add_resource(organisation.Index, '/api/v1.0/organisations/', endpoint='list_organisations')
api.add_resource(organisation.Entity, '/api/v1.0/organisation/<organisation_id>/', endpoint='get_organisation')
api.add_resource(organisation.Users, '/api/v1.0/organisation/<organisation_id>/users', endpoint='get_organisation_users')
api.add_resource(organisation.Link, '/api/v1.0/organisation/<organisation_id>/user/<user_id>/link/', endpoint='link_organisation_users')

if __name__ == '__main__':
    app.run()
