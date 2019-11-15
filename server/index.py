from flask import Flask
# from flask_cors import CORS
from instance import config
from api.interface import interface as interface_route
from api.recommendations import recommendations as recommendations_route


def create_flask_app(config):
    app = Flask(__name__)
    # CORS(app)
    app.config.from_pyfile(config)
    app.register_blueprint(recommendations_route, url_prefix='/api/recommendations/')
    app.register_blueprint(interface_route, url_prefix='/api/interface/')
    return app


if __name__ == '__main__':
    app = create_flask_app(config)
    app.run()
