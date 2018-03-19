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

api.add_resource(authenticate.Authenticate, '/authenticate/<user_id>/<user_secret>/list/', endpoint='index_keys')
api.add_resource(authenticate.Authenticate, '/authenticate/<user_id>/<user_secret>/generate/', endpoint='create_key')

if __name__ == '__main__':
    app.run()
