import os

from flask import Flask
from social.webserver.login import init_login

def create_app():
    app = Flask(__name__)
    init_login(app)
    app.config['SECRET_KEY'] = 'this is so secret'
    app.config['CURRENT_SERVER'] = os.environ.get('CURRENT_SERVER')
    from social.webserver.views import bp
    from social.webserver.api import api
    app.register_blueprint(bp)
    app.register_blueprint(api, url_prefix='/api')

    return app

