from flask import Flask
from api.restaurant import restaurant


def create_flask_app(config):
    app = Flask(__name__)
    app.config.from_pyfile(config)
    app.register_blueprint(restaurant)
    return app


if __name__ == '__main__':
    app = create_flask_app("config.py")
    app.run()
