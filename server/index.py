from flask import Flask
from recommendations.api import recommendations as recommendations_route
from interface.api import interface as interface_route

# from test.api import test as test_route


def create_flask_app(config):
    app = Flask(__name__)
    app.config.from_pyfile(config)
    app.register_blueprint(recommendations_route, url_prefix='/api/recommendations/')
    app.register_blueprint(interface_route, url_prefix='/api/interface/')
    # app.register_blueprint(test_route, url_prefix='/api/test')
    return app


if __name__ == '__main__':
    app = create_flask_app("instance/config.py")
    app.run()
