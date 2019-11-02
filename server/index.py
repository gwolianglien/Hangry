from flask import Flask
from restaurant.api import restaurant
from interface.api import interface


def create_flask_app(config):
    app = Flask(__name__)
    app.config.from_pyfile(config)
    app.register_blueprint(restaurant, url_prefix='/api/restaurant/')
    app.register_blueprint(interface, url_prefix='/api/interface/')
    return app


if __name__ == '__main__':
    app = create_flask_app("config.py")
    app.run()
