from flask import Flask

from social.webserver.login import init_login

def create_app():
    app = Flask(__name__)
    init_login(app)
    app.config['SECRET_KEY'] = 'this is so secret'
    from social.webserver.views import bp
    app.register_blueprint(bp)

    return app

