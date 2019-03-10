import os

from flask import Flask
from social.webserver.login import init_login

def create_app():
    app = Flask(__name__)
    init_login(app)
    app.config.from_pyfile(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'config.py'))
    app.config['SECRET_KEY'] = 'this is so secret'
    from social.webserver.views import bp
    from social.webserver.api import api
    app.register_blueprint(bp)
    app.register_blueprint(api, url_prefix='/api')

    return app

