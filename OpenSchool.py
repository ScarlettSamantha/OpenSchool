from flask import Flask

app = Flask(__name__)

from commands import *
from controllers import *

if __name__ == '__main__':
    app.run()
