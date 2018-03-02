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

api.add_resource(authenticate.Authenticate, '/authenticate/get_session_key')

@app.cli.command()
def test():
    user = User(username='test', password='123', email='test@test.nl', first_name='scarlett', last_name='verheul')
    db_session.add(user)
    db_session.commit()

if __name__ == '__main__':
    app.run()
