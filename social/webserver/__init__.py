from flask import Flask

def create_app():
    app = Flask(__name__)

    from social.webserver.views import bp
    from social.webserver.api import api
    app.register_blueprint(bp)
    app.register_blueprint(api)

    return app

